1. install package:
	pip install django-hashers-passlib==0.1

2. add this in settings.py:

	PASSWORD_HASHERS = (
		'django.contrib.auth.hashers.PBKDF2PasswordHasher',
		'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
		'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
		'django.contrib.auth.hashers.BCryptPasswordHasher',
		'django.contrib.auth.hashers.SHA1PasswordHasher',
		'django.contrib.auth.hashers.MD5PasswordHasher',
		'django.contrib.auth.hashers.CryptPasswordHasher',
		'hashers_passlib.phpass',
	)


3. add this in views.py:
	from django.contrib.auth.models import User
	from django.contrib.auth.hashers import get_hasher
	
	all_wp_usr = User.objects.filter(password__startswith='$P$B')
	hasher = get_hasher('phpass')

	for user in all_wp_usr:
        	user.password = hasher.from_orig(user.password)
        	user.save()
		

4. then run the server







