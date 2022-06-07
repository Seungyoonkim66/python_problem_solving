import basic_stack
import linked_list_stack

def main()->None:
    print("Choose action to execute.")
    # stack = basic_stack.Stack()
    stack = linked_list_stack.Stack()
    action = -1
    while True:
        action = int(input("\n*************\n1. push\n2. pop\n3. check top\n4. check is stack emtpy\n5. check stack status\n6. Exit\n>> "))
        if action == 1:
            data = input("Enter data to push to the stack >> ")
            print("PUSH : " , data)
            stack.push(data)
        elif action == 2:
            print("POP : " , stack.pop())
        elif action == 3:
            print("TOP : ", stack.check_top())
        elif action == 4:
            print("Is Stack Empty? : ", stack.is_empty())
        elif action == 5:
            stack.print_stack()
        elif action == 6:
            break
    
    
if __name__ == "__main__":
	main()