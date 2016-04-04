def get_leagues(db, pager, filter_dict = {}):
    """
    Retrieve a list of leagues from the database. 'filter_dict' can
    be used to filter leagues based on column. League fixtures and teams 
    data is not included.
    """

    query = db.Select(sets = 'leagues')
    offset, limit = pager.items
    query.offset = offset
    query.limit = limit
    query.order = 'name'

    # Apply filter
    for key in filter_dict:
        query.where &= "{} ILIKE '%{}%'".format(key, filter_dict[key])

    # Fetch all leagues
    return db.fetchall(query)


def get_league(db, league_id):
    """
    Retrieve a league with the given unique identifier. Returned
    structure is a tuple containing the league and its corresponding
    fixtures and teams.
    """

    # Fetch league
    query = db.Select(sets = 'leagues')
    query.where = 'id = {}'.format(league_id)
    league = db.fetchone(query)

    # Fetch fixtures
    query = db.Select(sets = 'fixtures')
    query.order = 'date'
    query.where = 'league_id = {}'.format(league_id)
    fixtures = db.fetchall(query)

    # Fetch teams
    query = db.Select(sets = 'teams')
    query.order = 'position'
    query.where = 'league_id = {}'.format(league_id)
    teams = db.fetchall(query)

    return (league, fixtures, teams)


def get_leagues_count(db, filter_dict = {}):
    """
    Retrieve the number of leagues in the database. 'filter_dict' can
    be used to filter leagues based on column.
    """
    
    query = db.Select('COUNT(*) as count', sets = 'leagues')
    
    # Apply filter
    for key in filter_dict:
        query.where &= "{} ILIKE '%{}%'".format(key, filter_dict[key])
    
    # Fetch count
    return db.fetchone(query)['count']