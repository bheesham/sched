requirejs.config(
  paths:
    lodash: '../bower_components/lodash/dist/lodash'
)

require ['lodash'], () ->
  _ = require('lodash')