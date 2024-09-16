# Python-Email-Extractor-from-Text-Files

Open your terminal or command line, and clone the newly created repository to your local machine:

bash

git clone https://github.com/yourusername/python-email-extractor.git

Replace yourusername with your GitHub username.
3. Add the Python Script:

Move your Python script, extract_emails.py, into the folder created by cloning the repository.
4. Push Your Changes:

Once the script is added, navigate to the repository folder in your terminal:

bash

cd python-email-extractor

Stage and commit the changes:

bash

git add extract_emails.py
git commit -m "Initial commit: Add email extraction script"
git push origin main

Script Usage:
Prerequisites:

    Python 3.x must be installed on your machine. You can download Python here.

Steps:

    Clone the Repository: Clone this repository to your local machine using:

    bash

git clone https://github.com/yourusername/python-email-extractor.git

Add .txt Files: Place the .txt files containing emails in the same directory as the script (extract_emails.py).

Run the Script: Open a terminal or command line, navigate to the directory where the script is located, and run:

bash

    python extract_emails.py

    Check the Results: For each .txt file in the directory, a corresponding _emails.txt file will be created, containing all unique email addresses.

Example:

Given a file sample.txt with the following content:

graphql

John Doe: john.doe@example.com
Jane Smith: jane.smith@example.com
info@company.com
contact@company.com
john.doe@example.com

After running the script, a new file sample_emails.txt will be created with the following content:

graphql

john.doe@example.com
jane.smith@example.com
info@company.com
contact@company.com

Contributing:

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request. Please make sure to follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -m 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.
