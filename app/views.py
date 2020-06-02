from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages



def index(request):

	if request.method == 'POST':
		message = request.POST['message']
		gmail = request.POST['gmail']
		name = request.POST['name']
		send_mail(name, 
		 message,  
		 settings.EMAIL_HOST_USER,
		 [gmail], 
		 fail_silently=False)


		messages.success(request, ('gmail sent successfully!'))
		return redirect('index')

	return render(request, 'app/index.html')






