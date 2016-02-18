import os, json
from .menuitems import FootballMenuItem
from .football import *

def initialize(supervisor):
    supervisor.exts.menuitems.register(FootballMenuItem)


def post_start(supervisor):
    db = supervisor.exts.databases['football']
    config = supervisor.config
    fsal_client = supervisor.exts.fsal
    (success, dirs, files) = fsal_client.list_dir(config['football.data_dir'])

    if files is None:
        # no new data, so just return
        return

    dump_database(db)
    for f in files:
        if f.name == 'leagues_list.json':
            q_delete = db.Delete('leagues')
            db.execute(q_delete, None)
            path = f.path
            with open(path) as json_data:
                data = json.load(json_data)
                for league in data:
                    q_insert = db.Insert('leagues', cols=['id',
                                                          'name', 
                                                          'created',
                                                          'current_matchday',
                                                          'number_of_matchdays'])
                    vals = { "id": league['id'],
                             "name": league['caption'],
                             "created": league['lastUpdated'],
                             "current_matchday": league['currentMatchday'],
                             "number_of_matchdays": league['numberOfMatchdays']
                    }
                    db.execute(q_insert, vals)
            break
