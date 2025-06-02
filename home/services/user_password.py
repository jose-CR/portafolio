from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages

template_general = "profile/password/"

class UserPasswordChange(PasswordChangeView):
        form_class = SetPasswordForm
        template_name = f"{template_general}change_password.html"
        success_url = reverse_lazy('profile')

        def form_valid(self, form):
            messages.success(self.request, _("The password has been changed successfully."))
            return super().form_valid(form)
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['title'] = _('Change Password')
                context['contents'] = ['new_password1', 'new_password2']
                context['content_button'] = _('Change')
                context['href'] = 'reset-password'
                context['href_text'] = _("Do you want to change your password?")
                return context

class UserPasswordReset(PasswordResetView):
        template_name = "emails/email_password.html"
        success_url = reverse_lazy('profile')
        email_template_name = f"{template_general}reset_email.html"

        def form_valid(self, form):
            messages.success(self.request, _("An email has been sent to your inbox."))
            return super().form_valid(form)

class UserPasswordConfirm(PasswordResetConfirmView):
        template_name = f"{template_general}reset_confirm.html"
        success_url = reverse_lazy('reset-password-done')

class UserPasswordComplete(PasswordResetCompleteView):
        template_name = f"{template_general}reset_password_complete.html"
