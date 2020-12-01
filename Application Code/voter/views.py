from django.contrib import messages
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from numpy.lib.function_base import hamming
from .models import ElectionStatus
from common.decorator import election_is_active, result_declared
from candi_register.models import Candidate

# Create your views here.
def homepage(request):
    context = None
    request.session['user_is_active'] = 1
    try:
        if ElectionStatus.objects.all()[0].result_declared:
            context = {
                'show_result_tab' : True,
            } 
    except:
        pass       
    return render(request, 'voter/index.html', context)

@election_is_active # we will see this vote page only if we have any active elction
@login_required # user can see this view only if he is logged in 
def vote(request):
    if request.session['user_is_active']:
        # if user hasn't voted till now
        candi = Candidate.objects.all()
        candidate = {}
        POSITION = {
                'Vice President',
                'General Secretary',
                'Literary Secretary',
                'Cultural Secretary',
                'Sports Secretary',
                'Girls Mess Secretary',
                'Boys Mess Secretary'
            }
        for position in POSITION:
            candidate[position] = candi.filter(position=position)
        context = {'show_result_tab':False, 'all_candidates':candidate, 'register_input':True} #list of all candidate
    else: #if user has voted
        context = {'response':'Thank You For Your Vote', 'show_result_tab':False, 'register_input':False}
    return render(request, 'voter/vote.html', context)

# No new link for result, it will be shown in vote page only
# @election_is_active
# @result_declared # if result is declared then add result tab in vote page {redirect to voter:result}
# def result(request):
#     context = {
#         'show_result_tab' : True,
#         'result':'Result will be shown here'
#     }
#     return render(request, 'voter/result.html', context)

@login_required
@election_is_active
def voted(request):
    user = User.objects.get(username=request.user)
    user.is_active=False
    user.save()
    request.session['user_is_active'] = 0
    cd = request.POST
    print(cd)
    POSITION = [
            'Vice',
            'General',
            'Literary',
            'Cultural',
            'Sports',
            'Girls',
            'Boys'
        ]
    for name in POSITION:
        try:
            opted_candidate = Candidate.objects.get(regno=cd[name])  
            opted_candidate.result += 1
            opted_candidate.save()
        except:
            pass
    return HttpResponseRedirect(reverse('voter:vote'))