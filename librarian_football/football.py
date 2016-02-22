class League(object):
    """docstring for League"""
    def __init__(self, params):
        super(League, self).__init__()
        self.id = params['id']
        self.name = params['name']
        self.current_matchday = params['current_matchday']
        self.number_of_matchdays = params['number_of_matchdays']
        self.fixtures = []
        self.teams = []


class Fixture(object):
    """docstring for Fixture"""
    def __init__(self, params):
        super(Fixture, self).__init__()
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
        self.name = params['name']
        self.position = params['position']
        self.wins = params['wins']
        self.losses = params['losses']
        self.draws = params['draws']
        

def _league_row_to_dict(row):
    return { "id": row[0],
             "name": row[1],
             "created": row[2],
             "current_matchday": row[3],
             "number_of_matchdays": row[4]
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
    query = db.Select(sets='fixtures')
    query.where = 'league_id = ' + str(l_db[0])
    fixtures_db = db.fetchall(query)

    fixtures = []
    for f_db in fixtures_db:
        fixture = Fixture(_fixture_row_to_dict(f_db))
        fixtures.append(fixture)

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


def get_all_leagues(db):
    query_leagues = db.Select(sets='leagues')
    leagues_db = db.fetchall(query_leagues)
    leagues = []

    for l_db in leagues_db:
        league = League(_league_row_to_dict(l_db))
        league.fixtures = _get_league_fixtures(l_db, db)
        league.teams = _get_league_teams(l_db, db)
        leagues.append(league)

    return leagues