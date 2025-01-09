
const form = document.querySelector('#send-email-form');
form.addEventListener('submit', sendEmailSystem);

async function sendEmailSystem(e) {
    e.preventDefault();

    const textareaData = tinymce.get('amaraEditor').getContent();
    const subject = document.querySelector('[name=subject]').value;
    const retreiveEmails = document.querySelector('[name=emails]').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const emailUser = document.querySelector('#emailUser').value;
    console.log(emailUser);

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

    const response = await fetch('/account/dashboard/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            emails: retreiveEmails,
            subject: subject,
            textareaData: textareaData,
            emailUser: emailUser,
        })
    });

    const result = await response.json();

    if (response.ok) {
        alert(result.message);
    } else {
        alert(result.message);
    }
}