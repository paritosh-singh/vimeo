from django.shortcuts import render_to_response
from django.template import RequestContext

from models import User

# This view is triggered on root path
def home(request):
    context = _search_users(request)
    return render_to_response("search/home.html", context, RequestContext(request))
# This view is triggered on ajax call
def ajax(request):
    context = _search_users(request)
    return render_to_response("search/results.html", context, RequestContext(request))

# This method takes input as request object
# and returns hash of users, count and search_term
# for searched users
def _search_users(request):
    search_term = request.GET.get("search", None)
    staff_pick = request.GET.get("staffpick", None)
    uploaded = request.GET.get("uploaded", None)
    paying = request.GET.get("paying", None)
    count = 0
    users = []
    if search_term:
        users = User.objects.filter(name__icontains=search_term)
        if staff_pick: users = users.filter(staffpick = True)
        if uploaded: users = users.filter(uploaded = True)
        if paying: users = users.filter(paying=True)
        count = users.count()
    users = users[:100]
    return dict(users=users, count=count, search_term=search_term)