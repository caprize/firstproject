from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

urlpatterns = [
    path('', views.post_list, name='post_list'),

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
