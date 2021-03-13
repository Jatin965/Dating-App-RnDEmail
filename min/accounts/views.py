# from django.shortcuts import render

# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from .forms import SignUpForm
# from random import choice
# from string import letters

# def sign_up(request):
# 	""" User sign up form """
# 	if request.method == 'POST':
# 		data = request.POST.copy() # so we can manipulate data
	
# 	# random username
# 	data['username'] = ''.join([choice(letters) for i in xrange(30)])
# 	form = SignUpForm(data)
	
# 	if form.is_valid():
# 		user = form.save()
# 		return HttpResponseRedirect('/sign_up_success.html')
# 	else:
# 		form = SignUpForm()

# 	return render('templates/signup.html', {'form':form}, context_instance=RequestContext(request))
