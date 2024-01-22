# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('details/(?P<id>\w{0,50})/$',views.details)
#     # other URL patterns...
# ]
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('add/', views.add, name='add')
]

