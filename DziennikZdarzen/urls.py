
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('changeLog/', include('changeLog.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.LoginUserView.as_view(), name='signin'),
    path('signout/', views.signout, name='signout'),

]
