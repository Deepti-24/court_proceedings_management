$(function() {
    $('#btnLogin').click(function() {

        $.ajax({
            url: '/logIn',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                window.location.reload();
                console.log(response);
            },
            error: function(error) {
                console.log(error);
                alert('Login failed.');
            }
        });
    });
});
