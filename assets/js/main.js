document.addEventListener('DOMContentLoaded', () => {
    // Function to load HTML components
    const loadComponent = async (url, elementId) => {
        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error(`Failed to load ${url}: ${response.statusText}`);
            const text = await response.text();
            const element = document.getElementById(elementId);
            if (element) {
                element.innerHTML = text;
            }
        } catch (error) {
            console.error(error);
        }
    };

    // Load header and footer
    Promise.all([
        loadComponent('components/header.html', 'header-placeholder'),
        loadComponent('components/footer.html', 'footer-placeholder')
    ]).then(() => {
        // Initialize scripts that depend on the loaded components
        initializeScripts();
        if (window.lucide && typeof lucide.createIcons === 'function') {
            lucide.createIcons(); // Ensure icons in header/footer are rendered
        }
    });

});

function initializeScripts() {
    const isLegalPage = window.location.pathname.includes('legal.html');

    const desktopNav = document.getElementById('desktop-nav');
    const mobileNav = document.getElementById('mobile-nav');

    if (!isLegalPage && desktopNav && mobileNav && !desktopNav.dataset.initialized) {
        const navLinks = [
            { href: '#process', text: 'Our Process' },
            { href: '#about', text: 'About Us' },
            { href: '#faq', text: 'FAQ' },
        ];

        navLinks.forEach(link => {
            desktopNav.innerHTML += `<a href="${link.href}" class="text-sm font-medium text-subtle-text hover:text-light-text transition-colors px-3 py-2 rounded-md hover:bg-black-accent">${link.text}</a>`;
            mobileNav.innerHTML += `<a href="${link.href}" class="block px-4 py-3 text-base font-medium text-light-text hover:bg-black-accent rounded-md">${link.text}</a>`;
        });

        desktopNav.innerHTML += `<a href="https://calendly.com/silvaautomation/consultation" target="_blank" rel="noopener noreferrer" class="ml-4 text-sm font-semibold bg-cta-color text-black-bg px-4 py-2 rounded-full shadow-soft-glow hover:bg-cta-hover transition-colors flex items-center gap-2">
            <span>Get Your Free System Built</span>
            <i data-lucide="calendar" class="w-4 h-4"></i>
        </a>`;

        mobileNav.innerHTML += `<a href="https://calendly.com/silvaautomation/consultation" target="_blank" rel="noopener noreferrer" class="mt-2 block px-4 py-3 text-base font-semibold text-black-bg bg-cta-color rounded-md text-center hover:bg-cta-hover flex items-center justify-center gap-2">
            <span>Get Your Free System Built</span>
            <i data-lucide="calendar" class="w-5 h-5"></i>
        </a>`;

        desktopNav.dataset.initialized = 'true';
    }

    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mobileMenuBtn.setAttribute('aria-controls', 'mobile-menu');
        mobileMenuBtn.setAttribute('aria-label', 'Toggle navigation menu');
        
        mobileMenuBtn.addEventListener('click', () => {
            const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
            mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
            mobileMenu.classList.toggle('hidden');
            
            // Toggle between menu and close icons
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                if (isExpanded) {
                    icon.setAttribute('data-lucide', 'menu');
                } else {
                    icon.setAttribute('data-lucide', 'x');
                }
                if (window.lucide && typeof lucide.createIcons === 'function') {
                    lucide.createIcons();
                }
            }
        });
    }
    
    // FAQ Accordion
    const faqButtons = document.querySelectorAll('[onclick^="toggleFaq"]');
    faqButtons.forEach(button => {
        button.setAttribute('role', 'button');
        button.setAttribute('aria-expanded', 'false');
        button.setAttribute('aria-controls', button.nextElementSibling?.id || 'faq-content');
        
        if (!button.nextElementSibling?.id) {
            const contentId = 'faq-' + Math.random().toString(36).substr(2, 9);
            button.nextElementSibling.id = contentId;
            button.setAttribute('aria-controls', contentId);
        }
    });
    
    // Back to top button
    const backToTopButton = document.getElementById('back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopButton.classList.remove('hidden');
            } else {
                backToTopButton.classList.add('hidden');
            }
        });

        backToTopButton.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    const mobileCtaBar = document.getElementById('mobile-cta-bar');
    if (mobileCtaBar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                mobileCtaBar.classList.remove('hidden');
            } else {
                mobileCtaBar.classList.add('hidden');
            }
        });
    }

    // Initialize Lucide Icons
    if (window.lucide && typeof lucide.createIcons === 'function') {
        lucide.createIcons();
    }

    // Set current year in any footer that has the span
    const yearEl = document.getElementById('current-year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }
}


// FAQ toggle handler used by inline onclick attributes on FAQ buttons
function toggleFaq(button) {
    if (!button) return;

    const content = button.nextElementSibling;
    if (!content) return;

    const isHidden = content.classList.contains('hidden');
    content.classList.toggle('hidden');

    button.setAttribute('aria-expanded', isHidden ? 'true' : 'false');

    const icon = button.querySelector('i[data-lucide]');
    if (icon) {
        icon.classList.toggle('rotate-180', isHidden);
        if (window.lucide && typeof lucide.createIcons === 'function') {
            lucide.createIcons();
        }
    }
}


// Smooth scrolling for anchor links (works for dynamically added links)
document.addEventListener('click', (e) => {
    const anchor = e.target.closest('a[href^="#"]');
    if (!anchor) return;

    const href = anchor.getAttribute('href');
    if (!href || href === '#') return;

    const targetElement = document.querySelector(href);
    if (!targetElement) return;

    e.preventDefault();

    window.scrollTo({
        top: targetElement.offsetTop - 100, // Adjust for fixed header
        behavior: 'smooth'
    });

    // Close mobile menu if open
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    if (mobileMenu && mobileMenuBtn && !mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');

        // Reset menu icon
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            icon.setAttribute('data-lucide', 'menu');
            if (window.lucide && typeof lucide.createIcons === 'function') {
                lucide.createIcons();
            }
        }
    }
});

// Lazy load videos
function lazyLoadVideos() {
    const videos = document.querySelectorAll('video[data-src]');
    
    const videoObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const video = entry.target;
                video.src = video.getAttribute('data-src');
                video.load();
                videoObserver.unobserve(video);
            }
        });
    }, {
        rootMargin: '200px',
        threshold: 0.1
    });
    
    videos.forEach(video => videoObserver.observe(video));
}

// Run lazy loading when DOM is loaded
if ('IntersectionObserver' in window) {
    document.addEventListener('DOMContentLoaded', lazyLoadVideos);
}
