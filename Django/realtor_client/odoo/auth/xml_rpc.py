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


# Submit offer
def submit(email, password, db, name, offer, apartment):
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, email, password, {})

    fetched_apartment = models.execute_kw(db, uid, password,'apartment', 'search_read', [[['name', '=', apartment]]])
    apartment_id = [fetched_apartment[0]['id'], fetched_apartment[0]['name']]

    if fetched_apartment[0]['offer'] < int(offer) and ((fetched_apartment[0]['offer'] / 100) * 90) < int(offer):
        print('Given price is higher')
        search_user = models.execute_kw(db, uid, password,'res.partner', 'search_read', [[['name', '=', name]]])
        if len(search_user) == 0:
            print('User does not exist')
            models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': name}])
            search_user = models.execute_kw(db, uid, password,'res.partner', 'search_read', [[['name', '=', name]]])
        models.execute_kw(db, uid, password, 'res.partner', 'write', [search_user[0]['id'], {'apartment' : apartment_id[0], 'offered_price': int(offer)}])