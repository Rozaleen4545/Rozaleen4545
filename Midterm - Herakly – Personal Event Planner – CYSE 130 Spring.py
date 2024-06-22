print("Welcome to the Event Planner!")

# Ask the user to choose the type of event
print("Choose the type of event:")
print("1. Engagement")
print("2. Graduation")
print("3. Wedding")

#Get the User's input
event_choice = input("Enter the number next to your event type: ")

# Use conditional statements to branch based on the event type
if event_choice == "1":
       print("You choose Engagement! Let's plan a great celebration!")
       # Ask for the full date of the event in "YYYY-MM-DD" format
       print("Please enter the date!")
       event_date = input("Enter the full date of the Engagement (YYYY-MM-DD): ")
       # Use slicing to display the year, month, and day separately
       year = event_date[:4]
       month = event_date[5:7]
       day = event_date[8:]
       print(f"Year: {year}, month={month}, day= {day}")
       # Ask the user to input the name of the event
       event_name = input("Please enter the name of the Engagement: ")
       # Create an acronym from the name of the event
       if event_name:
         first_letter = event_name[0]
         last_letter = event_name[-1]
         acronym = first_letter + last_letter
       else:
         acronym = "Input not given."
       # Display the acronym
       print(f"The acronym for the Engagement is '{acronym}'.")
       # Ask the user to enter the number of guests
       number_of_guests = int(input("Please enter the number of guests:"))
       # Give advice based on the number of guests
       if number_of_guests <= 50:
          Venue_type=input("You're planning a small-sized gathering. Based on your guest count and event type, I recomend recommend the following venues: Restaurant (1) / Scenic rooftop (2) / Bar(3) ")
          if Venue_type == "1": 
           print( "You choose a Restruant.")  
           choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
           if choice == '1':
           # Vegan options
            print("Here are some Vegan menu suggestions:Vegan Burger")
           elif choice == '2':
           # Gluten-Free options
            print("Here are some Gluten-Free menu suggestions: Chicken Salad")
           elif choice=="3":
           # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")
           else:
             print("Invaild")
 
          elif Venue_type == "2":
             print("You choose a Scenic rooftop.")
             choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
             if choice == '1':
         # Vegan options
              print("Here are some Vegan menu suggestions: Vegan Burger")
             elif choice == '2':
          # Gluten-Free options
              print("Here are some Gluten-Free menu suggestions:Chicken Salad")
             elif choice=="3":
         # Vegatrian option
              print("Here are some Vegatrain Options:Stuffed Peppers")
             else:
              print("Invalid")

          elif Venue_type == "3":
           print("You choose Bar.") 
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
            print("Here are some Vegan menu suggestions: Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
            print("Here are some Gluten-Free menu suggestions:Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")
          else: 
           print("Invaild Choice. Please choose numbers 1-3")

       elif 51 <= number_of_guests <= 100:
        Venue_type=input("You're planning a medium-sized gathering. You should consider a venues such as: Hotel (1) / Banquet room (2) / Vineyard (3) ")
        if Venue_type == "1": 
            print( "You choose a Hotel.")
            choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
        if choice == '1':
         # Vegan options
            print("Here are some Vegan menu suggestions:Vegan Burger")
        elif choice == '2':
          # Gluten-Free options
            print("Here are some Gluten-Free menu suggestions: Chicken Salad")
        elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

        elif Venue_type == "2":
          print("You choose a Banquet Room.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

        elif Venue_type == "3":
            print("You choose Vineyard.") 
            choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
            if choice == '1':
         # Vegan options
             print("Here are some Vegan menu suggestions:Vegan Burger")
            elif choice == '2':
          # Gluten-Free options
             print("Here are some Gluten-Free menu suggestions: Chicken Salad")
            elif choice=="3":
         # Vegatrian option
             print("Here are some Vegatrain Options:Stuffed Peppers")
       
       else:
        Venue_type=input("You're planning a large - sized gathering. I recommend the following Venues: Banquet Hall (1) / Garden (2) / Outdoor park (3)")
        if Venue_type == "1":
         print("You choose Banquet Hall.")
         choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
         if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
         elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
         elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

        elif Venue_type == "2":
         print("You choose a Garden.")
         choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
         if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
         elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
         elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

        elif Venue_type == "3":
         print("You choose a Outdoor Park")
         choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
         if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
         elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
         elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")
        else: 
         print("Invaild Choice. Please choose numbers 1-3")

elif event_choice == "2":
    print("You choose Graduation! Lets plan a wonderful ceremony!")
    # Ask for the full date of the event in "YYYY-MM-DD" format
    print("Please enter the date!")
    event_date = input(f"Enter the full date of the Graduation (YYYY-MM-DD): ")
    # Use slicing to display the year, month, and day separately
    year = event_date[:4]
    month = event_date[5:7]
    day = event_date[8:]
    print(f"Year: {year}, month={month}, day= {day}")
    # Ask the user to input the name of the event
    event_name = input("Please enter the name of the Graduation: ")
    # Create an acronym from the name of the event
    if event_name:
         first_letter = event_name[0]
         last_letter = event_name[-1]
         acronym = first_letter + last_letter
    else:
         acronym = "Input not given."
    # Display the acronym
    print(f"The acronym for the Graduation is '{acronym}'.")
     # Ask the user to enter the number of guests
    number_of_guests = int(input("Please enter the number of guests: "))
     # Give advice based on the number of guests
    if number_of_guests <= 50:
      Venue_type = input("You're planning a small-sized gathering. A cozy and small venue might be ideal such as: Restaurant (1) / Event Hall (2) / Garden (3).")
      if Venue_type == "1": 
          print( "You choose a Restaurant.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

      elif Venue_type == "2":
          print("You choose a Event Hall.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

      elif Venue_type == "3":
            print("You choose Garden.") 
            choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
            if choice == '1':
         # Vegan options
              print("Here are some Vegan menu suggestions:Vegan Burger")
            elif choice == '2':
          # Gluten-Free options
              print("Here are some Gluten-Free menu suggestions: Chicken Salad")
            elif choice=="3":
         # Vegatrian option
               print("Here are some Vegatrain Options:Stuffed Peppers")
      else: 
          print("Invaild Choice. Please choose numbers 1-3")

    elif 51 <= number_of_guests <= 100:
       Venue_type = input("You're planning a medium-sized gathering. You should consider a venue such as: Hotel (1) / Ballhouse (2) / Large Restaurant (3).")
       if Venue_type == "1":
          print("You choose Hotel.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

       elif Venue_type == "2":
          print("You choose a Ballhouse.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

       elif Venue_type == "3":
          print("You choose a Large Restaurant")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")
       else: 
          print("Invaild Choice. Please choose numbers 1-3")

    else:
        Venue_type=input("You're planning a large - sized gathering. I recommend the following Venues: Banquet Hall (1) / University event space (2) / Outdoor park (3)")
    if Venue_type == "1":
         print("You choose Banquet Hall.")
         choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
         if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
         elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
         elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

    elif Venue_type == "2":
         print("You choose a University Event Space.")
         choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
         if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
         elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
         elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

    elif Venue_type == "3":
         print("You choose a Outdoor Park")
         choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
         if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
         elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
         elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")
    else: 
         print("Invaild Choice. Please choose numbers 1-3")

elif event_choice == "3":
    print("You choose Wedding! Let's plan a great reception!")
    # Ask for the full date of the event in "YYYY-MM-DD" format
    print("Please enter the date!")
    event_date = input(f"Enter the full date of the Wedding (YYYY-MM-DD): ")
    # Use slicing to display the year, month, and day separately
    year = event_date[:4]
    month = event_date[5:7]
    day = event_date[8:]
    print(f"Year: {year}, month={month}, day= {day}")
    # Ask the user to input the name of the event
    event_name = input("Please enter the name of the Wedding: ")
    # Create an acronym from the name of the event
    if event_name:
         first_letter = event_name[0]
         last_letter = event_name[-1]
         acronym = first_letter + last_letter
    else:
         acronym = "Input not given."
    # Display the acronym
    print(f"The acronym for the Wedding is '{acronym}'.")
    number_of_guests = int(input("Please enter the number of guests: "))
     # Give advice based on the number of guests
    if number_of_guests <= 50:
      Venue_type = input("You're planning a small-sized gathering. A cozy and small venue might be ideal such as: Garden (1) / Hotel (2) / Beachfront (3).")
      if Venue_type == "1":
          print("You choose Garden.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

      elif Venue_type == "2":
          print("You choose a Hotel.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

      elif Venue_type == "3":
          print("You choose a Beachfront")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

      else: 
          print("Invaild Choice. Please choose numbers 1-3")

    elif 51 <= number_of_guests <= 100:
       Venue_type = input("You're planning a medium-sized gathering. Some venues you should consider are: Hall (2) / Vineyard (2) / Mansion (3)")
       if Venue_type == "1":
          print("You choose Hall.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

       elif Venue_type == "2":
          print("You choose a Vineyard.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

       elif Venue_type == "3":
          print("You choose a Mansion")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

       else: 
          print("Invaild Choice. Please choose numbers 1-3")
    else:
        Venue_type =input("You're planning a large - sized gathering. You should choose a venue like these: Ballroom (1) / Hotel (2) / Country Club")
        if Venue_type == "1":
          print("You choose Ballroom.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

        elif Venue_type == "2":
          print("You choose a Hotel.")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")

        elif Venue_type == "3":
          print("You choose a Country Club")
          choice= input("Do you have any dietary preferences or restrictions? Vegan (1), Gluten-Free (2), or Vegatatrain (3)")
          if choice == '1':
         # Vegan options
           print("Here are some Vegan menu suggestions:Vegan Burger")
          elif choice == '2':
          # Gluten-Free options
           print("Here are some Gluten-Free menu suggestions: Chicken Salad")
          elif choice=="3":
         # Vegatrian option
            print("Here are some Vegatrain Options:Stuffed Peppers")
        else: 
          print("Invaild Choice. Please choose numbers 1-3")
else:
 print("Invalid choice. Please enter a number between 1 and 3.")




