class laptop:
    storage_type = "ssd"

    def __init__(self, RAM, Storage):
        self.RAM = RAM
        self.Storage = Storage

    def get_info(self): # instance method 
        print(f"Laptop has {self.RAM} RAM & {self.Storage} {self.storage_type}")

l1 = laptop("16gb", "512gb")
l2 = laptop("8gb", "256gb")

l1.get_info()
