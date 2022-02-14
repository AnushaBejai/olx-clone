from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect



# Create your views here.
def productlist(request, category_slug=None):
    category=None
    productlist=Product.objects.all()
    categorylist=Category.objects.annotate(total_products=Count('product'))
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug  )
        #category=Category.objects.get(slug=category_slug)
        productlist=productlist.filter(category=category)
    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(conditon__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query) |
            Q(category__category_name__icontains=search_query)
        )
        
    paginator = Paginator(productlist, 3) 
    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    context={'productlist':productlist, 'categorylist':categorylist, 'category':category}
    template='product/product_list.html'
    return render(request, template, context)

def productdetail(request, product_slug):
    productdetail=Product.objects.get(slug=product_slug)
    productimages=ProductImages.objects.filter(product=productdetail)
    context={'productdetail':productdetail, 'productimages':productimages}
    template='product/product_detail.html'
    return render(request, template, context)


def Post(request):
    user=request.user
    if request.method == "POST":
    #images will be in request.FILES
        form = PostFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            data=form.save(commit=False)
            data.owner=user
            data.save()
            
            for f in files:
                ProductImages.objects.create(product=data,image=f)
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print("Form invalid")
    else:
        form=PostFullForm()
    context={'form':form}
    template='product/post_ad.html'
    return render(request, template, context)

    





#@login_required
#def Post(request):
    #user=request.user
    #if request.method=="POST":
        #form=PostForm(request.POST, request.FILES )
        #if form.is_valid():
            #data=form.save(commit=False)
            #data.owner=user
            #data.save()
            #template='product/product_detail.html'
            #return render(request, template)
    #else:
        #form=PostForm()
    #context={'form':form}
    #template='product/post_ad.html'
    #return render(request, template, context)

    
    













