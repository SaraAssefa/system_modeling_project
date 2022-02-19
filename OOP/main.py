import jsonschema
class Address(object):
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __str__(self):
        return "{0} {1}".format(self.street, self.number)

class User(object):
    def __init__(self, name, address):
        self.name = name
        self.address = Address(**address)

    def __str__(self):
        return "{0} ,{1}".format(self.name, self.address)

if __name__ == '__main__':
    js = '''{"name":"Sara", "address":{"street":"Mulatiear","number":8}}'''
    j = jsonschema.loads(js)
    print(j)
    u = User(**j)
    print(u)