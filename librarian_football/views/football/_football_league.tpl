<%namespace file="/ui/nojs.tpl" name="nojs"/>

<%def name="league(name)">
    <section class="football-league o-collapsible-section ${nojs.cls_toggle(name, 'o-collapsed', flip=True)}" id="football-${name}">
    <h2 class="o-collapsible-section-title" id="football-${name}-header">
        <a role="button">
            <span class="icon"></span>
            ${name}
        </a>
    </h2>
    <div class="football-league-content o-collapsible-section-panel" id="dashboard-${name}-panel">
        <p>yoyo</p>
    </div>
    </section>
</%def>