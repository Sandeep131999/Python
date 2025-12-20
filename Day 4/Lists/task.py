#simple collection of ordered items using a Python list.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Modifying Items
#use the same syntax to get hold of items in a List to modify.
states_of_america[0] = "India"

# Adding Items
#add items to the end of a List using the append() function.
states_of_america.append("Nepal")

states_of_america.append("Japan")

print(states_of_america[len(states_of_america)-1])

states_of_india = ["Karnataka","Andhra","Tamil","gujarat","UttarPradesh","assam","bihar"]

merged_states = [states_of_america, states_of_india]

print(merged_states)