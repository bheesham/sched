define 'models/appointment', ['jquery', 'underscore', 'backbone', 'moment'], () ->
  $ = require('jquery')
  Backbone = require('backbone')
  moment = require('moment')

  Model = Backbone.Model.extend
    defaults:
      date: undefined
      time: undefined
    saveAppointment: (date, hour, name, email) ->
      that = this
      $.ajax 'api/save-appointment',
        dataType: 'json'
        data:
          date: date
          hour: hour
          name: name
          email: email
        method: 'POST'
        success: (data) ->
          alert(data.message)
  return Model
