import os

from bottle import request
from bottle_utils.i18n import i18n_url
from librarian_core.contrib.templates.renderer import view
from adapters import footballdata as adapter


EXPORTS = {
    'routes': {'required_by': ['librarian_core.contrib.system.routes.routes']}
}


@view('football/football')
def football_scores():
    key = request.app.config['football.footballdata_key']
    leagues = adapter.get_all_leagues(key)
    leagues.sort(key=lambda x: x.name)

    return dict(leagues=leagues,
    	        base_path=i18n_url('football'),
                view=request.params.get('view'))


def routes(config):
    return (
        ('football:scores', football_scores, 'GET', '/football/', {}),
    )