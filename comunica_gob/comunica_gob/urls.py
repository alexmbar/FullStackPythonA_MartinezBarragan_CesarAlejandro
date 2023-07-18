from django.contrib import admin
from django.urls import path, include
from administracion import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('reporte/', views.reporte, name='reporte'),
    path('misreportes/', views.misreportes, name='misreportes'),
    path('verperfil/',views.verperfil, name='verperfil'),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token de acceso
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token de acceso
]
