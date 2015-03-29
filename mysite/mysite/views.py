from django.http import HttpResponse

def hello(request):
	return HttpResponse("--2--Hello World---")