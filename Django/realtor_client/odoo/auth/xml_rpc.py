import xmlrpc.client

# Connection information
url = 'http://localhost:8069'

# Connects using given credential
def connect(username, password, db):
    global url
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    try:
        uid = common.authenticate(db, username, password, {})
        if not uid:
            return False
        else:
            return True
    except ConnectionRefusedError:
        return False
    except xmlrpc.client.Fault:
        return False


# Search an apartment
def search(db, uid, password):
    global url
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    command = ''
    while command != 'quit':
        command = input("Enter the name of an apartment : ")
        products = models.execute_kw(db, uid, password, 'product.template', 'search_read', [[
            ['apartment_product.name', '=', command]
        ]])
        if products:
            for product in products:
                apartments = models.execute_kw(db, uid, password, 'apartment', 'search_read', [[
                    ['name', '=', command]
                ]])
                for apartment in apartments:
                    print("=> Name :", apartment['name'])
                    if not apartment['description']:
                        print("=> Description : (nothing)")
                    else:
                        print("=> Description :", apartment['description'])
                    print("=> Price : ", apartment['price'], "$")
                    print("=> Available date :", apartment['available_date'])
                print("=> Quantity of available apartments", command, ": ", product['qty_available'])
        elif command != 'quit':
            print("Cannot find an product with the apartment name", command)
        else:
            print("Exited")
