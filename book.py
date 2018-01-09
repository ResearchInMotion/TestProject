Collection=["Alchemist" , "Scooby Doo" , "Badminton"]
print("Enter the name of the book")
bookToBeChecked=input()
for book in Collection:
    if(book==bookToBeChecked):
        print("yes we have that book !")
        break
else:
    print("I dont have that book")