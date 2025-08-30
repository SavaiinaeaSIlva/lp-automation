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

