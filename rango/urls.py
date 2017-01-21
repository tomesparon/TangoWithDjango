from django.conf.urls import url
from rango import views

urlpatterns = [
	#REMEMBER TO PUT COMMAS IN AFTER EACH!!!!
	url(r'^$', views.index, name='index'),

	url(r'^about/', views.about, name='About'),

	#Add parameterised url mapping for category
	# will invoke view.show_category() when the URL pattern below is matched:
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category, name='show_category'),
]
