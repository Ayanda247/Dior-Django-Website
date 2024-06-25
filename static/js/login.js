// login.js

document.addEventListener('DOMContentLoaded', function() {
    // DOMContentLoaded event ensures all elements are loaded before executing JS

    // Function to handle form submission and add slick behavior
    const form = document.querySelector('form'); // Assuming there's only one form on the page
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Perform client-side validation or other operations if needed

        // Simulate loading state with a loading spinner or text
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Logging in...';

        // Optionally, you can make an AJAX request here to submit the form data
        // For simplicity, I'm adding a delay to simulate the process
        setTimeout(function() {
            // After processing, restore the button text
            submitBtn.textContent = 'Login';

            // Redirect to a new page or handle success message
            window.location.href = "{% url 'shop:home' %}"; // Redirect to home page after login
        }, 2000); // Simulate a 2-second delay (adjust as needed)
    });

    // Additional JavaScript functionalities can be added as per your requirements
});