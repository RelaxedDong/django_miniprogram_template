import datetime
import json

import base64
import requests
from Crypto.Cipher import AES
from common_tool.datetime import datetime_to_str
from django.conf import settings
from django.core.cache import cache



class WxServiceManager(object):

    def __init__(self):
        self.AppID = settings.WX_MINI_SETTINGS['APP_ID']
        self.AppSecret = settings.WX_MINI_SETTINGS['APP_SECRET']
        self.get_open_id_url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code={0}&grant_type=authorization_code" \
                               % (self.AppID, self.AppSecret)

    def get_user_openid_and_session_key(self, code):
        """
        授权按钮点击，获取用户openid与session_key
        :return:
        """
        url = self.get_open_id_url.format(code)
        resp = requests.get(url)  # 请求微信服务器
        result_dict = json.loads(resp.text)
        openid = result_dict.get("openid")
        if not openid:
            return None, "获取openid 失败"
        return (openid, result_dict['session_key']), ""

    def real_get_access_token(self):
        """
        生成一个基础 access_token
        :return:
        """
        cache_name = 'weixin:access_token'
        access_token = cache.get(cache_name)
        if not access_token:
            tokenUrl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
                self.AppID, self.AppSecret)
            resp = requests.get(url=tokenUrl)
            urlResp = json.loads(resp.text)
            access_token = urlResp['access_token']
            cache.set(cache_name, access_token, timeout=60 * 60)
        return access_token

    def decrypt(self, encryptedData, iv, sessionKey):
        # base64 decode
        sessionKey = base64.b64decode(sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        if decrypted['watermark']['appid'] != self.AppID:
            raise Exception('Invalid Buffer')
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


weixin_service = WxServiceManager()
