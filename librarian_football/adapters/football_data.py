import json


def parse(db, files, dirs):
    """
    Reads in all football data files and imports the data
    into the database.
    """

    leagues_file = _find_leagues_file(files)
    fixture_files = _find_fixture_files(files)
    rankings_files = _find_rankings_files(files)

    _import_leagues(db, leagues_file)
    _import_fixtures(db, fixture_files)
    _import_rankings(db, rankings_files)


def _find_leagues_file(files):
    file = None
    for f in files:
        if _is_leagues_file(f.path):
            file = f
            break
    return file


def _find_fixture_files(files):
    fixture_files = []
    for f in files:
        if _is_fixture_file(f.path):
            fixture_files.append(f)
    return fixture_files


def _find_rankings_files(files):
    rankings_files = []
    for f in files:
        if _is_rankings_file(f.path):
            rankings_files.append(f)
    return rankings_files


def _is_leagues_file(path):
    path_elems = path.split('/')
    file_name = path_elems[-1]
    return file_name == 'leagues_list.json'


def _is_fixture_file(path):
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


def _is_rankings_file(path):
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


def _import_leagues(db, file):
    """
    Import the new leagues into the database
    """

    file_path = file.path
    with open(file_path) as f:
        json_leagues = json.load(f)
        cols = ['id', 'name', 'short_name', 'current_matchday', 'number_of_games',
                'number_of_matchdays', 'last_updated', 'year', 'number_of_teams']
        query = db.Insert('leagues', cols=cols)
        vals = (_get_league_dict(league) for league in json_leagues)
        db.executemany(query, vals)


def _import_fixtures(db, files):
    """
    Import the new fixtures into the database
    """

    for file in files:
        file_path = file.path
        with open(file_path) as f:
            json_fixtures = json.load(f)
            if json_fixtures.has_key('fixtures'):
                cols = ['id', 'league_id', 'home_team_name', 'away_team_name', 'status',
                        'date', 'matchday', 'home_team_goals', 'away_team_goals']
                query = db.Insert('fixtures', cols=cols)
                vals = (_get_fixture_dict(fixture) for fixture in json_fixtures['fixtures'])
                db.executemany(query, vals)


def _import_rankings(db, files):
    """
    Import the new rankings data into the database
    """
    
    for file in files:
        file_path = file.path
        with open(file_path) as f:
            json_rankings = json.load(f)
            if json_rankings.has_key('standing') and json_rankings.has_key('_links'):
                cols = ['id', 'league_id', 'name', 'position', 'wins', 'losses', 'draws']
                query = db.Insert('teams', cols=cols)
                league_id = _get_league_id_from_rankings_links(json_rankings['_links'])
                vals = (_get_team_dict(team, league_id) for team in json_rankings['standing'])
                db.executemany(query, vals)


def _get_league_dict(league):
    return { 'id': league['id'],
             'name': league['caption'],
             'short_name': league['league'],
             'current_matchday': league['currentMatchday'],
             'number_of_games': league['numberOfGames'],
             'number_of_matchdays': league['numberOfMatchdays'],
             'last_updated': league['lastUpdated'],
             'year': league['year'],
             'number_of_teams': league['numberOfTeams']
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