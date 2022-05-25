import multiprocessing
import time
from time import gmtime, strftime


def job(idx):
    start = strftime('%H:%M:%S', gmtime())
    time.sleep(2)
    end = strftime('%H:%M:%S', gmtime())

    msg = 'Thread: {}, start: {}, end: {}'.format(idx, start, end)
    print(msg)


if __name__ == '__main__':
    timeStr = time.time()
    multiprocessing.freeze_support()

    processes = [multiprocessing.Process(target=job, args=(i,)) for i in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    timeEnd = time.time()
    print('Total time: {:.3f}s'.format(timeEnd - timeStr))