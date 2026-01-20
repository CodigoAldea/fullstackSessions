from django.urls import path, include
from exptracker.views import home

'''
url pattern / syntax : 
    path('endpoint', view, name='alias')
'''
urlpatterns = [
    path('', home, name='home'),
]