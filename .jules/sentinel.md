## 2024-05-18 - Missing Authentication on Profile Endpoints
**Vulnerability:** The `profile` and `edit_profile` views in `accounts/views.py` were missing the `@login_required` decorator, allowing unauthenticated access and potentially leading to 500 internal server errors or data exposure.
**Learning:** Decorators for access control must be consistently applied to all views requiring authentication. Missing authentication on user specific objects fetching endpoints leads to server errors when `request.user` is `AnonymousUser`.
**Prevention:** Always verify endpoint authorization requirements when implementing new views or features, ensuring `@login_required` or equivalent is used for views that depend on `request.user`.
