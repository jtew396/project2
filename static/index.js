$(document).ready(function() {
	const chat = io.connect('http://' + document.domain + ':' + location.port + '/chat');
	chat.on('connect', function() {
		chat.emit('join');

		chat.on('send_message', function(data) {
			// $("#messages").append('<div class=\"alert alert-primary\" id=\"' + data.user_id + data.timestamp + '\"><div class=\"row\"><div class="col"><div class=\"float-left\"><span class=\"font-weight-bold\">' + data.user_id + '</span> - ' + data.timestamp + '</div></div><div class=\"co\"><button type=\"button\" class=\"close\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button></div></div><div class=\"row\" id=\"message\"><div class=\"col\"><div class=\"float-left\">' + data.msg + '</div></div></div></div>');
			$("#messages").append('<div class=\"alert alert-primary\" id=\"' + data.message_id + '\"><div class=\"row\"><div class=\"col\"><div class=\"float-left\"><span class=\"font-weight-bold\">' + data.user_id + '</span> - ' + data.timestamp + '</div></div><div class=\"col\"><button type=\"button\" id=\"deleteMessage\" data-value=\"' + data.message_id + '\" class=\"close\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button></div></div><div class=\"row\" id=\"message\"><div class=\"col\"><div class=\"float-left\">' + data.msg + '</div></div></div></div>');
			// if (data.socket_id == chat.id) {
			// 	$("#messages").append('<div class=\"alert alert-primary\" id=\"messageBox\"><div class=\"row\"><div class="col"><div class=\"float-left\"><span class=\"font-weight-bold\">' + data.user_id + '</span> - ' + data.timestamp + '</div></div><div class=\"co\"><button type=\"button\" class=\"close\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button></div></div><div class=\"row\" id=\"message\"><div class=\"col\"><div class=\"float-left\">' + data.msg + '</div></div></div></div>');
			// } else {
			// 	$("#messages").append('<div class=\"alert alert-secondary\" id=\"messageBox\"><div class=\"row\"><div class="col"><div class=\"float-left\"><span class=\"font-weight-bold\">' + data.user_id + '</span> - ' + data.timestamp + '</div></div><div class=\"co\"></div></div><div class=\"row\" id=\"message\"><div class=\"col\"><div class=\"float-left\">' + data.msg + '</div></div></div></div>');
			// };
		});

		chat.on('delete_message', function(data){
			console.log(data.message_id);
			$('#' + data.message_id).remove();
		});

		$('#sendbutton').on('click', function() {
			console.log('We are trying to send a message and you pressed the button.');
			console.log($('#myMessage').val());
			var data = {
				// socket_id: chat.id,
				msg: $('#myMessage').val()
			};
			chat.emit('send_message', data);
			$('#myMessage').val('');
		});

		$('#myMessage').on('keypress', function(e) {
			if(e.which == 13 && $('#myMessage').val() != '') {
				var data = {
					// socket_id: chat.id,
					msg: $('#myMessage').val()
				};
				chat.emit('send_message', data);
				$('#myMessage').val('');
			};
		});

		$('#deleteMessage').on('click', function() {
			console.log('We have clicked the x');
			var data = {
				message_id: $(this).data('value'),
			};
			chat.emit('delete_message', data);
		});

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
