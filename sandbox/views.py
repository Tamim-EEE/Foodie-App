from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sandbox.models import Feedback
from sandbox.forms import FeedbackForm
from recipes.models import Recipe
from foodie_app.models import Category
from django.views.generic import ListView, DetailView
from django.contrib import messages


# Create your views here.
def index(request): 
    # data = ["Briryani", "Pizza","Burger","Noodles", "Pasta"]
    data = Recipe.objects.all()
    context = {"recipes": data}
    return render(request, "sandbox/index.html", context)

class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/index.html"
    context_object_name = "recipes"
    
    #Using this we can filter the recipes
    # def get_queryset(self):
    #     filtered_recipes = Recipe.objects.filter(category__name__iexact="drinks")
    #     return filtered_recipes

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = "sandbox/recipe_details.html"
    context_object_name = "recipe"
    
def thank_you(request):
    return HttpResponse("Thank you for your feedback")
        
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            feedback = form.cleaned_data["feedback"]
            satisfaction = form.cleaned_data["satisfaction"]
            Feedback.objects.create(
                name = name,
                email = email,
                feedback = feedback,
                satisfaction = satisfaction
            )
            # messages.add_message(request, messages.SUCCESS, "Feedback sent successfully!") 
            # faster way in below:
            messages.success(request, "Feedback sent successfully!") 
            return redirect("sandbox:index")
    else:
        form = FeedbackForm()
    context = {"form": form}
    return render(request, "sandbox/feedback_form.html", context)        
    