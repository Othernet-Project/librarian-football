import logging
import fsal.events as fs
import adapters.football_data as adapter


def fsal_callback(supervisor, event):
    """
    Callback function that handles new football data. The function will ignore
    deleted and modified files of any kind. New football data is downloaded
    as a bundle, so when this callback is fired, the new directory will already
    contain all files. Fired FSAL events include all new files as well as
    directories, so we filter out new file additions, and only handle the new
    bundle directory. If there is new football data, the old data in the database
    will be deleted, and the adapter will parse the json files, and import the 
    new data into the database. Finally, the callback will delete the downloaded
    files.
    """

    if event.event_type != fs.EVENT_CREATED:
        return

    if event.is_dir == False:
        return

    if 'football' not in event.src:
        return

    logging.info('FOOTBALL: New data has been downloaded')
    config = supervisor.config
    fsal_client = supervisor.exts.fsal
    db = supervisor.exts.databases['football']
    (success, dirs, files) = fsal_client.list_dir(event.src)

    if success:
        dump_database(db)
        logging.info('FOOTBALL: Database dumped')
        adapter.parse(db, files, dirs)
        logging.info('FOOTBALL: New data imported to database')
        fsal_client.remove(event.src)
    else:
        logging.info('FOOTBALL: Something unexpected happened, ignore new data')

    return


def dump_database(db):
    """
    Delete all data in the football database. 'leagues' table has to be deleted
    last because 'teams' and 'fixtures' tables have foreign keys that reference
    'leagues'.
    """
   
    for table in ('teams', 'fixtures', 'leagues'):
        db.execute(db.Delete(table))