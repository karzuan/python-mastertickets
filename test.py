def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError( "It's too short for a new Idea name!")
    return product_idea + "inator"

newname = input("Enter the name ")
print( suggest(newname) )