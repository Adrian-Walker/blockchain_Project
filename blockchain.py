blockchain = [100]


def get_last_value():
    return blockchain[-1]


def add_one(t):
    blockchain.append([get_last_value(), t])


add_one(200)
add_one(300)
add_one(400)

print(blockchain)
