from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.yourprofile.as_view(), name='homepage'),
    # dołączenie adresów z pliku urls.py z aplikacji changeLog
    path('changeLog/', include('changeLog.urls')),
    # rejestracja
    path('signup/', views.signup, name='signup'),
    # logowanie
    path('signin/', views.LoginUserView.as_view(), name='signin'),
    # wylogowanie
    path('signout/', views.signout, name='signout'),
    # wyświetl twój profil (możliwość zaktualizowana swoich danych)
    path('profile/', views.yourprofile.as_view(), name='yourprofile'),
    # wyświetl profil użytkownika o nazwie użytkownika name
    path('profile/<str:name>', views.userprofile.as_view(), name='userprofile'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
