"""This file contain custom useful modules"""
import uuid
import glob
from gitcdn_prj.settings import STATICFILES_DIRS
from os.path import basename


def unamer(*args, **kwargs):
    """this function will check the statich dirs and base on files on there make uniq name
    :return uniq string
    """

    files = []
    for dir in STATICFILES_DIRS:
        for file in (glob.glob(f'{dir}/*')):
            files.append(basename(file)[:basename(file).find('.')])

    choos = str(uuid.uuid4())
    while choos in files:
        choos = str(uuid.uuid4())

    return choos
