#!/usr/bin/env python3

import csv
import glob

# Path pattern to match your files
file_pattern = '*/*-answer.txt'
output_csv_file = 'output.csv'

# Open the CSV file for writing
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the CSV header
    writer.writerow(['File Name', 'Status', 'Message'])
    
    # Iterate through each matching file
    for filename in glob.glob(file_pattern):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        # Initialize variables to hold the extracted information
        status = ''
        message_lines = []
        in_message = False  # Flag to start capturing message lines
        
        # Iterate through each line of the file
        for line in content:
            if line.startswith('Status:'):
                status = line.strip().split('Status: ')[1]
            elif line.startswith('Message:'):
                in_message = True
                message_lines.append(line.strip().split('Message: ')[1])  # Append the part after "Message: "
            elif line.strip() == '================================================================================':
                in_message = False
            elif in_message:
                message_lines.append(line.strip())
        
        # Combine all message lines into a single string
        message = ' '.join(message_lines)
        
        # Write the extracted information to the CSV file
        writer.writerow([filename, status, message])

        
