from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from sales.forms import SalesEditForm
from sales.models import day

# Create your views here.
def daily_report(request):
    pan_list = day.objects.order_by('pan_date')
    return render(
        request,
        'view_daily.html',
        {
            'list':pan_list,
        },
        
    )


