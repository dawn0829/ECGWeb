from mysite.main import wstest
import threading


def print_data():
    while True:
        print("nmsl")   

a = threading.Thread(target=print_data()).start()

a.start()

