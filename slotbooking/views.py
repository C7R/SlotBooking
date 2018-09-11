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

        c1 = rno.split('-')
        print(c1[0])
        if c1[0] != 'CRED18':
            val = True
            return render(request, 'Login.html', {'val': val})

        r = requests.post('http://app.credenz.info/retrive/getKey.php', json={"uniKey": rno}).json()
        # r = requests.post('http://192.168.43.154/app/getKey.php', json={"uniKey": rno}).json()

        #r = {"uniKey":"CRED18-165-PIZ","name":"sumit pramod Badase","email":"badasumit29@gmail.com","Clash":"1","Reverse_Coding":"1"}
        print(r['uniKey'])

        if r['uniKey'] != -1:
            robj = Player.objects.filter(receiptno=rno)
            print(robj)

            if not robj :
                user = User.objects.create_user(username=p1name, password='clash')

                d = Player.objects.create(pid=user, p1name=p1name, p1email=r['email'], p2name=p2name, receiptno=rno,
                                          clash=r['Clash'], rc=r['Reverse_Coding'])
                d.save()

                u2 = authenticate(request, username=p1name, password='clash')

                login(request, u2)

                ob = user.player
                context = {'clash ': ob.clash, 'rc': ob.rc}
                return render(request,'Slotselection.html', context)
            else:
                user = request.user
                pobj = user.Player
                if pobj.booked:
                    val = True
                    return render(request, 'Login.html', {'val': val})
                else:
                    context = {'clash ': pobj.clash, 'rc': pobj.rc}
                    return render(request, 'Slotselection.html', context)
        else:
            val = True
            context = {'val': val}
            return render(request, 'Login.html', context)
    else:
        return render(request, 'Login.html')


def books(requst):
    if requst.method == 'POST':
        pass