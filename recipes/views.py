from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from comments.forms import CommentForm
from recipes.models import Recipe
from django.db.models import Q


# Create your views here.
def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    # recipes = Recipe.objects.filter(category__name__exact="Drinks")
    # recipes = Recipe.objects.filter(category__name__contains="Drinks") both are same
    # recipes = Recipe.objects.exclude(name__contains="coffee") Its use to excluse the specific recipes by entering the recipe name
    # recipes = Recipe.objects.filter(category__name__exact="Drinks").exclude(name__contains="Hot").order_by("date_added")
    # recipes = Recipe.objects.filter(Q(name__startswith="Biriyani") | Q(description__contains="rice"))
    # print("Recipes", recipes)
    return render(request, "recipes/recipes.html", context)
def recipe_details(request, recipe_id):
    # recipe = Recipe.objects.get(id=recipe_id) its another but below one is the safest
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect(recipe.get_absolute_url())
        
    else:
        comment_form = CommentForm()
            
    context = {"recipe": recipe, "comments": comments, "comment_form": comment_form}
    return render(request, "recipes/recipe.html", context)