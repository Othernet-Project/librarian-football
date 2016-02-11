from bottle_utils.i18n import lazy_gettext as _

from librarian_menu.menu import MenuItem


class FootballMenuItem(MenuItem):
    name = 'football'
    label = _("Football")
    icon_class = 'football'
    route = 'football:scores'