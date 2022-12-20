import xmlrpc.client
import json

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


# Fetch all products
def fetch(email, password, db):
    global url
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, email, password, {})
    result = []
    products = models.execute_kw(db, uid, password, 'product.template', 'search_read', [[]])
    for product in products:
        apartment = models.execute_kw(db, uid, password, 'apartment', 'search_read', [[ 
            ['id', '=', product['apartment_product'][0] ] 
            ]])
        apartment[0]['qty_available'] = product['qty_available']
        result.append(apartment[0])
    return result