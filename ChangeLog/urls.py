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
    path('create/', views.ChangelogCreate.as_view(), name='changelogCreate'),
    path('<str:name>/settings/', views.ChangelogSettings.as_view(), name='changelogSettings'),
    path('<str:name>/<int:page>', views.LogCreate.as_view(), name='logCreate'),
    path('<str:name>/', views.LogCreate.as_view(), name='logCreate'),
    path('<str:name>/search=<str:search_text>/<int:page>/', views.LogSearch.as_view(), name='logSearch'),
    path('<str:name>/search=<str:search_text>', views.LogSearch.as_view(), name='logSearch'),
    path('<str:name>/update', views.LogUpdate, name='logUpdate'),
    path('<str:name>/save', views.LogSave, name='logSave'),

]
