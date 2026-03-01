def categorize_expense(description):
    categories = {
        "food": ["swiggy", "zomato", "restaurant"],
        "transport": ["uber", "ola", "metro"],
        "shopping": ["amazon", "flipkart"]
    }

    for category, keywords in categories.items():
        for word in keywords:
            if word in description.lower():
                return category

    return "other"