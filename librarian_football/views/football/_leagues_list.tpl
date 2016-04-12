<%namespace name="ui_pager" file="/ui/pager.tpl"/>

<ul class="list">
    % for l in leagues:
    <li class="list-item">
        <p>${l['name']}</p>
        <a href="${i18n_url('league:schedule', league_id=l['id'])}">Schedule</a>
        <a href="${i18n_url('league:standings', league_id=l['id'])}">Standings</a>
        <p>Last Updated: ${l['last_updated']}</p>
    </li>
    % endfor
</ul>

<p class="pager">
${ui_pager.pager_links(pager, _('Previous'), _('Next'))}
</p>