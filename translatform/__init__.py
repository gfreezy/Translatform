from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.init import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('toc', '/')
    config.add_route('chapter', '/{chapter}/')
    config.add_route('translation',
                     '/{chapter}/{para_id}/translation/')
    config.add_route('translation_history',
                     '/{chapter}/{para_id}/translation/history/')
    config.add_route('comment',
                     '/{chapter}/{para_id}/comment/')
    config.add_route('all_comment',
                     '/{chapter}/{para_id}/comment/all/')

    config.scan()
    return config.make_wsgi_app()
