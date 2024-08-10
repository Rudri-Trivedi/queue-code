class creat_queue:
    def __init__(self):
        global queue
        self.queue =[]
        
    def __repr__(self):
        return print(self.queue)
    
    def insert_in_queue(self):
        value_append_in_queue = input("Entar a Value :")
        self.queue.append(value_append_in_queue)

    def user_input(self):
        while True:
            print("\n1-Inser a element .")

            user_input = input("Entar your choice ..")

            if user_input == "1":
                self.insert_in_queue()
                self. __repr__()

queue = creat_queue()
queue.user_input()