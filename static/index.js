// Template for creating a channel
// const template = Handlebars.compile("<li>New Channel</li>");

// Storing a list of channels
const channels = []

// Storing a list of users
const users = []

// Once the DOM is loaded, run the following function
document.addEventListener('DOMContentLoaded', () => {

    // Hide the inner HTML of the frame before logging the user in
    document.querySelector('#frame').style.visibility = 'hidden';

    // Connect to web socket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Once the web socket is established
    socket.on('connect', () => {

        // Listen for the user to submit a display name
        document.querySelector('#new-user').onclick = () => {

            // Store the display name as username
            const username = document.querySelector('#username-create').value;

            // Hide the welcome page and display name input
            document.querySelector('#introduction').innerHTML = "";
            document.querySelector('#introduction').classList.remove('p-5');

            // Display the available chat rooms and users
            document.querySelector('#frame').style.visibility = 'visible';

        };

        document.querySelector('#message-send').onclick = () => {

            
        };
    });
});
