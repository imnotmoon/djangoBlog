from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from django.utils import timezone
from .form import ArticleUpdate
from faker import Faker


# Create your views here.
def article(request):
    articles = Articles.objects.all()
    return render(request, 'article.html', {'articles' : articles})

def create(request):
    article = Articles()
    article.title = request.GET['title']
    article.body = request.GET['body']
    article.pub_date = timezone.datetime.now()
    article.save()
    return redirect('/article/')

def write(request):
    return render(request, 'write.html')

def detail(request, article_id):
    article_detail = get_object_or_404(Articles, pk=article_id)
    return render(request, 'detail.html', {'article' : article_detail})

def update(request, article_id):
    return render(request, 'update.html', {'article_id' : article_id})

def delete(request, article_id):
    Articles.objects.get(id=article_id).delete()
    return redirect('/article/')

def update(request, article_id):
    article = Articles.objects.get(id=article_id)
    if request.method =='POST':
        form = ArticleUpdate(request.POST)
        if form.is_valid():
            print("pass")
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.pub_date=timezone.now()
            article.save()
            return redirect('/article/')
    else:
        form = ArticleUpdate(instance = article)
 
        return render(request,'update.html', {'form':form})

def fake(request):
    for i in range(10):
        blog = Articles()
        myfake = Faker()
        blog.title = myfake.name()
        txt = ''
        for j in range(10):
            txt = txt + myfake.text()
        blog.body = txt
        blog.pub_date = timezone.datetime.now()
        blog.save()
    return redirect('/article/')
