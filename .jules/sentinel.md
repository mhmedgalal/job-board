## 2023-10-24 - [Contact Form Open Mail Relay]
**Vulnerability:** The contact form allowed any user to specify the `recipient_list` in the `send_mail` function via the `email` field. This allowed attackers to use the application's email server as an open mail relay to spam arbitrary email addresses.
**Learning:** Never trust user input for sensitive parameters like email recipients. Always send contact form submissions to a predefined, trusted email address (e.g., site administrator).
**Prevention:** Hardcode the destination email address for contact forms and include the user's email in the message body instead.
