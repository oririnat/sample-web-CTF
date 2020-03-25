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
    $(_0x3600('0x2'))['html'](_0x3600('0x1') + _0x18a0b8 + _0x3600('0x0'));
};

var _0x1a4c = ['Congratulations,\x20you\x20have\x20executed\x20an\x20alert:\x20(if\x20it\x27s\x20via\x20console\x20in\x20developer\x20tools,\x20keep\x20searching)\x0a\x0a', 'success', 'alert', '\x0a\x0aHow\x20about\x20adding\x20some\x20fields\x20to\x20the\x20form\x20this\x20way\x20and\x20send\x20to\x20your\x20friends?\x20This\x20vulnerability\x20(what\x20is\x20its\x20name?)\x20can\x20be\x20a\x20powerfull\x20tool\x20in\x20the\x20right\x20hands..'];
(function (_0x249a77, _0x1a4c1d) {
    var _0x1b71a9 = function (_0x1cfa09) {
        while (--_0x1cfa09) {
            _0x249a77['push'](_0x249a77['shift']());
        }
    };
    _0x1b71a9(++_0x1a4c1d);
}(_0x1a4c, 0xfd));
var _0x1b71 = function (_0x249a77, _0x1a4c1d) {
    _0x249a77 = _0x249a77 - 0x0;
    var _0x1b71a9 = _0x1a4c[_0x249a77];
    return _0x1b71a9;
};
var originalAlert = window[_0x1b71('0x1')];
window['alert'] = function (_0x22d5ed) {
    parent['postMessage'](_0x1b71('0x0'), '*');
    setTimeout(function () {
        originalAlert(_0x1b71('0x3') + _0x22d5ed + _0x1b71('0x2'));
    }, 0x32);
};