# 错误使用规范：
# 1. 新定义的错误类型必须继承BaseError
# 2. 只为有特殊处理的错误定义错误类型
# 3. 一般性错误使用CommonError，可以指定自己的错误信息
# 使用示例:
# raise InvalidArgsError('项目名称为必填项')
# raise CommonError('无权限访问')

class BaseError(Exception):
    '''
    错误基类，自定义错误必须继承此类x
    '''
    errcode = 10000
    errmsg = '服务暂时不可用'

    def __init__(self, *errmsgs):
        if errmsgs:
            errmsgs = [str(msg) for msg in errmsgs]
            self.errmsg = ','.join(errmsgs)


class MethodError(BaseError):
    errcode = 10001
    errmsg = '不支持的请求方式'


class InvalidArgsError(BaseError):
    errcode = 10002
    errmsg = '无效的参数'


class LoginExpireError(BaseError):
    errcode = 10003
    errmsg = '登录状态过期，请重新登录'


class CommonError(BaseError):
    errcode = 10010
    errmsg = '服务暂时不可用'
