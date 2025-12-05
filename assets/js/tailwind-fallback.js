// Fallback Tailwind CSS - Basic styles that will be loaded if the CDN fails
// This is a minimal set of styles to ensure the site remains usable
console.log('Loading fallback Tailwind CSS');

const style = document.createElement('style');
style.textContent = `
  /* Base styles */
  * { box-sizing: border-box; }
  body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.5; }
  
  /* Layout */
  .container { width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 1rem; }
  .flex { display: flex; }
  .flex-col { flex-direction: column; }
  .items-center { align-items: center; }
  .justify-between { justify-content: space-between; }
  .hidden { display: none; }
  .block { display: block; }
  
  /* Spacing */
  .p-4 { padding: 1rem; }
  .py-8 { padding-top: 2rem; padding-bottom: 2rem; }
  .px-4 { padding-left: 1rem; padding-right: 1rem; }
  .my-4 { margin-top: 1rem; margin-bottom: 1rem; }
  .mx-auto { margin-left: auto; margin-right: auto; }
  
  /* Text */
  .text-center { text-align: center; }
  .text-white { color: white; }
  .font-bold { font-weight: 700; }
  .text-lg { font-size: 1.125rem; }
  
  /* Colors */
  .bg-black { background-color: #000; }
  .bg-gray-800 { background-color: #1f2937; }
  
  /* Buttons */
  .btn { 
    display: inline-block; 
    padding: 0.5rem 1rem; 
    border-radius: 0.25rem; 
    text-decoration: none; 
    font-weight: 600;
  }
  .btn-primary { 
    background-color: #3b82f6; 
    color: white;
  }
  
  /* Responsive */
  @media (min-width: 768px) {
    .md\:flex { display: flex; }
    .md\:hidden { display: none; }
  }
`;

document.head.appendChild(style);

// Notify the user that the fallback styles have been loaded
const notification = document.createElement('div');
notification.style.position = 'fixed';
notification.style.bottom = '1rem';
notification.style.right = '1rem';
notification.style.padding = '0.75rem 1.25rem';
notification.style.backgroundColor = '#1f2937';
notification.style.color = 'white';
notification.style.borderRadius = '0.375rem';
notification.style.zIndex = '50';
notification.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
notification.textContent = 'Using fallback styles. Some styling may appear different.';

document.body.appendChild(notification);

// Remove notification after 5 seconds
setTimeout(() => {
  notification.style.opacity = '0';
  notification.style.transition = 'opacity 0.5s ease';
  setTimeout(() => notification.remove(), 500);
}, 5000);
