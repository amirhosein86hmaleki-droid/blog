from django.urls import path
from.import views

app_name = 'blog'
urlpatterns = [
    path('messages/', views.MessagesListView.as_view(), name='message_list'),
    path('details/<slug:slug>',views.ArticleDetailView.as_view(),name='article_details'),
    path('list',views.ArticleListView.as_view(),name='article_list'),
    path('category/<int:pk>',views.category_detail,name="category_detail"),
    path('search/',views.search,name="search_articles"),
    # path('new/',views.post_new,name='post_new'),
    path('contactus',views.MessageView.as_view(),name='contact_us'),
    path('red/<slug:slug>',views.HomePageRedirect.as_view(),name='redirect'),
    path('messages/edit/<int:pk>',views.MessagesUpdateView.as_view(),name='message_edit'),
    path('messages/delete/<int:pk>',views.MessagesDeleteView.as_view(),name='message_delete'),
    path('archive',views.ArchiveIndexArticleView.as_view(),name='archive'),
    path('archive/<int:year>',views.YearArchiveArticleView.as_view(),name='year_archive'),
    path('like/<slug:slug>/<int:pk>',views.Like,name='like'),

]