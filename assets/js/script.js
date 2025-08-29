document.addEventListener('DOMContentLoaded', function() {
    // --- Section Animate In/Out on Scroll ---
    const animatedSections = document.querySelectorAll('.section-animate');
    if (animatedSections.length > 0) {
        const sectionObserver = new IntersectionObserver((entries) => {
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
    }

    // --- Hero Logo Shrink and Hero Animate Out ---
    const heroLogo = document.getElementById('hero-logo');
    const heroContent = document.getElementById('hero-content');
    const heroSection = document.getElementById('hero');

    if (heroSection) {
        function handleHeroScroll() {
            const scrollY = window.scrollY;
            const heroRect = heroSection.getBoundingClientRect();
            
            // Shrink logo when not at top
            if (heroLogo) {
                if (scrollY > 40) {
                    heroLogo.classList.add('hero-logo-shrink');
                } else {
                    heroLogo.classList.remove('hero-logo-shrink');
                }
            }
            
            // Animate hero content out when scrolled past hero
            if (heroContent) {
                if (heroRect.bottom < 60) {
                    heroContent.classList.add('hero-content-hidden');
                } else {
                    heroContent.classList.remove('hero-content-hidden');
                }
            }
        }
        
        window.addEventListener('scroll', handleHeroScroll);
        // Run once on load
        handleHeroScroll();
    }

    // Initialize AOS library
    if (typeof AOS !== 'undefined') {
        AOS.init({ 
            duration: 800, 
            once: true, 
            offset: 50 
        });
    }

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
        
        // Initialize on load
        if (window.scrollY > 50) {
            header.classList.add('header-scrolled');
        }
    }

    // Mobile menu functionality
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');

    // Toggles the mobile menu's sliding animation
    function openMobileMenu() {
        if (mobileMenu) {
            mobileMenu.classList.add('mobile-menu-open');
            mobileMenu.classList.remove('mobile-menu-closed');
            document.body.style.overflow = 'hidden';
        }
    }
    
    function closeMobileMenu() {
        if (mobileMenu) {
            mobileMenu.classList.add('mobile-menu-closed');
            mobileMenu.classList.remove('mobile-menu-open');
            document.body.style.overflow = '';
        }
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

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (mobileMenu && 
            !mobileMenu.classList.contains('mobile-menu-closed') &&
            !mobileMenu.contains(e.target) &&
            e.target !== mobileMenuButton &&
            !mobileMenuButton.contains(e.target)) {
            closeMobileMenu();
        }
    });

    // Automatically updates the copyright year in the footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // Cookie Banner Logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');

    // Show banner only if not previously accepted
    if (cookieBanner && acceptCookiesButton) {
        if (localStorage.getItem('cookiesAccepted') === 'true') {
            cookieBanner.style.display = 'none';
        } else {
            cookieBanner.style.display = 'block';
        }
        
        acceptCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.style.display = 'none';
        });
    }
});
