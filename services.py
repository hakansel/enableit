import abc


class BaseClientService(abc.ABC):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance._init_client()
        return cls.instance

    @abc.abstractmethod
    def get_client(self):
        """return connection of concrete service"""
        pass

    @abc.abstractmethod
    def _init_client(self):
        """initialize and set the client with proper parameters"""
        pass


class MinioClientService(BaseClientService):

    def get_client(self):
        print('You got it Minio client..')
        pass

    def _init_client(self):
        print('Minio Client initialized...')
        pass


class RedisClientService(BaseClientService):

    def get_client(self):
        print('You got it Redis client..')
        pass

    def _init_client(self):
        print('Redis Client initialized...')
        pass
