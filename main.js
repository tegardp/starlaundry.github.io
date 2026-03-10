// Close mobile nav on link click
document.querySelectorAll('.nav-links a').forEach(function(link) {
    link.addEventListener('click', function() {
        document.getElementById('navLinks').classList.remove('open');
    });
});

// Track WhatsApp clicks (BEAD-028)
document.querySelectorAll('a[href*="wa.me"]').forEach(function(link) {
    link.addEventListener('click', function() {
        if (typeof gtag === 'function') {
            gtag('event', 'whatsapp_click', {
                event_category: 'contact',
                event_label: link.closest('nav') ? 'navbar' : link.classList.contains('wa-float') ? 'floating' : 'page'
            });
        }
    });
});

// Dynamic copyright year (BEAD-029)
document.querySelectorAll('.footer-bottom').forEach(function(el) {
    el.innerHTML = el.innerHTML.replace(/© \d{4}/, '© ' + new Date().getFullYear());
});
