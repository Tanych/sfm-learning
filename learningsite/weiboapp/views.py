from django.shortcuts import render

# Create your views here.
def index(request):
    weibo_list=weiboapp.objects.all()
    return render(request,"weiboapp/index.html",{'weibo_list':weibo_list},)

def add_done(request):
    add_question=Weibo()
    content=request.POST['content']
    add_question.context=content
    add_question.save()
    return render(request,"weiboapp/add_done.html",{'question':content},)

def add(request):
    return render(request,"weiboapp/weibo/index.html")

