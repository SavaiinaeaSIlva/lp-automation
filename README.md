Silva Automation Website

1. Project Overview
This repository contains the source code for the official website of Silva Automation, a business automation service based in Waipahu, Hawaii.

The website is a professional, responsive single-page landing site designed to attract service-based business clients, explain the services offered, and capture leads through a contact form and a Calendly consultation booking link.

2. Design Philosophy
The site is built with a "dark mode," modern aesthetic that emphasizes professionalism and clarity. The goal is to convey high-tech solutions in a simple, approachable way, focusing on performance, clean typography, and a smooth user experience.

3. Key Features
The website's functionality is primarily controlled by assets/js/main.js and includes:

Fully Responsive Design: Tailwind CSS utility-first styling across mobile, tablet, and desktop.

Animate On Scroll (AOS): Subtle animations on scroll for a polished feel.

Smooth Navigation: Fixed header with active-link highlighting and mobile flyout menu.

Consent-Gated Analytics: GA4 loads only after "Accept All" cookies (or if already accepted).

Cookie Consent Banner: Stores the user choice in localStorage and respects it.

Legal Pages: Dedicated pages for Privacy, Terms, Refund, Cookie, and SLA.

Lead Capture: Contact form and direct Calendly CTA.

4. Technologies Used
Technology

Purpose

HTML5

Core structure and content.

Tailwind CSS

Utility-first CSS for rapid UI development.

Vanilla JS (ES6)

All interactive features, keeping it lightweight.

AOS Library

Scroll-triggered animations.

Formspree

Backend for the contact form.

Node.js / npm

Managing dev dependencies and build scripts.

5. File Structure
The project follows a standard structure for static websites.

/
|-- assets/
|   |-- images/         # All static images (logo, hero, etc.)
|   |-- js/
|       |-- main.js     # Main JavaScript file for all site functionality
|
|-- dist/
|   |-- output.css      # FINAL, compiled CSS file (do not edit directly)
|
|-- src/
|   |-- input.css       # SOURCE CSS file for Tailwind styles (edit this one)
|
|-- index.html          # The main HTML file for the website
|-- tailwind.config.js  # Config file for Tailwind CSS
|-- package.json        # Lists project dependencies and scripts
|-- readme.md           # This file

6. Setup and Development
To run this project locally, you will need to have Node.js and npm installed.

Step 1: Install Dependencies
Navigate to the project's root directory in your terminal and run this command to install the necessary development tools (like tailwindcss):

npm install

Step 2: Run the Build Process
This project uses Tailwind CSS to compile styles.

For continuous development (watches src/input.css and rebuilds dist/output.css on save):

npm run watch

For a one-off build (no watcher):

npm run build

Important: If you add new Tailwind classes to your index.html (e.g., bg-red-500, p-8), you must have this build process running. Otherwise, the styles for those new classes will not be generated, and they will not appear on your website.

6.1 Blog Images
Place blog images in assets/images/ and reference them in pages.

Naming convention suggestion for previews:

- assets/images/pic1.png
- assets/images/pic2.png
- assets/images/pic3.png

Example usage in HTML:

<img src="assets/images/pic1.png" alt="Blog post image" />

7. Deployment
This is a static website, making deployment simple.

Ensure you have run the final build command (npm run build) to generate the latest dist/output.css.

Upload the entire project folder (or all files except node_modules, src, package.json, etc.) to any static hosting provider.

Recommended Providers:

Netlify

Vercel

GitHub Pages

Cloudflare Pages

8. Contact
Owner: Savaiinaea Silva

Email: contact@silvaautomation.com

Website: www.silvaautomation.com
