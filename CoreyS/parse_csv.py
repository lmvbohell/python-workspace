'''
#  -How to Read, Parse, and Write CSV Files
'''
# import csv
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)   #-csv.reader(csv_file) Dictr.(ger key) vs reader
#     # # for line in csv_reader: -Använd with loop nedan istället.
#     # #     print(line['email'])     #print(line['email'])
#     #print(csv_reader) -Bara ett objekt i minnet visas. Måste loopa över raderna i csv_reader.
#     #next(csv_reader)    -Loopar över rubrk.
#     with open('new_names.csv', 'w') as new_file:
#         fieldnames = ['first_name', 'last_name', 'email']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#         csv_writer.writeheader()    # Skriver rubrik
#         ##csv_writer = csv.writer(new_file, delimiter='/t')
#         for line in csv_reader:
#             del line['email']   #Ta även bort email ur fieldnames ovan.
#             csv_writer.writerow(line)
#     #         #print(line[2])  #-Skriver email.

'''
# -Parsing Names From a CSV to an HTML List
'''
# import csv
# html_output = ''
# names = []


# with open('patrons.csv', 'r') as data_file:
#     #csv_data = csv.reader(data_file) 
#     #Dictionary has each field as a key and data as a value.
#     csv_data = csv.DictReader(data_file)    #Turn each line to a diction instead of a list.

#     # We don't want first line of bad data
#     #next(csv_data) # We don't want headers
#     next(csv_data)

#     #print(list(csv_data))
#     for line in csv_data:
#         if line['FirstName'] == 'No Reward':
#             break
#         #print(line)
#         #names.append(f"{line[0]} {line[1]}")
#         names.append(f"{line['FirstName']} {line['LastName']}")

# html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</P>'
# html_output += '\n<ul>'

# for name in names:
#     html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</ul>'

# print(html_output)
# # # for name in names:  -Print rader endast för test for..
# # #     print(name)
