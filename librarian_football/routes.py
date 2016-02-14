import os

from bottle import request
from bottle_utils.i18n import i18n_url
from librarian_core.contrib.templates.renderer import view
from adapters import xmlsoccer_demo as adapter

EXPORTS = {
    'routes': {'required_by': ['librarian_core.contrib.system.routes.routes']}
}


@view('football/football')
def football_scores():
    key = request.app.config['football.xmlsoccer_demo_key']
    leagues = adapter.get_all_leagues(key)

    return dict(leagues=leagues,
    	        base_path=i18n_url('football'),
                view=request.params.get('view'))


def routes(config):
    return (
        ('football:scores', football_scores, 'GET', '/football/', {}),
    )