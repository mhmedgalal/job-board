## 2024-05-24 - Open Email Relay in Contact Form
**Vulnerability:** The application's contact form accepted a user-provided email address and passed it to the Django `send_mail` function as the recipient list, using the server's configured email credentials to send the message. This allowed anyone to send arbitrary emails to any address through our mail server (Open Email Relay).
**Learning:** Never use untrusted input as the recipient (`recipient_list`) in an email sending function, as it essentially turns the application into an open proxy for spam and phishing.
**Prevention:** Always send contact form emails to a predefined internal/admin email address. Information about the sender (such as their email address) should be safely formatted and embedded within the body of the message.
