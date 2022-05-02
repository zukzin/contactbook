names = ["zuki"]
phone_numbers = ["079-968-5547"]


for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    
    names.append(name)
    phone_numbers.append(phone_numbers)

    print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
   

    search_term = input("\nEnter Search Term: ")
    print("Search Resut")
    
    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_number[index]
        print("Name: {}, Phone Number: {}",format(search_term, phone_number))
        
    else:
        print("Name not found")
