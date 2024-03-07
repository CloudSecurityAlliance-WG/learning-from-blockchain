#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

def extract_content(input_html, output_file):
    # Read the input HTML file
    with open(input_html, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the section with class "post-content"
    section = soup.find('section', class_='post-content')
    
    # Initialize a variable to store the content to be written
    content_to_write = ""
    
    # Check if the section is found
    if section:
        for sibling in section.next_siblings:
            if sibling.name == 'div' and sibling.get('id', '') == 'mc_embed_signup':
                break  # Stop when the specific div is found
            content_to_write += str(sibling)
        
        # Write the content of the section itself and then everything up to the div to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(str(section) + content_to_write)
    else:
        print("Section with class 'post-content' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_html_file.html output_file.txt")
        sys.exit(1)

    input_html_file = sys.argv[1]
    output_text_file = sys.argv[2]

    extract_content(input_html_file, output_text_file)

    print(f"Content extracted to {output_text_file}")

    
