## 2024-05-07 - Missing Authentication Check on Profile Endpoints
**Vulnerability:** The `/accounts/profile/` and `/accounts/edit_profile/` endpoints lacked the `@login_required` decorator.
**Learning:** This caused a 500 Internal Server Error when accessed by anonymous users, as the code attempted to pass an `AnonymousUser` object into `Profile.objects.get(user=request.user)`.
**Prevention:** Ensure all views that access `request.user` to fetch user-specific data are protected with `@login_required` (for FBVs) or `LoginRequiredMixin` (for CBVs) to gracefully redirect unauthenticated users instead of causing server errors or unintended behaviors.
