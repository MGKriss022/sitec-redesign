from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'school/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class PanelView(TemplateView):
    template_name = 'school/panel.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class SettingsView(TemplateView):
    template_name = 'school/settings.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        
class ReinscriptionView(TemplateView):
    template_name = 'school/reinscription.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)   
        
class CycleAdvanceView(TemplateView):
    template_name = 'school/cycle_advance.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)   
        
class KardexView(TemplateView):
    template_name = 'school/kardex.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)   
        
class LogView(TemplateView):
    template_name = 'school/log.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)