SQL = """
CREATE TABLE leagues
(
    id INT NOT NULL,
    name VARCHAR,
    created TIMESTAMP NOT NULL,
    current_matchday INT,
    number_of_matchdays INT,
    
    PRIMARY KEY (id)
);

CREATE TABLE fixtures
(
    id INT NOT NULL,
    league_id INT NOT NULL,
    home_team_name VARCHAR,
    away_team_name VARCHAR,
    status VARCHAR,
    date TIMESTAMP,
    matchday INT,
    home_team_goals INT,
    away_team_goals INT,
    created TIMESTAMP NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (league_id) REFERENCES leagues(id)
);
"""


def up(db, conf):
    db.executescript(SQL)