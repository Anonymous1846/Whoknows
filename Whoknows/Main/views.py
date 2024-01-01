from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,DeleteView
from .models import Topic
from .forms import TopicForm

#display for blog post list 

class MainView(ListView):
	model = Topic
	template_name = 'index.html'


class TopicView(DetailView):
	model = Topic
	template_name = 'topic_detail.html'


class CreateTopicView(CreateView):
	template_name = 'new_topic.html'

	def get(self, request):
		form = TopicForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = TopicForm(request.POST)
		if form.is_valid():
			# Set the author field to the currently logged-in user before saving
			if request.user.is_authenticated:
				form.instance.author = request.user
			new_topic = form.save()
			return redirect('topic-detail', pk=new_topic.pk)  # Change 'post_detail' to the name of your post detail view
		return render(request, self.template_name, {'form': form})

class DeleteTopic(DeleteView):
	model = Topic
	success_url = reverse_lazy('home')

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		response =JsonResponse({'success': True, 'url': success_url})
		response["Access-Control-Allow-Origin"] = "http://localhost:8000"  # Adjust to match your frontend URL
		response["Access-Control-Allow-Credentials"] = "true"

		return response