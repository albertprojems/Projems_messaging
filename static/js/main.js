function start_sendig() {

    $('#responce').html("Sending to <span id='curent-number'></span>");
    var numbers = $('#numbers').val();
    var message = $('#message').val();
    var path_uri = "multiple_number.php";
    var number = numbers.split('+');
    var key = "";
    var secrete = "";
    var dummy_number = "";


    //radio button value
    var provider = $('input[name=radio-grp]:checked').val();


    if (provider == "telnyx") {
        key = $('#api_key').val();
        secrete = $('#telnyx_token').val();
        dummy_number = $('#source').val();
    }


    $.ajax({
        type: "POST",
        url: path_uri,
        data: {
            numbers: number_loop(number),
            message: message,
            provider: provider,
            key: key,
            secrete: secrete,
            dummy_number: dummy_number
        },
        success: function (data) {

            console.log(data);


            var json = $.parseJSON(data);
            if (json[2] == "telnyx") {
                if (json[1] == "0") {
                    $('#responce').html("Message Sent Successfully to " + json[0] + " !!");
                }
            } else if (json.response == "success") {
                $('#responce').html("Message Sent Successfully to " + json.current + " !!");
            } else {
                $('#responce').html("Error to Sent " + json.current + " !!");
            }

        }

    });
}

var i = 1;
function number_loop(numbers) {
    var number = numbers[i];
    $("#curent-number").html(number);
   if (++i < numbers.length) {
        setTimeout(start_sendig, 1000);
   }
    return number;
}

//upload xls
$('#upload_list').on('change', function () {
    $('#outer-loader').show();
    var file_data = $('#upload_list').prop('files')[0];
    var form_data = new FormData();
    form_data.append('file', file_data);


    $.ajax({
        url: 'uploadtxt.php', // point to server-side PHP script 
        dataType: 'text', // what to expect back from the PHP script, if anything
        cache: false,
        contentType: false,
        processData: false,
        data: form_data,
        type: 'post',
        success: function (data) {
            $('#numbers').html(data);

        }
    });
});


$(document).ready(function () {
    $('input[name=radio-grp]').change(function () {
        if ($('#rdo-0').prop('checked')) {
            $('.enable-nexmo').show();
            $('.enable-twilio').hide();
            $('.enable-textlocal').hide();
        } else if ($('#rdo-1').prop('checked')) {

            //twilio
            $('.enable-twilio').show();
            $('.enable-nexmo').hide();
            $('.enable-textlocal').hide();

        } else if ($('#rdo-2').prop('checked')) {
            $('.enable-twilio').hide();
            $('.enable-nexmo').hide();
            $('.enable-textlocal').show();
        } else if ($('#rdo-4').prop('checked')) {
            $('.enable-twilio').hide();
            $('.enable-nexmo').hide();
            $('.enable-textlocal').hide();
            $('.enable-sinch').show();
            $('.enable-telnyx').hide();
        } else if ($('#rdo-5').prop('checked')) {
            $('.enable-twilio').hide();
            $('.enable-nexmo').hide();
            $('.enable-textlocal').hide();
            $('.enable-sinch').hide();
            $('.enable-telnyx').show();
        }
    });

});