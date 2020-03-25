$(document).ready(function () {
    // HINT: Subject is your friend

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

var _0xe84c = ['The\x20message\x20about\x20', '#messageSent', '\x20was\x20successfully\x20transmitted'];
(function (_0x3ae27f, _0xe84cbd) {
    var _0x360020 = function (_0x298f7e) {
        while (--_0x298f7e) {
            _0x3ae27f['push'](_0x3ae27f['shift']());
        }
    };
    _0x360020(++_0xe84cbd);
}(_0xe84c, 0x15b));
var _0x3600 = function (_0x3ae27f, _0xe84cbd) {
    _0x3ae27f = _0x3ae27f - 0x0;
    var _0x360020 = _0xe84c[_0x3ae27f];
    return _0x360020;
};
var sendMessage = function (_0x18a0b8) {
    // let's change only the text of the div, not its html
    $(_0x3600('0x2'))['text'](_0x3600('0x1') + _0x18a0b8 + _0x3600('0x0'));
};