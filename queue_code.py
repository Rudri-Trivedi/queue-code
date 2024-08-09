class creat_queue:
    def __init__(self):
        global queue
        self.queue =[]
        
    def __repr__(self):
        return print(self.queue)
    
    def insert_in_queue(self):
        value_append_in_queue = input("Entar a Value :")
        self.queue.append(value_append_in_queue)

    def delete_in_queue(self):
        self.queue.pop(0)

    def user_input(self):
        while True:
            print("\n1-Inser a element.")
            print("2-delete a element.")
            print("3-Exit from queue.\n")

            user_input = input("Entar your choice ..")

            if user_input == "1":
                self.insert_in_queue()
                self. __repr__()

            if user_input=='2':
                self.delete_in_queue()
                self.__repr__()
            
            if user_input == '3':
                break


queue = creat_queue()
queue.user_input()