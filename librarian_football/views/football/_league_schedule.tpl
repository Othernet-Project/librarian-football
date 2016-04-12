<div class="matchday-tab-set">
    <ul id="matchday-tab-links">
        % for k in range(1, league['number_of_matchdays'] + 1):
        <li class="{'matchday-selected tab_selected' if k == league['current_matchday'] else ''}"><a href="${'#matchday{}'.format(k)}">Round ${k}</a></li>
        % endfor
    </ul>
    <div class="matchday-tab-content">
        % for k in range(1, league['number_of_matchdays'] + 1):
        <div class="matchday-tab ${'matchday-selected' if k == league['current_matchday'] else ''}" id="${'matchday{}'.format(k)}">
            <% matchday = (fixture for fixture in fixtures if fixture['matchday'] == k) %>
            <table class="schedule-table">
                <tr class="schedule-table-row">
                    <th colspan="5">${league['name']}: Schedule &amp; Scores</th>
                </tr>
                <tr class="schedule-table-row">
                    <th>Date Time</th>
                    <th>Home Team</th>
                    <th>Home Goals</th>
                    <th>Away Goals</th>
                    <th>Away Team</th>
                </tr>
                % for match in matchday:
                <tr class="schedule-table-row">
                    <td>${match['date']}</th>
                    <td>${match['home_team_name']}</td>
                    <td>${match['home_team_goals']}</td>
                    <td>${match['away_team_goals']}</td>
                    <td>${match['away_team_name']}</td>
                </tr>
                % endfor
            </table>
        </div>
        % endfor
    </div>
</div>