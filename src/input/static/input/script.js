var input_count = 1;


function add_field() {
    var input_html = '<div class="name-item">\
    <input name="name_'+input_count+'" id="empty" type="text" />\
    <button style = "margin-left: 10px;"\
    onclick="send_data(document.getElementsByName(\'name_'+input_count+'\')[0], this)">Send</button>\
    </div>';

    var d1 = document.getElementsByClassName('item');
    d1[0].insertAdjacentHTML('beforeend', input_html);
    input_count += 1;
}


function send_data(element, bttn) {
        $.ajax({
            url: '/api/v1/create/',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'name' : element.name, 'data' : element.value}),
            statusCode:{
                201:function(){
                    element.disabled = true;
                    bttn.disabled = true;
                }
            }  
        });
}
