<%inherit file="/base.tpl"/>
<%namespace name="ui" file="/ui/widgets.tpl"/>
<%namespace name="forms" file="/ui/forms.tpl"/>
<%namespace name="league_standings" file="_league_standings.tpl"/>

<%block name="title">
## Translators, used as page title
${_('{} - Standings'.format(league['name']))}
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/league_standings']}">
</%block>

<%block name="main">
<div class="o-main-inner">
    ${league_standings.body()}
</div>
</%block>