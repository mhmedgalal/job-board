## 2024-05-04 - [Missing Authentication on Profile Views]
**Vulnerability:** The `profile` and `edit_profile` views in `accounts/views.py` queried `Profile.objects.get(user=request.user)` without checking if the user was authenticated.
**Learning:** This exposes the application to 500 errors when an unauthenticated user (AnonymousUser) accesses these views, as `AnonymousUser` is not a valid user to query.
**Prevention:** Always use `@login_required` decorator on views that require an authenticated user, especially those that query data related to `request.user`.
