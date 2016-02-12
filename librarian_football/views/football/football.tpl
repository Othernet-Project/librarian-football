<%inherit file="/base.tpl"/>

<%block name="title">
## Translators, used as page title
${_('Football')}
</%block>

<%block name="main">
<div class="tabs">

	<ul class="tab-links">
		% for continent in continents:
			% if loop.index == 0:
				<li class="active"><a href="#continent_${loop.index}">${continent.name}</a></li>
			% else:
				<li><a href="#continent_${loop.index}">${continent.name}</a></li>
			% endif
		% endfor
	</ul>

	<div class="tab-content">
		% for continent in continents:
			% if loop.index == 0:
				<div id="continent_${loop.index}" class="tab active">
        			% for league in continent.leagues:
        				<p>${league.name}</p>
        			% endfor
				</div>
			% else:
				<div id="continent_${loop.index}" class="tab">
        			% for league in continent.leagues:
        				<p>${league.name}</p>
        			% endfor
				</div>
			% endif
		% endfor
	</div>

</div>
</%block>

<%block name="extra_head">
<link rel="stylesheet" href="${assets['css/football']}">
</%block>

<%block name="extra_scripts">
<script src="${assets['js/football']}"></script>
</%block>