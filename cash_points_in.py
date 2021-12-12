simple_user_database = {
    'Master Moonlarkian':7000,
    'yap30317' : 0,
    'faithyhuong' : 0,
    'Siti Jazmina Abd Rashid' : 0,
    'Tester' : 0,
    'nellytingshisiu' : 0,
    'ernernmooi' : 0,
    'bor' : 0
}

simple_prize_database = { 
    'Hoodie' : 1500 ,
    'Bottle' : 1000 ,
    'Notebook' : 1000 ,
    'Phone case' : 1700,
    'Custom Playing Cards' : 5000
 }


def prizeItems (item) :
    if item in simple_prize_database:
        # if item does exist, return the point
        return simple_prize_database [item]
    else:
        #if item doesn't exist, throw an error
        raise ValueError ("Category doesn/'t exist")



user = input('What is your name?')
points = simple_user_database[user]

def deductPoints (user,points):
    #deduct points to existing points
    
    if user in simple_user_database:
        if simple_user_database[user] >= 1000:

            print('do you want to buy?')
            print('Yes/No')
            Answer = input('Answer')

            if Answer == 'No':
                print('ok bye')
            else:
                Current = simple_user_database[user]
                item=input("Enter your item: ")
                prize = prizeItems(item) 
                if prize < Current:
                     print(Current - prize)
                     print('Thank you!')
                else:
                    print('you do not have enough points')


            
                
            return simple_user_database[user]
    else:
        simple_user_database[user] = points
        return simple_user_database [user]
    
deductPoints(user,points)

   












