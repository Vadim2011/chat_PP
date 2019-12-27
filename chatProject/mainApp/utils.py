from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import reverse


class ObjectDetailMixin(View):
    model = None
    template = None
    
    def get(self, request, slug):
        context = dict()
        obj = {self.model.__name__.lower()[:-1]: get_object_or_404(self.model, slug__iexact=slug)}
        admin = {'admin_obj': get_object_or_404(self.model, slug__iexact=slug)}
        context.update(obj)
        context.update(admin)
        return render(request, self.template, context)

class ObjectCreateMixin(View):
    modelForm = None
    template = None

    def get(self, request):
        content = dict()
        form_field = {'form': self.modelForm()}
        content.update(form_field)
        return render(request, self.template, content)

    def post(self, request):
        bound_form = self.modelForm(request.POST) 
        if bound_form.is_valid():
            new_write = bound_form.save()
            return redirect(new_write)
        content = dict()
        bound_form = {'form': bound_form}
        content.update(bound_form)
        return render(request, self.template, content) 

class ObjectUpdateMixin(View):
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        context=dict()
        obj = self.model.objects.get(slug__iexact=slug)
        item = {'item': obj}
        context.update(item)
        bound_form = {'form': self.model_form(instance=obj)}
        context.update(bound_form)
        return render(request, self.template, context)
    
    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_write = bound_form.save()
            return redirect(new_write)
        context=dict()
        item = {'item': obj}
        context.update(item)
        bound = {'form': bound_form}
        context.update(bound)
        return render(request, self.template, context)


class ObjectDeleteMixin(View):
    model = None
    template = None
    template_redirect = None
        
    def get(self, request, slug):
        content=dict()
        obj = {'item': self.model.objects.get(slug__iexact=slug)}
        content.update(obj)
        return render(request, self.template, content)
    
    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.template_redirect))

