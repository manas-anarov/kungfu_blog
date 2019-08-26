from restpost import views
from django.conf.urls import url

urlpatterns = [
	url(r'^list/$', views.PostListAPIView.as_view(), name='restpost-list'),
	url(r'^add/$', views.AddPost.as_view(), name='restpost-add'),
	url(r'^(?P<id>[\w-]+)/$', views.ShowPost.as_view(), name='restpost-show'),
	url(r'^category/list/$', views.CategoryAllAPIView.as_view(), name='restpost-list-caregory'),
	url(r'^list/(?P<id>[\w-]+)/$', views.CategoryIdAPIView.as_view(), name='restpost-category-id'),
]