function makeFetchRequest(url, options) {
    fetch(url, options)
    .then(response => {
        if (!response.ok) {
            // This will catch HTTP error statuses (e.g., 404, 500)
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'success') {
            // Safely assume data.redirect_url is provided on success
            window.location.href = data.redirect_url;
        } else {
            // Check if missing_names is provided and is an array before joining
            const missingNamesMsg = Array.isArray(data.missing_names) ? "Error: missing names " + data.missing_names.join(", ") : "An error occurred.";
            showToastMessage(missingNamesMsg, "error");
        }
    })
    .catch(error => {
        // This catch will handle network issues and errors thrown from the first .then()
        showToastMessage(error.message, 'error');
    });
}


function showToastMessage(message, type) {
    const toastElId = type === 'error' ? 'errorToast' : 'successToast';
    const toastEl = document.getElementById(toastElId);
    const toastBody = toastEl.querySelector('.toast-body');
    toastBody.textContent = message;
    var toast = new bootstrap.Toast(toastEl);
    toast.show();
}

document.addEventListener('DOMContentLoaded', () => {
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    document.querySelectorAll('[data-action="fetchRequest"]').forEach(element => {
        element.addEventListener('click', (event) => {
            event.preventDefault();

            const url = element.getAttribute('data-url');
            const method = element.getAttribute('data-method') || 'GET'; // Default to GET if not specified
            const data = element.getAttribute('data-body') ? JSON.parse(element.getAttribute('data-body')) : {};

            const options = {
                method: method,
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
            };

            // If it's a POST request, add the body
            if (method === 'POST') {
                options.body = JSON.stringify(data);
            }

            makeFetchRequest(url, options);
        });
    });
});