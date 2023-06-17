cards_dict = {
    1 :[1,"h"],    2 :[1, "s"],  3  :[1, "c"],   4:[1, "d"],
    5 :[13, "h"],  6 :[ 13,"s"], 7  :[ 13,"c"],  8: [ 13, "d"],
    9 :[12, "h"],  10:[ 12,"s"], 11:[ 12,"c"],  12:[ 12, "d"],
    13:[11, "h"],  14:[ 11,"s"], 15:[ 11,"c"],  16:[ 11, "d"],
    17:[2, "h"],   18:[ 2,"s"],  19:[ 2,"c"],   20:[ 2, "d"],
    21:[3, "h"],   22:[ 3,"s"],  23:[ 3,"c"],   24:[ 3, "d"],
    25:[4, "h"],   26:[ 4,"s"],  27:[ 4,"c"],   28:[ 4, "d"],
    29:[5, "h"],   30:[ 5,"s"],  31:[ 5,"c"],   32:[ 5, "d"],
    33:[6, "h"],   34:[ 6,"s"],  35:[ 6,"c"],   36:[ 6, "d"],
    37:[7, "h"],   38:[ 7,"s"],  39:[ 7,"c"],   40:[ 7, "d"],
    41:[8, "h"],   42:[ 8,"s"],  43:[8,"c"],    44:[ 8, "d"],
    45:[9, "h"],   46:[ 9,"s"],  47:[ 9,"c"],   48:[ 9, "d"],
    49:[10, "h"],  50:[ 10,"s"], 51:[ 10,"c"],  52:[ 10, "d"]
}
lis = [17, 21, 25, 29, 33]
sorted_lis = sorted(lis)
card_lis = []
card = []
suit = []
for i in sorted_lis:
    card_lis.append(cards_dict[i])

for i in card_lis:
    card.append(i[0])
    suit.append(i[1])

card = sorted(card)

def checkthecard(suit, card):
    if len(set(suit)) == 1:
        #check for royal flush
        if (card[0] == card[1] and card[0] == card[2] and card[0] == card[3] and card[0] == card[4]):
            a = ("Its a **ROYAL FLUSH CARD**")
    
        elif (card[4] - card[3] == 1 and card[3] - card[2] == 1 and card[2] - card[1] == 1 and card[1] - card[0] == 1 ):
            a = ("Its a **Straight flush card**")
    
        else:
            a = ("It's a **Flush card**")
        
        return a

    elif (card[4] - card[3] == 1 and card[3] - card[2] == 1 and card[2] - card[1] == 1 and card[1] - card[0] == 1 ):
        print("Its a **Straight card**")

    elif (card[0] == card[1] and card[0] == card[2] and card[0] == card[3]) or (card[1] == card[2] and card[1] == card[3] and card[1] == card[4]):
        print("It's a **Four of a Kind Card**")
    
    elif (card[0] == card[1] and card[0] == card[2] and card[3] == card[4]) or (card[0] == card[1] and card[2] == card[3] and card[2] == card[4]):
        print("It's a **FUll house card**")
    
    elif (card[0] == card[1] and card[0] == card[2]) or (card[2] == card[3] and card[2] == card[4]):
        print("It's a **Three of a Kind Card**")
    
    elif (card[0] == card[1] and card[2] == card[3]) or (card[1] == card[2] and card[3] == card[4]):
        print("It's a **Two Pairs Card**")
    
    elif (card[0] == card[1]) or (card[1] == card[2]) or (card[2] == card[3]) or (card[3] == card[4]):
        print("It's a **One Pair Card**")
    
    else:
        print("Its a **High card**")

checks = checkthecard(suit, card)
print(checks)
    

