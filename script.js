document.addEventListener('DOMContentLoaded', () => {

    // --- NAVIGATION HIGHLIGHT LOGIC (SCROLL & CLICK) ---
    const navLinks = document.querySelectorAll('.side-nav a');
    const sections = document.querySelectorAll('.right-panel section');
    const rightPanel = document.querySelector('.right-panel');

    function setActiveLink(id) {
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${id}`) {
                link.classList.add('active');
            }
        });
    }

    if (navLinks.length > 0 && sections.length > 0 && rightPanel) {
        const isMobile = window.matchMedia("(max-width: 1024px)").matches;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setActiveLink(entry.target.getAttribute('id'));
                }
            });
        }, { 
            root: isMobile ? null : rightPanel,
            rootMargin: "-40% 0px -40% 0px"
        });

        sections.forEach(section => {
            observer.observe(section);
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                setActiveLink(link.getAttribute('href').substring(1));
            });
        });
    }
    
    // --- ROI CALCULATOR LOGIC ---
    const teamSizeSlider = document.getElementById('team-size');
    if (teamSizeSlider) {
        const hoursWastedSlider = document.getElementById('hours-wasted');
        const hourlyWageSlider = document.getElementById('hourly-wage');
        const teamSizeValue = document.getElementById('team-size-value');
        const hoursWastedValue = document.getElementById('hours-wasted-value');
        const hourlyWageValue = document.getElementById('hourly-wage-value');
        const annualSavingsResult = document.getElementById('annual-savings-result');
        const weeklySavingsResult = document.getElementById('weekly-savings-result');
        const monthlySavingsResult = document.getElementById('monthly-savings-result');
        const hoursSavedResult = document.getElementById('hours-saved-result');
        
        const calculateROI = () => {
            const teamSize = parseFloat(teamSizeSlider.value);
            const hoursWasted = parseFloat(hoursWastedSlider.value);
            const hourlyWage = parseFloat(hourlyWageSlider.value);
            
            teamSizeValue.textContent = teamSize;
            hoursWastedValue.textContent = hoursWasted;
            hourlyWageValue.textContent = `$${hourlyWage}`;
            
            const weeklyHours = teamSize * hoursWasted;
            const weeklySavings = weeklyHours * hourlyWage;
            const monthlySavings = weeklySavings * 4.33;
            const annualSavings = weeklySavings * 52;
            const annualHours = weeklyHours * 52;

            const formatCurrency = (value) => value.toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0, maximumFractionDigits: 0 });

            annualSavingsResult.textContent = formatCurrency(annualSavings);
            weeklySavingsResult.textContent = formatCurrency(weeklySavings);
            monthlySavingsResult.textContent = formatCurrency(monthlySavings);
            hoursSavedResult.textContent = annualHours.toLocaleString();
        };
        
        [teamSizeSlider, hoursWastedSlider, hourlyWageSlider].forEach(slider => {
            slider.addEventListener('input', calculateROI);
        });
        
        calculateROI();
    }

    // --- LEGAL MODAL (POPUP) LOGIC ---
    const openModalButtons = document.querySelectorAll('[data-modal-target]');
    const closeModalButtons = document.querySelectorAll('.modal .close-button');
    const overlay = document.getElementById('legal-modal-overlay');

    const openModal = (modal) => {
        if (!modal) return;
        modal.classList.add('active');
        overlay.classList.add('active');
    };

    const closeModal = (modal) => {
        if (!modal) return;
        modal.classList.remove('active');
        overlay.classList.remove('active');
    };

    openModalButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const modal = document.querySelector(button.dataset.modalTarget);
            openModal(modal);
        });
    });

    closeModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal');
            closeModal(modal);
        });
    });

    if (overlay) {
        overlay.addEventListener('click', () => {
            document.querySelectorAll('.modal.active').forEach(closeModal);
        });
    }

    // --- COOKIE BANNER LOGIC ---
    const cookieBanner = document.getElementById('cookie-banner');
    if (cookieBanner && !localStorage.getItem('cookieConsent')) {
        const acceptCookiesBtn = document.getElementById('cookie-accept');
        const declineCookiesBtn = document.getElementById('cookie-decline');

        setTimeout(() => {
            cookieBanner.classList.add('active');
            // ensure the right panel has extra bottom padding while the banner is visible
            if (rightPanel) rightPanel.classList.add('cookie-banner-active');
        }, 1500);

        const hideCookieBanner = (consent) => {
            cookieBanner.classList.remove('active');
            if (rightPanel) rightPanel.classList.remove('cookie-banner-active');
            localStorage.setItem('cookieConsent', consent);
        };

        acceptCookiesBtn.addEventListener('click', () => hideCookieBanner('accepted'));
        declineCookiesBtn.addEventListener('click', () => hideCookieBanner('declined'));
    }

    // --- CONTACT FORM: Client-side submit to Formspree with redirect fallback ---
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            // only intercept if action points to formspree
            const action = contactForm.getAttribute('action') || '';
            if (!action.includes('formspree.io')) return; // allow normal submit

            e.preventDefault();

            const formData = new FormData(contactForm);

            try {
                const res = await fetch(action, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json'
                    },
                    body: formData
                });

                if (res.ok) {
                    // client-side redirect to confirmation (works regardless of Formspree plan)
                    window.location.href = '/form_confirmation.html';
                    return;
                }

                // if Formspree returns validation errors, parse and fallback to normal submission
                const data = await res.json().catch(() => null);
                console.error('Formspree error response', data);
                contactForm.submit();
            } catch (err) {
                console.error('Form submit failed, falling back to native submit', err);
                contactForm.submit();
            }
        });
    }
});
