// adds, removes and clears li elements from a list on click
$(document).ready(() => {
  $('div#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').click(() => {
    $('ul.my_list li:last').remove();
  });

  $('div#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
