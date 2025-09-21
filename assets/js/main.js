// DOM Ready function
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Main initialization function
function initializeApp() {
    initializeAnimations();
    setupMobileMenu();
    setupSmoothScrolling();
    setupCookieBanner();
    setupLegalPages();
    setupHeaderScrollBehavior();
    setupContactForm();
    setCurrentYear();
}

// Animation setup
function initializeAnimations() {
    if (typeof AOS !== 'undefined') {
        AOS.init({ 
            duration: 800, 
            once: true, 
            offset: 50,
            easing: 'ease-out-cubic'
        });
    } else {
        // Fallback: wait for AOS to load (shouldn't happen with sync loading)
        const checkAOS = setInterval(() => {
            if (typeof AOS !== 'undefined') {
                AOS.init({ 
                    duration: 800, 
                    once: true, 
                    offset: 50,
                    easing: 'ease-out-cubic'
                });
                clearInterval(checkAOS);
            }
        }, 50);
        
        // Stop checking after 2 seconds
        setTimeout(() => clearInterval(checkAOS), 2000);
    }
}

// Mobile menu functionality
function setupMobileMenu() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', openMobileMenu);
    }

    if (closeMobileMenuButton) {
        closeMobileMenuButton.addEventListener('click', closeMobileMenu);
    }

    // Close mobile menu when nav links are clicked
    const navLinks = document.querySelectorAll('#mobile-menu .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });
}

function openMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu) {
        mobileMenu.classList.remove('translate-x-full');
        document.body.style.overflow = 'hidden';
        
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        if (mobileMenuButton) {
            mobileMenuButton.setAttribute('aria-expanded', 'true');
        }
    }
}

function closeMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu) {
        mobileMenu.classList.add('translate-x-full');
        document.body.style.overflow = '';
        
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        if (mobileMenuButton) {
            mobileMenuButton.setAttribute('aria-expanded', 'false');
        }
    }
}


// Smooth scrolling for anchor links on the same page
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            // Ignore simple hash links and legal links handled by SPA logic
            if (href === '#' || this.classList.contains('legal-link')) return;
            
            const targetElement = document.querySelector(href);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'start' 
                });
            }
        });
    });
}

// Cookie banner
function setupCookieBanner() {
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');
    
    if (cookieBanner && acceptCookiesButton) {
        setTimeout(() => {
            if (localStorage.getItem('cookiesAccepted') !== 'true') {
                cookieBanner.classList.remove('translate-y-full');
            }
        }, 2000);
        
        acceptCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.classList.add('translate-y-full');
        });
    }
}

// Legal pages SPA functionality
function setupLegalPages() {
    const mainView = document.getElementById('main-view');
    const legalView = document.getElementById('legal-view');
    const legalPages = document.querySelectorAll('.legal-page');
    const legalLinks = document.querySelectorAll('.legal-link');
    const backToMainButton = document.getElementById('back-to-main');
    const homeLinks = [
        document.getElementById('home-logo-link'), 
        document.getElementById('home-footer-link')
    ];

    function showMainView() {
        if (mainView) mainView.classList.remove('hidden');
        if (legalView) legalView.classList.add('hidden');
        window.scrollTo(0, 0);
        if (window.location.hash) {
            history.pushState(null, null, window.location.pathname);
        }
    }

    function showLegalPage(pageId) {
        if (mainView) mainView.classList.add('hidden');
        if (legalView) legalView.classList.remove('hidden');
        
        legalPages.forEach(page => page.classList.add('hidden'));
        const pageToShow = document.getElementById(pageId);
        if(pageToShow) pageToShow.classList.remove('hidden');
        
        window.scrollTo(0, 0);
    }

    legalLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const pageId = link.dataset.page;
            showLegalPage(pageId);
            history.pushState({page: pageId}, null, link.getAttribute('href'));
            closeMobileMenu();
        });
    });

    if (backToMainButton) {
        backToMainButton.addEventListener('click', (e) => { 
            e.preventDefault(); 
            showMainView(); 
        });
    }

    homeLinks.forEach(link => {
        if (link) {
            link.addEventListener('click', (e) => { 
                // If we're already on the main view, this acts as a "scroll to top"
                if (!mainView.classList.contains('hidden')) {
                    e.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                } else {
                    // If on a legal page, go back to main view
                    e.preventDefault();
                    showMainView();
                }
            });
        }
    });

    // Handle browser history
    window.addEventListener('popstate', (e) => {
        if (e.state && e.state.page) {
            showLegalPage(e.state.page);
        } else {
            showMainView();
        }
    });

    // Initial page load handling
    const hash = window.location.hash.substring(1);
    const pageMap = {
        'terms': 'terms-page', 
        'privacy': 'privacy-page', 
        'cookie': 'cookie-page', 
        'refund': 'refund-page'
    };
    
    if (pageMap[hash]) {
        showLegalPage(pageMap[hash]);
    }
}

// Header scroll behavior
function setupHeaderScrollBehavior() {
    const header = document.getElementById('main-header');
    if (!header) return;
    
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        if (currentScrollY > lastScrollY && currentScrollY > 100) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }
        lastScrollY = currentScrollY;
    }, { passive: true });
}

// Utility function to set current year
function setCurrentYear() {
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
}

// Contact form handling - now uses Formspree
function setupContactForm() {
    // The form submission is now handled by the 'action' attribute in the HTML.
    // No specific JavaScript is needed for submission itself.
}

// Export functions for global access if needed
window.App = {
    openMobileMenu,
    closeMobileMenu,
    initializeApp
};
