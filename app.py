from flask import Flask, render_template
import random

app = Flask(__name__)

african_meals = [

"Ugali and Sukuma Wiki",
"Pilau",
"Nyama Choma",
"Githeri",
"Chapati and Beans",
"Matoke",
"Jollof Rice",
"Egusi Soup",
"Fufu and Soup",
"Banku and Tilapia",
"Sadza",
"Pap and Wors",
"Bunny Chow",
"Akara",
"Suya",
"Kenyan Biriani",
"Fish Stew",
"Goat Stew",
"Rice and Beef",
"Bean Stew",
"Mandazi",
"Ndengu and Rice",
"Mukimo",
"Yam Porridge",
"Okra Soup",
"Chicken Stew",
"Tilapia Fry",
"Cassava and Fish",
"Plantain and Beans",
"Spicy Lentils",
"Coconut Rice",
"Fried Rice",
"Ugali and Fish",
"Maize and Beans",
"Beef Stew"

]

modern_meals = [

"Burger",
"Pizza",
"Hot Dog",
"Chicken Wings",
"French Fries",
"Spaghetti Bolognese",
"Lasagna",
"Fried Chicken",
"Steak",
"Caesar Salad",
"Sushi",
"Tacos",
"Burrito",
"Ramen",
"Mac and Cheese",
"Grilled Cheese",
"Sandwich",
"Pancakes",
"Waffles",
"Donuts",
"Ice Cream",
"BBQ Ribs",
"Seafood Pasta",
"Chicken Alfredo",
"Nachos",
"Fajitas",
"Cheeseburger",
"Club Sandwich",
"Milkshake",
"Omelette",
"Roast Chicken",
"Chicken Burger",
"Fish and Chips",
"Shawarma",
"Kebab",
"Rice Bowl",
"Beef Burger",
"Chicken Wrap",
"Avocado Toast",
"Smoothie Bowl",
"Croissant",
"Chocolate Cake",
"Vanilla Cake",
"Cupcakes",
"Fried Rice Special",
"Chicken Curry",
"Butter Chicken",
"Greek Salad",
"Beef Tacos",
"Roasted Potatoes"

]

fruits = [

"Mango",
"Banana",
"Apple",
"Orange",
"Pineapple",
"Watermelon",
"Papaya",
"Avocado",
"Grapes",
"Strawberries",
"Lemon",
"Lime",
"Kiwi",
"Pear",
"Peach",
"Guava",
"Passion Fruit",
"Dragon Fruit",
"Coconut",
"Blueberries"

]

alcoholic = [

"Beer",
"Wine",
"Whiskey",
"Vodka",
"Gin",
"Rum",
"Tequila",
"Champagne",
"Cocktail",
"Brandy"

]

non_alcoholic = [

"Water",
"Orange Juice",
"Mango Juice",
"Soda",
"Tea",
"Coffee",
"Milkshake",
"Smoothie",
"Lemonade",
"Energy Drink"

]

@app.route("/")

def home():

    return render_template(

        "index.html",

        african_meals=african_meals,
        modern_meals=modern_meals,
        fruits=fruits,
        alcoholic=alcoholic,
        non_alcoholic=non_alcoholic

    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
