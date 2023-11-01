// fetches and prints 'Hello' depending on the language
$(document).ready(function() {
  $('#btn_translate').click(function() {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function(data, status){
      $('#hello').text(data.hello);
    });
  });
});

