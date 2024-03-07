#!/usr/bin/env python3

import argparse
from markdownify import markdownify as md
import sys

def convert_html_to_markdown(input_html_file, output_markdown_file):
    try:
        with open(input_html_file, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        
        markdown_content = md(html_content)
        
        with open(output_markdown_file, 'w', encoding='utf-8') as markdown_file:
            markdown_file.write(markdown_content)
            
        print(f"Markdown file successfully created at: {output_markdown_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert HTML to Markdown")
    parser.add_argument("input_html", help="Path to the input HTML file")
    parser.add_argument("output_md", help="Path to the output Markdown file")
    
    args = parser.parse_args()
    
    convert_html_to_markdown(args.input_html, args.output_md)

if __name__ == "__main__":
    main()
