// Template for creating a channel
const template = Handlebars.compile("<li>New Channel</li>");

// Storing a list of channels
const channels = []

// Storing a list of users
const users = []

document.addEventListener('DOMContentLoaded', () => {

    // Hide the inner HTML of the frame before logging the user in
    document.querySelector('#frame').style.visibility = 'hidden';

    // This is adapted from the currency app, needs to be adjusted for register & login
    document.querySelector('#new-user').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();
        const username = document.querySelector('#username-create').value;
        request.open('POST', '/register');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from requests
            const data = JSON.parse(request.responseText);

            // Update the webpage
            if (data.success) {
                const contents = `${data.username}`;
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'Username already exists.';
            }
        };

        // Add data to send with request????
        const data = new FormData();
        data.append('currency', currency);

        // Send request
        request.send(data);
        return false;
    };

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // After websocket is connected...
    socket.on('connect', () => {

        // Register a new username
        document.querySelector('#username-submit').onclick = () => {

            // Generate a username from the input
            const username = parseText(document.querySelector('#username-create').value);
            socket.emit('registration', {'username': username});
        };

        // When a username has been created (or logged in), allow chatting feature
        socket.on('logged in', data => {

        })

        // After websocket is connected, create a channel.
        document.querySelector('#create-channel').onclick = () => {

            // Generate a submitted channel.
            const channel = parseText(document.querySelector('#new-channel').value);
            channels.push(channel)
        };
    });

    // On click for channel, send content to DOM.
    document.querySelector('#create-channel').onclick = () => {

        // Generate a submitted channel.
        const channel = parseText(document.querySelector('#new-channel').value);
        channels.push(channel)

        // Add the channel to DOM
        const channel_content = template({'value': roll});
        document.querySelector('#channels').innerHTML += channel_content;
    }

    // Update text on popping state
    window.onpopstate = e => {
        const data = e.state;
        document.title = data.title;
        document.querySelector('#body').innerHTML = data.text;
    };

    // Renders contents of new page in main view.
    function load_page(name) {
        const request = new XMLHttpRequest();
        request.open('GET', `/${name}`);
        request.onload = () => {
            const response = request.responseText;
            document.querySelector('#body').innerHTML = response;

            // Push state to URL.
            document.title = name;
            history.pushState({'title': name, 'text': response}, name, name);
        };
        request.send();
    };

});
