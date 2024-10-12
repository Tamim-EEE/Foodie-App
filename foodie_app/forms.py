from django import forms

from recipes.models import Recipe
from foodie_app.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        # labels = {"name": "Category Name"}
        widgets = {"name": forms.TextInput(attrs={"class": "form-control","placeholder": "Category Name"})}
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "ingredients", "directions", "category", "image"]
        widgets = {"name": forms.TextInput(attrs= {"class": "form-control", "placeholder": "Recipe Title"}), 
                   "description": forms.Textarea(attrs= {"class": "form-control", "placeholder": "Write Description", "rows": "5"}),
                   "ingredients": forms.Textarea(attrs= {"class": "form-control", "placeholder": "Write Ingredients", "rows": "5"}),
                   "directions": forms.Textarea(attrs= {"class": "form-control", "placeholder": "Write Directions", "rows": "5"}),
                   "category": forms.Select(attrs={"class": "form-select"})
                   
                   }