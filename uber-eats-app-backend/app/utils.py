def search_restaurants(restaurants, query):
    """Search restaurants by name or cuisine."""
    return [
        r for r in restaurants if query in r['name'].lower() or query in r['cuisine'].lower()
    ]

def filter_restaurants(restaurants, location, cuisine):
    """Filter restaurants by location and/or cuisine."""
    result = restaurants
    if location:
        result = [r for r in result if location in r['location'].lower()]
    if cuisine:
        result = [r for r in result if cuisine in r['cuisine'].lower()]

    return result
