import requests

# Correct API settings
MAILGUN_API_ENDPOINT = "https://api.mailgun.net/v3/sandbox1d02e0c4e1f644afab0e468fab53511c.mailgun.org/messages"  # Replace with correct domain
MAILGUN_API_KEY = "7dccebfdb573341a6b12968fa9833cc2-e298dd8e-67d51d96"  # Replace with correct key

def send_email(to, subject, body):
    data = {
        'from': 'postmaster@sandbox1d02e0c4e1f644afab0e468fab53511c.mailgun.org',  # Must be verified in Mailgun
        'to': to,
        'subject': subject,
        'text': body
    }

    response = requests.post(
        MAILGUN_API_ENDPOINT,
        auth=('api', MAILGUN_API_KEY),
        data=data
    )

    # Print response details for debugging
    if response.status_code == 200:
        print('✅ Email sent successfully!')
    else:
        print(f'❌ Error {response.status_code}: {response.text}')  # Show error details

# Example usage
to = "shaikharsalanme@gmail.com"
subject = "Testing Purpose"
body = "Just testing out how email works with python automation"
send_email(to, subject, body)
