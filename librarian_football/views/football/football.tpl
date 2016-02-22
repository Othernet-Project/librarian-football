<%inherit file="/base.tpl"/>
<%namespace file="_football_league_table.tpl" name="section"/>

<%block name="title">
## Translators, used as page title
${_('Football')}
</%block>

<%block name="main">
<div class="football-leagues-list o-collapsible" id="football-leagues-list">
% for l in leagues:
    <%section:league_table league="${l}" fixtures="${l.fixtures}"></%section:league_table>
% endfor
</div>
</%block>

<%block name="javascript_templates">
<script id="collapseIcon" type="text/template">
    <a href="javascript:void(0)" class="dash-expand-icon"></a>
</script>
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/football']}">
</%block>

<%block name="extra_scripts">
<script src="${assets['js/football']}"></script>
</%block>