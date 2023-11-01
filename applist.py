import random

print("Welcome to Avish's screen time app")
apps = []
time = []
option = ""

# menu
while (option != "q"):
    # gives the user all the options to do with there apps 
    print("Option a: Add app to your screen time report ")
    print("Option b: remove app from library ")
    print("Option c: Insert app anywhere")
    print("Option d: swap the order of two of your games")
    print("Option e: print your most used app in the screen report")
    print("Option f: print all your apps of the screen report") 
    print("Option g:  shuffles the order of  the apps")
    print("Option q: Quit ")
    option = input("Choose your option: ")

    # the user will input the app and time he used it for  
    if (option == "a"):
        print() 
        print("You picked option a!")
        app = input("Enter the name of the app: ")
        time_spent = int(input("How many hours: "))
        apps.append(app)
        time.append(time_spent)
        print()

      # the user can remove the app from the list 
    if (option == "b"):
        print()
        i = 0
        print("Your screen app:")
        for each_app in apps:
              print(str(i+1) +":",str(each_app) ,"("+str(time[i]),"hours used" + ")")
              i = i+1
        remove = int(input("which app do you want to remove: "))
        apps.pop(remove - 1)
        time.pop(remove - 1)  
        print()

       # The user can place his app anywhere in the list he wants to 
    if (option == "c"):
        print()
        i = 0
        print("Your screen app:")
        for each_app in apps:
            print(str(i+1) +":",str(each_app) ,"("+str(time[i]),"hours used" + ")")
            i = i+1
        app = input("Enter the name of the app: ")
        time_spent = int(input("How many hours: "))
        placement = int(input("what postion do you want it to be: "))
        apps.insert(placement-1,app)
        time.insert(placement-1,time_spent)
        print()

  # swaps two apps in the list 
    if (option == "d"):
        print()
        i = 0
        print("Your screen app:")
        for each_app in apps:
            print(str(i+1) +":",str(each_app) ,"("+str(time[i]),"hours used" + ")")
            i = i+1
        swap = int(input("which one do you want to swap: "))
        swap_two = int(input("Which is the second one you want to swap: "))
        app = apps[swap-1]
        apps[swap-1] = apps[swap_two-1] # 
        apps[swap_two-1] = app
       # this will swap each other by one of them being a variable 
        time_hours = time[swap-1]
        time[swap-1] = time[swap_two-1]
        time[swap_two-1] = time_hours
          # does the same thing but with time
        print()
        
      # it displays the users app with the most hours 
    if (option == "e"):
        print()
        max_hours = max(time) # finds the most hours in time list
        hours_in = time.index(max_hours) # finds its index so it can pair with the app
        print("Your most viewed app is",apps[hours_in],"with",max_hours,"hours viewed!")
        print()

  # displays full list of apps and hours
    if (option == "f"):
         print()
         i = 0
         print("Your screen app:")
         for each_app in apps:
              print(str(i+1) +":",str(each_app) ,"("+str(time[i]),"hours used" + ")")
              i = i+1
     
         print()
       # this will shuffle the users apps in the list 
    if (option == "g"):
        print()
        double_list = []
        for i in range(len(time)):
          double_list.append((apps[i],time[i]))
        random.shuffle(double_list)
        for i in range(len(double_list)):
          apps[i],time[i] = double_list[i]
    
    if (option == "q"):
       print()
       print("Good bye!!!")
       quit()
