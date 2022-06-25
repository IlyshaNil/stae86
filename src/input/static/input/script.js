var input_count = 1;


function add_field() {
    var input_html = '<div class="name-item">\
    <input id="name_'+input_count+'" type="text" />\
    <button style = "margin-left: 10px;"\
    onclick="send_data(document.getElementById(\'name_'+input_count+'\'))">Submit</button>\
    </div>';

    var d1 = document.getElementsByClassName('item');
    d1[0].insertAdjacentHTML('beforeend', input_html);
    input_count += 1;
}


function send_data(element) {
    if (element.name === ""){
        console.log('post')
        $.ajax({
            url: '/api/v1/list-create/',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'name' : element.id, 'data' : element.value}),
            success: function(data){
                alert(data);
                
            }
        });
        element.setAttribute('name', 'modified');
    }
    else{
        console.log('patch')
        $.ajax({
            url: '/api/v1/list-create/',
            method: 'PATCH',
            dataType: 'application/json; charset=utf-8',
            data: JSON.stringify(element.value),
            success: function(data){
                alert(data);
            }
        });
    }
}