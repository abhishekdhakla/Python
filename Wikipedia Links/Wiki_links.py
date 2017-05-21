import datetime


answer_format = '%m/%d'
link_format = '%b_%d'
link = 'http://en.wikipedia.org/wiki/{}'


while True:
    answer = input("""What date would you like?
                    Please give you answer in the MM/YY format
                    Type 'quit' to exit!!""")
    if answer.upper() == 'QUIT':
        break
    
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
        
    except ValueError:
        print("That's not a valid date")
