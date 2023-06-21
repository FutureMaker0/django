"""
URL configuration for pjt1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# import path, include 까지 해줘야 include 사용가능.
from django.urls import path, include

urlpatterns = [
    # 콤마 기준으로 앞에를 패턴, 뒤에를 맵핑이라 생각하면 된다.
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

