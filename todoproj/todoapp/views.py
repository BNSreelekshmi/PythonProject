from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'tasks'

class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'taskobj'

class taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'taskup'
    fields = ('tname','tpriority','tdate')

    def get_success_url(self):
        return reverse_lazy('classupdate',kwargs={'pk': self.object.id})

class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('classview')



# Create your views here.
def add(request):
    todotask = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('tname','')
        priority = request.POST.get('tpriority','')
        date = request.POST.get('tdate','')
        tasks = task(tname=name,tpriority=priority,tdate=date)
        tasks.save()
    return render(request,'home.html', {'tasks':todotask})

def delete(request,task_id):
    taskdel=task.objects.get(id=task_id)
    if request.method=='POST':
        taskdel.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task1=task.objects.get(id=taskid)
    formvar = todoform(request.POST or None, instance=task1)
    if formvar.is_valid():
        formvar.save()
        return redirect('/')
    return render(request,'edit.html',{'formkey':formvar,'formtask':task1})





