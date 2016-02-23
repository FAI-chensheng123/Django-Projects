
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


from products.models import ProductFeatured, Product
from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.

def home(request):
	title = "Sign Up Now"

	featured_image = ProductFeatured.objects.first()
	products = Product.objects.all()


	form = SignUpForm(request.POST or None)
	
	context = {
		"title": title,
		"form": form,
		"featured_image": featured_image,
		"products": products
	}

	

	if form.is_valid():
		
		#form.save()

		instance = form.save(commit = False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name

		# if not instance.full_name:
		# 	instance.full_name = "Sheng"
		instance.save()
		context = {
			"title": "Thank you"
		}


	
	return render(request, "home.html", context)

def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():

		#method3 for print the items:
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value

		# method2 for print the items:
		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)

		# method1 for print the items:
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, 
		subject = 'Site contact form'
		from_email =  settings.EMAIL_HOST_USER
		to_email = [from_email, '402541920@qq.com']
		contact_message = "%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)

		send_mail(subject, contact_message, from_email, [to_email], fail_silently = True) 

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,

	}
	return render(request, "forms.html", context)










