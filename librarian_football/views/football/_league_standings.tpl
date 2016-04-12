<div class="standings-table-container">
    % if len(teams) == 0:
    <div class="standings-table-error">
        Sorry, standings data is not available at this time. Please check back later.
    </div>
    % else:
    <table class="standings-table">
        <tr class="standings-table-row">
            <th colspan="5">${league['name']}: Current Standings</th>
        </tr>
        <tr class="standings-table-row">
            <th>No.</th>
            <th>Team Name</th>
            <th>Wins</th>
            <th>Losses</th>
            <th>Draws</th>
        </tr>
        % for t in teams:
        <tr class="standings-table-row">
            <td>${t['position']}</td>
            <td>${t['name']}</td>
            <td>${t['wins']}</td>
            <td>${t['losses']}</td>
            <td>${t['draws']}</td>
        </tr>
        % endfor
    </table>
    % endif
</div>