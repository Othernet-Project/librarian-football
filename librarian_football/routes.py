from bottle import request
from bottle_utils.i18n import i18n_url
from bottle_utils.ajax import roca_view
from bottle_utils.html import urlunquote

from librarian_ui.paginator import Paginator
from librarian_core.contrib.templates.renderer import view
from librarian_core.contrib.cache.decorators import cached
from librarian_core.contrib.templates.renderer import template

from . import football


EXPORTS = {
    'routes': {'required_by': ['librarian_core.contrib.system.routes.routes']}
}


@view('football/leagues_list')
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


@view('football/league_detail')
def league_detail(id):
    db = request.db['football']
    league = football.get_league(db, id)
    return dict(league=league,
                base_path=i18n_url('league:detail', id=id),
                view=request.params.get('view'))


def routes(config):
    return (
        ('leagues:list', leagues_list, 'GET', '/football/leagues/', {}),
        ('league:detail', league_detail, 'GET', '/football/leagues/<id>', {})
    )