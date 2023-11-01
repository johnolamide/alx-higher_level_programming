// fetches and prints how to say "hello" depending on the language
$(document).ready(function() {
  function translate() {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function(data, status){
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translate);
  $('#language_code').keypress(function(e) {
    if (e.which == 13) {  // Enter key pressed
      translate();
    }
  });
});
