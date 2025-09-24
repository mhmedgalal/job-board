from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from importlib.util import find_spec
_SPECTACULAR = find_spec('drf_spectacular') is not None
if _SPECTACULAR:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView  # type: ignore

def health_check(request):
    return HttpResponse(b"OK", status=200)

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('health/', health_check, name='health_check'),

    # حسابات المستخدمين (HTML)
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # API خاص بال accounts (JSON)
    path('api/', include('accounts.url_api')),  

    path('admin/', admin.site.urls),
    path('jobs/', include('job.urls', namespace='jobs')),
    path('contact-us/', include('contact.urls', namespace='contact')),
    path('blog/', include('Blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),

    # APIs أخرى
    path('api/', include('job.urls_api')),
    path('api/token/', TokenObtainPairView.as_view()),
]

if _SPECTACULAR:
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)