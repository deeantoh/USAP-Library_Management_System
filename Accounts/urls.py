from django.urls import path

from Accounts import views


app_name = 'accounts'

urlpatterns =[
    # Frontend
    path('', views.frontend, name="frontend"),
    path('register', views.SignUpView.as_view(), name="register"),
    # Backend
    # path('backend/', views.backend, name="backend"),
]