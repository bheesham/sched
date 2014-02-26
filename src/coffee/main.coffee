requirejs.config
  paths:
    backbone: '../bower_components/backbone/backbone'
    underscore: '../bower_components/lodash/dist/lodash.compat'
    jquery: '../bower_components/jquery/dist/jquery'
    'jquery.ui.core': '../bower_components/jquery.ui/ui/jquery.ui.core'
    'jquery.ui.datepicker': '../bower_components/jquery.ui/ui/jquery.ui.datepicker'
    moment: '../bower_components/momentjs/moment'
    text: '../bower_components/requirejs-text/text'
    templates: '../templates'
  shim:
    underscore:
      deps: ['jquery']
    backbone:
      deps: ['jquery', 'underscore']
      exports: 'Backbone'
    jquery:
      exports: 'jQuery'
    'jquery.ui.core':
      deps: ['jquery']
    'jquery.ui.datepicker':
      deps: ['jquery', 'jquery.ui.core']
      exports: '$'

require ['underscore', 'jquery.ui.datepicker', 'moment','views/times', 'models/times', 'models/appointment'], () ->
  _ = require('underscore')
  Backbone = require('backbone')
  $ = require('jquery')
  Times = require('models/times')
  moment = require('moment')

  $('#date').datepicker(
    minDate: 0
    maxDate: 10
  )

  TimesModel = require('models/times')
  TimesView =  require('views/times')

  timeModel = new TimesModel
  timeView = new TimesView
    el: $('#times')
    model: timeModel

  AppointmentModel = require('models/appointment')
  
  appointment = new AppointmentModel

  timeModel.update()
  $('#date').datepicker('option', 'onSelect', (date, obj) ->
    timeModel.update(moment(date, 'MM/DD/YYYY').format('DD-MM-YYYY'))
  )

  $('#book').click(() ->
    appointment.saveAppointment(timeModel.get('date'), timeView.getSelected(), $('#name').val(), $('#email').val())
    timeModel.update()
  )
