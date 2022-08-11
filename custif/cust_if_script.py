#!/usr/bin/env python3


## Program allows users to select movie and returns synopsis


## Movie Selection List
movies=["Harry Potter","Hobbit & Lord of the Rings","Chronicles of Narnia","Indiana Jones"]

## Movie SynopsisList
movieSynopsis=["Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.","The unwilling hero of The Hobbit, Bilbo Baggins, is persuaded to join Thorin and his 12 dwarfs to recover their stolen treasure, which is being guarded by the dragon Smaug. During the expedition, Bilbo finds a magical ring that renders the wearer invisible, which figures prominently in The Lord of the Rings.","During the World War II bombings of London, four English siblings are sent to a country house where they will be safe. One day Lucy (Georgie Henley) finds a wardrobe that transports her to a magical world called Narnia. After coming back, she soon returns to Narnia with her brothers, Peter (William Moseley) and Edmund (Skandar Keynes), and her sister, Susan (Anna Popplewell). There they join the magical lion, Aslan (Liam Neeson), in the fight against the evil White Witch, Jadis (Tilda Swinton).","Epic tale in which an intrepid archaeologist tries to beat a band of Nazis to a unique religious relic which is central to their plans for world domination. Battling against a snake phobia and a vengeful ex-girlfriend, Indiana Jones is in constant peril, making hair's-breadth escapes at every turn in this celebration of the innocent adventure movies of an earlier era."]
print("Choose Movie","1.) Harry Potter","2.) Hobbit & Lord of the Rings","3.) Chronicles of Narnia","4.) Indiana Jones", end="\n")

## Acquires movies selection from user
connection = float(input("Select movie choose."))

## Initializes return message
message=""
# if input value was is between 1-4
if connection == 1:
    message = "MovieChosen is: "+str(movies[0])+"\n\nSynopsis:\n" + str(movieSynopsis[0])
elif connection == 2:
    message = "MovieChosen is: "+str(movies[1])+"\n\nSynopsis:\n" + str(movieSynopsis[1])
elif connection == 3:
    message = "MovieChosen is: "+str(movies[2])+"\n\nSynopsis:\n" + str(movieSynopsis[2])
elif message == 4:
    message = "MovieChosen is: "+str(movies[3])+"\n\nSynopsis:\n" + str(movieSynopsis[3])
else:
    message = message + 'Incorrect Input.'

## Prints return message to user
print(message)
