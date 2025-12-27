from django.contrib import admin
from django.urls import path, include # Add include here
from portal.views import home
from portal.views import about
from portal.views import categories, quote
from django.urls import path, include
from portal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('portal/client/', views.client_dashboard, name='client_dashboard'),
    path('portal/owner/', views.owner_dashboard, name='owner_dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('categories/', categories, name='categories'),
    path('get-quote/', quote, name='quote'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)