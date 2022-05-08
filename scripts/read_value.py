from brownie import SimpleStorage, accounts, config


def read_contract():
    # Use -1 to read latest deployed contract, 0 to read the first deployed contract
    simple_storage = SimpleStorage[-1]
    # Take the index thats one lexx than the length
    # ABI
    # Address
    print(simple_storage.get())


def main():
    read_contract()
