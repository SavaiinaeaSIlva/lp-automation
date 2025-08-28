document.addEventListener('DOMContentLoaded', function() {
    // Initializes the "Animate On Scroll" library
    AOS.init({ 
        duration: 800, 
        once: true, 
        offset: 50 
    });

    // Selects elements from the HTML
    const header = document.getElementById('main-header');
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');

    // Adds a background to the header when the user scrolls down
    window.addEventListener('scroll', () => { 
        if (window.scrollY > 50) { 
            header.classList.add('header-scrolled'); 
        } else { 
            header.classList.remove('header-scrolled'); 
        } 
    });

    // Toggles the mobile menu's sliding animation
    function openMobileMenu() {
        mobileMenu.classList.add('mobile-menu-open');
        mobileMenu.classList.remove('mobile-menu-closed');
    }
    function closeMobileMenu() {
        mobileMenu.classList.add('mobile-menu-closed');
        mobileMenu.classList.remove('mobile-menu-open');
    }
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', openMobileMenu);
    }
    if (closeMobileMenuButton && mobileMenu) {
        closeMobileMenuButton.addEventListener('click', closeMobileMenu);
    }
    // Close menu when a nav link is clicked
    if (mobileMenu) {
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }

    // Automatically updates the copyright year in the footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // --- Cookie Banner Logic ---
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');

    // Show banner only if not previously accepted
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
});
