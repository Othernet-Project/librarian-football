import os, json
from .menuitems import FootballMenuItem

def initialize(supervisor):
    supervisor.exts.menuitems.register(FootballMenuItem)


def post_start(supervisor):
    db = supervisor.exts.databases['football']
    config = supervisor.config
    fsal_client = supervisor.exts.fsal
    (success, dirs, files) = fsal_client.list_dir(config['football.data_dir'])

    for f in files:
        if f.name == 'leagues_list.json':
            q_delete = db.Delete('leagues')
            db.execute(q_delete, None)
            path = f.path
            with open(path) as json_data:
                data = json.load(json_data)
                for league in data:
                    q_insert = db.Insert('leagues', cols=['id', 'name', 'created'])
                    vals = { "id": league['id'],
                             "name": league['caption'],
                             "created": league['lastUpdated']
                    }
                    db.execute(q_insert, vals)
            break