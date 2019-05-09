document.addEventListener('DOMContentLoaded', function() {

    // Have each button change the color of the heading
    document.querySelectorAll('.color-change').forEach(function(button) {
        button.onclick = function() {
            document.querySelector('#hello').style.color = button.dataset.color;
        };
    });
});