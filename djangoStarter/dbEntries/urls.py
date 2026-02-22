from django.urls import path
from . import views

urlpatterns = [
    path('dbEntries/', views.dbEntries, name='dbEntries'),
    path('Users/', views.Users, name='Users'),
]
