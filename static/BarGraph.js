/*
  Please notice that 10 is being associated with lulz and 12 is being
  associated with lol.

  The below variables are where the data needs to be fed from the backend.

  Upon deployment, please, get rid of the values those are being innitialized.
*/
/*integer*/var frequencyOfWord = yresult; // y-axis element
/*list*/var words = xresult; //X-axis element

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
