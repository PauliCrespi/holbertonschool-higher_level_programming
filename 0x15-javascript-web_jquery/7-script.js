$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (d) {
  $('#character').text(d.name);
});
