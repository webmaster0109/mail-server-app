const logoutUser= document.querySelector('#logoutUser');
const logoutForm = document.querySelector('#logoutUserForm');
logoutUser.addEventListener('click', logoutAuthentication);

async function logoutAuthentication(e) {
    e.preventDefault();

    const csrfTokenOut = logoutForm.querySelector('[name=csrfmiddlewaretoken]').value;
    
    try {
        const response = await fetch('/account/logout-user/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfTokenOut,
            },
        });
    
        const result = await response.json();
    
        if (response.ok) {
            alert(result.message);
            setTimeout(() => {
                window.location.replace('/account/login/');
            }, 2000);
        } else {
            alert (result.message);
        }
    } catch (error) {
        console.log(error);
        alert('Something went wrong, try again.')
    }
}