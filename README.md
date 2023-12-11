# Newsletter

Send a newsletter to a list of subscribers via email

## Features

- Sends a newsletter to subscribers via email.
- Customizable HTML email template.
- Reads subscriber email addresses from a text file.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Bojan9/Newsletter.git
```

2. Install required dependencies:

```bash
pip install python-dotenv
```

## Usage

1. Set up your Gmail credentials by editing the .env file in the project root

```bash
GMAIL_ADDRESS=your-email@gmail.com
GMAIL_PASSWORD=your-email-password
```

2. Edit the subscriber_emails.txt with your list of subscribers emails

3. Customize the HTML content in newsletter_template.html to fit your newsletter

4. Run the script
