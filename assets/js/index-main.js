document.addEventListener('DOMContentLoaded', function() {
    // --- Netlify Contact Form AJAX Submission ---
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const form = e.target;
            const formData = new FormData(form);
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.innerHTML;
            const formStatus = document.getElementById('form-status');

            submitButton.disabled = true;
            submitButton.innerHTML = 'Sending...';
            if(formStatus) formStatus.textContent = ''; 

            fetch('/', {
                method: 'POST',
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams(formData).toString(),
            })
            .then(() => {
                window.location.href = form.getAttribute('action');
            })
            .catch(() => {
                if(formStatus) {
                    formStatus.textContent = 'Sorry, there was an error. Please try again.';
                    formStatus.className = 'text-center h-4 text-red-400 text-sm';
                }
            })
            .finally(() => {
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonText;
            });
        });
    }

    // --- Single-Page View Logic for Legal Pages ---
    const mainView = document.getElementById('main-view');
    const legalView = document.getElementById('legal-view');
    const legalPages = document.querySelectorAll('.legal-page');
    const legalLinks = document.querySelectorAll('.legal-link');
    const backToMainButton = document.getElementById('back-to-main');
    const homeLogoLink = document.getElementById('home-logo-link');
    const homeFooterLink = document.getElementById('home-footer-link');

    const showMainView = (shouldScrollToTop = true) => {
        if (!mainView || !legalView) return;
        mainView.classList.remove('hidden');
        legalView.classList.add('hidden');
        if (shouldScrollToTop) window.scrollTo(0, 0);
        history.pushState(null, null, window.location.pathname);
    };

    const showLegalPage = (pageId) => {
        if (!mainView || !legalView) return;
        mainView.classList.add('hidden');
        legalView.classList.remove('hidden');
        legalPages.forEach(page => page.classList.add('hidden'));
        const pageToShow = document.getElementById(pageId);
        if(pageToShow) pageToShow.classList.remove('hidden');
        window.scrollTo(0, 0);
    };

    legalLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const pageId = link.dataset.page;
            showLegalPage(pageId);
            history.pushState({page: pageId}, null, link.getAttribute('href'));
        });
    });

    if (backToMainButton) backToMainButton.addEventListener('click', (e) => { e.preventDefault(); showMainView(); });
    if (homeLogoLink) homeLogoLink.addEventListener('click', (e) => { e.preventDefault(); showMainView(); });
    if (homeFooterLink) homeFooterLink.addEventListener('click', (e) => { e.preventDefault(); showMainView(); });

    // Handle browser back/forward buttons
    window.addEventListener('popstate', (e) => {
        if (e.state && e.state.page) {
            showLegalPage(e.state.page);
        } else {
            showMainView(false);
        }
    });

    // Check URL on initial load to show the correct legal page if linked directly
    const hash = window.location.hash.substring(1);
    const pageMap = {'terms': 'terms-page', 'privacy': 'privacy-page', 'cookie': 'cookie-page', 'refund': 'refund-page'};
    if (pageMap[hash]) {
        showLegalPage(pageMap[hash]);
    }
});	
