<%namespace file="/ui/nojs.tpl" name="nojs"/>

<%def name="league(id, name)">
    <section class="football-league-section o-collapsible-section ${nojs.cls_toggle(name, 'o-collapsed', flip=True)}" id="league-${id}">
    <h2 class="o-collapsible-section-title" id="league-${id}-header">
        <a href="${nojs.comp_url(name)}" role="button">
            <span class="icon"></span>
            ${name}
        </a>
    </h2>
    <div class="football-league-content o-collapsible-section-panel" id="league-${id}-panel">
        
    </div>
    </section>
</%def>