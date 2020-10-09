$(function() {
    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
              console.log(response);
              alert('Successfully signed up! Please login to continue.');
            },
            error: function(error) {
              console.log(error);
              alert('Sign up failed.');
            }
        });
    });
});
