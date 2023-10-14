from menu import products

def calculate_tab (table):
    subtotal = 0
    for product in products:
        for item in table: 
            if product['_id'] == item['_id']:
                print (product)
                subtotal += item['amount'] * product['price']
    return {"subtotal": f'${round(subtotal,2)}'}                
