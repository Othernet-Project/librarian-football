import requests
import xml.etree.ElementTree as ET

BASE_URL = 'http://www.xmlsoccer.com/FootballDataDemo.asmx/'

EU = 'Europe'
AS = 'Asia'
AF = 'Africa'
NA = 'North America'
SA = 'South America'
AU = 'Australia'

ENGLAND = 'England'
SCOTLAND = 'Scotland'
GERMANY = 'Germany'
ITALY = 'Italy'
FRANCE = 'France'
SPAIN = 'Spain'
GREECE = 'Greece'
HOLLAND = 'Holland'
BELGIUM = 'Belgium'
TURKEY = 'Turkey'
DENMARK = 'Denmark'
EUROPE = 'Europe'
PORTUGAL = 'Portugal'
USA = 'USA'
SWEDEN = 'Sweden'
MEXICO = 'Mexico'
BRAZIL = 'Brazil'
UKRAINE = 'Ukraine'
RUSSIA = 'Russia'
AUSTRALIA = 'Australia'
INTERNATIONAL = 'International'
NORWAY = 'Norway'
CHINA = 'China'
POLAND = 'Poland'
ARGENTINA = 'Argentina'

def _continent_for_country(country):
    if country == ENGLAND:
        return EU

    elif country == SCOTLAND:
        return EU

    elif country == GERMANY:
        return EU

    elif country == ITALY:
        return EU

    elif country == FRANCE:
        return EU

    elif country == SPAIN:
        return EU

    elif country == GREECE:
        return EU

    elif country == HOLLAND:
        return EU

    elif country == BELGIUM:
        return EU

    elif country == TURKEY:
        return EU

    elif country == DENMARK:
        return EU

    elif country == EUROPE:
        return EU

    elif country == PORTUGAL:
        return EU

    elif country == USA:
        return NA

    elif country == SWEDEN:
        return EU

    elif country == MEXICO:
        return NA

    elif country == BRAZIL:
        return SA

    elif country == UKRAINE:
        return EU

    elif country == RUSSIA:
        return EU

    elif country == AUSTRALIA:
        return AU

    elif country == INTERNATIONAL:
        return EU

    elif country == NORWAY:
        return EU

    elif country == CHINA:
        return AS

    elif country == POLAND:
        return EU

    elif country == ARGENTINA:
        return SA

    else:
        return None    


class League(object):
    def __init__(self, **kwargs):
	    super(League, self).__init__()
	    self.name = kwargs.get('name')
	    self.country = kwargs.get('country')
	    self.continent = _continent_for_country(kwargs.get('country'))


def get_all_leagues(api_key):
    url = BASE_URL + 'GetAllLeagues'
    params = dict(ApiKey=api_key)
    response = requests.get(url, params=params)

    leagues = []
    root = ET.fromstring(response.text.encode('utf-8'))
    for child in root.findall('League'):
        name = child.find('Name').text
        country = child.find('Country').text
        league = League(name=name, country=country)
        leagues.append(league)

    return leagues