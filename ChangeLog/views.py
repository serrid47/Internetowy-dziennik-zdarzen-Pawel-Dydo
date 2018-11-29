from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Log
from .forms import LogForm
from django.contrib.auth.decorators import login_required



@login_required
def changelog(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            l_text = form.cleaned_data['log_text']
            log = Log()
            log.log_text = l_text
            log.user = request.user
            log.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = LogForm()

    pages = (Log.objects.all().count()//20)+1
    pages_list = []
    for i in range(pages):
        pages_list.append(i+1)

    latest_log_list = Log.objects.order_by('-publication_date')[:20]
    context = {'latest_log_list': latest_log_list,
               'pages_list':pages_list}
    return render(request, 'changeLog/changeLog.html', context)

@login_required
def changelogwithpage(request, page):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            l_text = form.cleaned_data['log_text']
            log = Log()
            log.log_text = l_text
            log.user = request.user
            log.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = LogForm()

    pages = (Log.objects.all().count()//20)+1
    pages_list = []
    for i in range(pages):
        pages_list.append(i+1)

    latest_log_list = Log.objects.order_by('-publication_date')[((page-1)*20):(page*20)]
    context = {'latest_log_list': latest_log_list,
               'pages_list':pages_list}
    return render(request, 'changeLog/changeLog.html', context)

