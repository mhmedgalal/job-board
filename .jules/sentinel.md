## 2024-05-24 - Open Mail Relay in Contact Form
**Vulnerability:** The contact form sent emails to the email address provided in the form (`[email]`) instead of sending it to the site administrator. This is an Open Mail Relay vulnerability allowing an attacker to send spam/phishing emails to arbitrary addresses from the application's email server.
**Learning:** Contact forms should send messages TO the site administrator, while capturing the sender's email address in the body or Reply-To header. Never use untrusted input as the `recipient_list` in `send_mail`.
**Prevention:** Always hardcode or use environment variables for `recipient_list` when dealing with user-submitted contact forms.
