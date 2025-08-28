import os
import re

# --- TEMPLATES: The single source of truth for all shared HTML components ---

# Standardized <head> section for all pages
HEAD_TEMPLATE = """
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>{title}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&family=Inter:wght@400;600&display=swap" rel="stylesheet"/>
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet"/>
  <link href="https://placehold.co/32x32/3b82f6/FFFFFF?text=SA" rel="icon" type="image/png"/>
  <link href="assets/css/style.css" rel="stylesheet"/>
</head>
"""

# Header for the main index.html page
HEADER_TEMPLATE_MAIN = """
<header class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">
   <div class="container mx-auto px-6 py-4 flex justify-between items-center">
    <a aria-label="Silva Automation Home" href="index.html">
     <img alt="Silva Automation Logo" class="h-8 w-auto" src="assets/images/silvas.svg"/>
    </a>
    <nav class="hidden md:flex items-center space-x-8 text-sm">
     <a class="nav-link text-gray-300 hover:text-white" href="#how-it-works">How It Works</a>
     <a class="nav-link text-gray-300 hover:text-white" href="#about">About</a>
     <a class="nav-link text-gray-300 hover:text-white" href="#pricing">Pricing</a>
     <a class="nav-link text-gray-300 hover:text-white" href="#contact">Contact</a>
    </nav>
    <div class="md:hidden">
        <button id="mobile-menu-button" class="text-white focus:outline-none">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
        </button>
    </div>
   </div>
</header>
<div id="mobile-menu" class="fixed top-0 right-0 h-full w-64 bg-gray-900/90 backdrop-blur-lg z-40 p-8 mobile-menu-closed md:hidden">
    <nav class="flex flex-col space-y-6 text-lg text-right mt-16">
        <a class="nav-link text-gray-300 hover:text-white" href="#how-it-works">How It Works</a>
        <a class="nav-link text-gray-300 hover:text-white" href="#about">About</a>
        <a class="nav-link text-gray-300 hover:text-white" href="#pricing">Pricing</a>
        <a class="nav-link text-gray-300 hover:text-white" href="#contact">Contact</a>
    </nav>
</div>
"""

# Simplified header for all other pages (payment, legal, etc.)
HEADER_TEMPLATE_SECONDARY = """
<header class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">
   <div class="container mx-auto px-6 py-4 flex justify-between items-center">
    <a aria-label="Silva Automation Home" href="index.html">
     <img alt="Silva Automation Logo" class="h-8 w-auto" src="assets/images/silvas.svg"/>
    </a>
    <nav class="hidden md:flex items-center space-x-8 text-sm">
     <a class="nav-link text-gray-300 hover:text-white" href="index.html">Back to Main Site</a>
    </nav>
    <div class="md:hidden">
        <button id="mobile-menu-button" class="text-white focus:outline-none">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
        </button>
    </div>
   </div>
</header>
<div id="mobile-menu" class="fixed top-0 right-0 h-full w-64 bg-gray-900/90 backdrop-blur-lg z-40 p-8 mobile-menu-closed md:hidden">
    <nav class="flex flex-col space-y-6 text-lg text-right mt-16">
        <a class="nav-link text-gray-300 hover:text-white" href="index.html">Back to Main Site</a>
    </nav>
</div>
"""

# Footer and Scripts section for all pages
FOOTER_AND_SCRIPTS_TEMPLATE = """
<footer class="bg-neutral-900 border-t border-neutral-800 text-neutral-400">
   <div class="container mx-auto px-6 py-12">
    <div class="grid md:grid-cols-3 gap-8 text-center md:text-left">
     <div class="space-y-4">
      <a href="index.html">
       <img alt="Silva Automation Logo" class="h-8 w-auto mx-auto md:mx-0" src="assets/images/silvas.svg"/>
      </a>
      <p class="text-sm">
       Bespoke automation systems that save you time and help you grow your service business.
      </p>
     </div>
     <div class="space-y-4">
      <h4 class="font-bold text-white uppercase tracking-wider font-display">Menu</h4>
      <nav class="flex flex-col space-y-2 text-sm">
       <a class="hover:text-blue-500 transition-colors" href="index.html#how-it-works">How It Works</a>
       <a class="hover:text-blue-500 transition-colors" href="index.html#about">About</a>
       <a class="hover:text-blue-500 transition-colors" href="index.html#pricing">Pricing</a>
       <a class="hover:text-blue-500 transition-colors" href="index.html#contact">Contact</a>
      </nav>
     </div>
     <div class="space-y-4">
      <h4 class="font-bold text-white uppercase tracking-wider font-display">Contact</h4>
      <div class="flex flex-col space-y-2 text-sm">
        <a class="hover:text-blue-500 transition-colors" href="mailto:contact@ssilva.space">Email</a>
        <a class="hover:text-blue-500 transition-colors" href="https://github.com/SavaiinaeaSIlva" target="_blank">GitHub</a>
        <a class="hover:text-blue-500 transition-colors" href="tel:+18083081107">Call</a>
      </div>
     </div>
    </div>
    <div class="mt-12 pt-8 border-t border-neutral-800 text-center text-sm">
     <p class="text-xs text-neutral-600">
      © <span id="current-year"></span> Silva Automation. All Rights Reserved. |
      <a class="hover:text-white" href="terms.html">Terms &amp; Conditions</a> |
      <a class="hover:text-white" href="privacy.html">Privacy Policy</a> |
      <a class="hover:text-white" href="cookie.html">Cookie Policy</a> |
      <a class="hover:text-white" href="refund.html">Refund Policy</a>
     </p>
    </div>
   </div>
</footer>

<div id="cookie-banner">
   <p class="text-sm">
    This website uses cookies to ensure you get the best experience. By continuing, you agree to our
    <a class="text-blue-400 hover:underline" href="privacy.html">Privacy Policy</a>.
   </p>
   <button id="accept-cookies" class="cta-button-primary text-sm py-2 px-4 rounded-md">
    Accept
   </button>
</div>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script src="assets/js/script.js"></script>
"""

def process_html_file(filepath):
    """Reads an HTML file, extracts its unique parts, and rebuilds it with standard components."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract unique title and main content
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        main_match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL)

        if not title_match or not main_match:
            print(f"    [WARNING] Could not find <title> or <main> in {os.path.basename(filepath)}. Skipping.")
            return False

        title_content = title_match.group(1).strip()
        main_content = main_match.group(1).strip()

        # Choose the correct header based on the filename
        if os.path.basename(filepath) == 'index.html':
            header_content = HEADER_TEMPLATE_MAIN
        else:
            header_content = HEADER_TEMPLATE_SECONDARY

        # Rebuild the entire HTML document
        new_html = f"""
<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
{HEAD_TEMPLATE.format(title=title_content)}
<body class="antialiased">
{header_content}
<main>
{main_content}
</main>
{FOOTER_AND_SCRIPTS_TEMPLATE}
</body>
</html>
        """

        # Write the new content back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html.strip())
        
        print(f"    [SUCCESS] Successfully standardized {os.path.basename(filepath)}")
        return True

    except Exception as e:
        print(f"    [ERROR] Failed to process {os.path.basename(filepath)}: {e}")
        return False


def run_standardization():
    """Finds all HTML files and processes them."""
    print("🚀 Starting website standardization process...")
    
    # Find all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if not html_files:
        print("No HTML files found in this directory.")
        return

    update_count = 0
    for filename in html_files:
        if process_html_file(filename):
            update_count += 1
            
    print(f"\n✨ Process finished. {update_count}/{len(html_files)} files were updated.")


if __name__ == "__main__":
    run_standardization()
