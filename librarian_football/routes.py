import football

from bottle import request
from bottle_utils.i18n import i18n_url
from librarian_core.contrib.templates.renderer import view
from librarian_core.contrib.cache.decorators import cached


EXPORTS = {
    'routes': {'required_by': ['librarian_core.contrib.system.routes.routes']}
}


@view('football/football')
@cached(prefix='football_data')
def football_scores():
    db = request.db['football']
    leagues = football.get_all_leagues(db)
    leagues.sort(key=lambda x: x.name)
    
    return dict(leagues=leagues,
                base_path=i18n_url('football'),
                view=request.params.get('view'))


def routes(config):
    return (
        ('football:scores', football_scores, 'GET', '/football/', {}),
    )