# from email.message import Message
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.urls import reverse_lazy,reverse
from blog.models import Article, Category, Comment ,Message,Like
from django.core.paginator import Paginator
from .forms import ContactUsForm,MessageForm
from django.views.generic.base import View,TemplateView ,RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, ArchiveIndexView, YearArchiveView
from.mixins import LoginRequiredMixin

def article_detail(request,slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST' :
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body,article=article,user=request.user,parent_id=parent_id)

    return render(request, "blog/article_details.html", {"article":article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list =paginator.get_page(page_number)
    return render(request,"blog/articles_list.html",{"articles":objects_list })


def category_detail(request,pk=None):
    category = get_object_or_404(Category,id=pk)
    articles =category.articles.all()
    return  render(request,"blog/articles_list.html",context={"articles":articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request,"blog/articles_list.html",{"articles":objects_list})



def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.bmi = instance.weight *instance.height
            return redirect('home_app:home')
    else:
        form = MessageForm()
    return render(request,"blog/contact_us.html",{'form':form})

class TestBaseView(View):
    name ="amir"
    def get(self, request):
        return HttpResponse(self.name)





class BerListView(View):                                                                            #ber:یه حروف الکیه#
    queryset = Article.objects.all()
    template_name = "blog/articles_list.html"

    def get(self, request):
        return render(request, self.template_name, {'object_list': self.queryset})

class HomePageRedirect(RedirectView):
    # url = "/articles/list"
    pattern_name = 'blog:article_details'
    permanent = False
    query_string = False


    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class ArticleList(TemplateView):
    pass


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "blog/user_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_details.html"
    # context_object_name = "art"
    # slug_field = 'karim'
    # queryset = Article.objects.filter(published=True)******************************
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = "amir"
    #     return context


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 2
    template_name = "blog/articles_list.html"


class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForm
    success_url = "/"

    def form_valid(self, form):
        from_data = form.cleaned_data
        Message.objects.create(**from_data )
        return super().form_valid(form)


class MessageView(CreateView):
    model = Message
    fields = ('title','text','date', 'age')
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        print(self.object)
        return super(MessageView, self).get_success_url()

class MessagesListView(ListView):
    model = Message
class MessagesUpdateView(UpdateView):
    model = Message
    fields = ('title','text', 'age')
    template_name = "blog/message_update_form.html"
    success_url = reverse_lazy("blog:message_list")

class MessagesDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("blog:message_list")


class ArchiveIndexArticleView(ArchiveIndexView):
    model = Article
    date_field = 'updated'

class YearArchiveArticleView(YearArchiveView):
    model = Article
    date_field = 'pub_date'
    make_object_list = True
    allow_future = True

def like(request, slug, pk):
    try:
        like = Like.objects.get(article_slug=slug,user_id=request.user.id)
        like.delete()
    except Like.DoesNotExist:
        Like.objects.create(article_id=pk,user_id=request.user.id)
    return redirect('blog:article_details',slug=slug)