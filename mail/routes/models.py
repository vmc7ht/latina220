from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator
from decimal import Decimal
# Create your models here.


class Route(models.Model):

	Zone_Choices = (
		('20109', '20109'),
		('20110', '20110'),
	)
	route_id = models.AutoField(primary_key=True, editable=False)
	route_number = models.IntegerField(blank=False, null=True, verbose_name='Route Number')
	route_ns = models.CharField(max_length=30, blank=True, null=True, verbose_name='Route NS (YYYY-MM-DD)')
	route_carrier_first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='First Name')
	route_carrier_last_name = models.CharField(max_length=30, blank=False, null=True, verbose_name='Last Name')
	route_zone = models.CharField(max_length=30, blank=False, null=True, choices=Zone_Choices, default=None,verbose_name='Route Zone')
	current_route_ns = models.IntegerField(blank=True, null=True, default=-1,verbose_name='Current Route NS')

	T6_id = models.IntegerField(blank=False, null=True, verbose_name='T6 id')
	T6_type = models.CharField(max_length=30, blank=False, null=True,default="T-6", verbose_name='T6 Type')
	T6_carrier_zone = models.CharField(max_length=30, blank=False, null=True, choices=Zone_Choices, default=None,verbose_name='T6 Zone')
	T6_carrier_last_name = models.CharField(max_length=30, blank=False, null=True, verbose_name='Last Name')
	
class Override(models.Model):
	route = models.ForeignKey("routes.Route",on_delete=models.CASCADE,related_name ='override')
	date = models.DateField(blank=True, null=True, verbose_name='Date(YYYY-MM-DD)')
	text = models.CharField(max_length=10, blank=True, null=True, verbose_name='text')

class Override_T6(models.Model):
	route = models.ForeignKey("routes.Route",on_delete=models.CASCADE,related_name ='overrideT6')
	date = models.DateField(blank=True, null=True, verbose_name='Date(YYYY-MM-DD)')
	text = models.CharField(max_length=10, blank=True, null=True, verbose_name='text')
