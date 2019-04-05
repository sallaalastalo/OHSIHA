from django.urls import path
from django.conf.urls import url
from .views import list_events, create_event, update_event, delete_event

urlpatterns =[
    path('etusivu',	list_events, name='list_events'),
    path('new',	create_event, name='create_event'),
    path('update/<int:id>/', update_event,	name='update_event'),
    path('delete/<int:id>/', delete_event,	name='delete_event'),
]