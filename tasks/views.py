from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.asignee = self.request.user
        item.save()
        return redirect("show_project")
