from django.shortcuts import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    #return HttpResponse("Hello. You're at the todoList index.")
    #latest_todo_list = Task.objects.order_by('-pub_date')[:5]
    #output = ', '.join([t.task_text for t in latest_task_list])
    #return HttpResponse(output)

    latest_task_list = Task.objects.order_by('-pub_date')[:5]
    template = loader.get_template('task/index.html')
    context = {
        'latest_task_list':latest_task_list
    }
    return HttpResponse(output)

def task_list(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)

def create(request, task_id):
    return HttpResponse("You're creating a task%s." %task_id)