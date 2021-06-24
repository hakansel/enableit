import abc
from typing import Optional, Generic, TypeVar

from minio import Minio
from redis import Redis

T = TypeVar("T")


class BaseClientService(abc.ABC, Generic[T]):
    """
        T is the concrete client
    """

    _client: T = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance') or not cls.instance:
            try:
                cls.instance = super().__new__(cls)
                print("Initialization is starting: {}".format(type(cls.instance).__name__))
                cls.instance._init_client()
                print("Initialization is completed: {}".format(type(cls.instance).__name__))
            except Exception as e:
                print("Initialization failed: {} caused by: {}".format(type(cls.instance).__name__, e))
                cls.instance = None
        return cls.instance

    @abc.abstractmethod
    def get_client(self) -> Optional[T]:
        """return connection of concrete service"""
        return self._client

    @abc.abstractmethod
    def _init_client(self):
        """initialize and set the client with proper parameters"""
        pass


class MinioClientService(BaseClientService[Minio]):
    _client: Minio = None

    def get_client(self) -> Optional[Minio]:
        return self._client

    def _init_client(self):
        pass


class RedisClientService(BaseClientService[Redis]):
    _client: Redis = None

    def get_client(self) -> Optional[Redis]:
        return self._client

    def _init_client(self):
        pass
