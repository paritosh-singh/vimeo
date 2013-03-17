from parser.vimeo_user import VimeoUser, VimeoUsers
from django.conf import settings
from vimeo_assignment.models import User

## method crawl the data from vimeo api
#  and stores it to database
def get_vimeo_users():
    count = 0
    print "===========Collecting required users================\n"
    all_users = VimeoUsers([])
    all_users.get_required_user_ids(settings.USERS_LIMIT)
    user_ids = all_users.user_ids
    print "===========Collected required users=================\n\n"
    for id in user_ids:
        user = VimeoUser(id)
        if not user.blank_user:
            vimeo_user, new_user = User.objects.get_or_create(vimeo_id=user.id)
            if new_user:
                count = count + 1
                print "===========Creating new user#%s %s=========\n"%(count, user.display_name)
                try:
                    vimeo_user.name = user.display_name
                    vimeo_user.username = user.username
                    vimeo_user.url = user.vimeo_url
                    vimeo_user.paying = user.is_paying
                    vimeo_user.staffpic = user.is_staff
                    vimeo_user.uploaded = user.has_uploaded
                    vimeo_user.save()
                    print "===========Created user#%s %s=========\n\n"%(count, user.display_name)
                except:
                    print "===========Error occured while created user#%s %s=========\n\n"%(count, user.display_name)
                    count = count -1
            all_users.append(user)
