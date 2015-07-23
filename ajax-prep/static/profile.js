
function submitProfile(evt) {
    evt.preventDefault();

    $.post("/profile",
        $('#profile-form').serialize(),
        function (result) {
            $('#profile').append("<p>" + "Name: " + result.user_name + "</p>");
        }
    );
}

$("#profile-form").on('submit', submitProfile);
