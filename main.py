print("========================================")
print("         PERSONAL JOURNAL               ")
print("========================================")
print("1.Write new entry")
print("2.View all entries")
print("3.Search entry")
print("4.Exit")
print("Welcome developer")

choice=int(input("Enter your choice (1-4):"))

import journal

if choice==1:
    entry=input("Enter today's entry:")
    journal.write_entry(entry)      
elif choice==2:
    journal.view_entries()
elif choice==3:
    word=input("Enter the word to be searched:")
    found=journal.search_entry(word)
    if found:
        print("Entry found")
    else:
        print("Entry not found")
elif choice==4:
    print("Thank you for using personal journal")
else:
    print("Invalid choice, please enter 1 2 3 or 4")

    print("delete entry feature")

    print("branch push practice")

     # no need to write like result=journal.write_entry like that, see i am not going to print anything, it happes automatic so no need 


    
