def count_substring(string, sub_string):
    # Edge case 
    if sub_string not in string:
        return 0
    
    count = 0 
    for i in range(len(string)):
        if i+len(sub_string) > len(string):
            return count        
        if string[i] == sub_string[0]:
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
    return count 