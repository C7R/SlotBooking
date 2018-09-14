from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import *
import requests

# Create your views here.


def index(request):

    if request.method == 'POST':
        p1name = request.POST['p1']
        p2name = request.POST['p2']
        rno = request.POST['r1']
        c1 = rno.split('-')
        print(c1[0])
        if c1[0] != 'CRED18':
            val = 0
            return render(request, 'Login.html', {'val': val})
        print(rno)
        r = requests.post('http://app.credenz.info/retrive/getKey.php', data={"uniKey": rno}).json()
        # r = requests.post('http://192.168.43.154/app/getKey.php', json={"uniKey": rno}).json()

        #r = {"uniKey":"CRED18-165-PIZ","name":"sumit pramod Badase","email":"badasumit29@gmail.com","Clash":"1","Reverse_Coding":"1"}
        print(r)
        print()
        if r['uniKey'] != "-1":
            robj = Player.objects.filter(receiptno=rno).first()
            print(robj)

            if robj is None:
                user = User.objects.create_user(username=p1name, password='clash', email="asd@w.com")

                d = Player.objects.create(pid=user, p1name=p1name, p1email=r['email'], p2name=p2name, receiptno=rno,
                                          clash=int(r['Clash']), rc=int(r['Reverse_Coding']))
                d.save()

                #u2 = authenticate(request, username=p1name, password='Clash@123')

                login(request, user,  backend='django.contrib.auth.backends.ModelBackend')

                ob = user.player
                #slots = SlotCapacity.objects.all()

                context = {'clash ': ob.clash, 'rc': ob.rc}

                print("here")
                return slotpage(request)

            else:
                pobj = Player.objects.get(receiptno=rno)
                login(request, pobj.pid)

                if pobj.booked:
                    val = 1
                    logout(request)
                    return render(request, 'Login.html', {'val': val})
                else:
                    context = {'clash ': pobj.clash, 'rc': pobj.rc}
                    return slotpage(request)
        else:
            val = 0
            context = {'val': val}
            return render(request, 'Login.html', context)
    else:
        if request.user.is_authenticated:
            pobj = request.user.player
            if pobj.booked:
                    val = 1
                    return render(request, 'Login.html', {'val': val})
            context = {'clash ': pobj.clash, 'rc': pobj.rc}
            return slotpage(request)
        val = 3
        context = {'val': val}
        return render(request, 'Login.html',context)


def slotpage(request):
    clash = request.user.player.clash
    rc = request.user.player.rc
    print(clash)
    slot = Slot.objects.all()
    context = {
        'clash': intTOBool(clash),
        'rc': intTOBool(rc),
        'slot': slot
    }
    return render(request, "ss.html", context)


def getSlotInput(request):

    if request.method == 'POST' and request.user.is_authenticated:

        clash = request.user.player.clash
        rc = request.user.player.rc
        print("rc")
        print(rc)
        clashslot = None
        rcslot = None

        if clash == 1:
            clashslot  = request.POST['clash']
            slot = Slot.objects.get(id=clashslot)
            slot.count = slot.count - 1
            slot.save()
            u = request.user.player
            u.cslot = slot
            u.booked = True
            u.save()


        if rc == 1:
            rcslot = request.POST['rc']
            print(rcslot)
            slot = Slot.objects.get(id=rcslot)
            slot.count = slot.count - 1
            slot.save()
            u = request.user.player
            u.rslot = slot
            u.booked = True
            u.save()


        return logoutr(request)


            #return render(request, "ss.html", context)

    else:

        return render(request, 'Login.html')


def logoutr(request):

    logout(request)
    return render(request, "thnaks.html")
    # return HttpResponse("""<!doctype html>
# <title>Site Maintenance</title>
# <style>
#   body { text-align: center; padding: 150px; }
#   h1 { font-size: 50px; }
#   body { font: 20px Helvetica, sans-serif; color: #333; }
#   article { display: block; text-align: left; width: 650px; margin: 0 auto; }
#   a { color: #dc8100; text-decoration: none; }
#   a:hover { color: #333; text-decoration: none; }
# </style>

# <article>
#     <h1>See You At Credenz&r18</h1>
#     <div>
#         <p>Thanks For Booking Slot . If you need to you can always <a href="mailto:pisb.credenz@gmail.com">contact us</a></p>
#         <p>&mdash; The Team</p>
#     </div>
# </article>""")

def intTOBool(a):
    if a == 1:
        return True
    else :
        return False