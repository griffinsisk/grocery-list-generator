from flask import Flask, render_template, request
from collections import defaultdict

app = Flask(__name__)

# Dictionary containing recipes and their respective ingredients
recipes = {
    "Honey Teriyaki Chicken": ["chicken thighs", "soy sauce", "dark soy sauce", "honey", "mirin", "ginger", "garlic", "rice", "broccolini", "cornstarch"],
    "Firecracker Beef": ["ground beef", "sriracha", "honey", "soy sauce", "rice vinegar", "onion", "garlic", "ginger", "red chili", "sesame seeds", "green onion", "rice", "broccolini"],
    "Cajun Chicken": ["chicken thighs", "cajun seasoning", "smoked paprika", "red onion", "garlic", "oregano", "red pepper", "chicken stock", "cherry tomatoes", "half and half", "lime", "rice", "sour cream", "broccolini" ],
    "Buffalo Chicken Bowls": ["chicken breast", "salt", "parsley", "garlic", "cumin", "smoked paprika", "buffalo sauce", "white potatoes", "greek yogurt", "mayo", "honey", "tomatoes", "red onion", "cucumber", "green onion", "lemon"],
    "Arayes": ["ground beef", "garlic", "feta", "parsley", "harissa", "smoked paprika", "all spice", "onion", "salt", "pepper", "cumin", "cinnamon", "pita", "white sauce" ],
    "Thai Basil Pork": ["ground pork", "soy sauce", "dark soy sauce", "oyster sauce", "fish sauce", "red chili", "garlic", "sugar", "red onion", "chicken stock", "basil leaves", "eggs", "rice"],
    "Zesty Shrimp": ["raw shrimp", "oregano", "salt", "pepper", "lemon", "red chili flakes", "garlic", "asapargus", "deli pasta salad"],
    "Breakfast Tortilla": ["eggs", "tortillas", "feta", "avocado", "lime", "sriracha", "everything spice"],
    "Yogurt Bowl": ["greek yogurt", "blackberries", "strawberries", "dark chocolate chips", "shredded coconut", "almonds", "honey"],
    "Orange Vanilla Smoothie (great frozen)": ["orange", "vanilla protein", "orange juice/citrus collagen", "vanilla extract", "greek yogurt", "honey", "ice"],
    "Mocha Smoothie (great frozen)": ["coffee", "vanilla protein", "greek yogurt", "oats", "cocoa powder", "cinnamon", "dark chocolate chips", "avocado", "ice"],
    "Natural Gatorade": ["lime", "strawberries", "watermelon", "coconut water", "tequila (optional)", "ice"],

}

# Function to consolidate grocery list
def consolidate_grocery_list(selected_recipes):
    grocery_list = defaultdict(int)
    for recipe in selected_recipes:
        for ingredient in recipes[recipe]:
            grocery_list[ingredient] += 1
    return grocery_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_recipes = request.form.getlist('recipes')
        grocery_list = consolidate_grocery_list(selected_recipes)
        return render_template('result.html', grocery_list=grocery_list)

    return render_template('index.html', recipes=recipes.keys())

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)