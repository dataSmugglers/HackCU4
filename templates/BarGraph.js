/*
  Please notice that 10 is being associated with lulz and 12 is being
  associated with lol.
*/
/*integer*/var frequencyOfWord = [10, 12]; // y-axis element
/*list*/var words = ["lulz", "lol"]; //X-axis element

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
