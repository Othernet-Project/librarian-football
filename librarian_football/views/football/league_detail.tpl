<%inherit file="/base.tpl"/>
<%namespace name="ui" file="/ui/widgets.tpl"/>
<%namespace name="forms" file="/ui/forms.tpl"/>
<%namespace name="league_detail" file="_league_detail.tpl"/>

<%block name="title">
## Translators, used as page title
${_('Leagues')}
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/league_detail']}">
</%block>

<%block name="main">
<div class="o-main-inner" id="league-detail-container">
    ${league_detail.body()}
</div>
</%block>

<%block name="javascript_templates">
<script id="collapseIcon" type="text/template">
    <a href="javascript:void(0)" class="dash-expand-icon"></a>
</script>
</%block>

<%block name="extra_scripts">
<script src="${assets['js/league_detail']}"></script>
</%block>