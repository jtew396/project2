// Template for creating a channel
const template = Handlebars.compile("<li>New Channel</li>");

// Storing a list of channels
const channels = []

document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // After websocket is connected...
    socket.on('connect', () => {

        // Register a new usern
        document.querySelector('#')

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
