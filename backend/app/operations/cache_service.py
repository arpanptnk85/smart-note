import json
import redis
from typing import List, Dict, Set, Any
from abc import ABC, abstractmethod

redis_service = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
)

class CacheServiceBP(ABC):

    @abstractmethod
    def set_info(self, hkey: str, hdata: Dict[str, str], expiry: int):
        pass

    @abstractmethod
    def get_info(self, hkey: str):
        pass

class UserCacheService(CacheServiceBP):

    def __init__(self) -> None:
        self.cache_name = 'user_service'

    def __repr__(self) -> str:
        return f"UserCacheService(cache_name={self.cache_name})"

    def set_info(self, hkey: str, hdict: Dict[str, str], expiry: int = 20) -> None:
        if hkey not in hdict:
            raise KeyError(f"Key '{hkey}' not found in data.")
        _key = hdict.get(hkey)
        try:
            redis_service.hset(name=self.cache_name, key=_key, value=json.dumps(hdict))
            redis_service.expire(name=self.cache_name, time=expiry)
            print(f"Cache {self.cache_name} cached with TTL of {expiry} seconds.")
        except Exception as e:
            print(f'Error adding to redis hash {e}')

    def get_info(self, hkey: str) -> None:
        response = redis_service.hget(name=self.cache_name, key=hkey)
        if response is None:
            return None
        return json.loads(response)

user_cache = UserCacheService()