from django.http import HttpResponse

def index(request):
	return (HttpResponse("Hello,You are at polls index"))

def results(request,question_id):
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You are voting on question %s" % question_id)
	 
