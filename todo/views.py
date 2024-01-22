# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Todo
# # Create your views here.
# def index(request):
#     todo=Todo.objects.all()[:10]
#     context = {
#         'todos': todo, 'name': 'Firdous Khan'
#         }
#     return render(request, 'index.html',context)
#     # return HttpResponse('Hello Firdous Khan')
# def details(request,id):
#     todo =Todo.objects.get(id=id)
#     context={
#         'todo':todo
#     }
#     return render(request,'details.html',context)
from django.http import HttpResponse
from .models import Todo
from django.shortcuts import render, get_object_or_404 ,redirect 


# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = get_object_or_404(Todo, id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)
    
def add(request):
    if(request.method=='POST'):
        title=request.POST['title']
        text=request.POST['text']
        todo = Todo(title = title , text=text)
        todo.save()
        return redirect('/todo')
    else:
    # Your implementation for the add view
        return render(request, 'add.html')
