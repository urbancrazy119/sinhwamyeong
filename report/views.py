from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from sales.forms import SalesEditForm
from sales.models import day

from datetime import datetime

# Create your views here.
def daily_report(request):
    now = datetime.now()
    if request.method == "POST":

        # get POST Data
        pan_type = request.POST['pan_type']
        s_date = request.POST['s_date']
        e_date = request.POST['e_date']

        # if date input is null
        if s_date == "":
            s_date = now.strftime('%Y-%m-%d')
        if e_date == "":
            e_date = now.strftime('%Y-%m-%d')

        # replace from / to -
        s_date = s_date.replace('/','-')
        e_date = e_date.replace('/','-')

        #  selected all type
        if pan_type == '00':
            pan_list = day.objects.filter(pan_date__range=(s_date,e_date)).order_by('pan_date')
        else:
            pan_list = day.objects.filter(pan_date__range=(s_date,e_date), pan_type=pan_type).order_by('pan_date')
    else:
        s_date = now.strftime('%Y-%m-%d')
        e_date = now.strftime('%Y-%m-%d')
        pan_type = '00'
        pan_list = day.objects.order_by('pan_date')
    
    val_list = {'s_date':s_date.replace('-','/'),'e_date':e_date.replace('-','/'),'pan_type':pan_type}

    return render(
        request,
        'view_daily.html',
        {
            'list':pan_list,
            'val':val_list,
        },
    )   

