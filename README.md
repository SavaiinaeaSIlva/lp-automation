
This is the official front-end code for the Silva Automation business website. It's a modern, single-page responsive website designed to showcase automation services, generate leads, and provide key business information for clients in Hawaii.

---

## Features

-   🎨 **Modern Design:** A responsive split-screen layout with a dark, "glassmorphism" theme.
-   📱 **Fully Responsive:** Adapts cleanly for optimal viewing on desktop, tablet, and mobile devices.
-   🧮 **Interactive ROI Calculator:** Allows potential clients to calculate their potential savings by using your services.
-   ❓ **Dynamic FAQ Accordion:** A clean, interactive FAQ section to answer common questions.
-   📜 **Pop-up Modals:** Displays legal documents (Terms, Privacy Policy, etc.) in clean, scrollable pop-ups.
-   🍪 **Functional Cookie Consent Banner:** A simple banner to handle user consent, with choices remembered in local storage.

---

## Tech Stack

-   **HTML5:** For the core structure and content.
-   **CSS3:** For all styling, animations, and layout. It heavily uses modern features like:
    -   Flexbox & Grid for layout
    -   CSS Variables for easy theme management
    -   Keyframe Animations for the CTA button
    -   Backdrop Filter for the "glass" effect
-   **Vanilla JavaScript:** For all interactivity, including:
    -   IntersectionObserver for active navigation link highlighting on scroll.
    -   DOM manipulation for the ROI calculator and modals.

---

## File Structure

```

.
├── assets
│   ├── icons
│   │   ├── discover.png
│   │   ├── build.png
│   │   └── deliver.png
│   └── images
│       └── background.jpg
│       └── ... (your other images)
├── index.html          (Main page content)
├── style.css           (All styles)
└── script.js           (All interactivity)
└── README.md           (This file)

````

---

## How to Use

No complex setup is needed. This is a static website.

1.  Clone or download the repository.
2.  Open the `index.html` file in any modern web browser.

---

## Customization

Key parts of the website can be easily customized:

### Content
All text content, including headlines, paragraphs, and FAQ entries, can be edited directly in `index.html`.

### Styling
Key design elements like **colors and fonts** can be changed by editing the CSS variables in the `:root` section at the top of the `style.css` file.

```css
:root {
    --primary-color: #343a40; 
    --accent-blue: #0d6efd;   /* Change this for nav links */
    --cta-orange: #fd7e14;   /* Change this for the main button */
    /* ... etc. */
}
````

### Background Image

To change the background image of the left panel, replace the `background.jpg` file in the `assets/images` folder. You can also change the file path in the `.left-panel` rule in `style.css`.


