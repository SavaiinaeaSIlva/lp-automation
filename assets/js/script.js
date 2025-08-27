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

    // Adds a background to the header when the user scrolls down
    window.addEventListener('scroll', () => { 
        if (window.scrollY > 50) { 
            header.classList.add('header-scrolled'); 
        } else { 
            header.classList.remove('header-scrolled'); 
        } 
    });

    // Toggles the mobile menu visibility when the button is clicked
    mobileMenuButton.addEventListener('click', () => { 
        mobileMenu.classList.toggle('hidden'); 
        if (!header.classList.contains('header-scrolled')) { 
            header.classList.add('header-scrolled'); 
        } 
    });

    // Copies the desktop navigation links into the mobile menu
    const desktopNav = document.querySelector('nav.hidden.md\\:flex');
    if (desktopNav) {
        mobileMenu.innerHTML = `<nav class="flex flex-col items-center space-y-4">${desktopNav.innerHTML}</nav>`;
    }
    
    // Makes the mobile menu close when a link is clicked
    mobileMenu.querySelectorAll('a').forEach(link => { 
        link.addEventListener('click', () => { 
            mobileMenu.classList.add('hidden'); 
        }); 
    });

    // Automatically updates the copyright year in the footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // --- Cookie Banner Logic ---
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');

    if (cookieBanner && acceptCookiesButton) {
        if (!localStorage.getItem('cookieConsentGiven')) {
            setTimeout(() => {
                cookieBanner.classList.add('cookie-banner-visible');
            }, 1000);
        }

        acceptCookiesButton.addEventListener('click', () => {
            cookieBanner.classList.remove('cookie-banner-visible');
            localStorage.setItem('cookieConsentGiven', 'true');
        });
    }

});
