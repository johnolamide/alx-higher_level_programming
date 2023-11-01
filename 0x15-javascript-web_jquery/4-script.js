// toggles the class of the <header> when clicked
const header = $('header');
$('#toggle_header').click(() => {
  if (header.hasClass('red')) {
    header.toggleClass('red green');
  } else {
    header.toggleClass('green red');
  }
});
