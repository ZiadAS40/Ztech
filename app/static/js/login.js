document.querySelector('form').onsubmit = async function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const response = await fetch('/login', {
        method: 'POST',
        body: formData
    });

    // Ensure to handle the response once and check if it's JSON
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
        const data = await response.json();  // Read JSON response

        if (response.ok) {
            // Store the JWT in local storage
            localStorage.setItem('access_token', data.access_token);

            // Redirect to the page in the response
            window.location.href = data.redirect_url;
        } else {
            alert("Login failed: " + data.message || "An error occurred");
        }
    } else {
        const text = await response.text();
        alert("Unexpected response: " + text);
    }
};
