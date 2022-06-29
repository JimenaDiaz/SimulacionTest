from .conneccion import redis
from redis.exceptions import ResponseError


def save_hash(key: str, data: dict):
    try:
        print('**', key,'11', data)
        redis.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)


def get_hash(key: str):
    try:
        return redis.hgetall(name=key)
    except ResponseError as e:
        print(e)

def delete_hash(key: str, keys: list):
    try:
        redis.hdel(key, *keys)
    except ResponseError as e:
        print(e)
    