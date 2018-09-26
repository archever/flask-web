# flask-web demo

## 功能
* websocket 前后端实现
* jinja 模板嵌套, 继承
* peewee postgres
* redis session
* 用户登录注册, 邮箱验证
* 单点登录
* 请求日志中间件
* 错误处理中间件

## 特别实现
* git 仓库 md 文章自动生成
* geoip 分析客户端ip地址做语言检测, 国际化

## auto gen model

```shell
python3 -m pwiz -e postgresql -u demo -H 127.0.0.1 -P demo > ./models/_tmp.py
```
