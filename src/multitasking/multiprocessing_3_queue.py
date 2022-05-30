import multiprocessing
import time
from time import gmtime, strftime


class Cook(multiprocessing.Process):
    def __init__(self, cookIdx, queue):
        super().__init__()
        self.cookIdx = cookIdx
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            meals = self.queue.get()

            msg = 'Cook {}: Start to cook. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
            print(msg)

            cookTime = meals
            time.sleep(cookTime)

            msg = 'Cook {}: End of cooking. ({})'.format(self.cookIdx, strftime('%H:%M:%S', gmtime()))
            print(msg)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    orders = [8, 2, 5]

    my_queue = multiprocessing.Queue()
    for meals in orders:
        my_queue.put(meals)

    cook1 = Cook(cookIdx=1, queue=my_queue)
    cook2 = Cook(cookIdx=2, queue=my_queue)

    cook1.start()
    cook2.start()

    cook1.join()
    cook2.join()
