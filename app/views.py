from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ListForm, ItemForm
from .models import List, Item
import json
from django.http import JsonResponse
from random import randint
from django.db.models import F
from itertools import chain
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'app/landing.html')


@login_required(login_url="/login")
def home(request):
    q = List.objects.all()
    return render(request, 'app/home.html', {'lists': q})


def get_item(request):
    if request.method == 'POST':
        lists_obj = json.loads(request.body.decode('utf-8'))

        if len(lists_obj["lists"]) > 0:
            # Get Items from selected user created Lists
            q = Item.objects.filter(list_id__in=lists_obj["lists"])

            # Get Least Frequent Items (if requried)
            ordered_r = Item.objects.none()
            if "998" in lists_obj["lists"]:
                r_with_totals = Item.objects.annotate(totals=F('correct') + F('incorrect'))
                ordered_r = r_with_totals.order_by('totals')

                if len(ordered_r) > 5:
                    ordered_r = ordered_r[:5]
                else:
                    pass

            # Most Difficult Items (if required)
            ordered_s = Item.objects.none()
            if "999" in lists_obj["lists"]:
                s_with_stats = Item.objects.annotate(stats=(F('correct')/(F('correct') + F('incorrect'))))
                ordered_s = s_with_stats.order_by('stats')

                if len(ordered_s) > 5:
                    ordered_s = ordered_s[:5]
                else:
                    pass

            results = list(chain(q, ordered_r, ordered_s))

            selected_item = results[randint(0, len(results) - 1)]

            # Update occurrences
            selected_item.occur += 1
            selected_item.save()

            item = {"pk": selected_item.id,
                    "primary": selected_item.primary,
                    "secondary": selected_item.secondary,
                    "comments": selected_item.comments}
        else:
            # Change this to an error page
            item = {"primary": "Please select one or more Lists",
                    "secondary": "",
                    "comments": ""}

        # Check for bad json data here

        return JsonResponse({"item": item})
    else:
        return redirect('error')


def mark_correct(request):
    if request.method == 'POST':
        item_id = json.loads(request.body.decode('utf-8'))["item"]
        item_obj = get_object_or_404(Item, pk=item_id)
        item_obj.correct += 1
        item_obj.save()

        return JsonResponse({"status": "success"})
    else:
        return redirect('error')


def mark_incorrect(request):
    if request.method == 'POST':
        item_id = json.loads(request.body.decode('utf-8'))["item"]
        item_obj = get_object_or_404(Item, pk=item_id)
        item_obj.incorrect += 1
        item_obj.save()

        return JsonResponse({"status": "success"})
    else:
        return redirect('error')


def lists(request):
    q = List.objects.all()
    return render(request, 'app/lists.html', {'query': q})


def list_view(request, pk):
    list_obj = get_object_or_404(List, pk=pk)
    q = Item.objects.filter(list=list_obj.id)
    return render(request, 'app/list_view.html', {'list': list_obj, 'query': q})


def list_edit(request, pk):
    list_obj = get_object_or_404(List, pk=pk)

    if request.method == 'POST':
        edit_form = ListForm(request.POST, instance=list_obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list_view', pk)
        # Handle invalid forms
    else:
        edit_form = ListForm(instance=list_obj)

    return render(request, 'app/list_edit.html', {'form': edit_form, 'list': list_obj})


def list_create(request):
    if request.method == 'POST':
        f = ListForm(request.POST)
        if f.is_valid():
            obj = f.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('lists')
    else:
        f = ListForm()

    return render(request, 'app/list_create.html', {'form': f})


def list_remove(request, pk):
    list_obj = get_object_or_404(List, pk=pk)
    list_obj.delete()
    return redirect('lists')


def items(request):
    q = Item.objects.all()
    return render(request, 'app/items.html', {'query': q})


def item_view(request, pk):
    item_obj = get_object_or_404(Item, pk=pk)
    return render(request, 'app/item_view.html', {'item': item_obj})


def item_edit(request, pk):
    item_obj = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        edit_form = ItemForm(request.POST, instance=item_obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('item_view', pk)
        # Handle invalid forms
    else:
        edit_form = ItemForm(instance=item_obj)

    return render(request, 'app/item_edit.html', {'form': edit_form, 'item': item_obj})


def item_create(request, pk=None):
    list_obj = None
    print(pk)
    if request.method == 'POST':
        f = ItemForm(request.POST)
        if f.is_valid():
            f.save()

            print(pk)

            if pk is not None:
                return redirect('list_view', pk)
            else:
                return redirect('items')
    else:
        if pk is not None:
            list_obj = get_object_or_404(List, pk=pk)
            f = ItemForm(initial={'list': list_obj})
        else:
            f = ItemForm()

    return render(request, 'app/item_create.html', {'form': f, 'list': list_obj})


def item_remove(request, pk):
    item_obj = get_object_or_404(Item, pk=pk)
    item_obj.delete()
    return redirect('items')


def account(request):
    q = List.objects.all()
    return render(request, 'registration/account.html', {'query': q})


def reset_stats(request, pk):
    if pk == 'all':
        q = Item.objects.all()
    else:
        list_obj = get_object_or_404(List, pk=pk)
        q = Item.objects.filter(list=list_obj)
    for item in q:
        item.occur = 0
        item.correct = 0
        item.incorrect = 0
        item.save()

    return redirect('home')


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created.')
            return redirect('register')
    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})


def login(request):
    return render(request, 'registration/login.html')


def help(request):
    return render(request, 'app/help.html')


def error(request):
    return render(request, 'app/error.html')
