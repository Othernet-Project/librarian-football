###
#
# The MIT License (MIT)
#
# Copyright (c) 2014 joshreed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
#
# SCROLL TABS
#
# JQuery Plugin to manage scrollable tabs. See the 'defaultOptions' data structure for available options for configuration. The plugin is configured jointly via
# these Javascript options and CSS classes to style how it is displayed. Some of the CSS is set here in the javascript so that users will have minimal
# configuration to make the tabs themselves work, and should only have to do configuration on how they want it styled. 
#
# Known Limitations:
# IE6 problems, it does not properly apply scrolling and therefore is always the 'full width.' Additionally, the multiple-class CSS styling does not work
# properly in IE6. We can work around this in the future by apply distinct class stylings that represent all the combinations. 
#
# Version:   2.0 
# Author:    Josh Reed
###

(($) ->

  $.fn.scrollTabs = (opts) ->

    initialize = (state) ->
      opts = $.extend({}, $.fn.scrollTabs.defaultOptions, opts)
      if $(this).prop('tagName').toLowerCase() == 'ul'
        @itemTag = 'li'
      else
        @itemTag = 'span'
      $(this).addClass 'scroll_tabs_container'
      if $(this).css('position') == null or $(this).css('position') == 'static'
        $(this).css 'position', 'relative'
      $(@itemTag, this).last().addClass 'scroll_tab_last'
      $(@itemTag, this).first().addClass 'scroll_tab_first'
      $(this).html '<div class=\'scroll_tab_left_button\'></div><div class=\'scroll_tab_inner\'><span class=\'scroll_tab_left_finisher\'>&nbsp;</span>' + $(this).html() + '<span class=\'scroll_tab_right_finisher\'>&nbsp;</span></div><div class=\'scroll_tab_right_button\'></div>'
      $('.scroll_tab_inner > span.scroll_tab_left_finisher', this).css 'display': 'none'
      $('.scroll_tab_inner > span.scroll_tab_right_finisher', this).css 'display': 'none'
      _this = this
      $('.scroll_tab_inner', this).css
        'margin': '0px'
        'overflow': 'hidden'
        'white-space': 'nowrap'
        '-ms-text-overflow': 'clip'
        'text-overflow': 'clip'
        'font-size': '0px'
        'position': 'absolute'
        'top': '0px'
        'left': opts.left_arrow_size + 'px'
        'right': opts.right_arrow_size + 'px'
      # If mousewheel function not present, don't utilize it
      if $.isFunction($.fn.mousewheel)
        $('.scroll_tab_inner', this).mousewheel (event, delta) ->
          # Only do mousewheel scrolling if scrolling is necessary
          if $('.scroll_tab_right_button', _this).css('display') != 'none'
            @scrollLeft -= delta * 30
            state.scrollPos = @scrollLeft
            event.preventDefault()
          return
      # Set initial scroll position
      $('.scroll_tab_inner', _this).animate { scrollLeft: state.scrollPos + 'px' }, 0
      $('.scroll_tab_left_button', this).css
        'position': 'absolute'
        'left': '0px'
        'top': '0px'
        'width': opts.left_arrow_size + 'px'
        'cursor': 'pointer'
      $('.scroll_tab_right_button', this).css
        'position': 'absolute'
        'right': '0px'
        'top': '0px'
        'width': opts.right_arrow_size + 'px'
        'cursor': 'pointer'
      $('.scroll_tab_inner > ' + _this.itemTag, _this).css
        'display': '-moz-inline-stack'
        'display': 'inline-block'
        'zoom': 1
        '*display': 'inline'
        '_height': '40px'
        '-webkit-user-select': 'none'
        '-khtml-user-select': 'none'
        '-moz-user-select': 'none'
        '-ms-user-select': 'none'
        '-o-user-select': 'none'
        'user-select': 'none'

      size_checking = ->
        panel_width = $('.scroll_tab_inner', _this).outerWidth()
        if $('.scroll_tab_inner', _this)[0].scrollWidth > panel_width
          $('.scroll_tab_right_button', _this).show()
          $('.scroll_tab_left_button', _this).show()
          $('.scroll_tab_inner', _this).css
            left: opts.left_arrow_size + 'px'
            right: opts.right_arrow_size + 'px'
          $('.scroll_tab_left_finisher', _this).css 'display', 'none'
          $('.scroll_tab_right_finisher', _this).css 'display', 'none'
          if $('.scroll_tab_inner', _this)[0].scrollWidth - panel_width == $('.scroll_tab_inner', _this).scrollLeft()
            $('.scroll_tab_right_button', _this).addClass('scroll_arrow_disabled').addClass 'scroll_tab_right_button_disabled'
          else
            $('.scroll_tab_right_button', _this).removeClass('scroll_arrow_disabled').removeClass 'scroll_tab_right_button_disabled'
          if $('.scroll_tab_inner', _this).scrollLeft() == 0
            $('.scroll_tab_left_button', _this).addClass('scroll_arrow_disabled').addClass 'scroll_tab_left_button_disabled'
          else
            $('.scroll_tab_left_button', _this).removeClass('scroll_arrow_disabled').removeClass 'scroll_tab_left_button_disabled'
        else
          $('.scroll_tab_right_button', _this).hide()
          $('.scroll_tab_left_button', _this).hide()
          $('.scroll_tab_inner', _this).css
            left: '0px'
            right: '0px'
          if $('.scroll_tab_inner > ' + _this.itemTag + ':not(.scroll_tab_right_finisher):not(.scroll_tab_left_finisher):visible', _this).size() > 0
            $('.scroll_tab_left_finisher', _this).css 'display', 'inline-block'
            $('.scroll_tab_right_finisher', _this).css 'display', 'inline-block'
        return

      size_checking()
      state.delay_timer = setInterval((->
        size_checking()
        return
      ), 500)
      press_and_hold_timeout = undefined
      $('.scroll_tab_right_button', this).mousedown((e) ->
        e.stopPropagation()

        scrollRightFunc = ->
          left = $('.scroll_tab_inner', _this).scrollLeft()
          state.scrollPos = Math.min(left + opts.scroll_distance, $('.scroll_tab_inner', _this)[0].scrollWidth - $('.scroll_tab_inner', _this).outerWidth())
          $('.scroll_tab_inner', _this).animate { scrollLeft: left + opts.scroll_distance + 'px' }, opts.scroll_duration
          return

        scrollRightFunc()
        press_and_hold_timeout = setInterval((->
          scrollRightFunc()
          return
        ), opts.scroll_duration)
        return
      ).bind('mouseup mouseleave', ->
        clearInterval press_and_hold_timeout
        return
      ).mouseover(->
        $(this).addClass('scroll_arrow_over').addClass 'scroll_tab_right_button_over'
        return
      ).mouseout ->
        $(this).removeClass('scroll_arrow_over').removeClass 'scroll_tab_right_button_over'
        return
      $('.scroll_tab_left_button', this).mousedown((e) ->
        e.stopPropagation()

        scrollLeftFunc = ->
          left = $('.scroll_tab_inner', _this).scrollLeft()
          state.scrollPos = Math.max(left - (opts.scroll_distance), 0)
          $('.scroll_tab_inner', _this).animate { scrollLeft: left - (opts.scroll_distance) + 'px' }, opts.scroll_duration
          return

        scrollLeftFunc()
        press_and_hold_timeout = setInterval((->
          scrollLeftFunc()
          return
        ), opts.scroll_duration)
        return
      ).bind('mouseup mouseleave', ->
        clearInterval press_and_hold_timeout
        return
      ).mouseover(->
        $(this).addClass('scroll_arrow_over').addClass 'scroll_tab_left_button_over'
        return
      ).mouseout ->
        $(this).removeClass('scroll_arrow_over').removeClass 'scroll_tab_left_button_over'
        return
      $('.scroll_tab_inner > ' + @itemTag + (if @itemTag != 'span' then ', .scroll_tab_inner > span' else ''), this).mouseover(->
        $(this).addClass 'scroll_tab_over'
        if $(this).hasClass('scroll_tab_left_finisher')
          $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).addClass('scroll_tab_over').addClass 'scroll_tab_first_over'
        if $(this).hasClass('scroll_tab_right_finisher')
          $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).addClass('scroll_tab_over').addClass 'scroll_tab_last_over'
        if $(this).hasClass('scroll_tab_first') or $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).hasClass('scroll_tab_first')
          $('.scroll_tab_inner > span.scroll_tab_left_finisher', _this).addClass('scroll_tab_over').addClass 'scroll_tab_left_finisher_over'
        if $(this).hasClass('scroll_tab_last') or $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).hasClass('scroll_tab_last')
          $('.scroll_tab_inner > span.scroll_tab_right_finisher', _this).addClass('scroll_tab_over').addClass 'scroll_tab_right_finisher_over'
        return
      ).mouseout(->
        $(this).removeClass 'scroll_tab_over'
        if $(this).hasClass('scroll_tab_left_finisher')
          $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).removeClass('scroll_tab_over').removeClass 'scroll_tab_first_over'
        if $(this).hasClass('scroll_tab_right_finisher')
          $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).removeClass('scroll_tab_over').removeClass 'scroll_tab_last_over'
        if $(this).hasClass('scroll_tab_first') or $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).hasClass('scroll_tab_first')
          $('.scroll_tab_inner > span.scroll_tab_left_finisher', _this).removeClass('scroll_tab_over').removeClass 'scroll_tab_left_finisher_over'
        if $(this).hasClass('scroll_tab_last') or $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).hasClass('scroll_tab_last')
          $('.scroll_tab_inner > span.scroll_tab_right_finisher', _this).removeClass('scroll_tab_over').removeClass 'scroll_tab_right_finisher_over'
        return
      ).click (e) ->
        e.stopPropagation()
        $('.tab_selected', _this).removeClass 'tab_selected scroll_tab_first_selected scroll_tab_last_selected scroll_tab_left_finisher_selected scroll_tab_right_finisher_selected'
        $(this).addClass 'tab_selected'
        context_obj = this
        if $(this).hasClass('scroll_tab_left_finisher')
          context_obj = $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).addClass('tab_selected').addClass('scroll_tab_first_selected')
        if $(this).hasClass('scroll_tab_right_finisher')
          context_obj = $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).addClass('tab_selected').addClass('scroll_tab_last_selected')
        if $(this).hasClass('scroll_tab_first') or $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).hasClass('scroll_tab_first')
          $('.scroll_tab_inner > span.scroll_tab_left_finisher', _this).addClass('tab_selected').addClass 'scroll_tab_left_finisher_selected'
        if $(this).hasClass('scroll_tab_last') or $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).hasClass('scroll_tab_last')
          $('.scroll_tab_inner > span.scroll_tab_right_finisher', _this).addClass('tab_selected').addClass 'scroll_tab_left_finisher_selected'
        # "Slide" it into view if not fully visible.
        scroll_selected_into_view.call _this, state
        opts.click_callback.call context_obj, e
        return
      # Check to set the edges as selected if needed
      if $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_first', _this).hasClass('tab_selected')
        $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_left_finisher', _this).addClass('tab_selected').addClass 'scroll_tab_left_finisher_selected'
      if $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_last', _this).hasClass('tab_selected')
        $('.scroll_tab_inner > ' + _this.itemTag + '.scroll_tab_right_finisher', _this).addClass('tab_selected').addClass 'scroll_tab_right_finisher_selected'
      return

    scroll_selected_into_view = (state) ->
      _this = this
      selected_item = $('.tab_selected:not(.scroll_tab_right_finisher, .scroll_tab_left_finisher)', _this)
      left = $('.scroll_tab_inner', _this).scrollLeft()
      scroll_width = $('.scroll_tab_inner', _this).width()
      if selected_item and typeof selected_item != 'undefined' and selected_item.position() and typeof selected_item.position() != 'undefined'
        if selected_item.position().left < 0
          state.scrollPos = Math.max(left + selected_item.position().left + 1, 0)
          $('.scroll_tab_inner', _this).animate { scrollLeft: left + selected_item.position().left + 1 + 'px' }, opts.scroll_duration
        else if selected_item.position().left + selected_item.outerWidth() > scroll_width
          state.scrollPos = Math.min(left + selected_item.position().left + selected_item.outerWidth() - scroll_width, $('.scroll_tab_inner', _this)[0].scrollWidth - $('.scroll_tab_inner', _this).outerWidth())
          $('.scroll_tab_inner', _this).animate { scrollLeft: left + selected_item.position().left + selected_item.outerWidth() - scroll_width + 'px' }, opts.scroll_duration
      return

    ret = []
    @each ->
      backup = $(this).html()
      state = {}
      state.scrollPos = 0
      initialize.call this, state
      context_obj = this
      ret.push
        domObject: context_obj
        state: state
        addTab: (html, position) ->
          if typeof position == 'undefined'
            position = $('.scroll_tab_inner > ' + context_obj.itemTag, context_obj).length - (if context_obj.itemTag == 'span' then 2 else 0)
          $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_last', context_obj).removeClass 'scroll_tab_last'
          $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_first', context_obj).removeClass 'scroll_tab_first'
          backup = ''
          count = 0
          $('.scroll_tab_inner > ' + context_obj.itemTag, context_obj).each ->
            if $(this).hasClass('scroll_tab_left_finisher') or $(this).hasClass('scroll_tab_right_finisher')
              return true
            if position == count
              backup += html
            backup += $(this).clone().wrap('<div>').parent().html()
            count++
            return
          if position >= count
            backup += html
          @destroy()
          initialize.call context_obj, state
          @refreshFirstLast()
          return
        removeTabs: (jquery_selector_str) ->
          $('.scroll_tab_left_finisher', context_obj).remove()
          $('.scroll_tab_right_finisher', context_obj).remove()
          $(jquery_selector_str, context_obj).remove()
          $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_last', context_obj).removeClass 'scroll_tab_last'
          $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_first', context_obj).removeClass 'scroll_tab_first'
          @refreshState()
          return
        destroy: ->
          clearInterval state.delay_timer
          $(context_obj).html backup
          $(context_obj).removeClass 'scroll_tabs_container'
          return
        refreshState: ->
          $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_last', context_obj).removeClass 'scroll_tab_last'
          $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_first', context_obj).removeClass 'scroll_tab_first'
          backup = $('.scroll_tab_inner', context_obj).html()
          @destroy()
          initialize.call context_obj, state
          @refreshFirstLast()
          return
        clearTabs: ->
          backup = ''
          @destroy()
          initialize.call context_obj, state
          @refreshFirstLast()
          return
        refreshFirstLast: ->
          old_last_item = $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_last', context_obj)
          old_first_item = $('.scroll_tab_inner > ' + context_obj.itemTag + '.scroll_tab_first', context_obj)
          old_last_item.removeClass 'scroll_tab_last'
          old_first_item.removeClass 'scroll_tab_first'
          if old_last_item.hasClass('tab_selected')
            $('.scroll_tab_inner > span.scroll_tab_right_finisher', context_obj).removeClass 'tab_selected scroll_tab_right_finisher_selected'
          if old_first_item.hasClass('tab_selected')
            $('.scroll_tab_inner > span.scroll_tab_left_finisher', context_obj).removeClass 'tab_selected scroll_tab_left_finisher_selected'
          if $('.scroll_tab_inner > ' + context_obj.itemTag + ':not(.scroll_tab_right_finisher):not(.scroll_tab_left_finisher):visible', context_obj).size() > 0
            new_last_item = $('.scroll_tab_inner > ' + context_obj.itemTag + ':not(.scroll_tab_right_finisher):visible', context_obj).last()
            new_first_item = $('.scroll_tab_inner > ' + context_obj.itemTag + ':not(.scroll_tab_left_finisher):visible', context_obj).first()
            new_last_item.addClass 'scroll_tab_last'
            new_first_item.addClass 'scroll_tab_first'
            if new_last_item.hasClass('tab_selected')
              $('.scroll_tab_inner > span.scroll_tab_right_finisher', context_obj).addClass('tab_selected').addClass 'scroll_tab_right_finisher_selected'
            if new_first_item.hasClass('tab_selected')
              $('.scroll_tab_inner > span.scroll_tab_left_finisher', context_obj).addClass('tab_selected').addClass 'scroll_tab_right_finisher_selected'
          else
            $('.scroll_tab_inner > span.scroll_tab_right_finisher', context_obj).hide()
            $('.scroll_tab_inner > span.scroll_tab_left_finisher', context_obj).hide()
          return
        hideTabs: (domObj) ->
          $(domObj, context_obj).css 'display', 'none'
          @refreshFirstLast()
          return
        showTabs: (domObj) ->
          $(domObj, context_obj).css
            'display': '-moz-inline-stack'
            'display': 'inline-block'
            '*display': 'inline'
          @refreshFirstLast()
          return
        scrollSelectedIntoView: ->
          scroll_selected_into_view.call context_obj, state
          return
      return
    if @length == 1
      ret[0]
    else
      ret

  $.fn.scrollTabs.defaultOptions =
    scroll_distance: 300
    scroll_duration: 300
    left_arrow_size: 26
    right_arrow_size: 26
    click_callback: (e) ->
      val = $(this).attr('rel')
      if val
        window.location.href = val
      return
  return
) jQuery
