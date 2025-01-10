document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('#delete-mail');

    deleteButtons.forEach((button) => {
        button.addEventListener('click', async (e) => {
            e.preventDefault();

            const mailId = button.getAttribute('data-mail-id');
            const mailIdInt = parseInt(mailId);
            console.log(mailId, typeof mailIdInt);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            const response = await fetch(`/account/mail/delete/${mailIdInt}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                }
            });

            const result = await response.json();

            if (response.ok) {
                createToast(result.message, 'Success');
                // Optionally, remove the deleted mail row from the UI
                const mailRow = button.closest('tr');
                if (mailRow) {
                    mailRow.remove();
                }
            } else {
                createToast(result.message, 'Warning');
            }
        });
    });
});
