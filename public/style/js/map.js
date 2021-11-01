var settings = {
    "url": "http://127.0.0.1:5000/ioi?Num=3",
    "method": "GET",
    "timeout": 0,
};

$.ajax(settings).done(function(response) {
    console.log(response);
});