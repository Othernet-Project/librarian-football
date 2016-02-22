<%namespace file="/ui/nojs.tpl" name="nojs"/>
<%namespace file="_league_table_sections.tpl" name="section"/>

<%def name="league_table(league)">
    <section class="football-league-section o-collapsible-section ${nojs.cls_toggle(league.name, 'o-collapsed', flip=True)}" id="league-${league.id}">
    <h2 class="o-collapsible-section-title" id="league-${league.id}-header">
        <a href="${nojs.comp_url(league.name)}" role="button">
            <span class="icon"></span>
            ${league.name}
        </a>
    </h2>
    <div class="football-league-content o-collapsible-section-panel" id="league-${league.id}-panel">
        <div class="league-schedule-column">
            <%section:league_schedule fixtures="${league.fixtures}"></%section:league_schedule>
        </div>
        <div class="league-rankings-column">
            <%section:league_rankings teams="${league.teams}"></%section:league_rankings>    
        </div>
    </div>
    </section>
</%def>