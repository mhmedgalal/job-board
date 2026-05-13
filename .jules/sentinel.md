## 2024-05-13 - Open Email Relay via Contact Form
**Vulnerability:** The contact form `send_mail` function was using the user-supplied `email` input as the *recipient* `[email]`.
**Learning:** This turned the application into an open email relay, allowing attackers to leverage the server's legitimate SMTP credentials to send spam or phishing emails to arbitrary victims, completely bypassing spam filters.
**Prevention:** Always hardcode or use trusted environment variables/settings (e.g., `settings.DEFAULT_FROM_EMAIL`) for the recipient list in public contact forms. Include the sender's email address in the message body or as a Reply-To header.
