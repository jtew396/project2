// Template for creating a channel
// const template = Handlebars.compile("<li>New Channel</li>");

// Storing a list of channels
const channels = []

// Storing a list of users
const users = []

// Storing the user's display name as username
//const username = []

// Once the DOM is loaded, run the following function
document.addEventListener('DOMContentLoaded', () => {

    // Hide the inner HTML of the frame before loggin the user in
    document.querySelector('#frame').style.visibility = 'hidden';

    // This is adapted from the currency app, needs to be adjusted for register & login
    document.querySelector('#new-user').onsubmit = () => {

        // Initialize new request
        //const request = new XMLHttpRequest();
        const username = document.querySelector('#username-create').value;
        document.querySelector('#frame').style.visibility = 'visible';
        document.querySelector('#introduction').style.visibility = 'hidden';
        //console.log(username);
        //request.open('POST', '/register');
        //console.log("Past the request.");
        // Callback function for when request completes
        /*
        request.onload = () => {
            console.log("Onload of the request.")
            // Extract JSON data from requests
            const data = JSON.parse(request.responseText);
            console.log(data);

            // Update the webpage
            if (data.success) {
                const contents = `Hello ${data.username}!`;
                document.querySelector('#introduction').style.visibility = 'hidden';
                document.querySelector('#frame').style.visibility = 'visible';
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'Username already exists.';
            }
        };
        */

    };

});
