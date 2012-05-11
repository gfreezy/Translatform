#!/usr/bin/env python
#coding: utf8
import hashlib
import re

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
