from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import User
from .forms import UserForm


def user_list(request):
    users = User.objects.all()

    return render(request,
                'users/list.html',
                {'users': users})


def user_create(request):
    data = {}
    if request.method == 'POST':
        form  = UserForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_valid'] = True
            users = User.objects.all()
            data['html_user_list'] = render_to_string('users/includes/user-list.html',
                                                    {'users': users})
    else:
        form = UserForm()

    html_form = render_to_string('users/includes/user-create-form.html',
                        {'form': form},
                        request=request)
    data['html_form'] = html_form

    return JsonResponse(data)


def user_update(request, pk):
    data = {}
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            data['form_valid'] = True
            users = User.objects.all()
            data['html_user_list'] = render_to_string('users/includes/user-list.html',
                                                    {'users': users})
    else:
        form = UserForm(instance = user)

    html_form = render_to_string('users/includes/user-update-form.html',
                        {'form': form},
                        request=request)
    data['html_form'] = html_form

    return JsonResponse(data)


def user_delete(request, pk):
    data = {}
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        data['form_valid'] = True
        users = User.objects.all()
        data['html_user_list'] = render_to_string('users/includes/user-list.html',
                                                {'users': users})

    else:
        html_form = render_to_string('users/includes/user-delete-form.html',
                                {'user': user},
                                request=request)
        data['html_form'] = html_form

    return JsonResponse(data)