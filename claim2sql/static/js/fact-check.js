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


// function submitForm() {
//     const userInput = document.getElementById("input-text").value;
//     if (userInput === "") {
//         alert("Please input a claim to check!");
//         return;
//     }

//     fetch("/submit", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ text: userInput }),
//     })
//         .then((response) => response.text())
//         .then((html) => {
//             const parser = new DOMParser();
//             const doc = parser.parseFromString(html, "text/html");

//             // Get the input sentence element from the parsed HTML
//             const inputSentenceElement = doc.getElementById("inputSentence");

//             // Model outputs data
//             const model_outputs = {
//                 input_sentence: "Joe Biden voted for the Iraq War.",
//                 agent: { start: 0, end: 8, explanation: "Joe Biden is the agent." },
//                 target: { start: 10, end: 14, explanation: "voted is the target." },
//                 // frame_elements: {
//                 //     Agent: { start: 0, end: 8, explanation: "Explanation for 'agent'" },
//                 //     Issue: { start: 12, end: 16, explanation: "Explanation for 'issue'" },
//                 //     Position: { start: 4, end: 6, explanation: "Explanation for 'position'" },
//                 // },
//                 position: { start: 16, end: 19, explanation: "for is the position." },
//                 issue: { start: 20, end: 31, explanation: "the Iraq War is the issue." },
//             };

//             const sentenceText = model_outputs.input_sentence;
//             const elements = Object.keys(model_outputs).filter((key) => key !== "input_sentence" && key !== "frame_elements");
//             elements.sort((a, b) => model_outputs[a].start - model_outputs[b].start);

//             let sentenceHTML = "";
//             let lastIndex = 0;

//             elements.forEach(function (element, index) {
//                 const { start, end, explanation } = model_outputs[element];
//                 const before = sentenceText.substring(lastIndex, start);
//                 const word = sentenceText.substring(start, end + 1);

//                 // Generate a unique class name for each highlighted element
//                 const className = `highlight-${index + 1}`;

//                 sentenceHTML += `${before}<span class="highlight ${className}" onmouseover="showPopup(this);" onmouseout="hidePopup(this);">
//                     ${word}
//                     <span class="popup">${explanation}</span>
//                 </span>`;

//                 lastIndex = end + 1;
//             });

//             sentenceHTML += sentenceText.substring(lastIndex);

//             inputSentenceElement.innerHTML = sentenceHTML;

//             // Replace the result container's innerHTML with the modified HTML
//             document.getElementById("results-container").innerHTML = doc.documentElement.innerHTML;
//         })
//         .catch((error) => {
//             console.error("Error:", error);
//         });
//     $("html,body").animate(
//         {
//             scrollTop: $("#input-text").offset().top,
//         },
//         "slow"
//     );
// }

// function showPopup(element) {
//     const popup = element.querySelector(".popup");
//     popup.style.visibility = "visible";
// }

// function hidePopup(element) {
//     const popup = element.querySelector(".popup");
//     popup.style.visibility = "hidden";
// }
