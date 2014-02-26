define('models/times', ['jquery', 'underscore', 'backbone', 'moment', 'text!templates/time.html'], function() {
  var $, Backbone, Model, moment, template;
  $ = require('jquery');
  Backbone = require('backbone');
  moment = require('moment');
  template = _.template(require('text!templates/time.html'));
  Model = Backbone.Model.extend({
    defaults: {
      time: '8'
    },
    initialize: function() {
      this.set('date', moment().format('DD-MM-YYYY'));
      return this.set('available-hours', []);
    },
    update: function(date) {
      var that;
      that = this;
      if (date == null) {
        date = this.get('date');
      }
      $.ajax('api/get-avail-hours', {
        dataType: 'json',
        data: {
          date: date
        },
        method: 'POST',
        success: function(data) {
          return that.set('available-hours', data.hours);
        }
      });
      return this.set('date', date);
    }
  });
  return Model;
});

//# sourceMappingURL=times.js.map
