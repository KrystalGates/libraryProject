from django.conf.urls import url
from django.conf.urls import url, include
from .views import *
from django.urls import path

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='books'),
    path('books/<int:book_id>/', book_details, name='book'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^librarians$', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    url(r'^libraries$', list_libraries, name='libraries'),
    url(r'^library/form$', library_form, name='library_form'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
]