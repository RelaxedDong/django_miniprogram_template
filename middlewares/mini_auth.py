# encoding:utf-8
from django.utils.deprecation import MiddlewareMixin

from apps.decorators import get_openid_from_request

from apps.account.manager.db_manager import get_user_by_openid_safe


class MiniAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        openid = get_openid_from_request(request)
        wx_user = get_user_by_openid_safe(openid)
        setattr(request, 'openid', openid)
        setattr(request, 'wxuser', wx_user)
        setattr(request, '_dont_enforce_csrf_checks', True)
