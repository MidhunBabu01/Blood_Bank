from django.urls import path
from BloodBank_app import views




app_name = 'BloodBank_app'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('result',views.result, name="result"),
    # path('register',views.register, name="register"),
    # path('login',views.login, name="login")
]