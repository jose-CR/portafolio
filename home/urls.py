from django.urls import path
from .views import app, About_Me, Contact_Me, mark_as_seen, delete_contact_ajax
from home.services.user_profile import ProfileCreateView, Profile, ProfileUpdateView, ProfileDeleteView
from home.services.user_password import UserPasswordChange, UserPasswordReset, UserPasswordConfirm, UserPasswordComplete

urlpatterns = [
    path('', app, name="app"),
    path('logout', Profile.exit, name="exit"),
    path('about_me', About_Me.as_view(), name="about_me"),
    path('contact_me', Contact_Me.as_view(), name="contact_me"),
    path("mark-as-seen/", mark_as_seen, name="mark_as_seen"),
    path('delete-contact/', delete_contact_ajax, name='delete_contact_ajax'),
    # CRUD Profile
    path('register/', ProfileCreateView.as_view(), name='register'),
    path('profile/', Profile.index ,name="profile"),
    path('profile/edit/<int:pk>', ProfileUpdateView.as_view() , name="profile_edit"),
    path('profile/delete/<int:pk>', ProfileDeleteView.as_view() , name="profile_delete"),
    # Password
    path('profile/change-password/', UserPasswordChange.as_view(), name="change-password"),
    path('profile/reset-password/', UserPasswordReset.as_view(), name="reset-password"),
    path('profile/<uidb64>/<token>/', UserPasswordConfirm.as_view(), name="reset-password-confirm"),
    path('profile/reset/complete', UserPasswordComplete.as_view(), name="reset-password-done"),
]