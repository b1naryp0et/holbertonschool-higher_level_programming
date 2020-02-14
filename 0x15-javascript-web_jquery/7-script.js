$.getJSON('https://swapi.co/api/people/5/?format=json', function (elr) {
  $('div#character').text(elr.name);
});
