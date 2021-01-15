var counts, ebola, hiv, covid;

$.getJSON('http://127.0.0.1:8000/chart-data')
    .done(response => {
        counts = response['counts']
        ebola = Number(counts[0])
        hiv = Number(counts[1])
        covid = Number(counts[2])
        var ctx = document.getElementById("EbolaBarChart");
        if (ctx) {
            ctx.height = 150;
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ["Ebola", "HIV", "Covid"],
                    datasets: [
                        {
                            label: "Chart for infections",
                            data: [ebola, covid, hiv],
                            borderColor: "rgba(255, 255, 255, 0.1)",
                            borderWidth: "0",
                            backgroundColor: "rgba(255,255,255,0.5)"
                        }
                    ]
                },
                options: {
                    legend: {
                        position: 'top',
                        labels: {
                            fontFamily: 'Poppins'
                        }

                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                fontFamily: "Poppins"

                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontFamily: "Poppins"
                            }
                        }]
                    }
                }
            });
        }
    })

$.getJSON('http://127.0.0.1:8000/diseases-data')
    .done(response => {
        let diseases = Object.keys(response)
        let counts = Object.values(response)
        var ctx = document.getElementById("diseasespieChart");
        if (ctx) {
            ctx.height = 200;
            var myChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    datasets: [{
                        data: counts,
                        backgroundColor: [
                            "#52050A",
                            "#832161",
                            "#9B7EDE",
                            "#BCD2EE",
                            "#1C6E8C",
                            "#274156",
                            "#AF3B6E",
                            "#001F54",
                        ],
                        hoverBackgroundColor: [
                            "rgba(0, 123, 255,0.9)",
                        ]

                    }],
                    labels: diseases
                },
                options: {
                    legend: {
                        position: 'top',
                        labels: {
                            fontFamily: 'Poppins'
                        }

                    },
                    responsive: true
                }
            });
        }



    })
