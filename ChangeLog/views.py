from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm


def changelog(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            e_text = form.cleaned_data['event_text']
            event = Event()
            event.event_text = e_text
            event.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = EventForm()

    pages = (Event.objects.all().count()//20)+1
    pages_list = []
    for i in range(pages):
        pages_list.append(i+1)

    latest_event_list = Event.objects.order_by('-publication_date')[:20]
    context = {'latest_event_list': latest_event_list,
               'pages_list':pages_list}
    return render(request, 'changeLog/changeLog.html', context)


def changelogwithpage(request, page):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            e_text = form.cleaned_data['event_text']
            event = Event()
            event.event_text = e_text
            event.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = EventForm()

    pages = (Event.objects.all().count()//20)+1
    pages_list = []
    for i in range(pages):
        pages_list.append(i+1)

    latest_event_list = Event.objects.order_by('-publication_date')[((page-1)*20):(page*20)]
    context = {'latest_event_list': latest_event_list,
               'pages_list':pages_list}
    return render(request, 'changeLog/changeLog.html', context)

