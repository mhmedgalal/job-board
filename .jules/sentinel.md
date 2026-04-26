## 2024-05-24 - Open Email Relay in Contact Form
**Vulnerability:** The contact form in `contact/views.py` used the user-provided email address from the request as the recipient of the `send_mail` function. This created an open email relay, allowing anyone to use the server to send arbitrary emails to any address (e.g., spam or phishing) by submitting the form.
**Learning:** Never trust user input for the recipient list in email-sending functionality without strict validation or hardcoding the intended recipient (like the site administrator).
**Prevention:** Hardcode the recipient email address (e.g., `settings.EMAIL_HOST_USER` or `settings.DEFAULT_FROM_EMAIL`) when sending contact form submissions, and include the user's email in the message body or `Reply-To` header instead.
