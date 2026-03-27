## 2024-05-08 - Fix Open Mail Relay Vulnerability in Contact Form
**Vulnerability:** The contact form `send_mail` function blindly used the user-provided `email` POST data field as the recipient of the email.
**Learning:** This exposes an Open Mail Relay vulnerability. Anyone could submit arbitrary data to the server to send spam, phishing, or other malicious payloads to any email address using the server's email credentials.
**Prevention:** Never use user-submitted email addresses as the "To" field for emails generated through forms. Instead, send form submissions to an internal admin or default email address and format the body of the email to include the user's email for replies.
