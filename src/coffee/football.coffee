jQuery(document).ready ->
	jQuery('.tabs .tab-links a').on 'click', (e) ->
		currentAttrValue = jQuery(this).attr('href')
		# Show/Hide Tabs
		jQuery('.tabs ' + currentAttrValue).show().siblings().hide()
		# Change/remove current tab to active
		jQuery(this).parent('li').addClass('active').siblings().removeClass 'active'
		e.preventDefault()
		return
	return