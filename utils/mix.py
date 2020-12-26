import string
from random import choices
from random import randint
from random import shuffle


def gen_password(level=2, specil='!@#$%^&*()_+-=', length=8):
    if length < 6:
        raise errors.CommonError('密码长度至少为6位')
    digit = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    specil = specil
    result = choices(digit, k=randint(1,2))
    if level == 1:
        result.extend(choices(digit, k=length-len(result)))
    elif level == 2:
        result.extend(choices(upper, k=randint(1,2)))
        result.extend(choices(lower, k=length-len(result)))
    elif level == 3:
        result.extend(choices(specil, k=randint(1,2)))
        result.extend(choices(lower, k=length-len(result)))
    else:
        pass
    shuffle(result)
    return ''.join(result)
