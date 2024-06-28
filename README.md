# Django-小程序后端模版

快速启动一个小程序 django 后端项目

## 模块说明：
- apps
  - account: 通用的小程序用户表以及对应的views逻辑
    - managers: db的封装以及views的封装 
  - third_party_service: 三方模块，目前只有微信小程序服务（获取openid、session_key等逻辑）
- middlewares
  - 获取登陆状态用户信息，绑定到request对象,views能直接使用
- settings
  - base: 基础配置
  - prod: 线上配置
- utils
  - 工具包：目前只包含resultful想要封装的返回结果封装

## 使用步骤:
    1. 更改项目名, 全局替换 `django_miniprogram_template` 关键字, 替换成自己项目名称。   
    2. 更改数据库配置，小程序配置等

## 注意事项
- 加密方式需要自定义，目前是直接用的jwt。用户一旦进入小程序会调用login接口，然后后续接口会通过token传递到服务器。
如果需要更改方式，请重新自定义相关逻辑
- 