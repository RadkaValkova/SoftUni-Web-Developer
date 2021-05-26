class Worker:
    def work(self):
        print("I'm working!!")


class Manager:
    def __init__(self):
        pass

    def manage(self, employee):
        employee.work()


class SuperWorker:
    def work(self):
        print("I work very hard!!!")


# worker = Worker()
# manager = Manager(worker)
# manager.set_worker(worker)
# manager.manage()
#
# super_worker = SuperWorker()
# manager.
# try:
#     manager.set_worker(super_worker)
# except AssertionError:
#     print("manager fails to support super_worker....")

worker = Worker()
manager = Manager()
# manager.set_worker(worker)
manager.manage(worker)

super_worker = SuperWorker()
try:
    # manager.set_worker(super_worker)
    manager.manage(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
