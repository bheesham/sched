define 'models/times', ['jquery', 'underscore', 'backbone', 'moment', 'text!templates/time.html'], () ->
  $ = require('jquery')
  Backbone = require('backbone')
  moment = require('moment')
  template = _.template(require('text!templates/time.html'))

  Model = Backbone.Model.extend
    defaults:
      time: '8'
    initialize: () ->
      this.set('date', moment().format('DD-MM-YYYY'))
      this.set('available-hours', [])
    update: (date) ->
      that = this
      if not date?
        date = this.get('date')
      $.ajax 'api/get-date-hours',
        dataType: 'json'
        data:
          date: date
        method: 'POST'
        success: (data) ->
          that.set('available-hours', data.hours)
      this.set('date', date)

  return Model
