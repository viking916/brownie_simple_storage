//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 favouriteNumber;
    string name;

    struct People {
        uint256 favouriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavouriteNumber;

    function store(uint256 _favouriteNumber) public returns (uint256) {
        favouriteNumber = _favouriteNumber;
        return _favouriteNumber;
    }

    function get() public view returns (uint256) {
        return favouriteNumber;
    }

    function addToPerson(uint256 _favouriteNumber, string memory _name) public {
        people.push(People(_favouriteNumber, _name));
        nameToFavouriteNumber[_name] = _favouriteNumber;
    }

    // function getArrayItem(uint256 index) public view returns (memory string){
    //     return people[index][name];
    // }
}
