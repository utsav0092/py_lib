import pandas as p

my_data_set = {
    'Cars': ["BMW", "Volvo", "Ford"],
    'Passing': [3, 7, 4]
}
my_var = p.DataFrame(my_data_set)
print(my_var)
