from django.shortcuts import render

# Create your views here.
def index_main(request):
    return render(request, 'main/index.html')