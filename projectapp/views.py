from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

@method_decorator(login_required(login_url=reverse_lazy('myself:login')),'get')
@method_decorator(login_required(login_url=reverse_lazy('myself:login')),'post')

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.object.pk})
class ProjectDetailView(DetailView,MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 15

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(project=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 10