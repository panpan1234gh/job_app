class Employee:
    def __init__(self, full_name, job, work_place, start_time, retire):
        self.full_name = full_name
        self.job = job
        self.work_place = work_place
        self.start_time = start_time
        self.retire = retire


    def save(self):
        print(self.full_name , self.job , "saved")


    def find_by_full_name(self):
        print(f"{self.full_name} found")


    def validator(self):
        pass