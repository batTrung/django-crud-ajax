$(function(){

    var loadForm = function(){
        var form  = $(this);
        $.ajax({
            url: form.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-user').modal("show");
            },
            success: function(data){
                $('#modal-user .modal-content').html(data.html_form);
            }
        });
        return false;
    }

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            type: form.attr("method"),
            dataType: 'json',
            data: form.serialize(),
            success: function(data){
                if (data.form_valid){
                    $('#modal-user').modal("hide");
                    $('tbody').html(data.html_user_list);
                } else {
                    $('#modal-user .modal-content').html(data.html_form);
                }
            }
        })
        return false;
    }

// Created
$('#js-user-create').click(loadForm);
$('#modal-user').on('submit', '#js-user-create-form', saveForm);

// Update
$("#user-table").on('click', '#js-user-update', loadForm)
$('#modal-user').on('submit', '#js-user-update-form', saveForm);

// Delete
$("#user-table").on('click', '#js-user-delete', loadForm);
$('#modal-user').on('submit', '#js-user-delete-form', saveForm);
});