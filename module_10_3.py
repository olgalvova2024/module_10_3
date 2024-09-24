from threading import Thread, Lock
from time import sleep
from random import randint

lock = Lock()

class Bank:
    balance = 0

    def deposit(self):

        for i in range(100):
            num_ = randint(50, 500)
            self.balance += num_
            sleep(0.001)
            if self.balance >= 500 and lock.locked():
                lock.release()
            print(f'Пополнение: {num_}. Баланс {self.balance}.')

    def take(self):
        for i in range(100):

            num_ = randint(50, 500)
            print(f'Запрос на {num_}.')
            sleep(0.001)
            if self.balance >= num_:
                self.balance -= num_
                print(f'Снятие: {num_}. Баланс {self.balance}.')
            else:
                print('Запрос отклонен, недостаточно средств')
                if lock.locked() == False:
                    lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
