"""
URL configuration for homeworks project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hom1/', include('homeworks_app1.urls', namespace='homeworks_app1')),
    path('hom2/', include('homeworks_app2.urls', namespace='homeworks_app2')),
    path('', include('homeworks_app3.urls', namespace='homeworks_app3')),
    path('hom4/', include('homeworks_app4.urls', namespace='homeworks_app4')),
    path('hom5/', include('homeworks_app5.urls', namespace='homeworks_app5')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
