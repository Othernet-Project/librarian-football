from functools import partial

from .tasks import fsal_callback
from .menuitems import FootballMenuItem


def initialize(supervisor):
    """
    Register the callback function that will handle incoming
    football data. Also, allows the football app to appear
    in Librarian's menu.
    """
    
    supervisor.exts.menuitems.register(FootballMenuItem)
    supervisor.exts.events.subscribe('FS_EVENT', partial(fsal_callback, supervisor))