from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import TaskForm, TaskSearchForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = Task.objects.filter(user=self.request.user, is_complete=False)
        if q:
           queryset = queryset.filter(title__icontains=q)
        return queryset.order_by('priority', 'due_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm(self.request.GET)
        return context

class TaskCreation(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task created successfully!", 'success')
        return super().form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        messages.success(self.request, "Task updated successfully!", 'success')
        return super().form_valid(form)


class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Task deleted successfully!", 'success')
        return super().delete(request, *args, **kwargs)
