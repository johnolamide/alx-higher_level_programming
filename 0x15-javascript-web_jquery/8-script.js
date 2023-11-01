// fetches the character 'name' from the starwars URL
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const movieList = $('UL#list_movies');
$.getJSON(url, (data) => {
  let movies = data.results;
  $.each(movies, (index, movie) => {
    let title = movie.title;
    let listItem = $('<li></li>').text(title);
    movieList.append(listItem);
  });
});
