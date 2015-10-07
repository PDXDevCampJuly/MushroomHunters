from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import login

# Create your views here.
from Player.forms.forms import UserForm, UserProfileForm

def signup(request):

    if request.user.is_authenticated():
        return redirect('/home/')

    registered = False
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.FILES)
        # print(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('formsorm is valid')

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
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def log_in(request):
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
            # else:
            #     state = "Not active"


@login_required(login_url='/login')
def user_logout(request):
    logout(request)

    return redirect('/login/')

def home(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return redirect('/')