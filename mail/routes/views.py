#  Create your views here.
from django.views.generic.detail import DetailView
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from routes.models import Route
from routes.models import Override
from routes.models import Override_T6
from routes.forms import RouteModelForm
from django.http import JsonResponse
from datetime import date
from datetime import datetime
from datetime import timedelta
import holidays
from django.db.models import F
def homeView(request):
    return render(request, 'home.html')
    # return render(request,'home.html')

def dashboardView(request,week): # Dashboard view rn redirect('login_url')
	#monday 0, tues 1, wed 2, thur 3, fri 4, sat 5, sun 6
	url = request.build_absolute_uri().split('/')
	zone = url[len(url)-2] #get zone users requested
	week = int(url[len(url)-1]) #get week users requested
	find_ns_this_week(week,Route.objects.all()) #find ns this week for every route 
	partial_date_week = get_days_for_week(week,"%-d-%b")
	full_date_week = get_days_for_week(week,"%Y-%-m-%-d")
	holiday_this_week = find_holiday_this_week(week)
	routes = Route.objects.filter(route_zone=zone).order_by('route_number')
	routes = regular_list(routes,full_date_week[0],full_date_week[-1])
	T6 = Route.objects.filter(T6_carrier_zone=zone).order_by('T6_id')
	T6 = t6_list(T6,full_date_week[0],full_date_week[-1])
	return render(request, 'weekly.html',{'routes': routes,'T6':T6,'regular_size': len(routes),
		'partial_date_week':partial_date_week,'full_date_week':full_date_week,'holiday_this_week':holiday_this_week})

def find_ns_this_week(week,routes):#find ns for current week and updates the model for it 
	d1 = date.today() + timedelta(days=7*week)
	while(d1.weekday()!=5):
		d1 = d1 + timedelta(-1)
	for route in routes:
		if (route.route_ns == "-1"):
			Route.objects.filter(pk=route.route_id).update(current_route_ns=-1)
		else:
			d0 = route.route_ns.split("-")
			d0 = date(int(d0[0]),int(d0[1]),int(d0[2]))
			d0Sat = d0
			while(d0Sat.weekday()!=5):
				d0Sat = d0Sat + timedelta(-1) 
			diff = ((d1 - d0Sat)//7).days
			this_week_ns = d0.weekday()
			if (diff < 0 ):
				diff = diff*-1
				for x in range(diff):
					this_week_ns -= 1
					if this_week_ns==-1 : this_week_ns=5
			else:
				for x in range(diff):
					this_week_ns += 1
					if this_week_ns>=6 : this_week_ns=0
			Route.objects.filter(pk=route.route_id).update(current_route_ns=this_week_ns)


def get_days_for_week(week,format): #get days for the week
	d1 = date.today() + timedelta(days=7*week)
	days_of_week = []
	while(d1.weekday()!=5): 
		d1 = d1 + timedelta(-1)
	for x in range (7):
		days_of_week.append(d1.strftime(format))
		d1 = d1 + timedelta(1)		
	return days_of_week


def find_holiday_this_week(week):
	d1 = date.today() + timedelta(days=7*week)
	us_holidays = holidays.US() 
	while(d1.weekday()!=5):
		d1 = d1 + timedelta(-1)
	for x in range (6):
		if d1 in us_holidays :return d1.weekday()
		d1 = d1 + timedelta(1)
	return -1


def regular_list(regular,start,end):
	list_unique = [["" for col in range(10)] for row in range(len(regular))]
	start = start.split('-')
	start_date = date(int(start[0]), int(start[1]),int(start[2]))
	end = end.split('-')
	end_date = date(int(end[0]), int(end[1]),int(end[2]))
	override = Override.objects.filter(date__range=[start_date, end_date]).order_by('route__T6_id')
	for x in range(len(regular)):
		list_unique[x][regular[x].current_route_ns] = "NS"
		list_unique[x][6] = "NS"	
		list_unique[x][7] = regular[x].route_carrier_last_name
		list_unique[x][8] = regular[x].route_id	
		list_unique[x][9] = regular[x].route_number
		for y in override:
			if(y.route.route_id ==regular[x].route_id):	
				list_unique[x][y.date.weekday()] = y.text	
	return(list_unique)


def t6_list(T6,start,end):
	start = start.split('-')
	start_date = date(int(start[0]), int(start[1]),int(start[2]))
	end = end.split('-')
	end_date = date(int(end[0]), int(end[1]),int(end[2]))
	override = Override_T6.objects.filter(date__range=[start_date, end_date]).order_by('route__route_number')
	prev_id = T6[0].T6_id
	unique_T6 = 1
	for x in range(len(T6)): #find out how many unique t6 are there
		if (prev_id != T6[x].T6_id):
			prev_id = T6[x].T6_id	
			unique_T6 += 1
	list_unique = [["NS" for col in range(11)] for row in range(unique_T6)] 
	prev_id = T6[0].T6_id
	unique_T6 = 0
	list_unique[0][7] = T6[0].T6_carrier_last_name
	list_unique[0][8] = T6[0].route_id
	list_unique[0][9] = T6[0].T6_id
	list_unique[0][10] = T6[0].T6_type
	for x in range(len(T6)):
		if prev_id == T6[x].T6_id:list_unique[unique_T6][T6[x].current_route_ns] = T6[x].route_number
		if (prev_id != T6[x].T6_id):
			prev_id = T6[x].T6_id
			unique_T6 += 1
			list_unique[unique_T6][7] = T6[x].T6_carrier_last_name
			list_unique[unique_T6][8] = T6[x].route_id	
			list_unique[unique_T6][9] = T6[x].T6_id
			list_unique[unique_T6][10] = T6[x].T6_type
			list_unique[unique_T6][T6[x].current_route_ns] = T6[x].route_number
	for x in range(len(list_unique)):
		for y in override:
			if(list_unique[x][8]== y.route.route_id):	
				list_unique[x][y.date.weekday()] = y.text	
	return(list_unique)


class RouteCreate(CreateView):
	model = Route
	form_class= RouteModelForm
	template_name = 'employee_add.html'
	def form_valid(self, form):  #check if form is valid
		route = form.save(commit=False) #Get form but don't save yet. Make form changes below before saving 
		if self.request.POST.get('year') == None : route.route_ns = "-1"
		if (self.request.POST.get('year') != None):
			year = self.request.POST.get('year')
			month = self.request.POST.get('month')
			day = self.request.POST.get('day')
			date_string = year+"-"+month+"-"+day
			route.route_ns = date_string
		route.save() #finally save the form
		return HttpResponseRedirect(self.request.build_absolute_uri().replace('/employee_add', ''))


class RouteDelete(DeleteView):
	model = Route
	slug_field = 'route_id' #tells view to use application_id as the lookup field
	slug_url_kwarg = 'route_id' #tells view to use application_id as the lookup field
	template_name = 'delete_confirmation.html'
	def get_success_url(self):
		url = self.request.build_absolute_uri().split('/')
		string = "/"+url[len(url)-3]+"/"+url[len(url)-2]+"/"+url[len(url)-1]
		return self.request.build_absolute_uri().replace(string, '')


def deleteView(request,week):
	url_split = request.build_absolute_uri().split('/')
	zone = url_split[len(url_split)-3]
	week = url_split[len(url_split)-2]
	routes = Route.objects.filter(route_zone=zone).order_by('route_number')
	T6 = Route.objects.filter(T6_carrier_zone=zone).order_by('T6_id').exclude(T6_id=-1)
	T6 = t6_list(T6,"1990-01-01","1990-01-01")
	return render(request, 'employee_delete.html',{'routes': routes,'week':week,'zone':zone,'T6':T6})


class RouteEdit(UpdateView):
	model = Route
	slug_field = 'route_id' #tells view to use application_id as the lookup field
	form_class = RouteModelForm #pull up form
	slug_url_kwarg = 'route_id' #tells view to use application_id as the lookup field
	template_name = 'edit_page.html'
	def form_valid(self, form): #check if form is valid
		url = self.request.build_absolute_uri().split('/')
		string = "/"+url[len(url)-3]+"/"+url[len(url)-2]+"/"+url[len(url)-1]
		route = form.save(commit=False)   #Get form but don't save yet. Make form changes below before saving 
		if self.request.POST.get('year') == None : route.route_ns = "-1"
		if (self.request.POST.get('year') != None):
			year = self.request.POST.get('year')
			month = self.request.POST.get('month')
			day = self.request.POST.get('day')
			date_string = year+"-"+month+"-"+day
			route.route_ns = date_string
		route.save() #finally save the form
		return HttpResponseRedirect(self.request.build_absolute_uri().replace(string, ''))

def editView(request,week):
	url_split = request.build_absolute_uri().split('/')
	zone = url_split[len(url_split)-3]
	week = url_split[len(url_split)-2]
	routes = Route.objects.filter(route_zone=zone).order_by('route_number')
	T6 = Route.objects.filter(T6_carrier_zone=zone).order_by('T6_id')
	return render(request, 'employee_edit.html',{'routes': routes,'week':week,'zone':zone})


def update_name(request):
	name = request.GET.get('name', None)
	route_id = request.GET.get('route_id', None)	
	Route.objects.filter(pk=route_id).update(route_carrier_last_name=name)
	data = {
		'is_taken': Route.objects.filter(route_id=route_id).exists()
	}
	return JsonResponse(data)

def update_t6_type(request):
	name = request.GET.get('name', None)
	T6_id = request.GET.get('T6_id', None)	
	Route.objects.filter(T6_id=T6_id).update(T6_type=name)
	data = {
		'is_taken': Route.objects.filter(route_id=T6_id).exists()
	}
	return JsonResponse(data)


def update_t6_name(request):
	name = request.GET.get('name', None)
	T6_id = request.GET.get('T6_id', None)	
	Route.objects.filter(T6_id=T6_id).update(T6_carrier_last_name=name)
	data = {
		'is_taken': Route.objects.filter(route_id=T6_id).exists()
	}
	return JsonResponse(data)


def update_route_number(request):
	route_num = request.GET.get('route_num', None)
	route_id = request.GET.get('route_id', None)	
	Route.objects.filter(pk=route_id).update(route_number=route_num)
	data = {
		'is_taken': Route.objects.filter(route_id=route_id).exists()
	}
	return JsonResponse(data)


def update_override(request):
	override = request.GET.get('override', None)
	route_id = request.GET.get('route_id', None)
	date = request.GET.get('date', None)
	route = get_object_or_404(Route, pk=route_id)
	if not(Override.objects.filter(date=date).filter(route__route_id=route_id).exists()): #create new object since it doesn't exist
		Override.objects.create(route=route,text=override,date=date)
	else: #update the object
		Override.objects.filter(date=date).filter(route__route_id=route_id).update(text=override)
	data = {
		'is_taken': Route.objects.filter(route_id=route_id).exists()
	}
	return JsonResponse(data)

def update_t6_override(request):
	t6_override = request.GET.get('t6_override', None)
	route_id = request.GET.get('route_id', None)
	date = request.GET.get('date', None)
	route = get_object_or_404(Route, pk=route_id)
	if not(Override_T6.objects.filter(date=date).filter(route__route_id=route_id).exists()): #create new object since it doesn't exist
		Override_T6.objects.create(route=route,text=t6_override,date=date)
	else: #update the object
		Override_T6.objects.filter(date=date).filter(route__route_id=route_id).update(text=t6_override)
	data = {
		'is_taken': Route.objects.filter(route_id=route_id).exists()
	}
	return JsonResponse(data)

def delete_t6_view(request,week,name,t6id):
	url_split = request.build_absolute_uri().split('/')
	zone = url_split[len(url_split)-6]
	Route.objects.filter(T6_id=t6id).update(T6_id=-1)
	routes = Route.objects.filter(route_zone=zone).order_by('route_number')
	T6 = Route.objects.filter(T6_carrier_zone=zone).order_by('T6_id').exclude(T6_id=-1)
	T6 = t6_list(T6,"1990-01-01","1990-01-01")

	url_split = request.build_absolute_uri().split('/')
	zone = url_split[len(url_split)-3]
	week = url_split[len(url_split)-2]
	routes = Route.objects.filter(route_zone=zone).order_by('route_number')
	T6 = Route.objects.filter(T6_carrier_zone=zone).order_by('T6_id')
	return render(request, 'employee_edit.html',{'routes': routes,'week':week,'zone':zone})


