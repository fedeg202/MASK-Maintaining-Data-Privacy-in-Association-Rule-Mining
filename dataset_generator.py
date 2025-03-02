import random
import pandas as pd

ITEMS = {
    # Core high-frequency items (frequent in transactions, ensuring frequent itemsets)
    "Milk": 7, "Bread": 7, "Eggs": 7, "Rice": 7, "Bananas": 7, "Chicken": 7, "Cheese": 7, "Butter": 7,
    "Pasta": 7, "Tomato": 7, "Onion": 7, "Carrot": 7, "Potatoes": 7, "Coffee": 7, "Tea": 7, "Soda": 7,

    # Medium-to-high frequency items (increase frequent 3- and 4-itemsets)
    "Chocolate": 6, "Cookies": 6, "Yogurt": 6, "Cereal": 6, "Apples": 6, "Fish": 6, "Lettuce": 6,
    "Orange Juice": 6, "Peanut Butter": 6, "Jam": 6, "Honey": 6, "Nuts": 6, "Chips": 6,
    "Canned Beans": 6, "Canned Tuna": 6, "Mushrooms": 6, "Frozen Pizza": 6, "Flour": 6,

    # Supporting items to enhance 3-, 4-, and 5-itemsets
    "Sugar": 5, "Salt": 5, "Pepper": 5, "Olive Oil": 5, "Vinegar": 5, "Soy Sauce": 5, "Ketchup": 5,
    "Mustard": 5, "Mayonnaise": 5, "Garlic": 5, "Baking Powder": 5, "Ground Turkey": 5, "Sausages": 5,
    "Spinach": 5, "Broccoli": 5, "Cauliflower": 5, "Zucchini": 5, "Celery": 5, "Eggplant": 5, 

    # Lower frequency items (ensuring variety)
    "Sweet Potatoes": 4, "Lemons": 4, "Limes": 4, "Pineapple": 4, "Mango": 4, "Peaches": 4, "Plums": 4,
    "Watermelon": 4, "Cantaloupe": 4, "Corn": 4, "Raspberries": 4, "Coconut Milk": 4, "Ground Coffee": 4,
    "Herbal Tea": 4, "Maple Syrup": 4, "Granola Bars": 4, "Trail Mix": 4, "Pretzels": 4, "Popcorn": 4,

    # Expanding the diversity while keeping frequent sets strong
    "Frozen Vegetables": 3, "Frozen Berries": 3, "Frozen Chicken Nuggets": 3, "Oats": 3,
    "Whole Wheat Bread": 3, "Brown Rice": 3, "Quinoa": 3, "Hummus": 3, "Tortilla Wraps": 3,
    "Salmon": 3, "Shrimp": 3, "Cottage Cheese": 3, "Feta Cheese": 3, "Parmesan Cheese": 3,
    "Almond Butter": 3, "Canned Corn": 3, "Canned Soup": 3, "Pasta Sauce": 3, "Hot Sauce": 3,
    "BBQ Sauce": 3, "Pickles": 3, "Cashews": 3, "Walnuts": 3, "Pistachios": 3, "Sunflower Seeds": 3,

    # Newly added items to reach 150
    "Tomato Sauce": 4, "Basil": 3, "Oregano": 3, "Thyme": 3, "Cinnamon": 3, "Paprika": 3, "Curry Powder": 3,
    "Ginger": 3, "Turmeric": 3, "Cilantro": 3, "Parsley": 3, "Dill": 3, "Cabbage": 3, "Radish": 3,
    "Asparagus": 3, "Green Beans": 3, "Brussels Sprouts": 3, "Artichokes": 3, "Bell Peppers": 3,
    "Goat Milk": 3, "Coconut Flour": 3, "Cornmeal": 3, "Tapioca Flour": 3, "Arrowroot Powder": 3,
    "Almond Flour": 3, "Dark Chocolate": 3, "White Chocolate": 3, "Milk Chocolate": 3,
    "Whey Protein": 3, "Plant-Based Protein": 3, "Spaghetti": 3, "Macaroni": 3, "Lasagna Sheets": 3,
    "Ravioli": 3, "Gnocchi": 3, "Kimchi": 3, "Sauerkraut": 3, "Miso Paste": 3, "Tofu": 3, 
    "Tempeh": 3, "Seitan": 3, "Seaweed": 3, "Edamame": 3, "Pecorino Cheese": 3, "Brie Cheese": 3, "Blue Cheese": 3,
    "Polenta": 3, "Hot Chocolate": 3, "Pesto": 3, "Tortilla Chips": 3, "Mexican Sauce": 3, "Sunflower Oil": 3, "Coke-Soda": 7
}




print("Items num:"+str(len(ITEMS)))

# Function to generate synthetic transactions
def generate_transactions(num_transactions=10000, max_items_per_basket=10):
    transactions = []
    item_list = list(ITEMS.keys())
    item_weights = list(ITEMS.values())

    for _ in range(num_transactions):
        basket_size = random.randint(2, max_items_per_basket)  # Basket with at least 2 items
        transaction = random.choices(item_list, 
                                     weights=item_weights,
                                      k=basket_size)
        transactions.append(transaction)

    return transactions

# Generate transactions
num_transactions = 75000  # Adjust as needed
max_items_per_transaction = 7
transactions = generate_transactions(num_transactions,max_items_per_transaction)

# Save to CSV (only items per transaction, comma-separated)
with open("Datasets\synthetic_market_basket.csv", "w") as f:
    for transaction in transactions:
        f.write(",".join(transaction) + "\n")

print(f"Market basket dataset with {num_transactions} transactions saved as 'market_basket.csv'")
