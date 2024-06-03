"""Mule example."""
from time import sleep
from threading import Thread, Lock

import uwsgi  # type: ignore # pylint: disable=import-error


batch: list[str] = []
lock = Lock()


def process():
    """Process batch"""
    global batch

    print("--------------")
    with lock:
        work = batch
        batch = []
    sleep(2)
    print("\t", work)


def thread_loop():
    """Called every 10 seconds"""
    counter = 0
    while True:
        sleep(1)
        counter += 1
        if counter == 10:
            print("reset counter...")
            counter = 0
            process()


def loop():
    """Process loop messages"""
    while True:
        message = uwsgi.mule_get_msg()
        print("get message: ", message)
        batch.append(message)
        if len(batch) == 10:
            process()


if __name__ == '__main__':
    thread = Thread(target=thread_loop, daemon=True)
    thread.start()
    loop()
