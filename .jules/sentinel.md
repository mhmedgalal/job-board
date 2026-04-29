## 2024-05-24 - Fix Open Mail Relay Vulnerability
**Vulnerability:** Contact form allowed arbitrary user input for email recipient, turning the server into an open mail relay capable of sending spam or phishing emails from the app domain.
**Learning:** Never use untrusted user input as the recipient (`recipient_list`) in `send_mail()`. User inputs from contact forms should only appear in the email body or subject, not control where the email is sent.
**Prevention:** Hardcode the `recipient_list` to a trusted admin email (e.g., `settings.DEFAULT_FROM_EMAIL` or `settings.EMAIL_HOST_USER`) and append the user-provided contact email to the body.
