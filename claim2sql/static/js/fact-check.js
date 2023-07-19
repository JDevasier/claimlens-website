function submitForm() {
    const userInput = document.getElementById("input-text").value;
    if (userInput === "") {
        alert("Please input a claim to check!");
        return;
    }

    fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: userInput }),
    })
        .then((response) => response.text())
        .then((html) => {
            document.getElementById("results-container").innerHTML = html;
            $("html,body").animate(
                {
                    scrollTop: $("#input-text").offset().top,
                },
                "slow"
            );
            $('.fe-agent, .fe-issue, .fe-side, .fe-position, .fe-frequency, .fe-time, .fe-place, .fe-support_rate')
                .popup({
                    inline: true,
                    hoverable: true,
                    position: 'top center',
                    delay: {
                        show: 0,
                        hide: 0
                    }
                });
        });
}
