from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import River, Sensor, Reading
from .forms import Leitura
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    rivers = River.objects.all()
    return render(request, 'rios/post_list.html', {'rivers': rivers})

def description(request, pk):
	river = River.objects.get(pk=pk)
	sensors = river.sensor_set.all()
	return render(request, 'rios/description.html', {'river': river, 'sensors': sensors}) #Contexto do Sensor, como fazer?

@csrf_exempt
def new_reading(request):
		print('request received')
		print(request.POST.get('device'))
		print(request.POST.get('password'))
		print(request.POST.get('id'))
		print(request.POST.get('sensor_read'))
		user = authenticate(username=request.POST.get('device'), password=request.POST.get('password'))
		if user is not None:
			Nova_Leitura = Sensor.objects.get(pk=request.POST.get('id')) #pk = ID do sensor ---> Sensor de PH = 2.
			Nova_Leitura.reading_set.create(sensor_read=request.POST.get('sensor_read')) # sensor_read = leitura do sensor
			Nova_Leitura.save()
			return HttpResponse('Usuario Logado')
		else:
			return HttpResponse('Usuario Não Logado')

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/new')
	return render(request, 'rios/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')