from django import forms

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
			required = True,
			label = 'Username',
			max_length = 32
		)
	email = forms.CharField(
			required = True,
			label = 'Email',
			max_length = 32,
		)
	password = forms.CharField(
			required = True,
			label = 'Password',
			max_length = 32,
			widget = forms.PasswordInput()
		)
	first_name = forms.CharField(
			required = True,
			label = 'First Name',
			max_length = 32
		)
	last_name = forms.CharField(
			required = True,
			label = 'Last Name',
			max_length = 32
		)

class UserBookingForm(forms.Form):
	first_name = forms.CharField(
			required = True,
			label = 'First Name',
			max_length = 32
		)
	last_name = forms.CharField(
			required = True,
			label = 'Last Name',
			max_length = 32
		)

	gender = forms.CharField(
			required = True,
			label = 'Gender',
			max_length = 32
		)

	origin = forms.CharField(
			required = True,
			label = 'Origin',
			max_length = 32
		)

	destination = forms.CharField(
			required = True,
			label = 'Destination',
			max_length = 32
			
		)

	def __str__(self):
			return f"{self.id} {self.first_name} {self.last_name}{self.gender}{self.origin}{self.destination}"	

class UserBookingForm(forms.Form):
	first_name = forms.CharField(
			required = True,
			label = 'First Name',
			max_length = 32
		)
	last_name = forms.CharField(
			required = True,
			label = 'Last Name',
			max_length = 32
		)

	gender = forms.CharField(
			required = True,
			label = 'Gender',
			max_length = 32
		)

	origin = forms.CharField(
			required = True,
			label = 'Origin',
			max_length = 32
		)

	destination = forms.CharField(
			required = True,
			label = 'Destination',
			max_length = 32
			
		)
	email = forms.CharField(
			required = True,
			label = 'Email',
			max_length = 32
			
		)
	phone = forms.IntegerField(
			required = True,
			label = 'Phone Number'
			
		)
	

	def __str__(self):
			return f"{self.id} {self.first_name} {self.last_name}{self.gender}{self.origin}{self.destination} {self.email}"