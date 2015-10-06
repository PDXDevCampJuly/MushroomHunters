from django.shortcuts import render
from .models import *
import sys
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

game = Game()

def realsignup(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    pic = request.POST['profile']
    user = MyUser.objects.create_user(username, password, email, 0, pic)

    user.save



def signup(request):
    # state = "Sign up now!"
    username = password = ""

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # state = "Logged in"
                return redirect('/main/')
    return render(request, 'signup.html', context_instance=RequestContext(request))
            # else:
            #     state = "Not active"
@login_required(login_url='/login/')
def main(request):
    pass
        # else:
        #     state = "your username or password was incorrect"

# def make_decks(request):
#     games = Game.objects.all()
#
#     for i in range():


    # Get the cards from the db
    #Loop through the cards in Cards and push them in a deck