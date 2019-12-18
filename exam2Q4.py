from ExpressionTree import Stack

def is_valid(push_list, pop_list):
    stack = Stack()
    push_index = 0
    pop_index = 0
    while pop_index < len(pop_list):
        was_popped = False
        # check if current item to pop has already been pushed
        for i in range(push_index):
            if push_list[i] == pop_list[pop_index]:
                # pop item and check if it is current item in pop_list
                popped = stack.pop()
                if popped != pop_list[pop_index]:
                    return False
                pop_index += 1
                was_popped = True
            # if wasn't popped, push onto stack until current pop is reached
            if not was_popped:
                while push_list[push_index] != pop_list[pop_index]:
                    stack.push(push_list[push_index])
                    push_index += 1
                popped = stack.pop()
                if popped != pop_list[pop_index]:
                    return False
    return True

def main():
    push_list = [1, 2, 3, 4]
    pop_list = [2, 4, 3, 1]
    print(is_valid(push_list, pop_list))

if __name__ == "__main__":
    main()
