// PART 1: SHOW A FORTUNE

function showFortune(evt) {
    // TODO: get the fortune and show it in the fortune-text div
    $.get('/fortune', "test", function(results) {
      $('#fortune-text').html(results);
    })
}

$('#get-fortune-button').on('click', showFortune);





// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();
    var url = "/weather?zipcode=" + $("#zipcode-field").val();
    $.get(url, function(results) {
      console.log(results);
      $('#weather-info').html(results['forecast']);
    })
    // TODO: request weather with that URL and show the forecast in #weather-info
}

$("#weather-form").on('submit', showWeather);
