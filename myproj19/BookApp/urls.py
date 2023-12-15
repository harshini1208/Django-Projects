
from django.urls import path, include
from.import views

urlpatterns = [
    path('books',views.Book_data),
    path('books/<int:id>',views.Book_details)

]
