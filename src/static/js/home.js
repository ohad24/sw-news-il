var email;
var subModal = new bootstrap.Modal(document.getElementById('subscription-modal'));


$('#subscription-input-btn').click(function() {
    email = $('#subscription-input').val();
    if (email.length ==  0) {
        return;
    }
    subModal.show();
    $('#display-email-f-model').text(email);
});


$('#select-all-tags-btn').click(function() {
    var sub_modal_cb_tags = $("#tags-select-input-list-modal .form-check-input");
    sub_modal_cb_tags.each(function(i) {
        var cs_box = $(this);
        cs_box.prop("checked", true);
    });
});


$('#subscribe-tags-modal-btn').click(function() {
    var selected_cbs = $('#tags-select-input-list-modal .form-check-input:checked');
    var tag_names = [];
    selected_cbs.each(function() {
        var tag_name = $(this).val();
        tag_names.push(tag_name)
    });
    console.log(tag_names);
    $.post( "/_subscribe", JSON.stringify({ 
        tag_names: tag_names, 
        email: email
    }));
    subModal.hide();
    var toast = new bootstrap.Toast(document.getElementById('toast-sub-success-msg'));
    toast.show();
});
