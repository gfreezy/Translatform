#!/usr/bin/env python
#coding: utf8
import datetime
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    )
from sqlalchemy.orm import relationship

from .init import (
    Base,
    DBSession,
    )


class Paragraph(Base):
    __tablename__ = 'paragraph'
    id = Column(Integer, primary_key=True)
    para_number = Column(Integer,
                     nullable=False,
                     index=True)
    english = Column(Text)
    translations = relationship('ParagraphTranslation',
                               backref='english')
    comments = relationship('ParagraphComment',
                            backref='paragraph')
    chap_id = Column(ForeignKey('chapter.id'), nullable=False)

    def latest_translation(self):
        print self.translations
        return self.translations[-1].translation

    def add_translation(self, translation):
        t = ParagraphTranslation(author='system',
                                 translation=translation,
                                 para_id=self.id)
        DBSession.add(t)

    def all_translations(self):
        translations = DBSession.query(ParagraphTranslation).filter_by(para_id=self.id).order_by('id desc').all()
        return [t.translation for t in translations]


class ParagraphTranslation(Base):
    __tablename__ = 'paragraph_translation'
    id = Column(Integer, primary_key=True)
    author = Column(Text, nullable=False)
    time = Column(DateTime, default=datetime.datetime.now)
    translation = Column(Text, nullable=False)
    para_id = Column(ForeignKey('paragraph.id'), nullable=False)


class ParagraphComment(Base):
    __tablename__ = 'paragraph_comment'
    id = Column(Integer, primary_key=True)
    author = Column(Text, nullable=False)
    time = Column(DateTime, default=datetime.datetime.now)
    comment = Column(Text, nullable=False)
    para_id = Column(ForeignKey('paragraph.id'), nullable=False)
