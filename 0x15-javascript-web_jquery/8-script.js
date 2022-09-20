$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (d) {
  $('#list_movies').append(...d.results.map(movie => `<li>${movie.title}</li>`));
});
