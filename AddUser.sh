#!/bin/bash
# Provide bash script to request name from user and 
# adds user.

# Main Application
# Will perform addUser 
addUser(){
    
    # From user input name, create user
    sudo adduser $name
    # Wait a moment to create user
    sleep 1
    # Add user to group user specifies
    sudo usermod -aG $group $name
}

# Gets continue value from user
echo "Would you like to add a user [y/n]"
read cont


while [ $cont = "y" ]; do   

    # Get user name
    echo "Enter Name of user"
    read name
    
    # Get group name
    echo "Enter Name of Group, example people"
    read group

    # Invokes addUser function
    addUser

    # Repeat upon user input
    echo "Would you like to add another user [y/n]"
    read cont
done
    echo "Finished"   




