from pyramid.view import (
    view_config,
    view_defaults,
    )
from pyramid.httpexceptions import HTTPNotFound

from .models.init import DBSession
from .models.chapter import Chapter
from .models.paragraph import (
    Paragraph,
    ParagraphTranslation,
    ParagraphComment,
    )


@view_config(route_name='toc', renderer='templates/toc.mako')
def toc(request):
    toc = DBSession.query(Chapter).filter_by(name='index').first()
    return dict(content=toc)


@view_config(route_name='chapter', renderer='templates/chapter.mako')
def chapter(request):
    chap_name = request.matchdict.get('chapter')
    chapter = DBSession.query(Chapter).filter_by(name=chap_name).first()
    if not chapter:
        raise HTTPNotFound('chapter %s not found' % chap_name)
    return dict(content=chapter)


class TranslationBase(object):
    def __init__(self, request):
        self.request = request
        self.chap_id = request.matchdict.get('chapter')
        self.para_id = request.matchdict.get('para_id')
        self.para = DBSession.query(Paragraph).filter_by(
            chap_id=self.chap_id, identity=self.para_id).first()
        if not self.para:
            raise HTTPNotFound('Para. %s not exisits' % self.para_id)


@view_defaults(route_name='translation')
class Translation(TranslationBase):
    @view_config(request_method='GET',
                 renderer='json')
    def get(self):
        return dict(english=self.para.english,
                    translation=self.para.latest_translation())

    @view_config(request_method='POST',
                 renderer='json')
    def post(self):
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
        return dict(translations=self.para.all_translations())


@view_config(route_name='comment',
             request_method='POST')
def new_comment(request):
    pass


@view_config(route_name='all_comment',
             request_method='GET',
             renderer='json')
def all_comment(request):
    pass
