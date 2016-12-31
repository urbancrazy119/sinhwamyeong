from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import day
from sales.forms import SalesEditForm

from django.db import IntegrityError

# Create your views here.
@login_required
def insert_data(request):
    if request.method == "GET":
        insert_form = SalesEditForm()
    elif request.method == "POST":
        insert_form = SalesEditForm(request.POST, request.FILES)

        if insert_form.is_valid():
            try:
                insert_data = insert_form.save(commit=False)
                insert_data.save()
                return redirect('/sales/input')
            except IntegrityError as e:
                return render(
                    request,
                    'error_page.html',
                    {
                        'val':request.POST,
                    },
                )

    return render(
        request,
        'insert_data.html',
        {
            'form': insert_form,
        },
    )

@login_required
def delete_data(request):
    if request.method=="POST":
        a=1
        return redirect('/sales/input/')
    else :
        a=2
    return render(
        request,
        'delete_data.html',
        {
        },
    )

@login_required
def error(request):
    return render(
        request,
        'error_page.html',
    )
