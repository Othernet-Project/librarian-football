<%inherit file="/base.tpl"/>
<%namespace file="_football_league.tpl" name="section"/>

<%block name="title">
## Translators, used as page title
${_('Football')}
</%block>

<%block name="main">
<div class="leagues-list o-collapsible" id="leagues-list">
% for league in leagues:
	<%section:league name="${league.name}">
    </%section:league>
% endfor
</div>
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/football']}">
</%block>

<%block name="extra_scripts">
<script src="${assets['js/football']}"></script>
</%block>