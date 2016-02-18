class League(dict):
	"""docstring for League"""
	def __init__(self, params):
		super(League, self).__init__()
		self.name = params['caption']
		self.fixtures = params['fixtures']


class Fixture(dict):
	"""docstring for Fixture"""
	def __init__(self, params):
		super(Fixture, self).__init__()
		self.date = params['date']
		self.status = params['status']
		self.match_day = params['matchday']
		self.home_team = params['homeTeam']
		self.away_team = params['awayTeam']
		self.result = params['result']


class FixtureResult(dict):
	"""docstring for FixtureResult"""
	def __init__(self, params):
		super(FixtureResult, self).__init__()
		self.goals_away_team = params['goalsAwayTeam']
		self.goals_home_team = params['goalsHomeTeam']
		