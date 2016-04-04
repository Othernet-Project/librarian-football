from bottle import request
from bottle_utils.i18n import i18n_url
from bottle_utils.html import urlunquote

from librarian_ui.paginator import Paginator
from librarian_core.contrib.templates.renderer import view
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
        filter_dict = {}
    else:
        filter_dict = {'name': q}

    db = request.db['football']
    item_count = football.get_leagues_count(db, filter_dict = filter_dict)
    page = Paginator.parse_page(request.params)
    pager = pager = Paginator(item_count, page, per_page = 10)
    leagues = football.get_leagues(db, pager, filter_dict = filter_dict)
    
    return dict(leagues = leagues,
                pager = pager,
                base_path = i18n_url('leagues:list'),
                view = request.params.get('view'))


@view('football/league_detail')
def league_detail(league_id):
    db = request.db['football']
    (league, fixtures, teams) = football.get_league(db, league_id)

    return dict(league = league,
                fixtures = fixtures,
                teams = teams,
                base_path = i18n_url('league:detail', league_id = league_id),
                view = request.params.get('view'))


def routes(config):
    return (
        ('leagues:list', leagues_list, 'GET', '/football/leagues/', {}),
        ('league:detail', league_detail, 'GET', '/football/leagues/<league_id>', {})
    )