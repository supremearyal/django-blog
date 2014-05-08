from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from entries.models import Entry, Comment
from entries.forms import EntryForm, CommentForm

def get_entry(entry_id):
    return Entry.objects.get(id=int(entry_id))

def get_entries():
    return Entry.objects.order_by('-pub_date')

def get_comments(entry):
    return Comment.objects.filter(entry=entry).order_by('-pub_date')

def index(request):
    context = RequestContext(request)
    context_dict = {'entries': get_entries()}
    return render_to_response('entries/entries.html', context_dict, context)

def show_entry(request, entry_id):
    context = RequestContext(request)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.entry = get_entry(entry_id)
            comment.save()

            return redirect('show_entry',  entry_id)
        else:
            print form.errors
    else:
        form = CommentForm(initial={'entry': get_entry(entry_id)})

    entry = get_entry(entry_id)
    comments = get_comments(entry)
    context_dict = {'entry': entry, 'comments': comments, 'form': form}
    return render_to_response('entries/entry.html', context_dict, context)

def create_comment(request, entry_id):
    context = RequestContext(request)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            entry_id = form.save().entry.id

            return redirect('show_entry', entry_id)
        else:
            entry = get_entry(entry_id)
            comments = get_comments(entry)
            context_dict = {'entry': entry, 'comments': comments, 'form': form}
            return render_to_response('entries/entry.html', context_dict, context)

def create_entry(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            new_id = form.save().id

            return redirect('show_entry', new_id)
    else:
        form = EntryForm()

    return render_to_response('entries/create_entry.html', {'form' : form}, context)
