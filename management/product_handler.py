from menu import products

def get_product_by_id(id: int):

    if not type (id) is int:
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product
    return{}

def get_products_by_type(types: str):
    result = []

    if not type(types) is str:
        raise TypeError("product type must be a str")

    for item in products:
        if item["type"] == types:
            result.append(item)

    return result   


def add_product(menu, **new_product):
    if len(menu):
        max_id = max(item['_id'] for item in menu)
        new_product['_id'] = max_id + 1
        menu.append(new_product)
        return new_product
    new_product['_id'] = 1 
    menu.append(new_product)
    return new_product
        

def menu_report():
    amount_products = len(products)
    price_total = 0
    most_common_type = {}

    for item in products:
        price_total += item["price"]
        product_type = item["type"]
        if product_type in most_common_type:
            most_common_type[product_type] += 1
        else:
            most_common_type[product_type] = 1

    price_average = price_total / amount_products
    price_average = round(price_average, 2)

    most_common = max(most_common_type, key=most_common_type.get)

    result_str = f"Products Count: {amount_products} - Average Price: ${price_average} - Most Common Type: {most_common}"

    return result_str       

def add_product_extra(menu: list, *args, **kwargs):

    for required_key in args:
        if required_key not in kwargs:
            raise KeyError(f"field {required_key} is required")
    new_user = kwargs.copy()
    for request_key in kwargs.keys():
        if request_key not in args:
            del new_user[request_key]

    res = add_product(menu, **new_user)
    menu.append(res)
    return res

