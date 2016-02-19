from .menuitems import FootballMenuItem

def initialize(supervisor):
    supervisor.exts.menuitems.register(FootballMenuItem)