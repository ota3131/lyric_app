from django.shortcuts import render

from accounts.models import Account

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signin(request):
    return render(request, 'accounts/signin.html')

def signup(request):
    return render(request, 'accounts/signup.html')

# accountsテーブルにデータを追加
def add_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        Account.objects.create(username=username, email=email, password=password)
        print(f"アカウント作成成功:{username}")
        return render(request, 'accounts/index.html')
    
    print("アカウント作成失敗")
    return render(request, 'accounts/signup.html')
