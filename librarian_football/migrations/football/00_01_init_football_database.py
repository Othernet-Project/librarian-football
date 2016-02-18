SQL = """
create table leagues
(
    id varchar primary key not null,                -- ID
    name text,                                      -- league name
    created timestamp not null                      -- creation timestamp
);
"""


def up(db, conf):
    db.executescript(SQL)