from django.shortcuts import render
from accounts.models import Account
from django.db import IntegrityError

def index(request):
    return render(request, 'accounts/index.html')

def signin(request):
    return render(request, 'accounts/signin.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"ログイン試行: {username}, パスワード: {password}")

        if username and password:
            try:
                account = Account.objects.get(username=username, password=password)
                print(f"ログイン成功: {username}")
                session = request.session
                session['username'] = account.username
                return render(request, 'accounts/signin.html', {'success': True})
            except Account.DoesNotExist:
                print("ログイン失敗（アカウントが存在しない）")
        else:
            print("ログイン失敗（入力不備）")

    return render(request, 'accounts/signin.html', {'success': False})

def signup(request):
    return render(request, 'accounts/signup.html', {'success': None})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            if Account.objects.filter(email=email).exists():
                print("アカウント作成失敗（メール重複）")
                return render(request, 'accounts/signup.html', {
                    'success': False,
                    'error_message': 'このメールアドレスは既に使われています。'
                })

            try:
                Account.objects.create(username=username, email=email, password=password)
                print(f"アカウント作成成功: {username}")
                return render(request, 'accounts/signup.html', {'success': True})
            except IntegrityError as e:
                print(f"アカウント作成失敗（DBエラー）: {e}")
        else:
            print("アカウント作成失敗（入力不備）")

    return render(request, 'accounts/signup.html', {'success': False})