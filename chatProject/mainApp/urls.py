from django.urls import path

#from django.conf import settings
#from django.conf.urls.static import static


from .views import PostsCreate, PostsDetail, PostsUpdate, PostsDelete, posts_list
from .views import TagsCreate, TagsDetail, TagsUpdate, TagsDelete, tags_list
app_name = 'mainApp'
urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('posts/create/', PostsCreate.as_view(), name='posts_create_url'),
    path('posts/<str:slug>/', PostsDetail.as_view(), name='posts_detail_url'),
    path('posts/<str:slug>/update/', PostsUpdate.as_view(), name='posts_update_url'),
    path('posts/<str:slug>/delete/', PostsDelete.as_view(), name='posts_delete_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('tags/create/', TagsCreate.as_view(), name='tags_create_url'),
    path('tags/<str:slug>/', TagsDetail.as_view(), name='tags_detail_url'),
    path('tags/<str:slug>/update/', TagsUpdate.as_view(), name='tags_update_url'),
    path('tags/<str:slug>/delete/', TagsDelete.as_view(), name='tags_delete_url'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#posts_detail, , tags_detail