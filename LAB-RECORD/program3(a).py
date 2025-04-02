class ListOperations:
    def __init__(self):
        self.data = []
    
    def insert(self, value):
        self.data.append(value)
        print(f"Inserted {value} into the list.")
    
    def delete(self, value):
        if value in self.data:
            self.data.remove(value)
            print(f"Deleted {value} from the list.")
        else:
            print(f"Value {value} not found in the list.")
    
    def find(self, value):
        if value in self.data:
            print(f"Value {value} found in the list at index {self.data.index(value)}.")
        else:
            print(f"Value {value} not found in the list.")
    
    def sort_list(self):
        self.data.sort()
        print("List sorted:", self.data)
    
    def reverse_list(self):
        self.data.reverse()
        print("List reversed:", self.data)
    
    def display(self):
        print("Current list:", self.data)

# Example usage
if __name__ == "__main__":
    lst = ListOperations()
    lst.insert(10)
    lst.insert(5)
    lst.insert(30)
    lst.insert(20)
    lst.display()
    lst.sort_list()
    lst.reverse_list()
    lst.find(10)
    lst.delete(5)
    lst.display()
