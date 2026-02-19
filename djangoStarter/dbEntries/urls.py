from django.urls import path
from . import views

urlpatterns = [
    path('dbEntries/', views.dbEntries, name='dbEntries'),
]
