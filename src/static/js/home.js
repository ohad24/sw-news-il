var email;

$('#subscription-input-btn').click(function() {
    email = $('#subscription-input').val();
    var subModal = new bootstrap.Modal(document.getElementById('subscription-modal'))
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
    var selected_cbs = $('#tags-select-input-list-modal .form-check-input:checked')
    selected_cbs.each(function() {
        console.log($(this).val());
    });
});
