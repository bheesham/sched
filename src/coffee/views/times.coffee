define 'views/times', ['jquery', 'underscore', 'backbone', 'moment', 'text!templates/time.html'], () ->
  $ = require('jquery')
  Backbone = require('backbone')
  moment = require('moment')
  template = _.template(require('text!templates/time.html'))
  
  View = Backbone.View.extend
    initialize: () ->
      this.template = template
      this.render()
      this.listenTo(this.model, 'change', this.render)
    render: () ->
      this.$el.empty()
      for i in [8..16]
        to_append = $ this.template
            hour: i
        if _.contains(this.model.get('available-hours'), i)
          to_append.addClass('time-avail')
        this.$el.append(to_append)
    getSelected: () ->
      return this.$el.find('input[type=radio]:checked').val()
  
  return View
