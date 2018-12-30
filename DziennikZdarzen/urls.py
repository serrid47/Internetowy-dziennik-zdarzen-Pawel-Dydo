
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('changeLog/', include('changeLog.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.LoginUserView.as_view(), name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.yourprofile.as_view(), name='yourprofile'),
    path('profile/<str:name>', views.userprofile.as_view(), name='userprofile'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)