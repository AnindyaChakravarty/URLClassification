document.getElementById('urlForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const urlInput = document.getElementById('urlInput').value;
    const resultHeading = document.getElementById('resultHeading');

    // Validate URL format using a simple regular expression
    const urlPattern = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/i;
    if (!urlPattern.test(urlInput)) {
        alert("Please enter a valid URL.");
        return;
    }

    // Send POST request to Flask backend
    fetch('/check_url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: urlInput }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.result === 1) {
            document.body.style.backgroundColor = "#f8d7da"; // Light red background
            resultHeading.textContent = "This URL could be a phishing URL";
            resultHeading.style.color = "#721c24"; // Dark red text
        } else if (data.result === 0) {
            document.body.style.backgroundColor = "#d4edda"; // Light green background
            resultHeading.textContent = "This URL is safe";
            resultHeading.style.color = "#155724"; // Dark green text
        } else {
            document.body.style.backgroundColor = "#e2e3e5"; // Light purple background
            resultHeading.textContent = "There was an error, please try again later";
            resultHeading.style.color = "#6c757d"; // Dark grey text
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong. Please try again later.");
    });
});
