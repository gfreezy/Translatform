#!/usr/bin/env python
#coding: utf8
import hashlib
import re

def clean_format(rst):
    txt = re.sub(r':.*?:`~(?:[a-zA-Z]+[.])+(.*?)`', r'\1', rst)
    txt = re.sub(r':.*?:`(.*?)`', r'\1', txt)
    txt = re.sub(r'`(.*?)`_', r'\1', txt)
    txt = re.sub(r'`(.*?)`', r'\1', txt)
    txt = re.sub(r'[*]{1,2}(.*?)[*]{1,2}', r'\1', txt)
    txt = re.sub(r'[`]{1,2}(.*?)[`]{1,2}', r'\1', txt)
    txt = txt.replace(r'::', ':')
    return txt


def md5(t):
    if isinstance(t, unicode):
        t = t.encode('utf8')
    return hashlib.md5(t).hexdigest()


def clean_space(txt):
    txt = re.sub(r'\s', '', txt)
    return txt
