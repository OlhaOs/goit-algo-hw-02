from queue import Queue
import time
import random


queue = Queue()
request_id = 1

def generate_request():
    global request_id
    request = f"Заявка №{request_id}"
    queue.put(request)
    print(f"{request} додано до черги")
    request_id += 1


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється: {request}")
    else:
        print("Черга порожня.")



try:
    while True:
        generate_request()
        time.sleep(random.uniform(0.5, 2.0))
        process_request()
        time.sleep(random.uniform(0.5, 2.0))
except KeyboardInterrupt:
    print("\nРоботу завершено користувачем.")