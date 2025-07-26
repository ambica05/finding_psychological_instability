
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Count,Subquery
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import finding_psychology_model,finding_psychological_instability_model,ClientRegister_Model,review_Model,recommend_Model,psychology_accuracy_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            psychology_accuracy_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = finding_psychological_instability_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=finding_psychological_instability_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_DataSets(request): # Search
    if request.method == "POST":
        kword = request.POST.get('keyword')
        obj = finding_psychological_instability_model.objects.all().filter( Q(names__contains=kword))
        return render(request, 'SProvider/Search_DataSets.html', {'objs': obj})
    return render(request, 'SProvider/Search_DataSets.html')

def Predict_Psychological_Instability(request): # Using SVM
    se = ''

    obj1 = finding_psychological_instability_model.objects.values(
'names',
'age',
'gender',
'country',
'state',
'self_employeed',
'family_history',
'treatment',
'work_interferes',
'No_of_employees',
'remote_network',
'technical_company',
'benefits',
'care_options',
'welness_program',
'seek_help',
'anonymity',
'leave1',
'mental_health_consequence',
'physical_health_consequence',
'co_workers',
'supervisor',
'mental_health_interview',
'physical_health_interview',
'mental_health',
'obs_consequence',
'Remarks_or_comments',
'dislikes',
'likes')

    finding_psychology_model.objects.all().delete()
    for t in obj1:

        names=t['names']
        age=t['age']
        gender=t['gender']
        country=t['country']
        state=t['state']
        self_employeed=t['self_employeed']
        family_history=t['family_history']
        treatment=t['treatment']
        work_interferes=t['work_interferes']
        No_of_employees=t['No_of_employees']
        remote_network=t['remote_network']
        technical_company=t['technical_company']
        benefits=t['benefits']
        care_options=t['care_options']
        welness_program=t['welness_program']
        seek_help=t['seek_help']
        anonymity=t['anonymity']
        leave=t['leave1']
        mental_health_consequence=t['mental_health_consequence']
        physical_health_consequence=t['physical_health_consequence']
        co_workers=t['co_workers']
        supervisor=t['supervisor']
        mental_health_interview=t['mental_health_interview']
        physical_health_interview=t['physical_health_interview']
        mental_health=t['mental_health']
        obs_consequence=t['obs_consequence']
        Remarks_or_comments=t['Remarks_or_comments']
        dislikes=t['dislikes']
        likes=t['likes']

        for f in Remarks_or_comments.split():
            if f in ('hopelessness','disheartened','miserable','depressed'):
                se = 'Depressed'
            elif f in ('tension','strain','worry','stress','pressure','anxiety','sad'):
                se = 'Stress'
            elif f in ('enjoy'):
                se = 'Positive'


        finding_psychology_model.objects.create(names=names,age=age,gender=gender,country=country,state=state,self_employeed=self_employeed,
                                                family_history=family_history,
                                                treatment=treatment,
                                                work_interferes=work_interferes,
                                                No_of_employees=No_of_employees,
                                                remote_network=remote_network,
                                                technical_company=technical_company,
                                                benefits=benefits,
                                                care_options=care_options,
                                                welness_program=welness_program,
                                                seek_help=seek_help,
                                                anonymity=anonymity,
                                                leave1=leave,
                                                mental_health_consequence=mental_health_consequence,
                                                physical_health_consequence=physical_health_consequence,
                                                co_workers=co_workers,
                                                supervisor=supervisor,
                                                mental_health_interview=mental_health_interview,
                                                physical_health_interview=physical_health_interview,
                                                mental_health=mental_health,
                                                obs_consequence=obs_consequence,
                                                Remarks_or_comments=Remarks_or_comments,
                                                dislikes=dislikes,
                                                likes=likes,
                                                psycho_type=se)

    obj = finding_psychology_model.objects.all()

    return render(request, 'SProvider/Predict_Psychological_Instability.html', {'objs': obj})


def View_Depressed(request): # Positive # Using SVM
    atype = 'Depressed'
    f1 = 'Depressed'

    obj = finding_psychology_model.objects.all().filter(Q(psycho_type=f1) )
    obj1 = finding_psychology_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1
    if accuracy != 0:
        psychology_accuracy_model.objects.create(names=atype,accuracy=accuracy)
    return render(request, 'SProvider/View_Depressed.html', {'objs': obj,'count':accuracy})


def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = finding_psychological_instability_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = finding_psychological_instability_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = finding_psychological_instability_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def charts(request,chart_type):
    chart1 = psychology_accuracy_model.objects.values('names').annotate(dcount=Avg('accuracy'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def View_psychologyDataSets_Details(request):
    obj = finding_psychological_instability_model.objects.all()
    return render(request, 'SProvider/View_psychologyDataSets_Details.html', {'list_objects': obj})

def View_Stressed(request):
    atype = 'Stressed'
    f1 = 'Stress'

    obj = finding_psychology_model.objects.all().filter(psycho_type__contains=f1)
    obj1 = finding_psychological_instability_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1
    if accuracy != 0:
        psychology_accuracy_model.objects.create(names=atype, accuracy=accuracy)
    return render(request, 'SProvider/View_Stressed.html', {'objs': obj,'count':accuracy})

def likeschart(request,like_chart):
    charts = finding_psychological_instability_model.objects.values('names').annotate(dcount=Avg('likes'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})
