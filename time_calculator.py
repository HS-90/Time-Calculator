def add_time(start, duration, start_day = None):
    
 
        
    #set start hours and minutes
    start_hour = int(start[0:start.find(':')])
    start_min = int(start[start.find(':')+1:start.find(' ')])
    
    #duration hours and minutes
    dur_hour = int(duration[0:duration.find(':')])
    dur_min = int(duration[duration.find(':')+1:duration.find(':')+3])
    
    #AM or PM and convert start_hour to 24hr clock
    if 'A' in start:
        
        if start_hour == 12:
            start_hour = 0
        else:
            pass
    
    if 'P' in start:
    
        if start_hour == 12:
            start_hour = 12
        else:
            start_hour = start_hour + 12
    
    #if 60-start_min < dur_min we add one more hour to time elapsed or dur_hour:
    if (60 - start_min) < dur_min:
        dur_hour += 1
    
    #compute new time to 24 hr clock
    new_hour = (start_hour + dur_hour)%24
    new_min = (start_min + dur_min)%60

    
    if new_min < 10:
        new_min = '0'+ str(new_min)
        
    #check if new_hour = 0, if so make it 12
    if new_hour == 0:
        new_hour = 12
        new_time = str(new_hour) + ':' + str(new_min) + ' AM'
    
    elif new_hour == 12:
        new_time = str(new_hour) + ':' + str(new_min) + ' PM'
        
    elif new_hour > 12:
        new_hour = new_hour - 12
        new_time = str(new_hour) + ':' + str(new_min) + ' PM'
    else:
        new_time = str(new_hour) + ':' + str(new_min) + ' AM'
        
    #calculate number of days
    if ((24 - start_hour) < dur_hour%24) or (start_hour==23 and ((60-start_min) < dur_min)):
        days = dur_hour//24 + 1
        
    else: 
        days = dur_hour//24
    
    if start_day is not None:
        #make list with days of week in order
        weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day_counter = weekdays.index(start_day.lower())
        
        if days < 1:
            new_time += ', ' + weekdays[day_counter].title()
            return(new_time)
        
        elif days == 1:
            day_counter += 1
            new_time += ', ' + weekdays[day_counter%7].title() + ' (next day)'
            return(new_time)
        
        elif days > 1:
            day_counter += days
            new_time += ', ' + weekdays[day_counter%7].title() + ' (' + str(days) + ' days later)'
            return(new_time)
    else:
        if days < 1:
            return(new_time)
        
        elif days == 1:
            new_time += ' (next day)'
            return(new_time)
        
        elif days > 1:
            new_time += ' (' + str(days) + ' days later)'
            return(new_time)





