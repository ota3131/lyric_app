from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # アプリのトップページ
    path('signin/', views.signin, name='signin'), # サインインページ
    path('signup/', views.signup, name='signup'), # サインアップページ
    path('add_account/', views.add_account, name='add_account'), # アカウント追加処理
]
