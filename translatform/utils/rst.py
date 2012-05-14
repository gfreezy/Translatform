#!/usr/bin/env python
#coding: utf8
import re
import os
import time
import shutil
import hashlib
import subprocess

from ..conf import DOC_PATH

def clean_format(rst):
    txt = rst.replace(u'“', '"')
    txt = txt.replace(u'”', '"')
    txt = txt.replace(u'‘', '\'')
    txt = txt.replace(u'’', '\'')
    txt = re.sub(r'::$', ':', txt)
    txt = re.sub(r':.+?:`[~](?:[a-zA-Z]+[.])*(.+?)`', r'\1', txt)
    txt = re.sub(r':.+?:`(.+?)`', r'\1', txt)

    txt = re.sub(r'[*]{1,2}(.+?)[*]{1,2}', r'\1', txt)
    txt = re.sub(r'[`]{1,2}(.+?)[\s]?(?:<.+?>)?[`]{1,2}[_]?', r'\1', txt)

    return txt


def md5(t):
    if isinstance(t, unicode):
        t = t.encode('utf8')
    return hashlib.md5(t).hexdigest()


def clean_space(txt):
    txt = re.sub(r'\s', '', txt)
    return txt


def mkdirs(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


class BackupFile(object):
    def __init__(self, filepath):
        self.old_name = filepath

    def __enter__(self):
        self.bak_name = self.old_name+str(time.time())
        shutil.move(self.old_name, self.bak_name)
        return self.bak_name

    def __exit__(self, type, value, traceback):
        shutil.move(self.bak_name, self.old_name)


def sphinx_build(target, builder='html', lang='en'):
    src = os.path.join(DOC_PATH, 'conf_%s.py' % lang)
    dest = os.path.join(DOC_PATH, 'conf.py')
    path = os.path.join(DOC_PATH, target)

    with BackupFile(dest):
        shutil.copy(src, dest)

        mkdirs(path)
        cmd = ['sphinx-build', '-b', builder, DOC_PATH, path]
        subprocess.call(cmd)
