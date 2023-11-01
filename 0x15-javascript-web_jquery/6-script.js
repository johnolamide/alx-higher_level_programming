// updates the text of the <header>
const header = $('header');
const updateHeader= $('#update_header');
updateHeader.click(() => {
  header.text("New Header!!!");
});
