<%namespace name="ui_pager" file="/ui/pager.tpl"/>

<ul class="leagues-list" id="leagues-list">
    % for l in leagues:
    <li class="leagues-list-item" role="row">
        <a href="${i18n_url('league:detail', league_id=l['id'])}">${l['name']}</a>
        <p>Last Updated: ${l['last_updated']}</p>
    </li>
    % endfor
</ul>

<p class="pager">
${ui_pager.pager_links(pager, _('Previous'), _('Next'))}
</p>