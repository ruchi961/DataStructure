class node:
    #memory_loc=1000
    head=None
    def __init__(self, data, prev_pointer=None, next_pointer=None):
        self.data = data
        self.prev = None
        self.next = None
        self.memory_loc = None

class LinkedListOperations:
    nodes=[]
    def insert(self):
        if len(nodes) == 0:
            #root node
            data=input("Enter some data: ")
            node1 = node(data)
            node1.prev_pointer=None
            node1.next_pointer=None
            node1.memory_loc=id(node1)
            
            node.head = id(node1)
            nodes.append(node1)
            #remembers the start of the doubly linked list
            
            
        else:
            print("Please select option:\n\t1. Before(middle)\n\t2. After(middle)\n\t3. Append\n\t4. Begining")
            no2 = input("Enter choice: ")
            data=input("Enter some data: ")
            flag=True
            for t in nodes:
                if t.data == data:
                    flag=False
                    print("Data already exists in the doubly linked list. Hence, cannot insert it again.")
            if flag:
                if no2.lower()=="before" or no2 =="1":
                    node1 = node(data)
                    node1.memory_loc= id(node1)
                    before=input("Enter previous node's value: ")
                    flag=True
                    for i in nodes:
                        if i.data == before:
                            flag=False
                            node1.next = i.memory_loc
                            i.prev = id(node1)
                            for j in nodes:
                                if j.next == i.memory_loc:
                                    j.next =node1.memory_loc
                                    node1.prev = j.memory_loc
                                    break
                            
                            break
                    if flag:
                        print("Sorry, the before data entered not found in the doubly linked list. Hence, cannot add element.")
                    else:
                        for i in nodes:
                            if i.data == before:
                                val = nodes.index(i)
                        nodes.insert(val,node1)
                        print("Data inserted successfully.")
                elif no2.lower() == "after" or no2 =="2":
                    node1 = node(data)
                    node1.memory_loc= id(node1)
                    after=input("Enter after node's value: ")
                    flag=True
                    for i in nodes:
                        if i.data == after:
                            flag=False
                            node1.prev = i.memory_loc
                            copy_addr =i.next
                            i.next = id(node1)
                            for j in nodes:
                                if j.prev == i.memory_loc:
                                    j.prev =node1.memory_loc
                                    node1.next = j.memory_loc
                                    break
                            
                            break
                    if flag:
                        print("Sorry, the after data entered not found in the doubly linked list. Hence, cannot add element.")
                    else:
                        for i in nodes:
                            if i.data == after:
                                val = nodes.index(i)
                        nodes.insert(val+1,node1)
                        print("Data inserted successfully.")
                    
                if no2.lower() == "append" or no2 =="3":
                    node1 = node(data)
                    node1.next=None
                    node1.prev = nodes[-1].memory_loc
                    node1.memory_loc = id(node1)
                    nodes[-1].next = node1.memory_loc
                    nodes.append(node1)
                    print("Data inserted successfully.")
                    #print(prev_pointer)
                elif no2.lower == "begining" or no2 =="4":
                    node1 = node(data)
                    node1.prev=None
                    node1.next = node.head
                    node1.memory_loc = id(node1)
                    for i in nodes:
                        if i.memory_loc == node.head:
                            i.prev = node1.memory_loc
                            break
                    node.head = node1.memory_loc
                    nodes.insert(0,node1)
                    print("Data inserted successfully.")
            
            
    def delete(self):
        if len(nodes)==0:
            print("Sorry! cannot delete value, no elements present in the doubly linked list.")
        else:
            element = input("Enter element to delete : ")
            flag=False
            for t in nodes:
                if t.data == element:
                    flag=True
                    
            if flag:
                for i in nodes:
                    if i.data == element:
                        for j in nodes:
                            if j.memory_loc == i.next:
                                next_store = j.memory_loc
                                j.prev = i.prev
                                break
                        for k in nodes:
                            if k.memory_loc == i.prev:
                                prev_store = k.memory_loc
                                k.next = i.next                        
                                break
                        print("Data deleted successfully.")
                        nodes.remove(i)
                        break
            else:
                print("Data doesn't exists in the doubly linked list. Hence, cannot delete the data.")
    def update(self):
        if len(nodes)==0:
            print("Sorry! cannot update value, no elements in list")
        else:
            element = input("Enter element to update : ")
            new_data = input("Enter new value to update: ")
            flag=True
            for i in nodes:
                if i.data == element:
                    flag=False
                    i.data = new_data
                    print("Data updated successfully.")
                    break
            if flag:
                print("No such data present in the doubly linked list. Hence, cannot update the value of the data in the linked list.")
        
            
    def showList(self):
        if len(nodes)==0:
            print("No elements in the doubly linked list. Doubly linked list is empty.")
        else:
            print("Element No.|Previous Pointer|Data|Next Pointer|Memory Location")
            for i in nodes:
                print(nodes.index(i),"|",i.prev,"|",i.data,"|",i.next,"|",i.memory_loc)
    def search(self):
        if len(nodes)==0:
            print("Sorry! cannot search element, no elements in list")
        else:
            flag=True
            element = input("Enter element to search : ")
            for i in nodes:
                
                if i.data == element:
                    flag=False
                    print("Data found in the doubly linked list.")                  
                    break
            if flag:
                print("Data not found in the doubly linked list.")
        

choice="y"
nodes = []
operations = LinkedListOperations()
while choice == "y" or choice =="Y":
    print("Doubly Linked List".center(80,"*"))
    print("Select any one option of the following operations : \n\t1. Insert\n\t2. Delete\n\t3. Update\n\t4. Show List\n\t5. Search")
    
    no = input("Enter your choice : ")
    if no == "1" or no.lower() == "insert":
        operations.insert()

            
        
    elif no=="2" or no.lower() == "delete":
        operations.delete()
    elif no=="3" or no.lower() == "update":
        operations.update()
        
    elif no=="4" or no.lower() == "show list":
        operations.showList()
    elif no=="5" or no.lower() == "search":
        operations.search()

        
        
    
    choice = input("Do you want to continue (y/Y/n/N) : ")
