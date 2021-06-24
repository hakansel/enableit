import functools


def enable_minio(func):
    """make sure minio enabled before func is called"""

    @functools.wraps(func)
    def wrapper_enable_minio(*args, **kwargs):
        from services import MinioServiceClient
        from app_context import AppContext
        AppContext.minio_client = MinioServiceClient()
        return func(*args, **kwargs)

    return wrapper_enable_minio


def enable_redis(func):
    """make sure redis enabled before func is called"""

    @functools.wraps(func)
    def wrapper_enable_minio(*args, **kwargs):
        from services import RedisServiceClient
        from app_context import AppContext
        AppContext.redis_client = RedisServiceClient()
        return func(*args, **kwargs)

    return wrapper_enable_minio
