from functools import partial

from .tasks import fsal_callback
from .menuitems import FootballMenuItem


def initialize(supervisor):
    supervisor.exts.menuitems.register(FootballMenuItem)
    supervisor.exts.events.subscribe('FS_EVENT', partial(fsal_callback, supervisor))