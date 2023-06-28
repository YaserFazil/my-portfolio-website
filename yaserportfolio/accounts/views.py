from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the accounts index.")



# My own registration view
def registration(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # If it is, we validate the registration form.
        form = UserCreationForm(request.POST)
        # If the form is valid,
        if form.is_valid():
            # we save the user,
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #  log them in,
            login(request, user)
            # and redirect them to the home page (replace 'home' with the appropriate URL name for your home page).
            return redirect('index')
    # If the request method is not POST,
    else:
        # we create a new instance of the UserCreationForm
        form = UserCreationForm()
    # and render the registration.html template with the form.
    return render(request, 'registration/registration.html', {'form': form})