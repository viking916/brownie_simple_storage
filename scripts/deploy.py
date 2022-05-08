from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():

    # By default it pulls test ganache address
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.get()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.get()
    print(updated_stored_value)
    # Safest way to store private key, Loading on net accounts metamask,trustwallet etc
    # account = accounts.load("rinkby_1")
    # print(account)

    # Storing private key in env file, risky. Not advisable for real live accounts
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)

    # Using wallet key from config file to get account info
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
