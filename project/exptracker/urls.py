from django.urls import path, include
from exptracker.views import home , deleteexp

'''
url pattern / syntax : 
    path('endpoint', view, name='alias')
'''
urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:id>',deleteexp, name='del')
    #path
]