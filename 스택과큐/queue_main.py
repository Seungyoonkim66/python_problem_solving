import deque_queue
import linked_list_queue
import two_stack_queue

if __name__ == "__main__":
    # q = deque_queue.Queue()
    # q = linked_list_queue.Queue()
    q = two_stack_queue.Queue()
    for i in range(1,20,2):
        q.enqueue(i)

    for i in range(1,20,2):
        print(q.dequeue(), end=" ")

    # q.print_queue()
    # print(q.queue_size())
