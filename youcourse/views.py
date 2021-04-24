from django.shortcuts import redirect

def redirect_catalog(request):
	return redirect('courses_list_url')