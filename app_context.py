from services import MinioServiceClient, RedisServiceClient


class AppContext(object):

    def __init__(self):
        self.__minio_client = None
        self.__redis_client = None

    @property
    def minio_client(self) -> MinioServiceClient:
        return self.__minio_client

    @property
    def redis_client(self) -> RedisServiceClient:
        return self.__redis_client

    @minio_client.setter
    def minio_client(self, value: MinioServiceClient):
        self.__minio_client = value

    @redis_client.setter
    def redis_client(self, value: RedisServiceClient):
        self.__redis_client = value
