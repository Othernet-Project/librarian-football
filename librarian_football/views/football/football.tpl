<%inherit file="/base.tpl"/>

<%block name="title">
## Translators, used as page title
${_('Football')}
</%block>

<%block name="main">
<div class="tab-content">
% for league in leagues:
    <p>${league.name}</p>
% endfor
</div></%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/football']}">
</%block>

<%block name="extra_scripts">
<script src="${assets['js/football']}"></script>
</%block>