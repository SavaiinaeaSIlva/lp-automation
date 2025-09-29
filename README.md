# Silva Automation Website - README

### 1\. Project Overview

This repository contains the source code for the official website of Silva Automation, a business automation service based in Waipahu, Hawaii. The project is a multi-page professional website designed to attract service-based business clients, explain the services offered, and provide a comprehensive, interactive legal framework.

### 2\. Key Features

  * **Multi-Page Structure:** A full-featured site including Home, About, Pricing, and Blog pages.
  * **Interactive Legal Center:** All legal documents (Terms, Privacy, Refund, Cookie Policy) have been consolidated into a single `legal.html` file. This page functions like a mini single-page application (SPA) with sidebar navigation to switch between policies instantly and a live search feature to scan all documents.
  * **Fully Responsive Design:** Styled with Tailwind CSS for a seamless experience on mobile, tablet, and desktop devices.
  * **Standardized Page Layouts:** All pages share a consistent header, footer, and hero/title banner structure for a professional and cohesive user experience.
  * **Consent-Gated Analytics:** Google Analytics (GA4) loads only after the user consents by clicking "Accept All" on the cookie banner.

### 3\. Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **HTML5** | Core structure and content. |
| **Tailwind CSS** | Utility-first CSS for rapid UI development. |
| **Vanilla JS (ES6)** | All interactive features, including the mobile menu, cookie banner, and the legal center's navigation and search functionality. |
| **AOS Library** | Subtle scroll-triggered animations for a polished feel. |
| **Node.js / npm** | Managing development dependencies and build scripts for Tailwind CSS. |

### 4\. File Structure

The project follows a standard structure for static websites. The `legal/` directory is now obsolete and can be deleted.

```
/
|-- assets/
|   |-- images/         # All static images (logo.png, pic1.png, etc.)
|
|-- dist/
|   |-- output.css      # FINAL, compiled CSS file (do not edit directly)
|
|-- src/
|   |-- input.css       # SOURCE CSS file for Tailwind styles (edit this one)
|
|-- index.html          # Main homepage
|-- about.html          # About Us page
|-- pricing.html        # Pricing page
|-- blog.html           # Blog listing/preview page
|-- hawaii-business-automation-guide.html # Individual blog post
|-- legal.html          # New single-page interactive legal center
|
|-- tailwind.config.js  # Config file for Tailwind CSS
|-- package.json        # Lists project dependencies and scripts
|-- README.md           # This file
```

### 5\. Setup and Development

To run this project locally, you will need to have Node.js and npm installed.

**Step 1: Install Dependencies**
Navigate to the project's root directory in your terminal and run:
`npm install`

**Step 2: Run the Build Process**
For continuous development (watches for changes and rebuilds CSS automatically):
`npm run watch`

For a one-time build for deployment:
`npm run build`

### 6\. Deployment

This is a static website. After running the final `npm run build`, upload all relevant files and folders (everything except `node_modules`, `src`, `package.json`, etc.) to any static hosting provider like Netlify, Vercel, or GitHub Pages.

### 7\. Updates Log

  * **2025-09-29:** Performed a comprehensive content update on all legal policies to add stronger protective clauses (Disclaimer of Warranties, No Guarantee of Results, etc.).
  * **2025-09-29:** Consolidated all individual legal documents into a single interactive `legal.html` page with sidebar navigation and live search. The old `legal/` directory is now obsolete.
  * **2025-09-29:** Updated footers across the site to link to the new `legal.html` page.
  * **2025-09-29:** Enhanced `legal.html` header with an explicit, top-left "Back to main site" link for better usability.
  * **2025-09-29:** Added a feature image to the blog post page (`hawaii-business-automation-guide.html`) and standardized its hero section to match other pages.
  * **2025-09-29:** Removed the Service Level Agreement (SLA) from the public-facing legal documents.
