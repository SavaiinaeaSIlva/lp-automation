// ============================================
// ADD THIS SECTION AT THE TOP OF YOUR script.js
// (After the toggleMenu function)
// ============================================

// Load Header and Footer Components
async function loadComponent(elementId, filePath) {
  const element = document.getElementById(elementId);
  // If placeholder not present, skip fetch to avoid unnecessary network errors
  if (!element) return;
  try {
    const response = await fetch(filePath);
    if (!response.ok) throw new Error(`Failed to load ${filePath}`);
    const html = await response.text();
    element.innerHTML = html;
  } catch (error) {
    console.error('Error loading component:', error);
  }
}

// ============================================
// MODIFY YOUR EXISTING DOMContentLoaded
// Add these two lines at the very beginning:
// ============================================

// Consolidated DOMContentLoaded: initialize components and UI once
document.addEventListener('DOMContentLoaded', async function() {
  console.log('Page loaded - initializing...');

  // Load components only if placeholders exist (guarded inside loadComponent)
  await Promise.all([
    loadComponent('header-placeholder', 'includes/header.html'),
    loadComponent('footer-placeholder', 'includes/footer.html')
  ]).catch(err => {
    // swallow fetch errors as they are non-fatal if placeholders don't exist
    console.debug('Component load skipped or failed:', err);
  });

  // Add animation classes and initialize scroll and UI handlers
  addAnimationClasses();
  initScrollAnimations();

  // Tab switching
  const tablistEl = document.querySelector('.tabs[role="tablist"]');
  const tabs = tablistEl ? tablistEl.querySelectorAll('.tab[role="tab"]') : document.querySelectorAll('.tabs .tab');
  if (tabs.length > 0) {
    const panels = document.querySelectorAll('.tab-content[role="tabpanel"], .tab-content');

    function setActiveTab(tab) {
      tabs.forEach(t => {
        const selected = t === tab;
        t.setAttribute('aria-selected', selected ? 'true' : 'false');
        t.setAttribute('tabindex', selected ? '0' : '-1');
        t.classList.toggle('active', selected);
      });

      const targetId = tab.getAttribute('data-target');
      panels.forEach(p => {
        const match = p.id === targetId;
        p.classList.toggle('active', match);
        if (p.hasAttribute('role')) {
          p.toggleAttribute('hidden', !match);
        }
      });
    }

    const initial = Array.from(tabs).find(t => t.classList.contains('active')) || tabs[0];
    if (initial) setActiveTab(initial);

    tabs.forEach(tab => {
      tab.addEventListener('click', () => setActiveTab(tab));
      tab.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
          e.preventDefault();
          const idx = Array.from(tabs).indexOf(document.activeElement);
          const dir = e.key === 'ArrowRight' ? 1 : -1;
          const next = tabs[(idx + dir + tabs.length) % tabs.length];
          next.focus();
          setActiveTab(next);
        }
      });
    });
  }

  // FAQ Accordion
  const faqButtons = document.querySelectorAll('.faq-button');
  if (faqButtons.length > 0) {
    faqButtons.forEach(button => {
      button.addEventListener('click', function() {
        const content = this.nextElementSibling;
        const isOpen = content.classList.contains('open');
        document.querySelectorAll('.faq-content').forEach(c => c.classList.remove('open'));
        if (!isOpen) content.classList.add('open');
        const icon = this.querySelector('.faq-icon');
        if (icon) icon.style.transform = content.classList.contains('open') ? 'rotate(180deg)' : 'rotate(0)';
      });
    });
  }

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const targetElement = document.querySelector(href);
      if (targetElement) {
        e.preventDefault();
        const mobileMenu = document.getElementById('mobileMenu');
        if (mobileMenu && mobileMenu.classList.contains('active')) toggleMenu();
        window.scrollTo({ top: targetElement.offsetTop - 100, behavior: 'smooth' });
      }
    });
  });

  // Close mobile menu when clicking on mobile nav links
  document.querySelectorAll('.mobile-nav a').forEach(link => {
    link.addEventListener('click', function() {
      const mobileMenu = document.getElementById('mobileMenu');
      if (mobileMenu && mobileMenu.classList.contains('active')) toggleMenu();
    });
  });
});
// FIXED SCRIPT.JS - Works with your HTML
// Enhanced with scroll animations

// Mobile Menu Function
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  const isActive = menu.classList.toggle('active');
  document.body.style.overflow = isActive ? 'hidden' : '';

  // Sync ARIA state for all toggle buttons
  document.querySelectorAll('[data-menu-toggle]').forEach(btn => {
    btn.setAttribute('aria-expanded', String(isActive));
  });

  // Update menu aria-hidden
  if (menu) {
    menu.setAttribute('aria-hidden', String(!isActive));
  }
}

// Scroll Animation Function
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('.animate-on-scroll, .section');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        
        // Add a slight delay for section content animations
        if (entry.target.classList.contains('section')) {
          const childElements = entry.target.querySelectorAll('.card, .step-card, .grid > *');
          childElements.forEach((child, index) => {
            child.classList.add('animate-on-scroll');
            child.style.transitionDelay = `${index * 0.1}s`;
          });
        }
      } else {
        // Optional: Remove the class when element leaves viewport
        // entry.target.classList.remove('visible');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  });
  
  animatedElements.forEach(el => observer.observe(el));
}

// Add animation classes to elements on page load
function addAnimationClasses() {
  // Add animate-on-scroll to all cards and step cards
  const cards = document.querySelectorAll('.card, .step-card');
  cards.forEach(card => {
    card.classList.add('animate-on-scroll');
  });
  
  // Add section class to all sections
  const sections = document.querySelectorAll('section');
  sections.forEach(section => {
    section.classList.add('section');
  });
}

// Initialize everything when page loads
// Consolidation complete: the above DOMContentLoaded handles all initialization once.

// Make toggleMenu available globally
window.toggleMenu = toggleMenu;

// Temporary fix for missing price
document.addEventListener('DOMContentLoaded', function() {
  const middlePriceDisplay = document.querySelector('.pricing-highlight .price-display');
  if (middlePriceDisplay && !middlePriceDisplay.querySelector('.price-amount')) {
    const priceAmount = document.createElement('div');
    priceAmount.className = 'price-amount';
    priceAmount.textContent = '$3,800';
    priceAmount.style.cssText = 'display: block; color: white; font-size: 2.75rem; font-weight: 900; text-shadow: 0 2px 8px rgba(0,0,0,0.3);';
    middlePriceDisplay.insertBefore(priceAmount, middlePriceDisplay.querySelector('.price-duration'));
  }
});