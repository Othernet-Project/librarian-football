jQuery(document).ready ->
  jQuery('.tabs .tab-links a').on 'click', (e) ->
    currentAttrValue = undefined
    currentAttrValue = jQuery(this).attr('href')
    jQuery('.tabs ' + currentAttrValue).show().siblings().hide()
    jQuery(this).parent('li').addClass('active').siblings().removeClass 'active'
    e.preventDefault()
    return
  return