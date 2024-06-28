from functools import wraps

from common_tool.token import decode_jwt_token

from utils import restful


def get_openid_from_request(request):
    """
    获取用户
    :param request:
    :return:
    """
    try:
        jwt_token = request.META.get("HTTP_TOKEN")
        return decode_jwt_token(jwt_token).get("openid")
    except Exception as e:
        return ""


def user_passes_test(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.wxuser):
                return view_func(request, *args, **kwargs)
            else:
                return restful.param_error(msg='获取用户失败，请重新授权绑定～')
        return _wrapped_view
    return decorator


def mini_login_required(function=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: bool(u),
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
