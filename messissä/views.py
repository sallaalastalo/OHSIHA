from django.shortcuts import render, redirect
from datetime import datetime
import requests
from .models import Tapahtuma
from .forms import TapahtumaForm
    
def list_events(request):
        tapahtuma = Tapahtuma.objects.all()
        if requests.get('https://visittampere.fi:443/api/v1/event?tag=sport&start_datetime=1554448073000').status_code==200:
                
                response = requests.get('https://visittampere.fi:443/api/v1/event?tag=sport&start_datetime=1554448073000')
        
                print(response.status_code)
        
                eventdata = response.json()

                for events in eventdata:
                        if events['start_datetime'] != None:
                                events['pvm'] = datetime.fromtimestamp(events['start_datetime']/1000)

                return render(request, 'tapahtuma.html',{'event_list': eventdata, 'tapahtuma': tapahtuma})

def vusalisoi(requests):
        if requests.get('https://visittampere.fi:443/api/v1/event?start_datetime=1554210010&offset=1554210010').status_code==200:
                
                response = requests.get('https://visittampere.fi:443/api/v1/event?start_datetime=1554123610&offset=1554123610')
        
                print(response.status_code)
        
                eventdata = response.json()
                
                i = 0

                for events in eventdata:
                        if events['start_datetime']>=1546300918000:
                                if events['start_datetime'] <1577836798000:
                                        i += 1
                                        print(i)
                tag['music'] = i
                i = 0 
                print(tag)

        return render(request, 'tapahtuma.html', {'event_list' : eventdata})

def create_event(request):
        form = TapahtumaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('list_events')
        return render(request, 'tapahtuma-form.html',{'form':form})

def update_event(request, id):
        tapahtuma = Tapahtuma.objects.get(id=id)
        form = TapahtumaForm(request.POST or None, instance = tapahtuma)

        if form.is_valid():
                form.save()
                return redirect('list_events')
        return render(request, 'tapahtuma-form.html', {'form':form,'tapahtuma':tapahtuma})

def delete_event(request, id):
        tapahtuma = Tapahtuma.objects.get(id=id)

        if request.method == 'POST':
                tapahtuma.delete()
                return redirect('list_events')
        return render(request, 'tapahtuma-delete-confirm.html',{'tapahtuma':tapahtuma})
