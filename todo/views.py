from django.shortcuts import redirect, render
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
  


