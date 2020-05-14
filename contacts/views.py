from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import  Http404,HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.urls import  reverse

from medpril import local_settings

from .models import message,units,dop_info,Comment
def contact(request):
    dop = dop_info.objects.all()
    unit=units.objects.all()
    mesag = message.objects.all()
    return render(request, 'contact.html',{'unit':unit,'dop':dop,'mesag':mesag})

def AddReview(requset):
       Comment.create(neme=requset.POST['name'], text=requset.POST['message'],email=requset.POST['email'],phone=requset.POST['phone'])
       return HttpResponseRedirect( reverse('contact:contact'))





def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']

			recipients = ['ВАШ_EMAIL_ДЛЯ_ПОЛУЧЕНИЯ_СООБЩЕНИЯ']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'site/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'site/contact.html', {'form': form})
