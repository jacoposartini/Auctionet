from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView
from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registrazione tramite web page
    path("accounts/register/",
         RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
         ), name="django_registration_register"),

    # Registrazione one_step tramite web page
    path('accounts/',
        include("django_registration.backends.one_step.urls")),
    # Login tramite web page
    path('accounts/',
        include("django.contrib.auth.urls")),

    path('', include("auctions.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
