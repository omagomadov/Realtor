import xmlrpc.client
import getpass

# Connection information
url = 'http://localhost:8069'
db = None
username = None
password = None


# Display welcome message
def welcome():
    print("##########################################################")
    print("#            |  __ \          | | |                      #")
    print("#            | |__) |___  __ _| | |_ ___  _ __           #")
    print("#            |  _  // _ \/ _` | | __/ _ \| '__|          #")
    print("#            | | \ \  __/ (_| | | || (_) | |             #")
    print("#            |_|  \_\___|\__,_|_|\__\___/|_|             #")
    print("#                   XML-RPC script                       #")
    print("##########################################################")


# Asks credentials
def ask_credential():
    global username
    global password
    global db
    try:
        db = input("Enter your database : ")
        username = input("Enter your login : ")
        password = getpass.getpass("Enter your password : ")
        connect(username, password, db)
    except KeyboardInterrupt:
        print("Exited")


# Connects using given credential
def connect(username, password, db):
    global url
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    try:
        uid = common.authenticate(db, username, password, {})
        if not uid:
            print("Wrong credential")
            ask_credential()
        else:
            print("Successfully connected")
            search(db, uid, password)
    except ConnectionRefusedError:
        print("Cannot connect to localhost server")
    except xmlrpc.client.Fault:
        print("Cannot find database with the name : ", db)
        ask_credential()


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


if __name__ == '__main__':
    welcome()
    ask_credential()
