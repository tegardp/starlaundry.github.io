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

// Lebaran holiday popup (19-23 Mar 2026)
(function() {
    var now = new Date();
    var start = new Date(2026, 2, 18); // 18 Mar 2026
    var end = new Date(2026, 2, 23, 23, 59, 59); // 23 Mar 2026 end of day
    if (now >= start && now <= end) {
        var overlay = document.createElement('div');
        overlay.className = 'holiday-overlay';
        overlay.innerHTML =
            '<div class="holiday-popup">' +
                '<div class="holiday-icon">&#127772;</div>' +
                '<h2>Libur Hari Raya Idul Fitri</h2>' +
                '<p>Mohon maaf lahir dan batin</p>' +
                '<div class="holiday-dates">Libur: 19 &ndash; 23 Maret 2026</div>' +
                '<p class="holiday-reopen">Buka kembali: 24 Maret 2026</p>' +
                '<button class="holiday-close-btn" onclick="this.closest(\'.holiday-overlay\').remove()">Mengerti</button>' +
            '</div>';
        document.body.appendChild(overlay);
    }
})();

// Dynamic copyright year (BEAD-029)
document.querySelectorAll('.footer-bottom').forEach(function(el) {
    el.innerHTML = el.innerHTML.replace(/© \d{4}/, '© ' + new Date().getFullYear());
});
