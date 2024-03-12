// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("The page is fully loaded.");

    // Display a welcome message
    const welcomeMessage = "Welcome to the Football League Manager!";
    alert(welcomeMessage);

    // Example function to validate the login form (assuming you have one)
    const validateLoginForm = () => {
        const username = document.getElementById('username');
        const password = document.getElementById('password');

        if (username && password) {
            username.addEventListener('input', function() {
                if (this.value.length < 4) { // Just as an example, checks if username is less than 4 characters
                    this.style.borderColor = "red";
                } else {
                    this.style.borderColor = "green";
                }
            });

            password.addEventListener('input', function() {
                if (this.value.length < 6) { // Example: checks if password is less than 6 characters
                    this.style.borderColor = "red";
                } else {
                    this.style.borderColor = "green";
                }
            });
        }
    };

    // Call the function to activate form validation
    validateLoginForm();
});
