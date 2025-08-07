from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # アプリのトップページ
    path('signin/', views.signin, name='signin'), # サインインページ
    path('signin_view/', views.signin_view, name='signin_view'), # サインイン処理
    path('signup/', views.signup, name='signup'), # サインアップページ
    path('signup_view/', views.signup_view, name='signup_view'), # アカウント追加処理

]
