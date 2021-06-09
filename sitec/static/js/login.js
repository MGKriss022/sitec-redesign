$(window).on('load', function(){

    let loginForm = $('.login.form').form({

    }).api({
        on: 'submit',
        serializeForm: true,
        action: 'login',
        method: 'POST',
        beforeXHR: suiSetRequestHeaders,
        beforeSend: function(settings){
            return settings
        },
        onSuccess: function(){

        },
        onError: function(){
            
        }
    })
})