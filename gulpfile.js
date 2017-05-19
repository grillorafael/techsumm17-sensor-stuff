const gulp = require('gulp');
const scp = require('gulp-scp2');


gulp.task('upload', function(){
  return gulp.src('src/**/**').pipe(scp({
    host: '192.168.1.206',
    username: 'pi',
    password: 'muchSecurity',
    dest: '/home/pi/techsumm/sensors'
  }))
  .on('error', console.error.bind(console));
});

gulp.task('upload-npm', function(){
  return gulp.src('package.json').pipe(scp({
    host: '192.168.1.206',
    username: 'pi',
    password: 'muchSecurity',
    dest: '/home/pi/techsumm/sensors'
  }))
  .on('error', console.error.bind(console));
});

gulp.task('watch', function() {
  return gulp.watch('src/**/**', ['upload', 'upload-npm']);
});
