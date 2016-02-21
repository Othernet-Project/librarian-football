import fsal.events as fs
import adapters.football_data as adapter


def fsal_callback(supervisor, event):
    event_file_path = event.src
    config = supervisor.config

    # Ignore irrelevant events
    if config['football.data_dir'] not in event_file_path or
                     event.event_type == fs.EVENT_DELETED or 
                     event.event_type == fs.EVENT_MODIFIED:
        return

    # Get list of files in data directory
    fsal_client = supervisor.exts.fsal
    (success, dirs, files) = fsal_client.list_dir(config['football.data_dir'])

    # Get the file that caused the event
    for f in files:
        if _file_name_for_path(f.path) == _file_name_for_path(event_file_path):
            
            # Ignore filetype, adapter will handle that
            db = supervisor.exts.databases['football']
            adapter.parse(db, f.path)
            break


def _file_name_for_path(path):
    path_elems = path.split('/')
    file_name = path_elems[-1]
    return file_name