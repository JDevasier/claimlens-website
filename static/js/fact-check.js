function submitForm() {
    const userInput = document.getElementById("input-text").value;
    if (userInput === "") {
        alert("Please input a claim to check!");
        return;
    }

    //  Create AJAX call to send user input to server
    $.ajax({
        type: "GET",
        url: "https://idir.uta.edu/claimlens/api/",
        data: { query: userInput },
        success: function (response) {
            document.getElementById("results-container").innerHTML = response;
            $("html,body").animate(
                {
                    scrollTop: $("#input-text").offset().top,
                },
                "slow"
            );

            $('.fe-agent, .fe-issue, .fe-side, .fe-position, .fe-frequency, .fe-time, .fe-place, .fe-support_rate').popup({
                inline: true,
                hoverable: true,
                position: 'top center',
                delay: {
                    show: 0,
                    hide: 0
                }
            });

        },
        error: function (error) {
            console.log(error);
        }
    });
}

function toggleSummary(e) {
    $(e).parent().find('.bill-summary').toggleClass('hide-long-text');
    if ($(e).text() == 'Show more') {
        $(e).text('Show less');
    } else {
        $(e).text('Show more');
    }
}
