# Python Email Extractor from Text Files

## Overview
This script allows you to extract unique email addresses from `.txt` files in a specified directory. It processes each text file, finds all email addresses using regular expressions, and outputs the results to a new file with a `_emails.txt` suffix.

## How to Use

### Prerequisites
- **Python 3.x** must be installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**:
   First, clone this repository to your local machine using Git. Open your terminal or command prompt and run the following command:
   ```bash
   git clone https://github.com/FireXCore/Python-Email-Extractor-from-Text-Files.git

Replace yourusername with your actual GitHub username.

    Navigate to the Project Directory: After cloning, navigate to the directory where the project was cloned:

    bash

    cd python-email-extractor

    Prepare Your Text Files: Place any .txt files that you want to scan for email addresses into the same directory as the script (extract_emails.py).

Running the Script

    Run the Script: In the terminal, ensure you're in the correct directory (the one containing the Python script) and run:

    bash

    python extract_emails.py

    This will trigger the script to search for and extract all email addresses in each .txt file in the directory.

    Check the Output: For each .txt file processed, a new file will be created with the format originalfilename_emails.txt. This file will contain the list of unique email addresses found in the original text file.

    Example:
        If you have a file named contacts.txt, after running the script, a new file named contacts_emails.txt will be generated with all unique email addresses.

Example

Suppose you have a file named employees.txt with the following content:

graphql

employee1@example.com
employee2@example.com
contact@company.com
employee1@example.com

After running the script, a new file named employees_emails.txt will be created containing the following:

graphql

employee1@example.com
employee2@example.com
contact@company.com

Notes

    The script only processes .txt files in the same directory as the script.
    All email addresses are saved in a new file with duplicates removed.
    Ensure your .txt files are encoded in UTF-8 to avoid decoding errors during processing.

Troubleshooting

    If you encounter any issues with file encoding or email extraction, ensure that your text files are properly formatted and free of special characters that might interfere with the script.

Contact for Issues

If you run into any problems or have suggestions for improvements, please open an issue on the GitHub repository.
