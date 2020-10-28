from functools import wraps
from operator import itemgetter
from redis.exceptions import LockError
from django.conf import settings

from base import errors
from utils.redis_cli import RedisCli


class Onlyone:

    def __init__(self):
        redis_host = settings.ONLYONE_REDIS_HOST
        redis_port = settings.ONLYONE_REDIS_PORT
        redis_db = settings.ONLYONE_REDIS_DB
        self.redis_cli = RedisCli(redis_host, redis_port, redis_db)

    @classmethod
    def gen_key(cls, prifix, params_str, key_str, args, kwargs):
        param_dict = {}
        key_dict = {}
        params = params_str.split(':')
        keys = key_str.split(':')
        for k, v in zip(params, args):
            param_dict[k] = v
        kvs = params[len(args):]
        for kv in kvs:
            k, *vs = kv.split('=')
            if k in kwargs.keys():
                v = kwargs[k]
            else:
                v = vs[0]
            param_dict[k] = v
        for key in keys:
            key_dict[key] = param_dict[key]
        key = 'rurality:lock:{}:{}'.format(prifix, sorted(key_dict.items(), key=itemgetter(0)))
        return key

    def lock(self, prifix, params_str, key_str, timeout=10):
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                key = self.gen_key(prifix, params_str, key_str, args, kwargs)
                try:
                    with self.redis_cli.db.lock(key, timeout=timeout, blocking_timeout=timeout) as lock:
                        result = func(*args, **kwargs)
                except LockError:
                    raise errors.CommonError('不允许同时操作')
                return result
            return wrapper
        return decorate


onlyone = Onlyone()
