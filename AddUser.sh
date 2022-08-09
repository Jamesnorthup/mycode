#!/bin/bash
# Provide bash script to request name from user and 
# adds user.

# Main Application
# Will perform addUser 
addUser(){

    sudo adduser $name
    sleep 1
    sudo usermod -aG $group $name
}
echo "Would you like to add a user [y/n]"
read cont


while [ $cont = "y" ]; do   
    echo "Enter Name of user"
    read name
    echo "Enter Name of Group, example people"
    read group
    addUser
    echo "Would you like to add another user [y/n]"
    read cont
done
    echo "Finish"   




