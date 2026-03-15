## 2025-03-08 - Missing Authentication in Profile Views
**Vulnerability:** Missing Authentication in user profile views (`accounts/views.py`).
**Learning:** Views that implicitly depend on `request.user` to be an authenticated Django user model (e.g., calling `Profile.objects.get(user=request.user)`) will crash and potentially leak traceback details if a user accesses them unauthenticated (the user is resolved as an `AnonymousUser` object).
**Prevention:** Ensure any view that retrieves data based on `request.user` uses `@login_required` or `IsAuthenticated` (for APIs) to handle unauthenticated requests safely.
