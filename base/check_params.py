from base import errors
from utils import time_utils


class CheckParams:

    @classmethod
    def check_required(cls, name, value, condition):
        '''
        必填项校验
        '''
        if value is None or value == '':
            raise errors.InvalidArgsError(f'{name}为必填项')
        if len(condition) == 0:
            return value
        method, *condition = condition
        method = f'check_{method}'
        return getattr(cls, method)(name, value, condition)

    @classmethod
    def check_optional(cls, name, value, condition):
        '''
        可选项校验
        '''
        if value is None or value == '':
            return value
        if len(condition) == 0:
            return value
        method, *condition = condition
        method = f'check_{method}'
        return getattr(cls, method)(name, value, condition)

    @classmethod
    def check_str(cls, name, value, condition):
        '''
        '''
        if not isinstance(value, str):
            raise errors.InvalidArgsError(f'{name}需要字符串参数')
        value = value.strip()
        length = len(value)
        if len(condition) == 0:
            return value
        elif len(condition) == 1:
            max_length = int(condition[0])
            if length > max_length:
                raise errors.InvalidArgsError(f'{name}长度不能大于{max_length}')
        else:
            min_length, max_length, *_ = condition
            min_length = int(min_length)
            max_length = int(max_length)
            if not (min_length <= length <= max_length):
                raise errors.InvalidArgsError(f'{name}长度应在{min_length}~{max_length}个字符之间')
        return value

    @classmethod
    def check_int(cls, name, value, condition):
        '''
        '''
        if not isinstance(value, int) and (isinstance(value, str) and not value.isdigit()):
            raise errors.InvalidArgsError(f'{name}需要整数参数')
        value = int(value)
        if len(condition) == 0:
            return value
        elif len(condition) == 1:
            max_value = condition[0]
            if value > max_value:
                raise errors.InvalidArgsError(f'{name}最大值不超过{max_value}')
        else:
            min_value, max_value, *_ = condition
            if not (min_value <= value <= max_value):
                raise errors.InvalidArgsError(f'{name}值应在{min_value}~{max_value}之间')
        return value

    @classmethod
    def check_list(cls, name, value, condition):
        if not isinstance(value, list):
            raise errors.InvalidArgsError(f'{name}需要列表')
        return value

    @classmethod
    def check_datetime(cls, name, value, condition):
        '''
        检查日期格式
        '''
        try:
            value = time_utils.str2datetime_by_format(value)
        except ValueError as e:
            raise errors.InvalidArgsError(f'{name}格式不正确(yyyy-mm-dd HH:MM:SS)')
        return value

    @classmethod
    def check_date(cls, name, value, condition):
        '''
        检查日期格式
        '''
        try:
            value = time_utils.str2date(value)
        except ValueError as e:
            raise errors.InvalidArgsError(f'{name}格式不正确(yyyy-mm-dd)')
        return value

    @classmethod
    def check_bool(cls, name, value, condition):
        if value not in (True, False):
            raise errors.InvalidArgsError(f'{name}需要bool值')
        return value

    @classmethod
    def check_dict(cls, name, value, condition):
        if not isinstance(value, dict):
            raise errors.InvalidArgsError(f'{name}需要字典类型')
        return value
