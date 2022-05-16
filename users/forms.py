from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.core import validators
from users.models import *

def email_abes_check(value):
	if "@abes.ac.in" not in value:
		raise ValidationError("Email does not belongs to ABESEC")


BRANCHES = (
		('CSE','CSE'),
		('CS','CS'),
		('IT','IT'),
		('ME','ME'),
		('ECE','ECE'),
		('CSML','CSML'),
		('CSDS','CSDS'),
	)
YEAR = (
		(1,1),
		(2,2),
		(3,3),
		(4,4),

	)

class SingupForm(forms.Form):
	email = forms.EmailField(required=True,validators=[email_abes_check],widget=forms.TextInput(attrs={'class':'input','placeholder':'example@abes.ac.in'}))
	name = forms.CharField(max_length=100,required=True,)
	year = forms.ChoiceField(choices=YEAR,required=True,)
	phone = forms.CharField(max_length=10,required=True,)
	addmision_number = forms.CharField(max_length=100,required=True,)
	branch = forms.ChoiceField(choices=BRANCHES,required=True)
	password = forms.CharField(max_length=200,widget=forms.PasswordInput,required=True)
	confirm_password = forms.CharField(max_length=255,label="Confirm Password",widget=forms.PasswordInput)

	name.widget.attrs.update({'class':'input','placeholder':'John Doe'})
	year.widget.attrs.update({'class':'input'})
	phone.widget.attrs.update({'class':'input','placeholder':'0000000000'})
	addmision_number.widget.attrs.update({'class':'input','placeholder':'Addmision Number'})
	branch.widget.attrs.update({'class':'input'})
	password.widget.attrs.update({'class':'input'})
	confirm_password.widget.attrs.update({'class':'input'})


	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email already used")
		else:
			return email

	def clean_addminsion_number(self):
		addminsion_number = self.cleaned_data['addminsion_number']
		if Profile.objects.filter(addminsion_number=addminsion_number).exists():
			raise ValidationError("addminsion_number alredy taken")
		else:
			return addminsion_number

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password)<=5:
			raise ValidationError("Length must be more then 5 characters")
		else:
			return password

	def clean_year(self):
		year = self.cleaned_data['year']
		if int(year)>4:
			raise ValidationError("Invalid year")
		else:
			return year

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		if not phone.isdigit():
			raise ValidationError("Phone number has to be a numeric string")
		elif  len(phone)!=10:
			raise ValidationError("Phone number has to be of 10 digits")
		elif Profile.objects.filter(phone=phone).exists():
			raise ValidationError("Phone number alredy taken")
		else:
			return phone


class SigninForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True,widget=forms.PasswordInput)

	email.widget.attrs.update({'class':'input','id':'email','placeholder':'name.admission@abes.ac.in'})
	password.widget.attrs.update({'class':'input','placeholder':'********'})

