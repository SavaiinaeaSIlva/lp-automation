Silva Automation Website
1. Project Overview
This repository contains the source code for the official website of Silva Automation, a business automation service based in Waipahu, Hawaii. The website is a professional, responsive single-page landing site designed to attract service-based business clients, explain the services offered, and capture leads through a contact form and consultation booking link.

The site is built with modern web technologies, focusing on performance, clean aesthetics, and a smooth user experience.

2. Key Features
The website's functionality is primarily controlled by assets/js/main.js and includes:

Fully Responsive Design: Adapts seamlessly to all screen sizes, from mobile phones to desktop monitors.

Animate On Scroll (AOS): Subtle, professional animations trigger as the user scrolls down the page, enhancing visual engagement.

Smooth Scrolling Navigation: Clicking on navigation links glides the user to the corresponding section of the page.

"Single-Page App" for Legal Documents: Legal pages (Terms, Privacy Policy, etc.) load instantly within the same view without requiring a full page refresh, providing a fast and seamless user experience.

Dynamic Header: The main header elegantly hides when scrolling down and reappears when scrolling up, maximizing screen real estate.

Cookie Consent Banner: A non-intrusive banner at the bottom of the page to inform users about cookie usage, with a persistent "accept" state stored in local storage.

Automated Copyright Year: The copyright year in the footer is automatically updated by JavaScript.

Formspree Integration: The contact form is securely handled by Formspree, eliminating the need for a custom backend.

3. Technologies Used
HTML5: For the core structure and content.

Tailwind CSS: A utility-first CSS framework for rapid and responsive UI development.

Vanilla JavaScript (ES6): For all interactive features, ensuring the site is lightweight and fast without relying on heavy frameworks.

AOS (Animate On Scroll): A small JavaScript library for scroll animations.

Formspree: For backend handling of the contact form submissions.

Node.js / npm: For managing development dependencies and running the build process for Tailwind CSS.

4. File Structure
The project follows a straightforward and organized file structure:

/
|-- assets/
|   |-- images/         # All static images (logo, hero, etc.)
|   |-- js/
|       |-- main.js     # The main JavaScript file for all site functionality
|
|-- dist/
|   |-- output.css      # The FINAL, compiled CSS file (do not edit directly)
|
|-- src/
|   |-- input.css       # The SOURCE CSS file for Tailwind styles (edit this one)
|
|-- index.html          # The main HTML file for the website
|-- tailwind.config.js  # Configuration file for Tailwind CSS
|-- package.json        # Lists project dependencies and scripts
|-- readme.md           # This file

5. Setup and Development
To run this project locally for development, you will need to have Node.js and npm installed.

Step 1: Install Dependencies
Navigate to the project's root directory in your terminal and run the following command to install the necessary development tools (like Tailwind CSS):

npm install

Step 2: Run the Build Process
This project uses Tailwind CSS to compile styles. To watch for changes in your HTML and CSS files and automatically rebuild the dist/output.css file, run:

npm run build

This command will start a process that continuously watches for any saved changes and keeps your stylesheet up-to-date.

Step 3: View the Website
Simply open the index.html file in your web browser to see the website. Any changes you make to the HTML or src/input.css will be reflected after you save them (the build process will update the CSS automatically).

6. Contact
Owner: Savaiinaea Silva

Email: contact@silvaautomation.com

Website: www.silvaautomation.com
