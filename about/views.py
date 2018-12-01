from django.shortcuts import render

# Create your views here.

def aboutView(request):
	return render(request, 'abouthtml/about.html')