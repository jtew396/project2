// Template for creating a channel
// const template = Handlebars.compile("<li>New Channel</li>");

// Storing a list of channels
const channels = []

// Storing a list of users
const users = []

function FlackSettings(users, channels) {
	return settings
};

$(document).ready(function() {

	var socket = io.connect('http://127.0.0.1:5000');

	$('#create_display_name').on('click', function() {
		$.post("/", {
			display_name: $('#display_name').val('')
		});
		console.log('Display Name Created');
	});
	$('#display_name').on('keypress', function(e) {
		if(e.which == 13) {
			$.post("/", {
				display_name: $('#display_name').val('')
			});
			console.log('Display Name Created');
		}
	});

	socket.on('connect', function() {
		socket.send('User has connected!');
	});

	socket.on('message', function(msg) {
		$("#messages").append('<li>'+msg+'</li>');
		console.log('Received message');
	});

	$('#sendbutton').on('click', function() {
		socket.send($('#myMessage').val());
		$('#myMessage').val('');
	});
    $('#myMessage').on('keypress', function(e) {
        if(e.which == 13) {
            socket.send($('#myMessage').val());
    		$('#myMessage').val('');
        }
    });

});

// Once the DOM is loaded, run the following function
//document.addEventListener('DOMContentLoaded', () => {
//
//    // Hide the inner HTML of the frame before logging the user in
//    document.querySelector('#frame').style.visibility = 'hidden';
//
//    // Connect to web socket
//    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
//
//    // Once the web socket is established
//    socket.on('connect', () => {
//
//        // Listen for the user to submit a display name
//        document.querySelector('#new-user').onclick = () => {
//
//            // Store the display name as username
//            const username = document.querySelector('#username-create').value;
//
//            // Hide the welcome page and display name input
//            document.querySelector('#introduction').innerHTML = "";
//            document.querySelector('#introduction').classList.remove('p-5');
//
//            // Display the available chat rooms and users
//            document.querySelector('#frame').style.visibility = 'visible';
//
//        };
//
//        document.querySelector('#message-send').onclick = () => {
//
//
//        };
//    });
//});
