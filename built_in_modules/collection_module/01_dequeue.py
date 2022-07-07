from collections import deque

# print(deque.__doc__)

queue = deque([5, 6, 7])

# print(queue)
# print(queue.__class__)


# appending
new_item = 100
queue.append(new_item)
print(queue)

# prepending
new_item = -100
queue.appendleft(new_item)
print(queue)

# pop
last_element = queue.pop()
print(last_element)
print(queue)

# pop from first
first_element = queue.popleft()
print(first_element)
print(queue)
