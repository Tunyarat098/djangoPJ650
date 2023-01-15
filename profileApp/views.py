from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def edu(request):
    return render(request, 'edu.html')

def interest(request):
    return render(request, 'interest.html')

def influ(request):
    return render(request, 'influ.html')

def product(request):
    return render(request, 'product.html')

def test(request):
    return render(request, 'test.html')

