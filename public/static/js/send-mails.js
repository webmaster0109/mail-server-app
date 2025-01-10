
const form = document.querySelector('#send-email-form');
form.addEventListener('submit', sendEmailSystem);

async function sendEmailSystem(e) {
    e.preventDefault();

    const textareaData = tinymce.get('amaraEditor').getContent();
    const subject = document.querySelector('[name=subject]').value;
    const retreiveEmails = document.querySelector('[name=emails]').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const emailUser = document.querySelector('#emailUser').value;
    const attachments = document.querySelector('#file');
    const fileInput = attachments.files;

    // Validate form fields
    if (!emailUser) {
        alert('Please select a valid email user.');
        return;
    }
    if (!retreiveEmails) {
        alert('Please provide at least one email ID.');
        return;
    }
    if (!subject) {
        alert('Please provide a subject.');
        return;
    }
    if (!textareaData) {
        alert('Please provide email content.');
        return;
    }

    const formData = new FormData();
    formData.append('emails', retreiveEmails);
    formData.append('subject', subject);
    formData.append('textareaData', textareaData);
    formData.append('emailUser', emailUser);

    if (fileInput.length > 0) {
        for (let i = 0; i < fileInput.length; i++) {
            formData.append('file', fileInput[i]);
        }
    }

    const response = await fetch('/account/dashboard/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData
    });

    const result = await response.json();

    if (response.ok) {
        alert(result.message);
    } else {
        alert(result.message);
    }
}