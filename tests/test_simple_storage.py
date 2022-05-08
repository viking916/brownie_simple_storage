from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.get()
    expected_val = 0

    # Assert
    assert starting_value == expected_val


def test_updating_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(15, {"from": account})
    updated_value = simple_storage.get()
    expected_val = 15
    assert updated_value == expected_val
