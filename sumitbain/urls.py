

from django.urls import path
from.import views


urlpatterns = [

    path('',views.home),
    path('count/',views.count),
    path('eggs/',views.eggs),

]
