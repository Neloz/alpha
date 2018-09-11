$(function() {
  Alert = {
    show: function($div, msg) {
      $div.find('.alert-msg').text(msg);
      if ($div.css('display') === 'none') {
        // fadein, fadeout.
        $div.fadeIn(1000).delay(2000).fadeOut(2000);
      }
    },
    info: function(msg) {
      this.show($('#alert-success'), msg);
    },
  }
  $('body').on('click', '.alert-close', function() {
  	$(this).parents('.alert').hide();
  });
  $('#mensaje-1').click(function() {
    Alert.info('')
  });
});


