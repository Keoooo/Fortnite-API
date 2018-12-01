from django.shortcuts import render

# Create your views here.

def docsView(request):
	return render(request, 'docshtml/docs.html')