"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from bookstore import views
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),

    # ✅ Página da raiz
    path("", lambda request: HttpResponse("🚀 API Bookstore online!"), name="home"),
]
