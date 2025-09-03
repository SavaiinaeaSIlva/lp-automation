// script.js - FINAL VERSION
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

    document.addEventListener('click', function(event) {
        if (mobileMenu && mobileMenu.classList.contains('mobile-menu-open') && 
            !mobileMenu.contains(event.target) && 
            !mobileMenuButton.contains(event.target)) {
            closeMobileMenu();
        }
    });

    if (mobileMenu) {
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }
    
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
    
    // Handle Netlify contact form submission with redirect
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Stop the default page reload

            const form = e.target;
            const data = new FormData(form);
            const action = form.action;
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.innerHTML;
            const formStatus = document.getElementById('form-status');

            // Give user feedback
            submitButton.disabled = true;
            submitButton.innerHTML = 'Sending...';
            if(formStatus) formStatus.textContent = ''; 

            fetch('/', { // Netlify recommends fetching the root path for AJAX submissions
                method: 'POST',
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams(data).toString(),
            })
            .then(response => {
                // Netlify's AJAX submission doesn't return a standard response object,
                // but we assume success if no error is thrown. The redirect is the main goal.
                window.location.href = form.action; // Redirect to the 'action' URL (e.g., /success.html)
            })
            .catch(error => {
                if(formStatus) {
                    formStatus.textContent = 'Sorry, there was an error. Please try again.';
                    formStatus.className = 'text-center h-4 text-red-400';
                }
                // Restore button even on error
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonText;
            });
        });
    }
});
