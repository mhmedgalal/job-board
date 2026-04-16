## 2024-04-16 - Prevented Open Relay / Spam Gateway in Contact Form
**Vulnerability:** The contact form in `contact/views.py` passed the user-provided email as the recipient list in `send_mail()`. This allowed any malicious user to send custom emails with arbitrary subjects and messages to any email address, making the application an open relay for spam/phishing.
**Learning:** Never pass unvalidated user input directly to the `recipient_list` in email functions like `send_mail()`. It enables Server-Side Request Forgery (SSRF) affecting external email recipients.
**Prevention:** Always hardcode the recipient list to the trusted site administrator's email or `settings.DEFAULT_FROM_EMAIL`. Ensure the user's input only appears in the `message` body or headers properly.
