import json

from librarian_core.contrib.cache.decorators import invalidates


def parse(db, path):
    if not _is_json_file(path):
        return

    try:
        file = open(path)
    except IOError:
        return

    json_data = json.load(file)
    _import_data(path, db, json_data)


@invalidates(prefix='football_data')
def _import_data(path, db, data):
    if _is_leagues_file(path):
        _import_leagues(db, json_data)

    elif _is_league_fixtures_file(path):
        _import_league_fixtures(db, json_data)

    elif _is_league_rankings_file(path):
        _import_league_rankings(db, json_data)


def _is_json_file(path):
    return path[-5:] == '.json'


def _is_leagues_file(path):
    path_elems = path.split('/')
    file_name = path_elems[-1]
    return file_name == 'leagues_list.json'


def _is_league_fixtures_file(path):
    path_elems = path.split('/')
    file_name = path_elems[-1]
    file_name_elems = file_name.split('_')
    
    if len(file_name_elems) == 3:
        
        if file_name_elems[0] != 'league':
            return False

        try:
            int(file_name_elems[1])
        except:
            return False

        if file_name_elems[2] != 'fixtures.json':
            return False

        return True
    return False


def _is_league_rankings_file(path):
    path_elems = path.split('/')
    file_name = path_elems[-1]
    file_name_elems = file_name.split('_')
    
    if len(file_name_elems) == 3:
        
        if file_name_elems[0] != 'league':
            return False

        try:
            int(file_name_elems[1])
        except:
            return False

        if file_name_elems[2] != 'rankings.json':
            return False

        return True
    return False


def _get_league_dict(league):
    return { 'id': league['id'],
             'name': league['caption'],
             'current_matchday': league['currentMatchday'],
             'number_of_matchdays': league['numberOfMatchdays']
    }


def _get_fixture_dict(fixture):
    return { 'id': _get_fixture_id(fixture),
             'league_id': _get_league_id_from_fixture(fixture),
             'home_team_name': fixture['homeTeamName'],
             'away_team_name': fixture['awayTeamName'],
             'status': fixture['status'],
             'date': fixture['date'],
             'matchday': fixture['matchday'],
             'home_team_goals': _get_fixture_home_goals(fixture),
             'away_team_goals': _get_fixture_away_goals(fixture)
    }


def _get_team_dict(team, league_id):
    return { 'id': _get_team_id(team),
             'league_id': league_id,
             'name': team['teamName'],
             'position': team['position'],
             'wins': team['wins'],
             'losses': team['losses'],
             'draws': team['draws']
    }


def _get_league_id_from_fixture(fixture):
    links = fixture['_links']
    soccerseason = links['soccerseason']
    soccerseason_href = soccerseason['href']
    soccerseason_href_elems = soccerseason_href.split('/')
    return int(soccerseason_href_elems[-1])


def _get_league_id_from_rankings_links(links):
    soccerseason = links['soccerseason']
    soccerseason_href = soccerseason['href']
    soccerseason_href_elems = soccerseason_href.split('/')
    return int(soccerseason_href_elems[-1])


def _get_fixture_id(fixture):
    links = fixture['_links']
    self = links['self']
    self_href = self['href']
    self_href_elems = self_href.split('/')
    return int(self_href_elems[-1])


def _get_team_id(team):
    links = team['_links']
    team = links['team']
    team_href = team['href']
    team_href_elems = team_href.split('/')
    return int(team_href_elems[-1])


def _get_fixture_home_goals(fixture):
    result = fixture['result']
    home_goals = result['goalsHomeTeam']
    return home_goals


def _get_fixture_away_goals(fixture):
    result = fixture['result']
    away_goals = result['goalsAwayTeam']
    return away_goals


def _import_leagues(db, data):
    cols = ['id', 'name', 'current_matchday', 'number_of_matchdays']
    query = db.Insert('leagues', cols=cols)
    vals = (_get_league_dict(league) for league in data)
    db.executemany(query, vals)


def _import_league_fixtures(db, data):
    cols = ['id', 'league_id', 'home_team_name', 'away_team_name', 'status',
            'date', 'matchday', 'home_team_goals', 'away_team_goals']
    query = db.Insert('fixtures', cols=cols)
    vals = (_get_fixture_dict(fixture) for fixture in data['fixtures'])
    db.executemany(query, vals)


def _import_league_rankings(db, data):
    cols = ['id', 'league_id', 'name', 'position', 'wins', 'losses', 'draws']
    query = db.Insert('teams', cols=cols)
    league_id = _get_league_id_from_rankings_links(data['_links'])
    vals = (_get_team_dict(team, league_id) for team in data['standing'])
    db.executemany(query, vals)