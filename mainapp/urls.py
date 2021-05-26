from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('drive/bin/', views.binPage, name='bin'),
    path('drive/favourites/', views.favouritePage, name='favourite'),
    path('sign-up', views.register, name='register'),
    path('drive/<int:pk>', login_required(login_url='login')(views.InDirectoryView.as_view()), name='inDirectory'),
    path('drive/<int:pk>/upload_file', views.upload_file, name='upload_file'),
    path('sign-in', views.loginPage, name='login'),
    path('drive', views.drivePage, name='drive'),
    path('logout', views.logoutUser, name='logout'),
    path('drive/create_directory', views.create_directory, name='create_directory'),
    path('drive/rename_directory', views.rename_directory, name='rename_directory'),
    path('drive/rename_directory/<int:pk>', views.rename_directory_function, name='rename_directory_function'),
    path('drive/delete_directory', views.delete_directory, name='delete_directory'),
    path('drive/delete_directory/<int:pk>', views.delete_directory_function, name='delete_directory_function'),
    path('drive/<int:directory_key>/rename_file', views.rename_file, name='rename_file'),
    path('drive/<int:directory_key>/rename_file/<int:file_key>', views.rename_file_function, name='rename_file_function'),
    path('drive/<int:directory_key>/delete_file', views.delete_file, name='delete_file'),
    path('drive/<int:directory_key>/delete_file/<int:file_key>', views.delete_file_function, name='delete_file_function'),
    path('drive/<int:directory_key>/make_favourite', views.make_favourite, name='make_favourite'),
    path('drive/<int:directory_key>/make_favourite/<int:file_key>', views.make_favourite_function, name='make_favourite_function'),
    path('drive/<int:directory_key>/move_to_bin', views.move_to_bin, name='move_to_bin'),
    path('drive/<int:directory_key>/move_to_bin/<int:file_key>', views.move_to_bin_function, name='move_to_bin_function'),
    path('drive/bin/restore_file', views.restore_file, name='restore_file'),
    path('drive/bin/restore_file/<int:file_key>', views.restore_file_function, name='restore_file_function'),
    path('drive/favourites/unmake_favourite', views.unmake_favourite, name='unmake_favourite'),
    path('drive/favourites/unmake_favourite/<int:file_key>', views.unmake_favourite_function, name='unmake_favourite_function'),
    path('drive/favourites/rename_favourite', views.rename_favourite, name='rename_favourite'),
    path('drive/favourites/rename_favourite/<int:file_key>', views.rename_favourite_function, name='rename_favourite_function'),
]
