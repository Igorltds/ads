module.exports = function (grunt) {
    'use strict';
    
    grunt.initConfig({
        pkg  : grunt.file.readJSON("package.json"),
        connect: {
            ci: {
                options: {
                    port: 8000,
                    base: '.'
                }
            },
            keepalive: {
                options: {
                    keepalive: true,
                    port: 8000,
                    base: '.',
                    open: 'http://localhost:8000/_SpecRunner.html'
                }
            }
        },
        jasmine: {
            test: {
                src: 'src/**/*.js',
                host: 'http://localhost:8000/',
                options: {
                    specs: 'spec/**/*Spec.js',
                    helpers: 'helper/**/*Helper.js'
                }
            }
        }
    });
 
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-jasmine');

    grunt.registerTask('bdd', ['jasmine:test:build', 'connect:keepalive'])
    grunt.registerTask('default', ['connect:ci', 'jasmine']);
};
