from django.contrib import admin
from django.urls import path, include
from core.views import PostView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name="test"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name="obtain-token" ),
    path('rest-auth/', include('rest_auth.urls'))
]
