import hashlib


async def hash_string(input_string: str):
    hash_obj = hashlib.new("sha1")
    hash_obj.update(input_string.encode('utf-8'))
    return hash_obj.hexdigest()
