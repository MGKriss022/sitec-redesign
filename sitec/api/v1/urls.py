from rest_framework import routers
from rest_registration.api.urls import login, logout
from django.urls import path, include
from .views import sitec_login

router = routers.DefaultRouter()

app_name = 'api-v1'
urlpatterns = router.urls

urlpatterns += [
    path('accounts/login/', login, name='login'),
    path('accounts/logout', logout, name='logout'),
    path('accounts/sitec_login', sitec_login, name='sitec-login')
]