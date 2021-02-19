text = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks."



# function to convert list of strings to string

def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s))





def text_parser(transcription):

    nums = {'one': 1, 'two': 2, 'three:': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight':8, 'nine':9}

    
    
    
    transcription_list = transcription.split(" ")


    numbers = []

    for i, word in enumerate(transcription_list):
        if transcription_list[i] == 'Number':
            numbers.append(i)

    if len(numbers) > 0 and numbers[0] > 1:
        heading = listToString(transcription_list[0:numbers[0]])

    # find the first number item in the transcription by looking at the first Number n

        
    item_number = nums[transcription_list[numbers[0]+1]]
    dot = '.'


    # return output as a list of strings
    res = []

    res.append(heading)
    for i in range(len(numbers)-1):
        numbered_list = []

        numbered_list = transcription_list[numbers[i]+2:numbers[i+1]]
        numbering = str(item_number) + dot

        numbered_list.insert(0, numbering)

        res.append(listToString(numbered_list))
        item_number+=1
        print(numbered_list)  



    # add the last numbered list
    last_list = transcription_list[numbers[-1]+2:]
    last_number = str(item_number) + dot
    last_list.insert(0, last_number)
    res.append(listToString(last_list))            
    
    print(res)


    return res
text_parser(text)                                                                  
