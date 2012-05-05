#coding: utf8
import os
import sys
import transaction

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


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        chapter1 = Chapter(
            title='title 1',
            paragraphs=[
                Paragraph(
                    english='paragraph1',
                    para_number=1,
                    translations=[
                        ParagraphTranslation(
                            author='author1',
                            translation=u'段落1'
                            ),
                        ParagraphTranslation(
                            author='author1',
                            translation=u'段落1.'
                            ),
                        ParagraphTranslation(
                            author='author2',
                            translation=u'段落1..'
                            ),
                        ],
                    comments=[
                        ParagraphComment(
                            author='author3',
                            comment='comment1'
                            ),
                        ParagraphComment(
                            author='author1',
                            comment='comment2'
                            ),
                        ParagraphComment(
                            author='author3',
                            comment='comment3'
                            ),
                        ]),
                Paragraph(
                    english='paragraph2',
                    para_number=2,
                    translations=[
                        ParagraphTranslation(
                            author='author1',
                            translation=u'段落1'
                            ),
                        ParagraphTranslation(
                            author='author1',
                            translation=u'段落1.'
                            ),
                        ParagraphTranslation(
                            author='author2',
                            translation=u'段落1..'
                            ),
                        ],
                    comments=[
                        ParagraphComment(
                            author='author3',
                            comment='comment1'
                            ),
                        ParagraphComment(
                            author='author1',
                            comment='comment2'
                            ),
                        ParagraphComment(
                            author='author3',
                            comment='comment3'
                            ),
                        ]),
                ])

        chapter2 = Chapter(
            title='title 2',
            paragraphs=[
                Paragraph(
                    english='paragraph1',
                    para_number=1,
                    translations=[
                        ParagraphTranslation(
                            author='author1',
                            translation=u'段落1'
                            ),
                        ParagraphTranslation(
                            author='author1',
                            translation=u'段落1.'
                            ),
                        ParagraphTranslation(
                            author='author2',
                            translation=u'段落1..'
                            ),
                        ],
                    comments=[
                        ParagraphComment(
                            author='author3',
                            comment='comment1'
                            ),
                        ParagraphComment(
                            author='author1',
                            comment='comment2'
                            ),
                        ParagraphComment(
                            author='author3',
                            comment='comment3'
                            ),
                        ])
                ])
        DBSession.add(chapter1)
        DBSession.add(chapter2)
