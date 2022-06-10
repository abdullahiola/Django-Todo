from django.shortcuts import get_object_or_404, redirect, render
from . models import Todo
# Create your views here.                     
                                                      

def index(request):
  all_todos = Todo.objects.all

  if request.method == "POST":
    todo = request.POST['todo']
    new_todo = Todo(title=todo)
    new_todo.save()
    return redirect('/')

  return render(request,'index.html',{'todo':all_todos})

def delete(request,pk):
  todo_item = Todo.objects.get(id=pk)
  todo_item.delete()
  return redirect('/')

def edit(request,pk):
  item=get_object_or_404(Todo,id=pk)
  context={'item':item}
  # item=Todo.objects.get(id=pk)

  if request.method == "POST":
    real_data=Todo.objects.get(id=pk)
    edited_data=request.POST['edit']
    real_data.title= edited_data
    real_data.save()
    return redirect('/')


  return render(request,'edit.html',context)
  


