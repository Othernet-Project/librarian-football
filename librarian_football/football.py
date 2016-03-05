class League(object):
    """docstring for League"""
    def __init__(self, params):
        super(League, self).__init__()
        self.id = params['id']
        self.name = params['name']
        self.short_name = params['short_name']
        self.number_of_games = params['number_of_games']
        self.current_matchday = params['current_matchday']
        self.number_of_matchdays = params['number_of_matchdays']
        self.last_updated = params['last_updated']
        self.year = params['year']
        self.number_of_teams = params['number_of_teams']
        self.fixtures = []
        self.teams = []


class Fixture(object):
    """docstring for Fixture"""
    def __init__(self, params):
        super(Fixture, self).__init__()
        self.id = params['id']
        self.home_team_name = params['home_team_name']
        self.away_team_name = params['away_team_name']
        self.status = params['status']
        self.date = params['date']
        self.matchday = params['matchday']
        self.home_team_goals = params['home_team_goals']
        self.away_team_goals = params['away_team_goals']


class Team(object):
    """docstring for Team"""
    def __init__(self, params):
        super(Team, self).__init__()
        self.id = params['id']
        self.name = params['name']
        self.position = params['position']
        self.wins = params['wins']
        self.losses = params['losses']
        self.draws = params['draws']
        

def _league_row_to_dict(row):
    return { "id": row[0],
             "name": row[1],
             "short_name": row[2],
             "number_of_games": row[3],
             "created": row[4],
             "current_matchday": row[5],
             "number_of_matchdays": row[6],
             "last_updated": row[7],
             "year": row[8],
             "number_of_teams": row[9]
    }


def _fixture_row_to_dict(row):
    return { "id": row[0],
             "league_id": row[1],
             "home_team_name": row[2],
             "away_team_name": row[3],
             "status": row[4],
             "date": row[5],
             "matchday": row[6],
             "home_team_goals": row[7],
             "away_team_goals": row[8],
             "created": row[9]
    }


def _team_row_to_dict(row):
    return { "id": row[0],
             "league_id": row[1],
             "name": row[2],
             "position": row[3],
             "wins": row[4],
             "losses": row[5],
             "draws": row[6],
             "created": row[7]
    }


def _get_league_fixtures(l_db, db):
    league_id = str(l_db[0])
    num_matchdays = l_db[4]

    fixtures = []
    for k in range(1, num_matchdays + 1):
        query = db.Select(sets='fixtures')
        query.where = 'league_id = ' + league_id
        query.where &= 'matchday = ' + str(k) 
        fixtures_db = db.fetchall(query)

        fixtures_k = []
        for f_db in fixtures_db:
            fixture = Fixture(_fixture_row_to_dict(f_db))
            fixtures_k.append(fixture)

        fixtures.append(fixtures_k)

    return fixtures


def _get_league_teams(l_db, db):
    query = db.Select(sets='teams')
    query.where = 'league_id = ' + str(l_db[0])
    teams_db = db.fetchall(query)

    teams = []
    for t_db in teams_db:
        team = Team(_team_row_to_dict(t_db))
        teams.append(team)

    return teams


def get_leagues(db, pager, dict={}, fixtures=True, teams=True):
    query = db.Select(sets='leagues')
    offset, limit = pager.items
    query.offset = offset
    query.limit = limit
    query.order = 'name'

    for key in dict:
        query.where &= key + " LIKE '%" + dict[key] + "%'"

    leagues_db = db.fetchall(query)
    leagues = []

    for l_db in leagues_db:
        league = League(_league_row_to_dict(l_db))
        if fixtures == True:
            league.fixtures = _get_league_fixtures(l_db, db)
        if teams == True:
            league.teams = _get_league_teams(l_db, db)
        leagues.append(league)

    return leagues


def get_league(db, league_id, fixtures=True, teams=True):
    query = db.Select(sets='leagues')
    query.where = 'id = ' + str(league_id)
    l_db = db.fetchall(query)
    league = League(_league_row_to_dict(l_db[0]))
    if fixtures == True:
        league.fixtures = _get_league_fixtures(l_db[0], db)
    if teams == True:
        league.teams = _get_league_teams(l_db[0], db)
    return league


def get_leagues_count(db, dict={}):
    query = db.Select('COUNT(*) as count', sets='leagues')
    for key in dict:
        query.where &= key + " LIKE '%" + dict[key] + "%'"
    return db.fetchone(query)['count']