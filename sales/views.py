from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import day
from sales.forms import SalesEditForm

# Create your views here.
def insert_data(request):
    if request.method == "GET":
        insert_form = SalesEditForm()
    elif request.method == "POST":
        insert_form = SalesEditForm(request.POST, request.FILES)

        if insert_form.is_valid():
            insert_data = insert_form.save(commit=False)
            insert_data.save()
            return redirect('/sales/input')

    return render(
        request,
        'insert_data.html',
        {
            'form': insert_form,
        }
    )
