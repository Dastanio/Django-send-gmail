from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages



def index(request):

	if request.method == 'POST':
		message = request.POST['message']
		gmail = request.POST['gmail']
		send_mail('gmail почта клиента:  ' + gmail, 
		 'Текст сообщения от клиента:  ' + message, 
		 settings.EMAIL_HOST_USER,
		 ['dassu5588@gmail.com'], # <--- вот сдесь ты едешь 2 аккаунт  
		 fail_silently=False)


		messages.success(request, ('Ваш заказ успешно принят, доставщик свами свяжется'))
		return redirect('index')

	return render(request, 'app/index.html')






