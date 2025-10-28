import pandas as pd
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_trip(value):
    if value == 1:
        return "First big trip (2007)"
    elif value == 2:
        return "Great Lakes trip (2009)"
    elif value == 3:
        return "Second big trip (2010)"
    elif value == 4:
        return "Louisiana/Texas trip (2012)"
    elif value == 5:
        return "Third big trip (2016)"
    elif value == 6:
        return "New England trip (2018)"
    elif value == 7:
        return "Canada trip (2019)"
    elif value == 8:
        return "Coaster trip (2021)"
    elif value == 9:
        return "Eclipse trip (2024)"
    elif value == 10:
        return "Fifth big trip (2025)"
    
def show_states():
    print("1. Alabama           26. Montana")
    print("2. Alaska            27. Nebraska")
    print("3. Arizona           28. Nevada")
    print("4. Arkansas          29. New Hampshire")
    print("5. California        30. New Jersey")
    print("6. Colorado          31. New Mexico")
    print("7. Connecticut       32. New York")
    print("8. Delaware          33. North Carolina")
    print("9. Florida           34. North Dakota")
    print("10. Georgia          35. Ohio")
    print("11. Hawaii           36. Oklahoma")
    print("12. Idaho            37. Oregon")
    print("13. Illinois         38. Pennsylvania")
    print("14. Indiana          39. Rhode Island")
    print("15. Iowa             40. South Carolina")
    print("16. Kansas           41. South Dakota")
    print("17. Kentucky         42. Tennessee")
    print("18. Louisiana        43. Texas")
    print("19. Maine            44. Utah")
    print("20. Maryland         45. Vermont")
    print("21. Massachusetts    46. Virginia")
    print("22. Michigan         47. Washington")
    print("23. Minnesota        48. West Virginia")
    print("24. Mississippi      49. Wisconsin")
    print("25. Missouri         50. Wyoming")

def show_trips():
    print("1. First big trip (2007)")
    print("2. Great Lakes trip (2009)")
    print("3. Second big trip (2010)")
    print("4. Louisiana/Texas trip (2012)")
    print("5. Third big trip (2016)")
    print("6. New England trip (2018)")
    print("7. Canada trip (2019)")
    print("8. Coaster trip (2021)")
    print("9. Eclipse trip (2024)")
    print("10. Fifth big trip (2025)")

df = pd.read_csv('states.csv')

#print(df.to_string())
#print(df[["State", get_trip(1)]])

MainMenuLoop = True
Menu1Loop = False
Menu2Loop = False

while MainMenuLoop:
    print("1. Look up by state")
    print("2. Look up by trip")
    print("3. Quit")
    first_choice = input("Which would you like to do?: " )
    try:
        first_int = int(first_choice)
        if (first_int == 1):
            MainMenuLoop = False
            Menu1Loop = True
        elif (first_int == 2):
            MainMenuLoop = False
            Menu2Loop = True
        elif (first_int == 3):
            MainMenuLoop = False
    except ValueError:
        print()

while Menu1Loop:
        show_states()
        choice = input("Select a state, or enter 0 to quit: ")
        try:
            choice_int = int(choice)
            if choice_int == 0:
                Menu1Loop = False
            else:
                if (choice_int > 50):
                    print("Please enter a smaller number.")
                elif (choice_int < 0):
                    print("You can't enter a negative number.")
                else:
                    count = 0
                    clear()
                    print(df.iat[choice_int - 1, 0])
                    if ((df.iat[choice_int - 1, 1]) == True):
                        print("First big trip (2007)")
                        count += 1
                    if ((df.iat[choice_int - 1, 2]) == True):
                        print("Great Lakes trip (2009)")
                        count += 1
                    if ((df.iat[choice_int - 1, 3]) == True):
                        print("Second big trip (2010)")
                        count += 1
                    if ((df.iat[choice_int - 1, 4]) == True):
                        print("Louisiana/Texas trip (2012)")
                        count += 1
                    if ((df.iat[choice_int - 1, 5]) == True):
                        print("Third big trip (2016)")
                        count += 1
                    if ((df.iat[choice_int - 1, 6]) == True):
                        print("New England trip (2018)")
                        count += 1
                    if ((df.iat[choice_int - 1, 7]) == True):
                        print("Canada trip (2019)")
                        count += 1
                    if ((df.iat[choice_int - 1, 8]) == True):
                        print("Coaster trip (2021)")
                        count += 1
                    if ((df.iat[choice_int - 1, 9]) == True):
                        print("Eclipse trip (2024)")
                        count += 1
                    if ((df.iat[choice_int - 1, 10]) == True):
                        print("Fifth big trip (2025)")
                        count += 1

                    if (count == 0):
                        print("We did not visit this state on any of the \"trip journal\" trips.")
                    elif (choice_int == 18):
                        print("\nWe visited this trip on 1 \"trip journal\" trip. \nDespite that, before I had the trip journal, I received the book \nthat inspired the trip journal on my first trip to Louisiana!")
                    elif (count == 1):
                        print("\nWe visited this trip on 1 \"trip journal\" trip.")
                    elif (choice_int == 46):
                        print("\nOf course we went to Virginia on these trips, silly!")
                    else:
                        print(f"\nWe visited this trip on {count} \"trip journal\" trips.")
                    #print(df.iat[choice_int - 1, 2])
                    #print(df.iat[choice_int - 1, 3])
                    #print(df.iat[choice_int - 1, 4])
                    #print(df.iat[choice_int - 1, 5])
                    #print(df.iat[choice_int - 1, 6])
                    #print(df.iat[choice_int - 1, 7])
                    #print(df.iat[choice_int - 1, 8])
                    #print(df.iat[choice_int - 1, 9])
                    #print(df.iat[choice_int - 1, 10])
                    input("Press any key to continue.")
                    clear()

        except ValueError:
            print("Please enter a valid integer.")

while Menu2Loop:
    show_trips()
    second_choice = input("Select a trip, or enter 0 to quit: ")
    try:
        second_int = int(second_choice)
        if second_int == 0:
            Menu2Loop = False
        else:
            if (second_int > 10):
                print("Please enter a smaller number.")
            elif (second_int < 0):
                print("You can't enter a negative number.")
            else:
                clear()
                filter = df[df[get_trip(second_int)]]

                #print(df[["State", get_trip(second_int)]])
                #print(filter)
                #print(filter[["State", get_trip(second_int)]])
                print(get_trip(second_int))
                print(filter["State"].to_string(index=False))
                input("Press any key to continue.")
                clear()

    except ValueError:
        print("Please enter a valid integer.")

#print(df.loc[0])