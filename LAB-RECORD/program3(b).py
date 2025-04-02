def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}  # Merging dictionaries
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
