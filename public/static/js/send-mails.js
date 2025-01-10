
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

    console.log(textareaData);

    // Validate form fields
    if (!emailUser) {
        createToast('Please select a valid email user.', 'Warning');
        return;
    }
    if (!retreiveEmails) {
        createToast('Please provide at least one email ID.', 'Warning');
        return;
    }
    if (!subject) {
        createToast('Please provide a subject.', 'Warning');
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

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: formData
        });
    
        const result = await response.json();
    
        if (response.ok) {
            createToast(result.message, 'Success');
        } else {
            createToast(result.message, 'Error');
        }
    } catch (error) {
        console.log(error);
        createToast('Something went wrong, try again.', 'Error');
    }
}