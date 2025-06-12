document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('submit', async function(event) {
        if (event.target.matches('.restore-form') || event.target.matches('.permanent-delete-form')) {
            event.preventDefault();
            const form = event.target;
            const url = form.action;
            const csrf = form.querySelector('[name=csrfmiddlewaretoken]').value;
            const mailId = url.split('/').filter(Boolean).pop();
            // const isPermanent = form.matches('.permanent-delete-form');
            
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrf,
                    'Content-Type': 'application/json'
                }
            });

            const result = await response.json();
            if (response.ok) {
                createToast(result.message, 'Success');

                document.getElementById(`trash-row-${mailId}`).remove();
                document.getElementById(`deletePermanentModal-${mailId}`).remove();

                setTimeout(() => {
                  window.location.reload();
                })
            } else {
              alert('An error occurred: ' + data.message);
            }
        }
    });
});