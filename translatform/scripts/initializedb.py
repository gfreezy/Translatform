#coding: utf8
import os
import sys
import transaction
import glob
import simplejson
import codecs

from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models.init import (
    DBSession,
    Base,
    )
from ..models.chapter import Chapter
from ..models.paragraph import (
    Paragraph,
    ParagraphTranslation,
    ParagraphComment,
    )
from ..conf import DOC_PATH
from ..utils.rst import sphinx_build


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def insert_chapters():
    path = os.path.join(DOC_PATH, 'json')
    pattern = os.path.join(path, '*.fjson')
    for p in glob.glob(pattern):
        with codecs.open(p, encoding='utf8') as f:
            j = simplejson.loads(f.read())
            if not j.get('body'):
                continue
            chap = Chapter(
                title=j.get('title'),
                body=j.get('body'),
                toc=j.get('toc'),
                display_toc=j.get('display_toc'),
                current_page_name=j.get('current_page_name'),
                parents=simplejson.dumps(j.get('parents')),
                prev=simplejson.dumps(j.get('prev')),
                next=simplejson.dumps(j.get('next')),
                sourcename=j.get('sourcename'),
                )
            DBSession.add(chap)
    transaction.commit()


def insert_paragraphs(chapter):
    path = os.path.join(DOC_PATH, 'pot')
    filename = '.'.join((os.path.splitext(chapter.sourcename)[0], 'pot'))
    fullname = os.path.join(path, filename)
    for para_txt in get_paragraphs(fullname):
        para = Paragraph(para_txt)
        chapter.paragraphs.append(para)

    DBSession.merge(chapter)


def get_paragraphs(fullname):
    if not os.path.exists(fullname):
        return
    with codecs.open(fullname, encoding='utf8') as f:
        for line in f:
            if 'msgid' in line:
                msgtype, msg = line.split(' ', 1)
                msg = msg.strip('" \n')
                msg = msg.replace(r'\"', '"')
                yield msg


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    sphinx_build('json', builder='json')
    sphinx_build('pot', builder='gettext')
    insert_chapters()

    with transaction.manager:
        for chapter in DBSession.query(Chapter).all():
            insert_paragraphs(chapter)
