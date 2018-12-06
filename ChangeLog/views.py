from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Log, ChangeLog, MyUser
from .forms import LogForm, CreateChangelogForm, InviteToChangelogForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, View
from django.urls import reverse_lazy, reverse


class LogCreate(CreateView):
    template_name = 'ChangeLog/changelog.html'
    def post(self, request, name):
        form = LogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.changeLog = ChangeLog.objects.get(nazwa__exact=name)
            instance.save()
            return HttpResponseRedirect(request.path_info)

    def get(self, request, name):
        form = LogForm()
        pages = (Log.objects.all().count() // 20) + 1
        pages_list = []
        for i in range(pages):
            pages_list.append(i + 1)
        latest_log_list = Log.objects.filter(changeLog__nazwa=name).order_by('-publication_date')[:20]
        context = {'latest_log_list': latest_log_list,
                   'pages_list': pages_list}
        return render(request, 'changeLog/changeLog.html', context)


class ChangelogCreate(CreateView):
    template_name = 'ChangeLog/changelog_form.html'
    success_url = reverse_lazy('changeLog:changelogSettings')

    def post(self, request):
        form = CreateChangelogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            nazwa=form.cleaned_data['nazwa']
            changelog = ChangeLog.objects.get(nazwa=nazwa)
            changelog.users.add(request.user)
            return redirect(reverse('changeLog:changelogSettings', kwargs={'name': nazwa}))

    def get(self, request):
        form = CreateChangelogForm()
        return render(request, 'ChangeLog/changelog_form.html', {'form': form})


class ChangelogSettings(View):
    template_name = 'ChangeLog/changelogSettings.html'

    def post(self, request, name):
        form = InviteToChangelogForm(request.POST)
        if form.is_valid():
            user = MyUser.objects.get(username=form.cleaned_data['username'])
            changelog = ChangeLog.objects.get(nazwa=name)
            changelog.users.add(user)

        return HttpResponseRedirect(request.path_info)

    def get(self, request, name):
        form = InviteToChangelogForm()
        users_list = ChangeLog.objects.get(nazwa=name).users.all()
        return render(request, 'ChangeLog/changelogSettings.html', {'form': form, 'users_list': users_list})

