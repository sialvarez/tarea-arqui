from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Comment
from polls.form import Form
from ipware import get_client_ip

def index(request):
	ip, is_routable = get_client_ip(request)
	latest_comment_list = Comment.objects.order_by('-date')
	template = loader.get_template('polls/index.html')
	context = {
	'latest_comment_list': latest_comment_list,
	'ip': ip
	}

	if request.method == "POST":
		form = Form(request.POST)
		if form.is_valid():
			form.save()

	return HttpResponse(template.render(context, request))
	




def results(request):
    response = "You're looking at the results"
    return HttpResponse(response)

def comment(request):
    return HttpResponse("You're commenting on the page.")

