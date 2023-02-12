from django.shortcuts import render, HttpResponse, redirect
from .models import Notes
from django.contrib import messages
from django.contrib.auth.models import User
from utilities.authvalidation import signup_validation
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == "POST":
        title = request.POST['title'].strip()
        print("Title: ", title)
        try:
            if title == "" or title == " ":
                raise ValueError("Empty strings are not allowed")
            note = Notes(author = request.user,  title = title)
            note.save()
            print(note.title)
        except ValueError:
            return redirect('/')
        except Exception as e:
            print("Error ", e)
            messages.add_message(request, messages.ERROR, "Operation Failed! Some error occured")
    notes = Notes.objects.filter(author = request.user)
    return render(request, "todoApp/index.html", {"notes": notes, "username": request.user.username})


@login_required
def edit(request):
    return HttpResponse("Edit the following things")


@login_required
def deleteNote(request, id):
    if request.method == "POST":
        try:
            note = Notes.objects.get(pk=id)
            note.delete()
            return redirect('/')
        except Exception as e:
            print(e)
    return redirect("/")


def extract_email_details(request):
    email = request.POST['email']
    password = request.POST["password"]
    confirmPass = request.POST["confirmPass"]
    username = email.split('@')[0]
    user = User.objects.filter(username = username)
    if(len(user) > 0):
        username = username + "1"
    return {"email": email, "password":password, "confirmPass": confirmPass, "username": username}




def signup_view(request):
    """view to handle signing user
    Functionality:
        1. Get data from request and save it in a dictionary.
        2. Check if email is unique and data is valid
        3. If step 2 failed then return to the page with error message.
        4. If everything is fine then create the user"""

    if request.method  == 'POST' and not request.user.is_authenticated:

        #1. Get the data from request and save it in a dictionary
        details = extract_email_details(request)
        details['user'] = False
        #2. check if email is unique and data is valid.
        try:
            user = User.objects.filter(email=details['email'])
            if len(user) > 0:
                details['user'] = True
        except Exception as e:
            print(e)

        #validate credenctials and check if user is already exits or not.
        checkPass = signup_validation(details)


        #3. If everything is fine then create the user else return with error message

        message_content = ""
        message_status = ""
        if checkPass['status'] == False:
            message_content = checkPass['message']
            message_status = messages.ERROR
        else:
            user = User.objects.create_user(details["username"], details['email'], details['password'])
            if user:
                message_content = "User is created successfully"
                message_status = messages.SUCCESS
                messages.add_message(request, message_status, message_content)
                return redirect('login')
            else:
                message_content = "Operation failed try again"
                message_status = messages.ERROR

        messages.add_message(request, message_status, message_content)
        return render(request, 'registration/signup.html')


    #4. handling case when user is already authenticated or request is not post
  
    if request.user.is_authenticated:
        return redirect('/')
    
    messages.add_message(request, messages.INFO, 'please enter your email and passwords')
    return render(request, "registration/signup.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        email = request.POST['email']
        password  = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('/')
        except Exception as e:
            print(e)
        messages.add_message(request, messages.ERROR, "Wrong credentials. Try again")
        return render(request, "registration/login.html")
    return render(request, "registration/login.html")


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    
    return redirect('/')


@login_required
def addConfirm(request, pk):
    print("I am here")
    try:
        note = Notes.objects.get(pk = pk)
        print("Previous ", note.isCompleted)
        note.isCompleted = not note.isCompleted
        note.save()
        print("After: ", note.isCompleted)

    except Exception as e:
        print(e)
    return redirect('/')