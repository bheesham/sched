define('views/times', ['jquery', 'underscore', 'backbone', 'moment', 'text!templates/time.html'], function() {
  var $, Backbone, View, moment, template;
  $ = require('jquery');
  Backbone = require('backbone');
  moment = require('moment');
  template = _.template(require('text!templates/time.html'));
  View = Backbone.View.extend({
    initialize: function() {
      this.template = template;
      this.render();
      return this.listenTo(this.model, 'change', this.render);
    },
    render: function() {
      var i, to_append, _i, _results;
      this.$el.empty();
      _results = [];
      for (i = _i = 8; _i <= 16; i = ++_i) {
        to_append = $(this.template({
          hour: i
        }));
        if (_.contains(this.model.get('available-hours'), i)) {
          to_append.addClass('time-avail');
        }
        _results.push(this.$el.append(to_append));
      }
      return _results;
    },
    getSelected: function() {
      return this.$el.children('input[type=radio]:checked').val();
    }
  });
  return View;
});

//# sourceMappingURL=times.js.map
