"""
URL configuration for info_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from super.views import HomeView, ContactView, PubgView, PubgCommnetView, SearchView, ContactUsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view(), name='contact_url'),
    path('pubg/<int:pk>/', PubgView.as_view(), name='pubg'),
    path('pubg/<int:pk>/create_comment/', PubgCommnetView.as_view()),
    path('search/', SearchView.as_view(), name='search'),
    path('contact/contact/', ContactUsView.as_view()),
    path('<str:lang>/', HomeView.as_view(), name='home_url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)