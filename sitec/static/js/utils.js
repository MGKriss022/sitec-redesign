
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            };
        };
    };
    return cookieValue;
  }
  
var requestHeaders = {
    'Accept-Language': navigator.language,
    'X-CSRFToken': getCookie('csrftoken'),
  }

function suiSetRequestHeaders(xhr){
    xhr.setRequestHeader('Accept-Language', navigator.language)
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
    return xhr
  }