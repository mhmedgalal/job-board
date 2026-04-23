## 2025-05-18 - First Security Review

## 2026-04-23 - Missing Authentication on Profile Endpoints
**Vulnerability:** Missing authentication check on profile and edit_profile endpoints in accounts/views.py.
**Learning:** These views handled sensitive user profile data using `request.user` but lacked the `@login_required` decorator. If accessed by an unauthenticated user, `request.user` would resolve to an AnonymousUser, causing `Profile.objects.get(user=request.user)` to fail and potentially throwing a 500 server error, while theoretically exposing sensitive information if not properly isolated.
**Prevention:** Always ensure views dealing with sensitive or user-specific data are protected with appropriate authentication decorators (like `@login_required`) or permissions checks.
