from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Player
import requests

# Create your views here.


def index(request):

    if request.method == 'POST':
        p1name = request.POST.get('p1')
        p2name = request.POST.get('p2')
        rno = request.POST.get('r1')

        # r = requests.post('http://app.credenz.info/retrive/getKey.php', json={"uniKey": rno}).json()
        r = {"uniKey":"CRED18-165-PIZ","name":"sumit pramod Badase","email":"badasumit29@gmail.com","Clash":"1","Reverse_Coding":"1"}
        print(r['uniKey'])

        if r != -1:
            robj = Player.objects.filter(receiptno=rno)
            print(robj)

            if robj in '<QuerySet []>':
                user = User.objects.create_user(username=p1name, password='clash')

                d = Player.objects.create(pid=user, p1name=p1name, p1email=r['email'], p2name=p2name, receiptno=rno,
                                          clash=r['Clash'], rc=r['Reverse_Coding'])
                d.save()
                return HttpResponse("<h1>Login Successfull</h1>")
            elif robj.booked:
                    val = True
                    return render(request, 'Login.html', {'val': val})
            else:
                return HttpResponse("<h1>You still have to book a slot</h1>")



    else:
        val = False
        context = {'val': val}
        return render(request, 'Login.html', context)
