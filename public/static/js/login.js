
const form = document.querySelector('.login-form');

form.addEventListener('submit', loginFormAuthentication);

async function loginFormAuthentication(e) {
    e.preventDefault();

    const formData = new FormData(form);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch('/account/login/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData,
    });

    const result = await response.json();

    if (response.ok) {
        alert(result.message);
        setTimeout(() => {
            window.location.replace('/account/dashboard/');
        }, 2000);
    } else {
        alert(result.message);
    }
}