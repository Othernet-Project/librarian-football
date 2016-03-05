import football

from bottle import request
from bottle_utils.i18n import i18n_url
from bottle_utils.ajax import roca_view
from bottle_utils.html import urlunquote
from librarian_core.contrib.templates.renderer import view
from librarian_core.contrib.templates.renderer import template
from librarian_core.contrib.cache.decorators import cached
from librarian_ui.paginator import Paginator


EXPORTS = {
    'routes': {'required_by': ['librarian_core.contrib.system.routes.routes']}
}


@view('football/leagues_list')
@cached(prefix='leagues_list')
def leagues_list():
    try:
        q = urlunquote(request.params['q'])
    except KeyError:
        is_search = False
    else:
        is_search = True

    db = request.db['football']
    if is_search:
        item_count = football.get_leagues_count(db, dict={'name': q})
        page = Paginator.parse_page(request.params)
        pager = pager = Paginator(item_count, page, per_page=10)
        leagues = football.get_leagues(db, pager, dict={'name': q}, fixtures=False, teams=False)

    else:
        item_count = football.get_leagues_count(db)
        page = Paginator.parse_page(request.params)
        pager = pager = Paginator(item_count, page, per_page=10)
        leagues = football.get_leagues(db, pager, fixtures=False, teams=False)
    
    return dict(leagues=leagues,
                pager=pager,
                is_search=is_search,
                base_path=i18n_url('leagues:list'),
                view=request.params.get('view'))


def routes(config):
    return (
        ('leagues:list', leagues_list, 'GET', '/football/leagues/', {}),
    )