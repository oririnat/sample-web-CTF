$(document).ready(function () {
    // HTML5 automatically adds the attribute 'novalidate=novalidate'     <- Maybe this is a hint?
    // $('#contactForm').removeAttr('novalidate');

    // validate contactForm form
    $('#contactForm').validate({
        rules: {
            subject: {
                required: true,
                minlength: 4
            },
            message: {
                required: true,
                minlength: 20
            }
        },
        messages: {
            subject: {
                required: "come on, you have a subject, don't you?",
                minlength: "your subject must consist of at least 4 characters"
            },
            message: {
                required: "um...yea, you have to write something to send this form.",
                minlength: "thats all? really?"
            }
        },
        submitHandler: function (form) {
            $(form).ajaxSubmit({
                type: "GET",
                data: $(form).serialize(),
                success: function () {
                    alert("ok");
                },
            })
        }
    })

    var subject = getUrlVars()['subject'];

    if (subject != null) {
        sendMessage(decodeURIComponent(subject));
    }

    $('#submit').click(function () {
        $("#contactForm").valid();
    });
})

var getUrlVars = function () {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}

var sendMessage = function (subject) {
    if ((subject != null) && (subject != "")) {
        $("#messageSent").html("The message about " + subject + " was successfully transmitted");
    }
}