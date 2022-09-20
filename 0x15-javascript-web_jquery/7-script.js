$.get('https://swapi-api.hbtn.io/api/people/5/', function (d) {
  $('#character').text(d.name);
});
