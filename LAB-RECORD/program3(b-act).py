def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = str(merged_dict[key]) + str(value)  # Concatenating values if key exists in both
        else:
            merged_dict[key] = value
    
    return merged_dict

# Getting user input for two dictionaries
def get_dictionary_input():
    user_dict = {}
    n = int(input("Enter the number of key-value pairs: "))
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        user_dict[key] = value
    return user_dict

print("Enter first dictionary:")
dict1 = get_dictionary_input()

print("Enter second dictionary:")
dict2 = get_dictionary_input()

# Merging the dictionaries
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged_dict)
