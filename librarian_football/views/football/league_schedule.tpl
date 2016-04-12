<%inherit file="/base.tpl"/>
<%namespace name="ui" file="/ui/widgets.tpl"/>
<%namespace name="forms" file="/ui/forms.tpl"/>
<%namespace name="league_schedule" file="_league_schedule.tpl"/>

<%block name="title">
## Translators, used as page title
${_('{} - Schedule'.format(league['name']))}
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/league_schedule']}">
</%block>

<%block name="main">
<div class="o-main-inner" id="league-schedule-container">
    ${league_schedule.body()}
</div>
</%block>

<%block name="extra_scripts">
<script src="${assets['js/league_schedule']}"></script>
</%block>