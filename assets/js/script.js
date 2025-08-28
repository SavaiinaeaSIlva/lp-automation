document.addEventListener('DOMContentLoaded', function() {
    // --- Section Animate In/Out on Scroll ---
    const animatedSections = document.querySelectorAll('.section-animate');
    const sectionObserver = new window.IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-in');
                entry.target.classList.remove('section-out');
            } else {
                entry.target.classList.remove('section-in');
                entry.target.classList.add('section-out');
            }
        });
    }, {
        threshold: 0.25
    });
    animatedSections.forEach(section => {
        sectionObserver.observe(section);
    });
    // --- Hero Logo Shrink and Hero Animate Out ---
    const heroLogo = document.getElementById('hero-logo');
    const heroContent = document.getElementById('hero-content');
    const heroSection = document.getElementById('hero');

    function handleHeroScroll() {
        const scrollY = window.scrollY;
        const heroRect = heroSection.getBoundingClientRect();
        // Shrink logo when not at top
        if (scrollY > 40) {
            heroLogo && heroLogo.classList.add('hero-logo-shrink');
        } else {
            heroLogo && heroLogo.classList.remove('hero-logo-shrink');
        }
        // Animate hero content out when scrolled past hero
        if (heroRect.bottom < 60) {
            heroContent && heroContent.classList.add('hero-content-hidden');
        } else {
            heroContent && heroContent.classList.remove('hero-content-hidden');
        }
    }
    window.addEventListener('scroll', handleHeroScroll);
    // Run once on load
    handleHeroScroll();
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
