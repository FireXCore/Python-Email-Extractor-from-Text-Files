import os
import re

# Function to extract emails from a text file
def extract_emails_from_file(filepath):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file {filepath}.")
        return
    
    # Find all emails and remove duplicates using a set
    emails = set(re.findall(email_pattern, content))
    
    # Write the emails to a new file
    output_filename = filepath.replace('.txt', '_emails.txt')
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')
    
    print(f"Emails have been saved to {output_filename}")

# Path to the folder where the Python file is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Search for text files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(current_directory, filename)
        extract_emails_from_file(filepath)
