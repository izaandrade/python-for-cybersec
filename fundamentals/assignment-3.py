#Create an inventory tracking system that has all of the following features:
    #Each item will have a name, quantity, and description as a dictionary.
    #All dictionaries will be saved in a master inventory list.
    #A function that adds something to that list (creates the dictionary and adds to the list).
    #A function that displays the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).
    #A function that will change the quantity of an item (this is difficult to do and many ways to do it).
    #A function that removes an item from the list. Research required :)


inventory = [] # para criar list, entre chaves
items = {} # para criar um dictionary, entre colchetes

while True: 
    option = input('1 - set an item // 2 - display inventory // 3 - change the quantity of an item '
'// 4 - remove an item from the list // 5 - exit') # criando menuzito
    option = int(option) # garantindo que as opções são números inteiros

    if option == 1:
        name = input('enter a name>> ')
        quantity = int(input('set the quantity>> '))
        description = input('enter a description>> ')
        item = {'name': name, 'quantity': quantity, 'description': description}  # cria um dictionary para o item
        inventory.append(item)  # append eh a call que adiciona o item entre parenteses à lista mencionada 
        print('item added to inventory successfully!')

    elif option == 2:
        print("inventory:")
        for idx, item in enumerate(inventory, start=1): # idx enumera os item no inventário para posterior consulta ou alteração
            print(f"{idx}. name: {item['name']}, quantity: {item['quantity']}, description: {item['description']}") # lista o item e suas características

    elif option == 3:
        if not inventory:
            print('no item is set yet. add an item to be able to change it')
        else:
            print('inventory:')
            for idx, item in enumerate(inventory, start=1):
                print(f"{idx}. name: {item['name']}, quantity: {item['quantity']}, description: {item['description']}")
            
            try:
                item_index = int(input('enter the number of the item you want to change the quantity: ')) - 1
                if 0 <= item_index < len(inventory): # o 'len' verifica quantos itens tem na lista para garantir que o numero que o user colocou existe
                    new_quantity = int(input(f"enter the new quantity for {inventory[item_index]['name']}: "))
                    inventory[item_index]['quantity'] = new_quantity
                    print('quantity updated!')
                else:
                    print('invalid item number. try again.')
            except ValueError:
                print('invalid input. enter a valid number.')

    elif option == 4:
        if not inventory:
            print('no item is setted yet. add items first!')
        else:
            print('inventory: ')
            for idx, item in enumerate(inventory, start=1): 
                print(f"{idx}. name: {item['name']}, quantity : {item['quantity']}, description: {item['description']}")
            try: 
                item_index = int(input('enter the number or the item you want to change')) - 1
                if 0 <= item_index < len(inventory):
                    removed_item = inventory.pop(item_index) # pop apaga o item do inventário
                    print(f"item {removed_item['name']} removed") 
                else:
                    print('invalid number. try again.')
            except ValueError:
                print('invalid input. enter a valid number.')         

    elif option == 5: 
        print('closing the program, goodbye!')
        break # para a exibição do menu

    else:
        print( 'please choose a valid option')
