import csv
my_list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open('c:\\pythonsamples\\assignment_4.csv','w') as f:
    write = csv.writer(f,delimiter = ',')
    for i in my_list:
        write.writerow(i)
