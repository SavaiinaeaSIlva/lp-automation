// DOM Ready function
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Main initialization function
function initializeApp() {
    initializeAnimations();
    setupMobileMenu();
    setupBackToTopButton();
    setupSmoothScrolling();
    setupScrollSnap();
    setupCookieBanner();
    setupLegalPages();
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
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });
}

function openMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu) {
        mobileMenu.classList.remove('translate-x-full');
        document.body.style.overflow = 'hidden';
    }
}

function closeMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu) {
        mobileMenu.classList.add('translate-x-full');
        document.body.style.overflow = '';
    }
}

// Back to top button
function setupBackToTopButton() {
    const backToTopBtn = document.createElement('button');
    backToTopBtn.id = 'back-to-top-btn';
    backToTopBtn.textContent = '↑ Top';
    backToTopBtn.className = 'fixed right-8 bottom-8 z-50 p-3 bg-blue-600 text-white rounded-full shadow-lg hover:bg-blue-700 transition-all duration-300 opacity-0 pointer-events-none';
    
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 400) {
            backToTopBtn.classList.remove('opacity-0', 'pointer-events-none');
            backToTopBtn.classList.add('opacity-100', 'pointer-events-auto');
        } else {
            backToTopBtn.classList.remove('opacity-100', 'pointer-events-auto');
            backToTopBtn.classList.add('opacity-0', 'pointer-events-none');
        }
    });

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Smooth scrolling
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
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

// Enhanced scroll snap functionality
function setupScrollSnap() {
    let isScrolling = false;
    let scrollTimeout;
    
    // Add scroll snap behavior
    document.documentElement.style.scrollSnapType = 'y mandatory';
    
    // Handle scroll events for smooth transitions
    window.addEventListener('scroll', function() {
        if (!isScrolling) {
            isScrolling = true;
            document.body.classList.add('scrolling');
        }
        
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(function() {
            isScrolling = false;
            document.body.classList.remove('scrolling');
        }, 150);
    });
    
    // Add intersection observer for section visibility
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -20% 0px',
        threshold: 0.5
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Skip scaling animation for FAQ section to prevent vibrating
                if (!entry.target.id === 'faq') {
                    entry.target.classList.add('section-active');
                }
                // Add subtle animation to section content
                const content = entry.target.querySelector('.section-content');
                if (content) {
                    content.style.animation = 'fadeInUp 0.8s ease-out';
                }
            } else {
                entry.target.classList.remove('section-active');
            }
        });
    }, observerOptions);
    
    // Observe all sections
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
    
    // Enhanced keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
            e.preventDefault();
            const sections = Array.from(document.querySelectorAll('section'));
            const currentSection = sections.find(section => {
                const rect = section.getBoundingClientRect();
                return rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2;
            });
            
            if (currentSection) {
                const currentIndex = sections.indexOf(currentSection);
                let targetIndex;
                
                if (e.key === 'ArrowDown') {
                    targetIndex = Math.min(currentIndex + 1, sections.length - 1);
                } else {
                    targetIndex = Math.max(currentIndex - 1, 0);
                }
                
                sections[targetIndex].scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'start' 
                });
            }
        }
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
                e.preventDefault(); 
                showMainView(); 
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

// Utility function to set current year
function setCurrentYear() {
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
}

// Export functions for global access if needed
window.App = {
    openMobileMenu,
    closeMobileMenu,
    initializeApp
};
