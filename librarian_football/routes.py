import os

from bottle import request
from bottle_utils.i18n import i18n_url
from librarian_core.contrib.templates.renderer import view
from adapters.football_data import League


EXPORTS = {
    'routes': {'required_by': ['librarian_core.contrib.system.routes.routes']}
}


@view('football/football')
def football_scores():
    db = request.db['football']
    q = db.Select(sets='leagues')
    leagues_db = db.fetchall(q)

    leagues = []
    for l in leagues_db:
        name = l[1]
        league = League(name, None)
        leagues.append(league)

    leagues.sort(key=lambda x: x.name)

    return dict(leagues=leagues,
    	        base_path=i18n_url('football'),
                view=request.params.get('view'))


def routes(config):
    return (
        ('football:scores', football_scores, 'GET', '/football/', {}),
    )