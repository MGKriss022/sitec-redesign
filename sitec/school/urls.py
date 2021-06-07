from django.urls import path
from .views import (
    LoginView,
    PanelView,
    SettingsView,
    ReinscriptionView,
    CycleAdvanceView,
    KardexView,
    LogView
)

app_name = 'school'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('panel/', PanelView.as_view(), name='panel'),
    path('configuracion/', SettingsView.as_view(), name='settings'),
    path('reinscripcion/', ReinscriptionView.as_view(), name='reinscription'),
    path('avance-ciclo/', CycleAdvanceView.as_view(), name='cycle-advance'),
    path('kardex/', KardexView.as_view(), name='kardex'),
    path('log/', LogView.as_view(), name='log')
]