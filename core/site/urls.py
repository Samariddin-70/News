from django.urls import path

from .views import index, category, contact, search, view

urlpatterns = [
  path('', index, name='home'),
  path('ctg/', category, name='ctg'),
  path('con/', contact, name='con'),
  path('srch', search, name='srch'),
  path('view/', view, name='view'),
]
