from services import MinioClientService, RedisClientService


class AppContext(object):

    def __init__(self):
        self.__minio_client = None
        self.__redis_client = None

    @property
    def minio_client(self) -> MinioClientService:
        return self.__minio_client

    @property
    def redis_client(self) -> RedisClientService:
        return self.__redis_client

    @minio_client.setter
    def minio_client(self, value: MinioClientService):
        self.__minio_client = value

    @redis_client.setter
    def redis_client(self, value: RedisClientService):
        self.__redis_client = value
