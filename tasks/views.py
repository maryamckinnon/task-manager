from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.urls import reverse_lazy

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = [
        "name",
        "start_date",
        "due_date",
        "project",
        "assignee",
        "description",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.project.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = "/tasks/mine/"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    fields = ["delete"]
    success_url = "/tasks/mine/"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    fields = ["description"]
    template_name = "tasks/detail.html"
