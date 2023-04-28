from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User  =get_user_model()
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# from common.decorators import ajax_required
from .models import Contact
from actions.utils import create_action
from actions.models import Action


# User Login View
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# User Dashboard View
@login_required
def dashboard(request):
    # Display all actions by default
    actions = Action.objects.exclude(user=request.user)
    # print(actions)
    following_ids = request.user.following.values_list('id',
    flat=True)
    if following_ids:
    # If user is following others, retrieve only their actions
        # actions = actions.filter(user_id__in=following_ids)
        actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__profile').prefetch_related('target')
        actions = actions[:10]
    template_name = 'account/dashboard.html'
    context = {
        'section': 'dashboard',
        'actions': actions
    }
    return render(request,template_name, context)



# User Logout View
def logout_view(request):
    logout(request)
    template_name = 'account/logout.html'
    return render(request,template_name)


# User Registration View
def register(request):
    template_name = 'account/register.html'
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    context={
        'user_form': user_form
    }
    return render(request,template_name,context)

@login_required
def edit(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    # print(profile)
    if created:
        profile.save()
    if request.method == 'POST':
        # print(request.POST)
        user_form = UserEditForm(instance=request.user,
        data=request.POST)
        profile_form = ProfileEditForm(
        instance=profile,
        data=request.POST,
        files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            # print("User save")
        if  profile_form.is_valid():
            profile_form.save()

        # messages.success(request, "Changes has been updated successfully.")
        # mess
            # print("Profile save")
        # return render(request,
        # 'account/edit.html',
        # {'user_form': user_form,
        # 'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm( instance=profile)

    # print(profile_form)
    return render(request,
    'account/edit.html',
    {'user_form': user_form,
    'profile_form': profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
    'account/user/list.html',
    {'section': 'people',
    'users': users})
    
@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
    username=username,
    is_active=True)
    return render(request,
    'account/user/detail.html',
    {'section': 'people',
    'user': user})


# @require_POST
@login_required
def user_follow(request):
    # print("requested")
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create( user_from=request.user, user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})