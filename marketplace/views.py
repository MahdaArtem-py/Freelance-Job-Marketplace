from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from marketplace.forms import ProjectForm
from marketplace.models import Project


# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'marketplace/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(status='open').order_by('-created_at')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'marketplace/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'marketplace/project_create.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


