import os

def apply_changes(file_path, replacements):
    """
    Reads a file, applies a series of string replacements, and writes the changes back.

    Args:
        file_path (str): The path to the file to be modified.
        replacements (dict): A dictionary where keys are the old strings
                             and values are the new strings.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'. Skipping.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        original_content = content
        for old_string, new_string in replacements.items():
            content = content.replace(old_string, new_string)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Successfully applied changes to '{file_path}'.")
        else:
            print(f"No changes needed for '{file_path}'. Content may already be up to date.")

    except Exception as e:
        print(f"An error occurred while processing '{file_path}': {e}")

def main():
    """
    Main function to define and apply all website edits.
    """
    # --- Edits for index.html ---
    # Goal: Remove the "Regular Price" lines from all three pricing cards.
    index_file = 'index.html'
    index_replacements = {
        '<p class="text-lg text-gray-400 mb-1">Regular Price: $1,900</p>': '',
        '<p class="text-lg text-blue-200 mb-1">Regular Price: $5,900</p>': '',
        '<p class="text-lg text-gray-400 mb-1">Regular Price: $7,900</p>': ''
    }
    apply_changes(index_file, index_replacements)

    # --- Edits for blog.html ---
    # Goal: Replace Unsplash image links with local image files.
    blog_file = 'blog.html'
    blog_replacements = {
        '<img alt="Team discussing a project on a whiteboard" class="rounded-lg hover:opacity-80 transition-opacity duration-300" src="https://images.unsplash.com/photo-1556742502-ec-c0e9f34b1?q=80&w=800&h=500&fit=crop"/>':
        '<img alt="Team discussing a project on a whiteboard" class="rounded-lg hover:opacity-80 transition-opacity duration-300" src="assets/images/blog3.png"/>',
        '<img alt="An overview of a business workflow on a desk" class="rounded-lg hover:opacity-80 transition-opacity duration-300" src="https://images.unsplash.com/photo-1605910246477-74f03ee44aaa?q=80&w=800&h=500&fit=crop"/>':
        '<img alt="An overview of a business workflow on a desk" class="rounded-lg hover:opacity-80 transition-opacity duration-300" src="assets/images/blog2.png"/>'
    }
    apply_changes(blog_file, blog_replacements)

    # --- Edits for marketing-agency-onboarding-guide.html ---
    # Goal: Update the social media preview image (og:image) to use the local file.
    marketing_post_file = 'marketing-agency-onboarding-guide.html'
    marketing_post_replacements = {
        '<meta content="https://images.unsplash.com/photo-1556742502-ec-c0e9f34b1?q=80&amp;w=1200&amp;h=630&amp;fit=crop" property="og:image"/>':
        '<meta content="assets/images/blog3.png" property="og:image"/>'
    }
    apply_changes(marketing_post_file, marketing_post_replacements)

    # --- Edits for hawaii-business-automation-guide.html ---
    # Goal: Update the social media preview image (og:image) to use the local file.
    hawaii_post_file = 'hawaii-business-automation-guide.html'
    hawaii_post_replacements = {
        '<meta content="https://images.unsplash.com/photo-1605910246477-74f03ee44aaa?q=80&amp;w=1200&amp;h=630&amp;fit=crop" property="og:image"/>':
        '<meta content="assets/images/blog2.png" property="og:image"/>'
    }
    apply_changes(hawaii_post_file, hawaii_post_replacements)


if __name__ == '__main__':
    main()

