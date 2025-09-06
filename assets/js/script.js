document.addEventListener('DOMContentLoaded', function() {
    // --- Initialize Animate On Scroll (AOS) Library ---
    if (typeof AOS !== 'undefined') {
        AOS.init({ 
            duration: 800, 
            once: true, 
            offset: 50
        });
    }
    
    // --- Header Scroll Behavior ---
    /*
    const header = document.getElementById('main-header');
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('header-scrolled');
            } else {
                header.classList.remove('header-scrolled');
            }
        };
        handleScroll(); 
        window.addEventListener('scroll', handleScroll);
    }
    */
    
    // --- Mobile Menu Functionality ---
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');
    
    const openMobileMenu = () => {
        if (!mobileMenu || !mobileMenuButton) return;
        mobileMenu.classList.add('mobile-menu-open');
        mobileMenu.classList.remove('mobile-menu-closed');
        mobileMenuButton.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
    };

    const closeMobileMenu = () => {
        if (!mobileMenu || !mobileMenuButton) return;
        mobileMenu.classList.add('mobile-menu-closed');
        mobileMenu.classList.remove('mobile-menu-open');
        mobileMenuButton.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    };

    if (mobileMenuButton) mobileMenuButton.addEventListener('click', openMobileMenu);
    if (closeMobileMenuButton) closeMobileMenuButton.addEventListener('click', closeMobileMenu);
    
    if (mobileMenu) {
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }
    
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('mobile-menu-open')) {
            closeMobileMenu();
        }
    });
    
    // --- Dynamic Copyright Year ---
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
    
    // --- Cookie Banner Logic ---
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');
    
    if (cookieBanner && acceptCookiesButton) {
        setTimeout(() => {
            if (localStorage.getItem('cookieConsentGiven') !== 'true') {
                cookieBanner.style.transform = 'translateY(0)';
            }
        }, 1500);
        
        acceptCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookieConsentGiven', 'true');
            cookieBanner.style.transform = 'translateY(100%)';
        });
    }
    
    // --- Smooth Scrolling for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            // Ensure it's not a link used by the SPA logic
            if (href === '#' || href.length < 2 || this.classList.contains('legal-link')) {
                return;
            }
            const targetElement = document.getElementById(href.substring(1));
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});
