<%inherit file="/base.tpl"/>
<%namespace name="ui" file="/ui/widgets.tpl"/>
<%namespace name="forms" file="/ui/forms.tpl"/>
<%namespace name="leagues_list" file="_leagues_list.tpl"/>

<%block name="title">
## Translators, used as page title
${_('Leagues')}
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/leagues_list']}">
</%block>

<%block name="menubar_panel">
<form class="o-multisearch o-panel" id="leagues-list-search">
    <div class="o-panel">
        ## Translators, used as label for search field, appears before the text box
        <label for="q" class="o-multisearch-label">${_('Search:')}</label>
    </div>
    <div class="o-panel">
        ${forms.text('q', _('League or team keywords'), value=None)}
    </div>
    <div class="o-panel">
        <button class="o-multisearch-button" id="files-multisearch-button" type="submit">
            ## Translators, used as button in content list
            <span class="o-multisearch-button-label">${_('Start search')}</span>
            <span class="o-multisearch-button-icon icon"></span>
        </button>
    </div> 
</form>
</%block>

<%block name="main">
<div class="o-main-inner" id="leagues-list-container">
    ${leagues_list.body()}
</div>
</%block>