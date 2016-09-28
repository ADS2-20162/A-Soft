//Servidor web gulp para desarrollo 

var gulp = require('gulp');
var connect = require('gulp-connect');

gulp.task(
	'web_server', 
	function() {
		connect.server ({
			port: 9000,
			host: 'localhost'
		});
	}
);
