from services import MinioClientService, RedisClientService


class AppContext(object):
    __minio_client_service = None
    __redis_client_service = None

    @classmethod
    def get_minio_client_service(cls) -> MinioClientService:
        return cls.__minio_client_service

    @classmethod
    def set_minio_client_service(cls, value: MinioClientService):
        cls.__minio_client_service = value

    @classmethod
    def get_redis_client_service(cls) -> RedisClientService:
        return cls.__redis_client_service

    @classmethod
    def set_redis_client_service(cls, value: RedisClientService):
        cls.__redis_client_service = value
