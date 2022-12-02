import xmlrpc.client
import getpass

# Connection information
url = 'http://localhost:8069'
db = 'dev01'
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
def askCredential():
    global username
    global password
    username = input("Enter your login : ")
    password = getpass.getpass("Enter your password : ")
    connect(username, password)


# Connects using given credential
def connect(username, password):
    global url
    global db
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    try:
        uid = common.authenticate(db, username, password, {})
        if not uid:
            print("Wrong credential")
            askCredential()
        else:
            print("Successfully connected")
            search(db, uid, password)
    except ConnectionRefusedError:
        print("Cannot connect to localhost server")


def search(db, uid, password):
    global url
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    command = ''
    result = None
    while command != 'quit':
        command = input("Enter the name of an apartment : ")
        result = models.execute_kw(db, uid, password, 'apartment', 'search_read', [[['name', '=', command]]])
        if result:
            for apartment in result:
                print("=> The name :", apartment['name'])
                if not apartment['description']:
                    print("=> The description : (nothing)")
                else:
                    print("=> The description :", apartment['description'])
                print("=> The price : ", apartment['price'], "$")
                print("=> The available date :", apartment['available_date'])
        elif command != 'quit':
            print("Cannot find an apartment with the name", command)
        else:
            print("Exited")


if __name__ == '__main__':
    welcome()
    askCredential()
