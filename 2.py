from prettytable import PrettyTable

table = PrettyTable()
print("POKDEX") 
table.add_column("pokemon name",["pikachu","Squirtle","charmender"])
table.add_column("pokemon Type",["Electric","water","fire,"])
print(table)