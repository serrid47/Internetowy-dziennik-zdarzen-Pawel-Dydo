"""DziennikZdarzen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
app_name = 'changeLog'

urlpatterns = [
    # tworzenie dziennika zdarzen
    path('create/', views.ChangelogCreate.as_view(), name='changelogCreate'),
    # ustawienia dziennika zdarzen o nazwie name
    path('<str:name>/settings/', views.ChangelogSettings.as_view(), name='changelogSettings'),
    # wyświetl listę dzienników zdarzeń, do których należysz
    path('changelogs/', views.Changelogs.as_view(), name='changelogs'),
    # wyświetlenie dziennika zdarzen o nazwie name na stronie page
    path('<str:name>/<int:page>', views.LogCreate.as_view(), name='logCreate'),
    # wyświetlenie dziennika zdarzen o nazwie name
    path('<str:name>/', views.LogCreate.as_view(), name='logCreate'),
    # wyświetlenie rezultatów wyszukiwania słowa search_text w dzienniku zdarzen o nazwie name na stronie page
    path('<str:name>/search=<str:search_text>/<int:page>/', views.LogSearch.as_view(), name='logSearch'),
    # wyświetlenie rezultatów wyszukiwania słowa search_text w dzienniku zdarzen o nazwie name
    path('<str:name>/search=<str:search_text>', views.LogSearch.as_view(), name='logSearch'),
    # funkcja wywoływana przez javascript służaca do zmiany fragmentu strony
    path('<str:name>/update', views.LogUpdate, name='logUpdate'),
    # funkcja wywoływana przez javascript służaca do zmiany fragmentu strony oraz zapisu wczytanej ze strony wartości
    path('<str:name>/save', views.LogSave, name='logSave'),
]
