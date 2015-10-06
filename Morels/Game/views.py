from django.shortcuts import render
from .models import *
import sys
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from Game.forms.forms import UserForm, UserProfileForm

def signup(request):

    registered = False
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        print(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('form is valid')

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            return redirect('/login/')

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'signup.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )




#
game = Game()

# def signup(self):
    # username = request.POST['username']
    # password = request.POST['password']
    # email = request.POST['email']
    # pic = request.POST['profile']
    # user = MyUser.objects.create_user(username, password, email, 0, pic)

    # return render(request, 'signup.html')

    # user.save



def log_in(request):
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
    return render(request, 'login.html', context_instance=RequestContext(request))
            # else:
            #     state = "Not active"
@login_required(login_url='/login')
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