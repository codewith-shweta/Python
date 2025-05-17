# switch statement (match - case ) = alternative using many elif statements , 
#                                     execute id a value matches a case
#                                     better n cleaner way oh plus readable 

def week(day):
    match day:
        case 1:
            return "Monday"
        
        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"
            
        case 4:
            return "Thursday"
            
        case 5:
            return "Friday"
            
        case 6:
            return "Saturday"
            
        case 7:
            return "Sunday"

        case 8:
            return "Not a DAY!"
            
print(week(3))


# just kinda ex 

def new(day):
    match day:
        case "saturday" | "monday":
            return True
        case "rest days":
            return False

print(new("rest days"))