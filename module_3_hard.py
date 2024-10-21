def calculate_structure_sum(data_structure):
    if isinstance(data_structure, (list, tuple, set)):
        return sum(calculate_structure_sum(num) for num in data_structure)
    elif isinstance(data_structure, dict):
       return sum(data_structure.values()) + sum(len(key) for key in data_structure.keys())
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (int, float)):
        return data_structure

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)