class League(object):
    """docstring for League"""
    def __init__(self, params):
        super(League, self).__init__()
        self.name = params['name']
        self.current_matchday = params['current_matchday']
        self.number_of_matchdays = params['number_of_matchdays']
        self.fixtures = []


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


def get_all_leagues(db):
    query_leagues = db.Select(sets='leagues')
    leagues_db = db.fetchall(query_leagues)
    leagues = []

    for league_db in leagues_db:
        league = League(_league_row_to_dict(league_db))
        query_fixtures = db.Select(sets='fixtures')
        query_fixtures.where = 'league_id = ' + str(league_db[0])
        fixtures_db = db.fetchall(query_fixtures)
        
        fixtures = []
        for fixture_db in fixtures_db:
            fixture = Fixture(_fixture_row_to_dict(fixture_db))
            fixtures.append(fixture)

        league.fixtures = fixtures
        leagues.append(league)

    return leagues