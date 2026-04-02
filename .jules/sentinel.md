## 2024-05-14 - Authorization Bypass in Account Views
**Vulnerability:** Django view functions for rendering account profiles (`profile` and `edit_profile`) lacked the `@login_required` decorator despite assuming `request.user` was authenticated.
**Learning:** This results in an authorization bypass, allowing unauthenticated users to crash the server (Internal Server Error) because `AnonymousUser` evaluates poorly when querying `Profile.objects.get(user=request.user)`.
**Prevention:** Always verify that view functions accessing sensitive user-specific models or endpoints are properly decorated with authentication/authorization checks.
