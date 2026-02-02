
from . import views
from django.urls import path


urlpatterns = [

    path('django1/',views.django1,name='dj1'),
    path('django2/',views.django2,name='dj2'),
    path('select_django/',views.select_django,name='select_django'),
    path('delete_django/',views.delete_django,name='delete_django'),
    path('update_django/',views.update_django,name='update_django'),
    path('insert_django/',views.insert_django,name='insert_django'),


]
