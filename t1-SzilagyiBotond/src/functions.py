def get_product_name(product):
    return product["name"]


def set_product_name(product, new_name):
    product["name"] = new_name


def get_quantity(product):
    return product["quantity"]


def set_quantity(product, new_quantity):
    product["quantity"] = new_quantity


def get_price(product):
    return product["price"]


def set_price(product, new_price):
    product["price"] = new_price


def create_product(name, quantity, price):
    return {"name": name, "quantity": quantity, "price": price}


def add_product(all_products, name, quantity, price):
    new_product = create_product(name, quantity, price)
    all_products.append(new_product)


def delete_product(all_products, name):
    result = list(filter(lambda products: products["name"]!=name,all_products))
    return result

def test_add():
    all_products=[]
    add_product(all_products,"apple",10,10)
    assert all_products[0]["name"]=="apple",("Addition not working")
    add_product(all_products,"alma",10,10)
    assert all_products[1]["quantity"]==10,("Addition not working")

def test_delete():
    all_products=[]
    add_product(all_products,"apple",10,10)
    add_product(all_products,"alma",10,10)
    all_products=delete_product(all_products,"apple")
    assert all_products[0]["name"]=="alma",("Delete not working")