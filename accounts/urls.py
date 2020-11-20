from django.conf.urls import url
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('test/', views.test),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]