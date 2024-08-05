
function toggleApproval(bidId) {
    $.ajax({
        type: 'GET',
        url: `/api/toggle_approval/${bidId}/`,
        success: function(response) {
            if (response.status === 'success') {
                const bidStatusElement = $('.current-status');
                const button = $('#approvalButton');

                if (response.is_approved === 'yes') {
                    bidStatusElement.text('Approved').removeClass('text-danger').addClass('text-success');
                    button.text('Change Status');
                } else {
                    bidStatusElement.text('Not Approved').removeClass('text-success').addClass('text-danger');
                    button.text('Change Status');
                }
            } else {
                console.error(response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
}


function toggleUserApproval(userId) {
    $.ajax({
        type: 'GET',
        
        url: `/api/toggle_user_approval/${userId}/`,
        success: function(response) {
            if (response.status === 'success') {
                const bidStatusElement = $('.current-status');
                const button = $('#userapprovalButton');

                if (response.is_approved === 'yes') {
                    bidStatusElement.text('Approved').removeClass('text-danger').addClass('text-success');
                    button.text('Change Status');
                } else {
                    bidStatusElement.text('Not Approved').removeClass('text-success').addClass('text-danger');
                    button.text('Change Status');
                }
            } else {
                console.error(response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
}

function toggle_user_assessment_approval(assissment_id) {
    $.ajax({
        type: 'GET',
        
        url: `/api/toggle_user_assessment_approval/${assissment_id}/`,
        success: function(response) {
            if (response.status === 'success') {
                const bidStatusElement = $('.current-status');
                const button = $('#assessment-approval');

                if (response.is_approved === 'yes') {
                    bidStatusElement.text('Approved').removeClass('text-danger').addClass('text-success');
                    button.text('Change Status');
                } else {
                    bidStatusElement.text('Not Approved').removeClass('text-success').addClass('text-danger');
                    button.text('Change Status');
                }
            } else {
                console.error(response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
}


function toggle_product_approval(product_id) {
    $.ajax({
        type: 'GET',
        
        url: `/api/toggle-product-approval/${product_id}/`,
        success: function(response) {
            if (response.status === 'success') {
                const bidStatusElement = $('.current-status');
                const button = $('#product-approval');

                if (response.is_approved === 'yes') {
                    bidStatusElement.text('Approved').removeClass('text-danger').addClass('text-success');
                    button.text('Change Status');
                } else {
                    bidStatusElement.text('Not Approved').removeClass('text-success').addClass('text-danger');
                    button.text('Change Status');
                }
            } else {
                console.error(response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
}