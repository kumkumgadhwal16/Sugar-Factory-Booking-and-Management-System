/* ═══════════════════════════════════════════════════════════════
   Sugar Factory Booking System — Main JavaScript
   ═══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

    // ── Auto-dismiss flash messages ──────────────────────────────
    const alerts = document.querySelectorAll('.alert.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

    // ── Active nav link highlighting ────────────────────────────
    const currentPath = window.location.pathname;
    document.querySelectorAll('.sf-navbar .nav-link').forEach(function (link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // ── Smooth scroll for anchor links ──────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ── Hamburger menu (mobile) ──────────────────────────────────
    const toggler = document.querySelector('.navbar-toggler');
    if (toggler) {
        toggler.addEventListener('click', function () {
            this.classList.toggle('collapsed');
        });
    }

    // ── Scroll-to-top button ─────────────────────────────────────
    const scrollBtn = document.getElementById('scrollTopBtn');
    if (scrollBtn) {
        window.addEventListener('scroll', function () {
            scrollBtn.style.display = window.scrollY > 400 ? 'block' : 'none';
        });
        scrollBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ── Navbar scroll shadow ─────────────────────────────────────
    const navbar = document.querySelector('.sf-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.3)';
            } else {
                navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
            }
        });
    }

    // ── Tooltip init (Bootstrap 5) ───────────────────────────────
    const tooltipElems = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipElems.forEach(function (el) {
        new bootstrap.Tooltip(el);
    });

    console.log('Sugar Factory Booking System — JS loaded.');
});
