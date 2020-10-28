import redis


class RedisCli:
    def __init__(self, host, port, db):
        self.db = redis.Redis(host, port, db)
