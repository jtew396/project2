$(document).ready(function() {
	const chat = io.connect('http://' + document.domain + ':' + location.port + '/chat');
	chat.on('connect', function() {
		// $('#join_channel').click(function () {
		// 	var channel_name = $(this)[0].innerHTML;
		// 	// console.log($(this)[0].innerHTML);
		// 	console.log("We're trying to join the " + channel_name + " channel.");
		// 	socket.emit('join', {'room': channel_name});
		// });
		socket.on('send_message', function(data) {
			console.log('The user: ' + data['user_id']);
			console.log('The message: ' + data['msg']);
			$("#messages").append('<div class=\"alert alert-primary\" id=\"messageBox\"><div class=\"row\"><div class=\"float-left\"><span class=\"font-weight-bold\">' + data['user_id'] + '</span> - 12:23 PM</div></div><div class=\"row\" id=\"message\">' + data['msg'] + '</div></div>');
			console.log('Received message');
		});

		socket.on('json', function(data) {
			console.log('The user: ' + data['user_id']);
			console.log('The message: ' + data['msg']);
			$("#messages").append('<div class=\"alert alert-primary\" id=\"messageBox\"><div class=\"row\"><div class=\"float-left\"><span class=\"font-weight-bold\">' + data['user_id'] + '</span> - 12:23 PM</div></div><div class=\"row\" id=\"message\">' + data['msg'] + '</div></div>');
			console.log('Received message');
		})

		$('#sendbutton').on('click', function() {
			console.log('We are trying to send a message and you pressed the button.');
			console.log($('#myMessage').val());
			socket.emit('send_message', $('#myMessage').val());
			$('#myMessage').val('');
		});

		// socket.send('User has connected!');

	});


	// // Have a new user create a display name
	// socket.on('my response', function(user_data) {
	// 	console.log(user_data);
	// 	$("#user").append('<li>'+user_data["display_name"]+' has joined Flack.</li>');
	// 	console.log('User has joined Flack.');
	// });
	//
	// $('#create_display_name').on('click', function() {
	// 	console.log('So you clicked the button.')
	// 	socket.emit( 'my event', {
	// 		"display_name": $('#display_name').val()
	// 	} )
	// 	console.log($('#display_name').val(''));
	// });
	//
	// $('#display_name').on('keypress', function(e) {
	// 	console.log('So you pressed enter.')
	// 	if(e.which == 13) {
	// 		socket.emit( 'my event', {
	// 			"display_name": $('#display_name').val()
	// 		} )
	// 		$('#display_name').val('');
    //     }
	// });
	//
	//
	//
    // $('#myMessage').on('keypress', function(e) {
    //     if(e.which == 13) {
    //         socket.send($('#myMessage').val());
    // 		$('#myMessage').val('');
    //     }
    // });
	//
	// $('#joinChannelButton').on('click', function() {
	// 	var room = $(this).val();
	// 	console.log(room);
	// 	//socket.join(room);
	// });

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
