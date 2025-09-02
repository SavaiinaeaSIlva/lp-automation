// script.js - ENHANCED VERSION
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    AOS.init({ duration: 800, once: true, offset: 50 });
    
    // Header scroll behavior
    const header = document.getElementById('main-header');
    if (header) {
        if (window.scrollY > 50) {
            header.classList.add('header-scrolled');
        }
        
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
    
    function openMobileMenu() {
        if (mobileMenu && mobileMenuButton) {
            mobileMenu.classList.add('mobile-menu-open');
            mobileMenu.classList.remove('mobile-menu-closed');
            mobileMenuButton.setAttribute('aria-expanded', 'true');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeMobileMenu() {
        if (mobileMenu && mobileMenuButton) {
            mobileMenu.classList.add('mobile-menu-closed');
            mobileMenu.classList.remove('mobile-menu-open');
            mobileMenuButton.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        }
    }

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', openMobileMenu);
    }

    if (closeMobileMenuButton && mobileMenu) {
        closeMobileMenuButton.addEventListener('click', closeMobileMenu);
    }

    // Close menu when clicking outside (FIXED)
    document.addEventListener('click', function(event) {
        if (mobileMenu && mobileMenu.classList.contains('mobile-menu-open') && 
            !mobileMenu.contains(event.target) && 
            !mobileMenuButton.contains(event.target)) { // <-- FIX is here
            closeMobileMenu();
        }
    });

    // Close menu when nav links are clicked
    if (mobileMenu) {
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }
    
    // Close menu on escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('mobile-menu-open')) {
            closeMobileMenu();
        }
    });
    
    // Update copyright year
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
    
    // Cookie banner logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');
    
    if (cookieBanner && acceptCookiesButton) {
        // Use a slight delay to prevent layout shift issues on load
        setTimeout(() => {
            if (localStorage.getItem('cookiesAccepted') !== 'true') {
                cookieBanner.style.display = 'block';
            }
        }, 500);
        
        acceptCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.style.display = 'none';
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Handle custom contact form submission
document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Stop the default page reload

            const form = e.target;
            const data = new FormData(form);
            const action = form.action;
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.innerHTML;

            // Give user feedback
            submitButton.disabled = true;
            submitButton.innerHTML = 'Sending...';
            formStatus.textContent = ''; 

            fetch(action, {
                method: 'POST',
                body: data,
            })
            .then(response => {
                if (response.ok) {
                    formStatus.textContent = "Thanks! Your message has been sent.";
                    formStatus.className = 'text-center h-4 text-green-400';
                    form.reset(); // Clear the form
                } else {
                    throw new Error('Server responded with an error.');
                }
            })
            .catch(error => {
                formStatus.textContent = 'Sorry, there was an error. Please try again.';
                formStatus.className = 'text-center h-4 text-red-400';
            })
            .finally(() => {
                // Restore button
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonText;
            });
        });
    }
});
