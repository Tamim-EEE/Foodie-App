from django.urls import path
from . import views
app_name = "sandbox"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/", views.RecipeListView.as_view()),
    path("recipes/<int:pk>", views.RecipeDetailsView.as_view(), name="recipe_details"),
    path("feedback/", views.feedback, name="feedback"),
    path("thank-you/", views.thank_you, name="thank_you")
      
]
