import os
from bs4 import BeautifulSoup

WEBSITE_ROOT = '.'

NEW_FOOTER_HTML = """
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
      <h4 class="font-bold text-white uppercase tracking-wider">
       Menu
      </h4>
      <nav class="flex flex-col space-y-2 text-sm">
       <a class="hover:text-blue-500 transition-colors" href="index.html#how-it-works">
        How It Works
       </a>
       <a class="hover:text-blue-500 transition-colors" href="pricing.html">
        Pricing
       </a>
       <a class="hover:text-blue-500 transition-colors" href="about.html">
        About
       </a>
       <a class="hover:text-blue-500 transition-colors" href="contact.html">
        Contact
       </a>
      </nav>
     </div>
     <div class="space-y-4">
      <h4 class="font-bold text-white uppercase tracking-wider">
       Contact
      </h4>
      <div class="flex justify-center md:justify-start space-x-6 text-sm">
       <a aria-label="GitHub Profile" class="hover:text-blue-500 transition-colors" href="https://github.com/SavaiinaeaSIlva" target="_blank">
        GitHub
       </a>
       <a class="hover:text-blue-500 transition-colors" href="mailto:contact@ssilva.space">
        Email
       </a>
       <a class="hover:text-blue-500 transition-colors" href="tel:+18083081107">
        Call
       </a>
      </div>
     </div>
    </div>
    <div class="mt-12 pt-8 border-t border-neutral-800 text-center text-sm">
     <p class="text-xs text-neutral-600">
      ©
      <span id="current-year">
      </span>
      Silva Automation. All Rights Reserved. |
      <a class="hover:text-white" href="terms.html">
       Terms &amp; Conditions
      </a>
      |
      <a class="hover:text-white" href="privacy.html">
       Privacy Policy
      </a>
      |
      <a class="hover:text-white" href="cookie.html">
       Cookie Policy
      </a>
     </p>
    </div>
   </div>
"""

def update_footers(soup):
    footer_tag = soup.find('footer')
    if footer_tag:
        footer_soup = BeautifulSoup(NEW_FOOTER_HTML, 'html.parser')
        footer_tag.clear()
        footer_tag.append(footer_soup)
        return True
    return False

def process_files():
    print("Starting website update process...")
    for root, _, files in os.walk(WEBSITE_ROOT):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                print(f"--- Processing: {filepath}")
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        soup = BeautifulSoup(content, 'lxml')
                    
                    if update_footers(soup):
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(str(soup.prettify()))
                        print(f"    [SUCCESS] Footer updated in {filename}")
                    else:
                        print(f"    [INFO] No footer tag found in {filename}")
                except Exception as e:
                    print(f"    [ERROR] Could not process {filename}: {e}")
    print("\nUpdate process finished.")

if __name__ == "__main__":
    process_files()
