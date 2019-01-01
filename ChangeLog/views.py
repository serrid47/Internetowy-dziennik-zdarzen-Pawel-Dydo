from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Log, ChangeLog, MyUser, UserInChangelog
from .forms import LogForm, CreateChangelogForm, InviteToChangelogForm, UserInChangelogForm, LogSearchForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, View, ListView
from django.urls import reverse_lazy, reverse
from .functions import check_permission, check_if_user_in_changelog
from django.template.loader import render_to_string


class LogCreate(View):
    template_name = 'changelog/changelog.html'
    def post(self, request, name, page=1):
        form_add = LogForm(request.POST)
        form_search = LogSearchForm(request.POST)
        if form_add.is_valid():
            if (check_permission('w', name, request.user)):
                instance = form_add.save(commit=False)
                user_in = UserInChangelog.objects.get(user_id=request.user, changeLog__nazwa=name)
                instance.user_changelog = user_in
                instance.save()
                return HttpResponseRedirect(request.path_info)
            else:
                return render(request, 'changelog/access_denied.html')

        if form_search.is_valid():
            if (check_permission('r', name, request.user)):
                search_text = form_search.cleaned_data['search_text']
                return redirect(reverse('changeLog:logSearch', kwargs={'name': name, 'search_text': search_text}))
            else:
                return render(request, 'changelog/access_denied.html')

    def get(self, request, name, page=1):
        if (check_permission('r', name, request.user)):
            form_add = LogForm()
            form_search = LogSearchForm()
            pages = (Log.objects.filter(user_changelog__changeLog__nazwa=name).count() // 10) + 1
            pages_list = []
            for i in range(pages):
                pages_list.append(i + 1)
            latest_log_list = Log.objects.filter(user_changelog__changeLog__nazwa=name).order_by('-publication_date')[(page-1)*10:page*10]
            write_perm = check_permission('w', name, request.user)
            edit_perm = check_permission('x', name, request.user)
            admin_perm = check_permission('a', name, request.user)

            context = {'latest_log_list': latest_log_list,
                       'pages_list': pages_list,
                       'form_add': form_add,
                       'form_search': form_search,
                       'name': name,
                       'write_perm': write_perm,
                       'edit_perm': edit_perm,
                       'admin_perm': admin_perm
                       }
            return render(request, 'changelog/changeLog.html', context)
        else:
            return render(request, 'changelog/access_denied.html')


class LogSearch(View):
    template_name = 'changelog/changeLogSearch.html'

    def get(self, request, name, search_text, page=1):
        if (check_permission('r', name, request.user)):
            form_search = LogSearchForm()
            search_results = Log.objects.filter(user_changelog__changeLog__nazwa=name)\
                .filter(log_text__contains=search_text)
            search_results_page = Log.objects.filter(user_changelog__changeLog__nazwa=name)\
                .filter(log_text__contains=search_text).order_by('-publication_date')[(page - 1) * 10:page * 10]
            pages = (search_results.count() // 10) + 1
            pages_list = []
            for i in range(pages):
                pages_list.append(i + 1)

            context = {'search_results': search_results_page,
                       'pages_list': pages_list,
                       'form_search': form_search,
                       'name': name,
                       'search_text': search_text}
            return render(request, 'changelog/changeLogSearch.html', context)
        else:
            return render(request, 'changelog/access_denied.html')


class ChangelogCreate(CreateView):
    template_name = 'changelog/changelog_form.html'
    success_url = reverse_lazy('changeLog:changelogSettings')

    def post(self, request):
        form = CreateChangelogForm(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['nazwa']
            if(ChangeLog.objects.filter(nazwa=nazwa).count()<1):
                instance = form.save(commit=False)
                instance.save()
                user_in = UserInChangelog()
                user_in.user = request.user
                user_in.changeLog = instance
                user_in.permission = 'rwixad'
                user_in.save()
                return redirect(reverse('changeLog:changelogSettings', kwargs={'name': nazwa}))

        return render(request, 'changelog/changelog_form.html', {'form': form, 'alert': 'Dziennik z taką nazwą już istnieje'})

    def get(self, request):
        form = CreateChangelogForm()
        return render(request, 'changelog/changelog_form.html', {'form': form})


class ChangelogSettings(View):
    template_name = 'changelog/changelogSettings.html'

    def post(self, request, name):
        form_invite = InviteToChangelogForm(request.POST)
        form_role = UserInChangelogForm(request.POST)

        if form_invite.is_valid():
            if (check_permission('i', name, request.user)):
                user = MyUser.objects.get(username=form_invite.cleaned_data['username'])
                users = UserInChangelog.objects.filter(changeLog__nazwa=name, user_id=user.pk)
                if(users.count()<1):
                    changelog = ChangeLog.objects.get(nazwa=name)
                    user_in = UserInChangelog()
                    user_in.user = user
                    user_in.changeLog = changelog
                    user_in.save()

        if form_role.is_valid():
            if (check_permission('a', name, request.user)):
                user = form_role.cleaned_data['user']
                permission = form_role.cleaned_data['permission']
                user_in = UserInChangelog.objects.filter(changeLog__nazwa=name).get(user__username=user)
                user_in.permission = permission
                user_in.save()

        return HttpResponseRedirect(request.path_info)

    def get(self, request, name):
        if (check_permission('r', name, request.user)):
            form_invite = InviteToChangelogForm()
            users_list = UserInChangelog.objects.filter(changeLog__nazwa=name)
            form_role = UserInChangelogForm()
            form_role.fields["user"].queryset = MyUser.objects.filter(userinchangelog__changeLog__nazwa=name)
            admin = check_permission('a', name, request.user)
            invite = check_permission('i', name, request.user)
            return render(request, 'changelog/changelogSettings.html', {'form_invite': form_invite, 'form_role': form_role,
                                                                        'users_list': users_list, 'admin': admin, 'invite': invite, 'name': name})
        else:
            return render(request, 'changelog/access_denied.html')



def LogUpdate(request, name):
    if request.is_ajax():
        log_id = request.POST['log_id']
        log = Log.objects.get(id=log_id)
        html = render_to_string('changelog/logUpdate.html', {'log': log})
        return HttpResponse(html)


def LogSave(request, name):
    if request.is_ajax():
        log_id = request.POST['log_id']
        log = Log.objects.get(id=log_id)
        log_text = request.POST['log_text']
        log.log_text=log_text
        log.save()
        html = render_to_string('changelog/logSave.html', {'log': log})
        return HttpResponse(html)


class Changelogs(ListView):
    template_name = 'changelog/changelogs.html'
    model = ChangeLog


    def get_queryset(self):
        queryset = ChangeLog.objects.filter(userinchangelog__user= self.request.user)
        return queryset




