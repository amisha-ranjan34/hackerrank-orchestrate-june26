# utils/cache.py

from diskcache import Cache

cache = Cache("./cache")


def get_cache(key):

    if key in cache:
        return cache[key]

    return None


def set_cache(
        key,
        value,
        expire=86400
):

    cache.set(
        key,
        value,
        expire=expire
    )