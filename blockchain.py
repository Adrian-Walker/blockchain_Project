blockchain = []


def get_last_value():
    return blockchain[-1]


def add_one(transaction, last_transaction=[1]):
    blockchain.append([last_transaction, transaction])


add_one(200)
add_one(300, get_last_value())
add_one(400, get_last_value())

print(blockchain)
