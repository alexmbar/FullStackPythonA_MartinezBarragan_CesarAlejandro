from django.contrib import admin
from django.urls import path
from administracion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('reportes/', views.reporte, name='reporte'),
    path('misreportes/', views.misreportes, name='misreportes')
]
