// fetches from URL and displays value of 'hello'
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(() => {
  const hello = $('div#hello');
  $.getJSON(url, (data) => {
    let greeting = data.hello;
    hello.text(greeting);
  });
});
