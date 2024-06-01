document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('.sidebar a');

    const currentPath = window.location.pathname;

    links.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});
