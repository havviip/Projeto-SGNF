"""
URL configuration for SGNF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Paginas import views as views_pagina
from Usuarios import views as views_usuarios


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_pagina.home, name='home'),
    path('login', views_pagina.login, name='login'),
    path('login_admin', views_pagina.login_admin, name='login_admin'),
    path('home_alunos', views_usuarios.home_alunos, name='home_alunos'),
    path('home_admin', views_usuarios.home_admin, name='home_admin')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
