module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    coffee: {
      default: {
        options: {
          bare: true,
          sourceMap: true
        },
        expand: true,
        flatten: false,
        cwd: 'src/coffee',
        src: ['*.coffee', '**/*.coffee'],
        dest: 'dist/js',
        ext: '.js'
      }
    },
    less: {
      default: {
        options: {
          paths: ["assets/"],
          strictImports: true,
          strictMath: true,
          strictUnits: true,
          cleancss: false
        },
        files: {
          "dist/css/main.css": "src/less/main.less"
        }
      },
      prod: {
        options: {
          paths: ["assets/"],
          strictImports: true,
          strictMath: true,
          strictUnits: true,
          cleancss: true
        },
        files: {
          "dist/css/main.css": "src/less/main.less"
        }
      }
    },
    copy: {
      html: {
        files: [
          {
            expand: true,
            src: '**',
            dest: 'dist/',
            cwd: 'src/html'
          }
        ]
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.registerTask('default', ['coffee:default', 'less:default', 'copy:html']);
  grunt.registerTask('prod', ['coffee:default', 'less:prod', 'copy:html']);
  grunt.registerTask('live', ['connect:dist']);
};