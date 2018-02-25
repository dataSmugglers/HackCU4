/*
  Please notice that 10 is being associated with lulz and 12 is being
  associated with lol.

  The below variables are where the data needs to be fed from the backend.

  Upon deployment, please, get rid of the values those are being innitialized.
*/

var frequencyOfWord = []; // y-axis element
var words = []; //X-axis element

// Grabs vars from html file
function resultant(x, y ) {
  frequencyOfWord = y;
  words = x;
}

var chartInit = document.getElementById("myChart").getContext('2d');

var chart = new Chart(chartInit, {
  type: 'bar',
  data: {
    labels: words,
    datasets:[{
      data: frequencyOfWord
    }],
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});
