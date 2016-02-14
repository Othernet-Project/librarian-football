import requests
import xml.etree.ElementTree as ET


BASE_URL = 'http://www.xmlsoccer.com/FootballDataDemo.asmx/'


class League(object):
    def __init__(self, **kwargs):
        super(League, self).__init__()
        self.name = kwargs.get('name')


def get_all_leagues(api_key):
    url = BASE_URL + 'GetAllLeagues'
    params = dict(ApiKey=api_key)
    response = requests.get(url, params=params)

    leagues = []
    root = ET.fromstring(response.text.encode(response.encoding))
    for child in root.findall('League'):
        name = child.find('Name').text
        country = child.find('Country').text
        league = League(name=name)
        leagues.append(league)

    return leagues