from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('jobs/', include('job.urls', namespace='jobs')),
    path('contact-us/', include('contact.urls', namespace='contact')),
    path('blog/', include('Blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
