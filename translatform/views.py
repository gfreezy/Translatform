from pyramid.view import (
    view_config,
    view_defaults,
    notfound_view_config,
    )
from pyramid.httpexceptions import HTTPNotFound

from .models.init import DBSession
from .models.chapter import Chapter
from .models.paragraph import (
    Paragraph,
    ParagraphTranslation,
    ParagraphComment,
    )

from .utils.generate_translated_html import generate


@notfound_view_config(append_slash=True)
def notfound(request):
    return HTTPNotFound('Not found, bro.')


@view_config(route_name='index', renderer='templates/index.mako')
def index(request):
    return dict()


@view_defaults(route_name='regenerate')
class Regenerate(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', renderer='templates/regenerate.mako')
    def get(self):
        return dict()

    @view_config(request_method='POST', renderer='json')
    def post(self):
        action = self.request.params.get('action')
        if action == 'regenerate':
            generate()
            return dict(status='ok')
        return dict(status='error')


class ChapterView(object):
    def __init__(self, request):
        self.request = request
        self.chap_name = request.matchdict.get('chapter')
        self.chapter = DBSession.query(Chapter).filter_by(name=self.chap_name).first()

    @view_config(route_name='chapter', renderer='templates/chapter.mako')
    def normal_chapter(self):
        if not self.chapter:
            raise HTTPNotFound('chapter %s not found' % self.chap_name)
        return dict(content=self.chapter)

    @view_config(route_name='translated_chapter', renderer='json')
    def translated_chapter(self):
        if not self.chapter:
            return dict(status='error', msg='chapter not found')
        return dict(
            status='ok',
            paragraphs=dict([(para.identity, para.latest_translation()) for para in self.chapter.paragraphs]))


class TranslationBase(object):
    def __init__(self, request):
        self.request = request
        self.chap_id = request.matchdict.get('chapter')
        self.para_id = request.matchdict.get('para_id')
        self.para = DBSession.query(Paragraph).filter_by(
            chap_id=self.chap_id, identity=self.para_id).first()


@view_defaults(route_name='translation')
class Translation(TranslationBase):
    @view_config(request_method='GET',
                 renderer='json')
    def get(self):
        if not self.para:
            return dict(status='error',
                        msg='Para. %s not exisits' % self.para_id)

        return dict(status='ok',
                    english=self.para.english,
                    translation=self.para.latest_translation())

    @view_config(request_method='POST',
                 renderer='json')
    def post(self):
        if not self.para:
            return dict(status='error',
                        msg='Para. %s not exisits' % self.para_id)

        translation = self.request.params.get('translation')
        if not translation:
            return dict(status='error',
                        msg='no translation')
        self.para.add_translation(translation)
        return dict(status='ok')


class AllTranslation(TranslationBase):
    @view_config(route_name='translation_history',
                 renderer='json')
    def get(self):
        return dict(status='ok',
                    translations=self.para.all_translations())



class CommentView(object):
    def __init__(self, request):
        self.request = request
        self.chap_id = request.matchdict.get('chapter')
        self.para_id = request.matchdict.get('para_id')
        self.para = DBSession.query(Paragraph).filter_by(
            chap_id=self.chap_id, identity=self.para_id).first()

    @view_config(route_name='comment',
                 request_method='POST',
                 renderer='json')
    def new_comment(self):
        if not self.para:
            return dict(status='error',
                        msg='Para. %s not exisits' % self.para_id)

        comment = self.request.params.get('comment')
        author = self.request.params.get('author')
        if not comment or not author:
            return dict(status='error',
                        msg='no comment or no author')
        self.para.add_comment(comment, author)
        return dict(status='ok')

    @view_config(route_name='all_comment',
                 request_method='GET',
                 renderer='json')
    def all_comment(self):
        if not self.para:
            return dict(status='error',
                        msg='chaper not found')

        return dict(
            status='ok',
            comments=self.para.all_comments())
