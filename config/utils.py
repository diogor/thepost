import hashlib


def make_filename(filename, request):
    return '{}.{}'.format(
        hashlib.sha224(filename.encode()).hexdigest(),
        filename.split(".")[-1:]
    )
