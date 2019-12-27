from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

#from django.conf import settings
from .models import Posts, Tags
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .form import TagsForm, PostsForm
# Create your views here.


def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Posts.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        #search_list = {'search': search_query}
    else:
        posts = Posts.objects.all()

    paginat = Paginator(posts, 2)
    numb_page = request.GET.get('page', 1)
    page = paginat.get_page(numb_page)
    is_paginator = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    pagin_page_obj = {'page_obj': page, 
                      'is_paginator': is_paginator, 
                      'next_url': next_url,
                      'prev_url': prev_url,
                      'search': search_query
                    }
    content=dict()
    content.update(pagin_page_obj)
    return render(request, 'mainTemp/index.html', content)


class PostsDetail(ObjectDetailMixin):
    model = Posts
    template = 'mainTemp/posts_detail.html'


class PostsCreate(LoginRequiredMixin, ObjectCreateMixin):
    modelForm = PostsForm
    template = 'mainTemp/post_create.html'
    raise_exception = True


class PostsUpdate(LoginRequiredMixin, ObjectUpdateMixin):
    model = Posts
    model_form = PostsForm
    template = 'mainTemp/post_update.html'
    raise_exception = True

class PostsDelete(LoginRequiredMixin, ObjectDeleteMixin):
    model = Posts
    template = 'mainTemp/post_delete.html'
    template_redirect = 'mainApp:posts_list'
    raise_exception = True

        
def tags_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tags = Tags.objects.filter(title__icontains=search_query)
    else:
        tags = Tags.objects.all()

    paginat = Paginator(tags, 2)
    numb_page = request.GET.get('page', 1)
    page = paginat.get_page(numb_page)
    is_paginator = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    pagin_page_obj = {'page_obj': page, 
                      'is_paginator': is_paginator, 
                      'next_url': next_url,
                      'prev_url': prev_url
                     }
    content=dict()
    content.update(pagin_page_obj)
    return render(request, 'mainTemp/tag_list.html', content)


class TagsDetail(ObjectDetailMixin):
    model = Tags
    template = 'mainTemp/tag_detail.html'


class TagsCreate(LoginRequiredMixin, ObjectCreateMixin):
    modelForm = TagsForm
    template = 'mainTemp/tag_create.html'
    raise_exception = True

class TagsUpdate(LoginRequiredMixin, ObjectUpdateMixin):
    model = Tags
    model_form = TagsForm
    template = 'mainTemp/tag_update.html'
    raise_exception = True


class TagsDelete(LoginRequiredMixin, ObjectDeleteMixin):
    model = Tags
    template = 'mainTemp/tag_delete.html'
    template_redirect = 'mainApp:tags_list_url'
    raise_exception = True



# class PostsUpdate(ObjectUpdateMixin):
#     def get(self, request, slug):
#         context=dict()
#         obj = Posts.objects.get(slug__iexact=slug)
#         item = {'item': obj}
#         context.update(item)
#         bound_form = {'form': PostsForm(instance=obj)}
#         context.update(bound_form)
#         return render(request, 'mainTemp/post_update.html', context)
    
#     def post(self, request, slug):
#         obj = Posts.objects.get(slug__iexact=slug)
#         bound_form = PostsForm(request.POST, instance=obj)
#         if bound_form.is_valid():
#             new_write = bound_form.save()
#             return redirect(new_write)
#         context=dict()
#         item = {'item': obj}
#         context.update(item)
#         bound_form = {'form': bound_form}
#         context.update(bound_form)
#         return render(request, 'mainTemp/post_update.html', context)


# class PostsCreate(ObjectCreateMixin):
#     modelForm = PostsForm
#     template = 'mainTemp/post_create.html'
    # def get(self, request):
    #     content = dict()
    #     form_post = {'form': PostsForm()}
    #     content.update(form_post)
    #     return render(request, 'mainTemp/post_create.html', content)

    # def post(self, request):
    #     bound_form = PostsForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     content = dict()
    #     bound_form = {'form': bound_form}
    #     content.update(bound_form)
    #     return render(request, 'mainTemp/post_create.html', content)

# class TagsDetail(View):
#     def get(self, request, slug):
#         context = dict()
#         tag = {'tag': Tags.objects.get(slug__iexact=slug)}
#         context.update(tag)
#         return render(request, 'mainTemp/tag_detail.html', context)

# class PostsDetail(View):
#     def get(self, request, slug):
#         context = dict()
#         post = {'post': get_object_or_404(Posts, slug__iexact=slug)}
#         context.update(post)
#         return render(request, 'mainTemp/posts_detail.html', context)

# class PostsDetail(View):
#     def get(self, request, slug):
#         context = dict()
#         post = {'post': Posts.objects.get(slug__iexact=slug)}
#         context.update(post)
#         return render(request, 'mainTemp/posts_detail.html', contex

# def posts_detail(request, slug: str):
#     context = dict()
#     post = {'post': Posts.objects.get(slug__iexact=slug)}
#     context.update(post)
#     return render(request, 'mainTemp/posts_detail.html', context)
#     pass

# def tags_detail(request, slug: str):
#     context =dict()
#     tag = {'tag': Tag.objects.get(slug__iexact=slug)}
#     context.update(tag)
#     return render(request, 'mainTemp/tag_detail.html', context)
#     pass


# def index(request):
#     print()
#     print(request)
#     print()
#     print(dir(request))
#     print()
#     return HttpResponse('hello')


