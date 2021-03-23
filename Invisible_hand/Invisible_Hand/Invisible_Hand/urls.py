from django.urls import path,include
from . import test,views
from django.contrib import admin

urlpatterns = [
    path('search/', include('search.urls')),
    path('test/', test.test),
    path('health/', include('health.urls')),
    path('dormitory/', include('dormitory.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.home),
]
