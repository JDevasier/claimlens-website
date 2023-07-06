function submitForm() {
    const userInput = document.getElementById("input-text").value;
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'text': userInput }),
    }).then(response => response.text())
        .then(html => {
            document.getElementById("result-container").innerHTML = html;
        });
}
