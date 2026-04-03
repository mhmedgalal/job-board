## 2024-05-24 - [Open Mail Relay / Email Spam Abuse]
**Vulnerability:** The contact form taking user input and setting the sender's email directly as the recipient parameter in `send_mail()`.
**Learning:** Using user-provided inputs directly to dictate the recipient of an email creates an open mail relay vulnerability, allowing attackers to use the server for spamming and phishing attacks.
**Prevention:** Send contact form emails directly to a designated admin email (`settings.EMAIL_HOST_USER`), using the app's standard sending address (`settings.DEFAULT_FROM_EMAIL`), and safely format the user's provided email address into the body of the message.
