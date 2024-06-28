from datetime import datetime

from common_tool.http import get_post_data
from common_tool.token import create_jwt_token
from django import views
from django.utils.decorators import method_decorator

from apps.account.manager.db_manager import get_user_by_openid_safe, update_user_info
from apps.decorators import mini_login_required
from apps.third_party_service.weixin import weixin_service
from django_miniprogram_template.settings import error_logger
from utils import restful


# Create your views here.
class UserLogin(views.View):
    """
    用户登陆
    """
    def post(self, request):
        post_data = get_post_data(request)
        code = post_data.get("code")
        if not code:
            return restful.param_error(msg='code未传递')

        info, error_msg = weixin_service.get_user_openid_and_session_key(code)
        if error_msg:
            return restful.param_error(msg=error_msg)
        token = create_jwt_token({'openid': info[0]})
        user = get_user_by_openid_safe(info[0])
        if not user:
            return restful.success({"token": token})
        update_user_info(user, session_key=info[1], last_login=datetime.now())
        return restful.success({
            "token": token,
            'user_id': user.id,
            'finish_user_info': user.phone and user.wechat
        })


@method_decorator(mini_login_required, name='dispatch')
class BindPhoneView(views.View):
    """
    绑定用户手机号，通过微信官方的button方式获取
    """

    def post(self, request):
        user = request.wxuser
        post_data = get_post_data(request)
        iv = post_data.get("iv")
        encryptedData = post_data.get("encryptedData")
        if not (iv and encryptedData):
            return restful.param_error(msg='手机号获取错误，稍后再试～')
        try:
            # 解密手机号
            mobile_obj = weixin_service.decrypt(encryptedData, iv, user.session_key)
            update_user_info(user, phone=mobile_obj['purePhoneNumber'])
        except Exception as e:
            error_logger.error(e)
            return restful.param_error(msg='获取失败，请手动输入~')
        return restful.success(user.phone)


@method_decorator(mini_login_required, name='dispatch')
class UpdateUserInfoView(views.View):
    """
    更新用户信息
    """

    def post(self, request):
        user = request.wxuser
        json_data = get_post_data(request)
        nickName = json_data.get("nickName", '')
        gender = json_data.get("gender", '')
        avatar_url = json_data.get("avatarUrl", '')
        age = json_data.get("age", '')
        phone = json_data.get("phone")
        update_user_info(
            user, nickname=nickName, gender=gender, avatar_url=avatar_url, phone=phone, age=age
        )
        return restful.success({'user_id': user.id})
