// Contact information constants
const CONTACT_INFO = {
    email: 'contact@silvaautomation.com',
    phone: '(808) 308-1107',
    address: 'Silva Automation, 94-207 Waipahu Street #323, Waipahu, HI 96797'
};

// DOM Ready function
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Main initialization function
function initializeApp() {
    initializeAnimations();
    setupMobileMenu();
    setupSmoothScrolling();
    // setupScrollSnap();
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
        
        // Update aria-expanded for accessibility
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
        
        // Update aria-expanded for accessibility
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        if (mobileMenuButton) {
            mobileMenuButton.setAttribute('aria-expanded', 'false');
        }
    }
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
            } else {
                console.warn(`Target element not found for href: ${href}`);
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
                if (entry.target.id !== 'faq') {
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

// Header scroll behavior - hide on scroll down, show on scroll up
function setupHeaderScrollBehavior() {
    const header = document.getElementById('main-header');
    if (!header) return;
    
    let lastScrollY = window.scrollY;
    let ticking = false;
    
    function updateHeader() {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > lastScrollY && currentScrollY > 100) {
            // Scrolling down and past 100px - hide header
            header.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up or at top - show header
            header.style.transform = 'translateY(0)';
        }
        
        lastScrollY = currentScrollY;
        ticking = false;
    }
    
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(updateHeader);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestTick, { passive: true });
}

// Utility function to set current year
function setCurrentYear() {
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
}

// Contact form handling - Switched to Formspree
function setupContactForm() {
    // The form submission is now handled by the 'action' attribute in the HTML.
    // The JavaScript fetch logic is no longer needed.
    // I am leaving the old code here, commented out, in case you want to switch back to n8n later.
    /*
    const contactForm = document.getElementById('contact-form');
    
    if (!contactForm) return;
    
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.textContent;
        
        // Show loading state
        submitButton.textContent = 'Sending...';
        submitButton.disabled = true;
        
        try {
            // Get form data
            const formData = new FormData(contactForm);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                message: formData.get('message'),
                form_type: 'contact',
                source: 'landing_page',
                timestamp: new Date().toISOString(),
                url: window.location.href
            };
            
            // Send to n8n webhook
            const response = await fetch('https://n8n.ssilva.space/webhook/31d9264e-2d99-4c75-bbd8-eb86c0ede5ee', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                // Show success message
                showFormMessage(contactForm, 'Thank you! I\'ll get back to you within 24 hours.', 'success');
                contactForm.reset();
            } else {
                throw new Error('Failed to send message');
            }
            
        } catch (error) {
            console.error('Form submission error:', error);
            showFormMessage(contactForm, 'Sorry, there was an error sending your message. Please try again or contact me directly.', 'error');
        } finally {
            // Reset button state
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
        }
    });
    */
}

// Helper function to show form messages - This is no longer used by the form, but kept for potential future use.
function showFormMessage(form, message, type) {
    // Remove any existing messages
    const existingMessage = form.querySelector('.form-message');
    if (existingMessage) {
        existingMessage.remove();
    }
    
    // Create new message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `form-message p-4 rounded-lg text-sm font-medium ${
        type === 'success' 
            ? 'bg-green-500/10 border border-green-500/20 text-green-400' 
            : 'bg-red-500/10 border border-red-500/20 text-red-400'
    }`;
    messageDiv.textContent = message;
    
    // Insert message before the submit button
    const submitButton = form.querySelector('button[type="submit"]');
    form.insertBefore(messageDiv, submitButton.parentElement);
    
    // Auto-remove success messages after 5 seconds
    if (type === 'success') {
        setTimeout(() => {
            messageDiv.remove();
        }, 5000);
    }
}


// Export functions for global access if needed
window.App = {
    openMobileMenu,
    closeMobileMenu,
    initializeApp
};
