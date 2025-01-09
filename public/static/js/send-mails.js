
const form = document.querySelector('#send-email-form');
form.addEventListener('submit', sendEmailSystem);

async function sendEmailSystem(e) {
    e.preventDefault();

    const textareaData = tinymce.get('amaraEditor').getContent();
    const subject = document.querySelector('[name=subject]').value;
    const retreiveEmails = document.querySelector('[name=emails]').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    

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
        })
    });

    const result = await response.json();

    if (response.ok) {
        alert(result.message);
    } else {
        alert(result.message);
    }
}