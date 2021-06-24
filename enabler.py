import functools


def enable_minio(func):
    """make sure minio enabled before func is called"""

    @functools.wraps(func)
    def wrapper_enable_minio(self, *args, **kwargs):
        from services import MinioClientService
        from app_context import AppContext
        AppContext.set_minio_client_service(MinioClientService())
        return func(self, *args, **kwargs)

    return wrapper_enable_minio


def enable_redis(func):
    """make sure redis enabled before func is called"""

    @functools.wraps(func)
    def wrapper_enable_minio(self, *args, **kwargs):
        from services import RedisClientService
        from app_context import AppContext
        AppContext.set_redis_client_service(RedisClientService())
        return func(self, *args, **kwargs)

    return wrapper_enable_minio
