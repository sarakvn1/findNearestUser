
def cache_key_maker(key, key_prefix, version):
    return '{key_prefix}:{key}'.format(
        key_prefix=key_prefix,
        key=key
    )
