from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from forms import CreateToDoItemForm
from .models import ToDoItem
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def index(request):
    active_items = []

    if request.user.is_authenticated():
        active_items = ToDoItem.objects.filter(done=False, owner=request.user)

    return render(request, 'index.html', {'the_data': active_items})


def email_send(to,message,timedate):
    send_mail('Reminder', message + " is due on " + str(timedate),'varun.hasija@practo.com',[to],fail_silently=False)

@login_required(login_url='/login/')
def new_todo_item(request):
    if request.method == "POST":
        form = CreateToDoItemForm(request.POST)
        if form.is_valid():
            todoItem = form.save(commit=False)
            todoItem.owner = request.user
            user = User.objects.get(id=todoItem.owner.id)
            user_email = user.email
            email_send(user_email,todoItem.description,todoItem.assigned_at)
            todoItem.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CreateToDoItemForm()

    return render(request, 'new_todo.html', {'form': form})


@login_required(login_url='/login/')
def save_changes(request):
    if request.method == "POST":
        check_items = request.POST.getlist('checked')

        ToDoItem.objects.filter(done=False, owner=request.user, id__in=check_items).update(done=True)

    return redirect(reverse('index'))
