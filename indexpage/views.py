from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

# class IndexPageView(View):
#     template_name = 'indexpage.html'
#
#     def get(self, request):
#         #logic
#         args = {
#             'text': 'eggs',
#         }
#         return render(request, template_name=self.template_name, context=args)

class IndexPageView(TemplateView):
    template_name = 'indexpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'text': 'eggs'
        })
        return context

    def post(self, request):
        return HttpResponse('Post')

    def get(self, request):
        return HttpResponse('Get')
        # return HttpResponseRedirect(reverse('home'))