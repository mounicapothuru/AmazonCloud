function Query() {
       // country= $('#MySQL')[0].selectedOptions[0].value;
        var query= $('#Query')[0].value;
        $.ajax({
            url: '/query/'+query,
            data: query,
            type: 'POST',
            success: function(response) {
                countrysuccess(response)
            },
            error: function(error) {
                console.log(error);
            }
        });

}

function countrysuccess(response) {

            html='';
            html = html + '<table class="table table-bordered">' +
                '<thead>' +
                '<tr>';
            $.each(response[0],function (index,column) {
                html = html + '<th scope="col">' + column + '</th>'
            });
            html = html + '</tr>' +
                '</thead>' +
                '<tbody>';
            $.each(response[1],function (key,value) {
                html = html + '<tr>'
                $.each(response[0],function (i,val) {
                     html=html+'<td>' + value[val] + '</td>'
                });
                html=html+'</tr>'
            });
            html=html+'</tbody>'+
            '</table>'
            $('.table').html(html);
}