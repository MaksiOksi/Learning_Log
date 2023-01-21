from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, 'learning_log_app/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log_app/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log_app/topic.html', context)


def new_topic(request):
    # Empty form
    if request.method != 'POST':
        form = TopicForm()
    # Proces the data
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log_app:topics')
    # Show empty or not valid form
    context = {'form': form}
    return render(request, 'learning_log_app/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # Empty form
    if request.method != 'POST':
        form = EntryForm()
    # Proces the data
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_log_app:topic', topic_id=topic_id)

    # Show empty or not valid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log_app/new_entry.html', context)


def edit_entry(request, entry_id):
    # Edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; proces data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log_app:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log_app/edit_entry.html', context)
