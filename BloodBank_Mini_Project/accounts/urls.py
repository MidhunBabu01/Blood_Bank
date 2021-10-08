from django.urls import path
from accounts import views



app_name = 'accounts'

urlpatterns = [
    path('',views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout/',views.logout, name="logout")
]