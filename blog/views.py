from django.shortcuts import render

# Create your views here.
def post_list(request):
	#Método render retorna http_response
	return render(request, 'blog/post_list.html', {})