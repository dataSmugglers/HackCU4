var data; // Fetch data to here.

var chartInit = document.getElementById("myChart").getContext('2d');
var chart = new Chart(chartInit, {
  type: 'bar',
  data: {
    labels: ["TestingOne", "TestingTwo"],
    datasets:[{
      data: [/* Pass data variable here. */]
    }]
  }
});
