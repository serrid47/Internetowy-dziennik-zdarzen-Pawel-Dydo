from .models import UserInChangelog

def check_if_letter_in_string(x, str):
    for letter in str:
        if(x==letter):
            return True
    return False


def check_permission(permission, changelog, user):
    return check_if_letter_in_string(permission, UserInChangelog.objects.filter(changeLog__nazwa=changelog).get(user=user).permission)


def check_if_user_in_changelog(changelog, user):
    if (UserInChangelog.objects.filter(changeLog__nazwa=changelog).filter(user=user).count()):
        return True
    else:
        return False


