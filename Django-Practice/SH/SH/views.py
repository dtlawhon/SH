from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render_to_response
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from models import UserProfile
# Create your views here.


from forms import UserForm, UserProfileForm

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        # user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if profile_form.is_valid():
            # Save the user's form data to the database.
            # user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            # user.set_password(user.password)
            # user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            # profile.user = user
            
            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
       # user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if request.POST.has_key('remember_me'):   
                    request.session.set_expiry(1209600) # 2 weeks
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your SH account is disabled")
        else:
            print "Invalid login details: {0}, {1}".format(username,password)
            return HttpResponse("Invalid login details")
    else:
        return render_to_response('login.html', {}, context)
    
@login_required
def restricted(request):
    return render(request, 'restricted.html')

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def chef_register(request):
    return render(request, 'chefregister.html')
    
def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', {}, context)

def about(request):
    return render(request, 'about.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    return render(request, 'contact.html')
        
        



