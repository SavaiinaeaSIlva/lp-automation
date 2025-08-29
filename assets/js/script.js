// script.js - CORRECTED VERSION
document.addEventListener('DOMContentLoaded', function() {
    // ALL code should be inside this callback
    const animatedSections = document.querySelectorAll('.section-animate');
    // ... existing code ...
    
    // Move ALL functionality inside this callback
    AOS.init({ duration: 800, once: true, offset: 50 });
    
    // Header scroll behavior
    const header = document.getElementById('main-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('header-scrolled');
            } else {
                header.classList.remove('header-scrolled');
            }
        });
    }
    
    // Mobile menu functionality
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');
    
    // ... rest of mobile menu code ...
    
    // Cookie banner logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');
    
    if (cookieBanner && acceptCookiesButton) {
        if (localStorage.getItem('cookiesAccepted') === 'true') {
            cookieBanner.style.display = 'none';
        } else {
            cookieBanner.style.display = '';
        }
        
        acceptCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.style.display = 'none';
        });
    }
}); // ONLY ONE closing brace and parenthesis here