// fetches the character 'name' from the starwars URL
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const character = $('#character');
$.getJSON(url, (data) => {
  let name = data.name;
  character.text(name);
});
