from django.shortcuts import get_object_or_404, redirect, render
from . models import Todo
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.                     
                                                      
@login_required(login_url='login')
def index(request):
  current_user= request.user
  all_todos = Todo.objects.filter(user=current_user)

  if request.method == "POST":
    todo = request.POST['todo']
    new_todo = Todo(title=todo,user=current_user)
    new_todo.save()
    return redirect('/')

  return render(request,'index.html',{'todo':all_todos})

@login_required(login_url='login')
def delete(request,pk):
  todo_item = Todo.objects.get(id=pk)
  todo_item.delete()
  return redirect('/')

@login_required(login_url='login')
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
  

def register(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    form=CreateUserForm()
    if request.method == "POST":
      form=CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user=form.cleaned_data.get('username')
        messages.success(request, "Account was created for " + user)

        return redirect('login')


    context={'form':form}
    return render(request,'register.html',context)



def loginPage(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method =="POST":
      user_name= request.POST.get('username')
      password= request.POST.get('password')

      user=authenticate(request,username=user_name,password=password)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.info(request,"Username Or Password Is Incorrect")


  context={}
  return render(request,'login.html',context)

def logoutUser(request):
  logout(request)
  return redirect('login')