from django.shortcuts import render,redirect,get_object_or_404

from project.form import ProjectForm
from .models import *

# Create your views here.
def client_detail(request):
    CD=Client.objects.all()
    C={'CD':CD}
    return render(request,"client-details.html",C)

def client_add(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        e=request.POST['email']
        m = request.POST['phone_number']
        # u = request.POST['update']
        try:
            Client.objects.create(name=n,email=e,phone_number=m,)
            error="no"
        except:
            error="yes"
    d={'error':error}        
    return render(request,'client-add.html',d)

def client_edit(request,eid): 
    my_object = get_object_or_404(Client, id=eid)

    if request.method == 'POST':
        # Get updated data from the POST request
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        # Add other fields as needed

        # Update the object's fields
        my_object.name = name
        my_object.email = email
        my_object.phone_number =phone_number
        # Update other fields as needed

        # Save the changes to the database
        my_object.save()

        return redirect('client-d')  # Redirect to a success page
    else:
        return render(request, 'client-edit.html', {'my_object': my_object})   

def user_edit(request,UEid): 
    my_object = get_object_or_404(Client, id=UEid)

    if request.method == 'POST':
        # Get updated data from the POST request
        Full_name = request.POST['Full_name']
        email = request.POST['email']
        Number = request.POST['Number']
        # Add other fields as needed

        # Update the object's fields
        my_object.name = Full_name
        my_object.email = email
        my_object.phone_number =Number
        # Update other fields as needed

        # Save the changes to the database
        my_object.save()

        return redirect('user_D')  # Redirect to a success page
    else:
        return render(request, 'user-edit.html', {'my_object': my_object})        

def delete_client(request,cid):
    client=Client.objects.get(id=cid)
    client.delete()
    return redirect("client-D")

def User_detail(request):
    UD=User.objects.all()
    U={'UD':UD}
    return render(request,"user-details.html",U)

def user_add(request):
    error=""
    if request.method=='POST':
        N = request.POST['name']
        E=request.POST['email']
        Num = request.POST['number']
        
        try:
            User.objects.create(Full_name=N,email =E,Number=Num,)
            error="no"
        except:
            error="yes"
    d={'error':error}        
    return render(request,'user-add.html',d)

def delete_user(request,uid):
    user=User.objects.get(id=uid)
    user.delete()
    return redirect("user_D")

# def Project_table(request):
#     if request.method =='POST':
#        form=ProjectForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('project-D')
#     context={'form':ProjectForm()}
#     return render(request,'project-table.html',context)
def Project_table(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)  # Don't save yet to add users
            selected_users = request.POST.getlist('users')  # Get selected user IDs
            project.save()  # Save the project first
            project.users.set(selected_users)  # Add selected users to the project
            return redirect('project-D')
    else:
        form = ProjectForm()
    
    return render(request, 'project-table.html', {'form': form})


def project_detail(request):
    projects = Project.objects.prefetch_related('users').all()
    
    PD=Project.objects.all()
    P={
        'PD':PD,
        'projects': projects
       }
    return render(request,"project-detail.html",P)

def project_add(request):
    error=""
    client1=Client.objects.all()
    user1=User.objects.all()
    if request.method=='POST':
        P = request.POST['name']
        C = request.POST['client']
        U=request.POST['user']
        S = request.POST['Sdate']
        E = request.POST['Edate']
        client=Client.objects.filter(name=C).first()
        user=User.objects.filter(Full_name=U).first()
        try:
            Project.objects.create(name=P,client=client,users=user,start_date=S,end_date=E,)
            error="no"
        except:
            error="yes"
    d={'client':client1,'user':user1,'error':error}        
    return render(request,'project-add.html',d)



def delete_project(request,pid):
    pj=Project.objects.get(id=pid)
    pj.delete()
    return redirect("project-D")


def admin_home(request):
    
    dc = User.objects.all().count()
    pc = Client.objects.all().count()
    ac = Project.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac}
    return render(request,'home.html', d)    