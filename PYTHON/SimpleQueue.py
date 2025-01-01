import queue

ordersQueue = queue.SimpleQueue()

ordersQueue.put("Sushi")
ordersQueue.put("Lasagna")
ordersQueue.put("Paella")

print("The size is :", ordersQueue.qsize())

print(ordersQueue.get())
print(ordersQueue.get())
print(ordersQueue.get())

print("Empty queue: ", ordersQueue.empty())