var index = 0;

$(function() {
    $("#pos").html(data['words'][0]['pos']);

    $('#word').keypress(function(e) {
        if (e.keyCode == 13) {
            data['words'][index]['newword'] = $("#word").val()
            $("#word").val('');
            index += 1;
            if (index >= data['words'].length) {
                $.post('/result', {data: JSON.stringify(data)}, function(result) {
                    result = result.replace( /\&lt;/g, '<').replace(/\&gt;/g, '>');
                    $("#wrapper").html(result);
                });
                return;
            }
            $("#prog").attr("value", 100*index/data['words'].length);
            $("#pos").html(data['words'][index]['pos']);
            e.preventDefault();
        }
    });
});
