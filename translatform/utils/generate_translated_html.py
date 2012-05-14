#!/usr/bin/env python
#coding: utf8
import os
import sys
import shutil
import glob
import codecs
import subprocess

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings

from ..models.init import DBSession
from ..models.paragraph import Paragraph
from ..conf import DOC_PATH
from .rst import (clean_format, md5, clean_space, sphinx_build, mkdirs)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def get_identity(line):
    msgtype, msg = line.split(' ', 1)
    msg = msg.strip('" \n')
    msg = msg.replace('\\"', '"')
    plain = clean_format(msg)
    return md5(clean_space(plain))


def replace_translation(txt, identity):
    para = DBSession.query(Paragraph).filter_by(identity=identity).first()
    if not para:
        return txt
    translation = para.latest_translation()
    if not translation:
        return txt
    return 'msgstr "%s"\n' % translation


def translate_to_po(path=DOC_PATH):
    po_path = os.path.join(path, 'po')
    pot_path = os.path.join(path, 'pot')

    mkdirs(po_path)
    pattern = os.path.join(pot_path, '*.pot')
    for p in glob.glob(pattern):
        filename = os.path.basename(p)
        po_name = '.'.join((os.path.splitext(filename)[0], 'po'))
        po_fullname = os.path.join(po_path, po_name)
        with codecs.open(p, encoding='utf8') as pot, \
                codecs.open(po_fullname, 'w', encoding='utf8') as po:
            identity = None
            for line in pot:
                if 'msgstr' in line:
                    if identity:
                        line = replace_translation(line, identity)
                        identity = None
                elif 'msgid' in line:
                    identity = get_identity(line)

                po.write(line)


def convert_to_mo(path=DOC_PATH):
    po_path = os.path.join(path, 'po')
    mo_path = os.path.join(path, 'translated/cn/LC_MESSAGES/')
    mkdirs(mo_path)
    pattern = os.path.join(po_path, '*.po')
    for p in glob.glob(pattern):
        filename = os.path.basename(p)
        mo_name = os.path.splitext(filename)[0]+'.mo'
        target = os.path.join(mo_path, mo_name)
        cmd = ['msgfmt', p, '-o', target]
        subprocess.call(cmd)


def generate():
    translate_to_po()
    convert_to_mo()
    sphinx_build('html_cn', lang='cn')
    sphinx_build('html_en', lang='en')


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)

    config_uri = argv[1]
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    generate()


if __name__ == '__main__':
    main()

