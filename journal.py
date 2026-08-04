#def write_entry():
#    pass      # in down we removed it bcoz we wrote here bcoz we can't write here as empty so  

# we created empty bcoz example if we r building a house we won't start painting, furniture and all. we just start with empty 
# kitchen, room, washroom and all and later after few months we can develop it
#    " IT IS CALLED AS SOFTWARE DESIGN "

# It's like building a skeleton before adding muscle

def write_entry(entry):
    file=open("journal.txt","a")
    file.write(entry + "\n")
    file.close()
    print("Saved sucessfully")

def view_entries():
    file=open("journal.txt","r")
    content=file.read()
    print(content)
    file.close()

def search_entry(word):
    file=open("journal.txt","r")
    content=file.read()

    if word in content:
        return True
    else:
        return False



