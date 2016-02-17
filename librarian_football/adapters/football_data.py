import requests, json


BASE_URL = 'http://api.football-data.org'


class League(object):
    def __init__(self, params):
        super(League, self).__init__()

        if 'caption' not in params or params == None:
            return None

        self.name = params['caption']


def get_all_leagues(api_key):
    url = BASE_URL + '/v1/soccerseasons/'
    params = { 'X-Auth-Token': api_key, 'X-Response-Control': 'minified' }
    response = requests.get(url, params=params)
    json_leagues = json.loads(response.text.encode('utf-8'))

    leagues = []
    for json_league in json_leagues:
        league = League(json_league)
        leagues.append(league)

    return leagues