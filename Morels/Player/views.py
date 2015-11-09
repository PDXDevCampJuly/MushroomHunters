from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import login
from django.db.models import Q
from Game.models import Game
from Player.models import Player
from Player.forms.forms import UserForm, UserProfileForm
from .models import MyUser
# Create your views here.


def signup(request):
    """Creates user if form is valid"""

    if request.user.is_authenticated():
        return redirect('/home/')

    registered = False
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.FILES)
        # print(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('form is valid')

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            print(request.FILES)

            try:
                profile.profilePic = request.FILES['profilePic']
            except:
                print('there are no files')

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
            {'user_form': user_form,
             'profile_form': profile_form,
             'registered': registered} )


def log_in(request):
    """Logs in user is info user has given is valid"""
    username = password = ""

    if request.user.is_authenticated():
        return redirect('/home/')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/home/')
    return render(request, 'login.html', context_instance=RequestContext(request))


@login_required(login_url='/login')
def user_logout(request):
    """Logs out user"""
    logout(request)

    return redirect('/login/')


def home(request):
    """If user is logged: Go to home page, Else: Go to signup page"""
    # request.session.delete_test_cookie()

    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return redirect('/')


def profile(request):
    """Sends info to template"""

    user = request.user.username

    current_player = MyUser.objects.filter(user=request.user)[0]

    member = Player.objects.filter(userPlayer=current_player)

    current_games = Game.objects.filter(Q(player_1__in=member) | Q(player_2__in=member))

    count = current_games.count()

    imagecount = current_player.profilePic

    return render(request, 'profile.html', {'user': user,
                                            'current_player': current_player,
                                            'current_games': current_games,
                                            'count': count, 'imagecount': imagecount})


def leader_board(request):
    """Sends info to template"""
    users = MyUser.objects.all()
    board = []

    print(users)
    print(board)

    return render(request, 'leaderboard.html', {'users':users})












