document.addEventListener('DOMContentLoaded', function() {
    // Select all flash messages
    const flashMessages = document.querySelectorAll('.flash-message');

    // Set the duration to display the message (e.g., 5 seconds)
    const displayDuration = 5000; // 5000 milliseconds = 5 seconds

    flashMessages.forEach(function(message) {
        // Set a timeout to hide the message after the duration
        setTimeout(function() {
            message.classList.add('hidden');
        }, displayDuration);
    });
});