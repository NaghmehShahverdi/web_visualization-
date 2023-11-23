from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf import settings
from app import views
from users import views as auth

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', auth.GetOrCreateUser.as_view(), name='login'),
    path('logout/', auth.Logout.as_view(), name='logout'),
]


if not settings.PRODUCTION:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
