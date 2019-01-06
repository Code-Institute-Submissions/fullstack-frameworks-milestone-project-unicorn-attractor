from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Bugs, Features, Comments
from django.utils import timezone
from .forms import AddBugsForm, AddFeaturesForm, AddCommentForm
from checkout.views import cart


def tickets(request):   # Render the ticket main page. 
    return render(request, 'tickets.html')
    
    
def bugs(request):  # Render the bugs ticket page. 
    bugs = Bugs.objects.all()
    return render(request, 'bugs.html', {'bugs': bugs})
    
    
def add_bug(request):
    if request.method=="POST":
        form = AddBugsForm(request.POST)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            bug = form.save()
            return redirect(bugs)
    else:
        form = AddBugsForm
    return render(request, 'add_bug.html', {'form': form})
    
    
def bug_detail(request, pk):
    
    bug = get_object_or_404(Bugs, pk=pk)   # Returns the bug based on its ID. 
    bug.views += 1 # Increments the number of views by 1.
    bug.save()
    
    user = request.user
    
    comments = Comments.objects.filter(bug=bug)
    
    if request.method=="POST":
        
        form = AddCommentForm(request.POST)
        bug_id = request.POST['bug_id']
        
        if form.is_valid:
            save = Comments(bug_id = bug_id, message = form.save(), user = user) # Save the feature ID from the front end and the contents of the form to the message field & feature field in the database.
            save.save()
            return redirect(bug_detail, bug.pk)
    
    else:
        form = AddCommentForm(instance=bug)   
        
    contexts = {'bug': bug, 'form': form, 'comments': comments }
    
    return render(request, 'bug_detail.html', contexts)
    
    
def edit_bug(request, pk=None):
    bug = get_object_or_404(Bugs, pk=pk) if pk else None    # Instantiate the 'Bugs' object from models, gets the object or returns a 404 error.
    if request.method=="POST":
        form = AddBugsForm(request.POST, instance=bug)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = AddBugsForm(instance= bug)
    return render(request, 'edit_bug.html', {'form': form})
    
    
def bug_upvote(request, pk):
    
    bug = get_object_or_404(Bugs, pk=pk)
    bug.likes += 1
    bug.save()
    
    return redirect(bugs)
    
    
def bug_downvote(request, pk):
    
    bug = get_object_or_404(Bugs, pk=pk)
    bug.likes -= 1
    bug.save()
    
    return redirect(bugs)
    

def features(request):  # Render the features ticket page. 
    features = Features.objects.all()
    likes = Features.objects.all()
    user = request.user
        
    return render(request, 'features.html', {'features': features, 'likes': likes, 'user': user})
    
    
def add_feature(request):
    if request.method=="POST":
        form = AddFeaturesForm(request.POST)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            feature = form.save()
            return redirect(features)
    else:
        form = AddFeaturesForm
    return render(request, 'add_feature.html', {'form': form})
    
    
def features_detail(request, pk):
    
    feature = get_object_or_404(Features, pk=pk) 
    feature.views += 1
    feature.save()

    user = request.user
    
    comments = Comments.objects.filter(feature=feature)

    if request.method=="POST":
        
        form = AddCommentForm(request.POST)
        feature_id = request.POST['feature_id']

        if form.is_valid:
            save = Comments(feature_id = feature_id, message = form.save(), user = user) # Save the feature ID from the front end and the contents of the form to the message field & feature field in the database. 
            save.save()
            return redirect(features_detail, feature.pk)
    else:
        form = AddCommentForm()   
        
    contexts = {'feature': feature, 'form': form, 'comments': comments }
    
    return render(request, 'features_detail.html', contexts)
    
    
def edit_feature(request, pk):
    feature = get_object_or_404(Features, pk=pk)  # Instantiate the 'Bugs' object from models, gets the object or returns a 404 error.
    if request.method=="POST":
        form = AddFeaturesForm(request.POST, instance=feature)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            feature = form.save()
            return redirect(features_detail, feature.pk)
    else:
        form = AddFeaturesForm(instance=feature)
    return render(request, 'edit_feature.html', {'form': form, 'feature': feature})
    
 
def feature_upvote(request, pk):
    
    feature = get_object_or_404(Features, pk=pk)
    feature.likes += 1
    feature.save()
    
    return redirect(features)
 
    
def feature_downvote(request, pk):
    
    feature = get_object_or_404(Features, pk=pk)
    feature.likes -= 1
    feature.save()
    
    return redirect(features)