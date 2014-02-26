define('models/appointment', ['jquery', 'underscore', 'backbone', 'moment'], function() {
  var $, Backbone, Model, moment;
  $ = require('jquery');
  Backbone = require('backbone');
  moment = require('moment');
  Model = Backbone.Model.extend({
    defaults: {
      date: void 0,
      time: void 0
    },
    saveAppointment: function(date, hour) {
      var that;
      alert(date);
      alert(hour);
      that = this;
      return $.ajax('api/save-appointment', {
        dataType: 'json',
        data: {
          date: date,
          hour: hour
        },
        method: 'POST',
        success: function(data) {
          return alert(data.message);
        }
      });
    }
  });
  return Model;
});

//# sourceMappingURL=appointment.js.map
