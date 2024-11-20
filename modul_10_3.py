import random
import threading
import time

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        n = random.randint(50, 500)
        with lock:
            if self.balance <= 500 and lock.locked():
                self.balance += n
                print(f'Пополнение: {n}. Баланс: {self.balance}')
        time.sleep(0.001)
    def take(self):
        for i in range(100):
            n1 = random.randint(50, 500)
            print(f'Запрос на {n1}')
            with lock:
                if n1 <= self.balance:
                    print(f'Снятие: {n1}. Баланс: {self.balance - n1}"')
                else:
                    print(f'Запрос отклонён, недостаточно средств')
            time.sleep(0.001)



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

