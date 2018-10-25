from models import User, Product
from faker import Faker
from datetime import timedelta
import textwrap

# Create Users
users = []
for i in (1,10):
	u_email = fake.ascii_email()
	u_password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
	u_name = fake.first_name() + " " + fake.last_name()
	u_rating = fake.random_int(0, 5)
	u_profile_picture = fake.file_name(category=None, extension=".png")
	u_userID = fake.uuid4()

	user = User(email=u_email, password=u_password, name=u_name, rating=u_rating, profile_picture=u_profile_picture, userID=u_userID)
	user.save()
	users.append(user)
	
# Create Products
products = []
for i in range(1, 10):
    p_productID = fake.pystr(min_chars=5, max_chars=20)
	p_userID = fake.uuid4()
	p_name = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
	p_description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
	p_price = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
	p_picture = fake.file_name(category=None, extension=".png")
	p_seller_rating = fake.random_int(0, 5)fake.random_int(0, 5)
	p_category = fake.word(ext_word_list=None)
	
    product = Product(productID=p_productID, userID=p_userID, name=p_name, 
		description=p_description, price=p_price, picture=p_picture, seller_rating=p_seller_rating, category=p_category)
	product.save()
	products.append(user_page)

username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
=
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
=
"""
print(message)