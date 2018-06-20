#!_*_coding:utf-8_*_

import os
import subprocess
import hashlib
import time


class UpdateGit:

    PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self,dir_name,update_step=5):
        self.dir_name = dir_name
        self.update_step = update_step
        self.file_name = ""
        self.push_time_stamp = 0

    @staticmethod
    def get_time_stamp():
        return time.time()

    def get_random_data(self):
        random_data = self.get_time_stamp()
        hash_data = hashlib.md5(str(random_data).encode('utf-8')).hexdigest()
        return hash_data

    @staticmethod
    def get_date():
        now_time = time.strftime("%Y-%m-%d")
        return now_time

    def write_file(self):
        self.file_name = self.get_date()
        file_data = self.get_random_data()
        with open('{path}/{dir_name}/{name}.txt'.format(path=self.PATH,dir_name=self.dir_name,name=self.file_name),"a") as f:
            f.write(file_data)
            f.close()

    @staticmethod
    def __run_git_status():
        git_response = subprocess.Popen('git status', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout = git_response.stdout.read()
        stderr = git_response.stderr.read()
        print("msg:",stdout.decode(),stderr.decode())

    def __run_git_add(self):
        git_response = subprocess.Popen('git add {data}'.format(data=self.dir_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout = git_response.stdout.read()
        stderr = git_response.stderr.read()
        print("msg:", stdout.decode(),stderr.decode())

    def __run_git_commit(self):
        commit_msg = self.get_date()
        git_response = subprocess.Popen('git commit -m {commit_msg}'.format(commit_msg=commit_msg), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout = git_response.stdout.read()
        stderr = git_response.stderr.read()
        print("msg:", stdout.decode(),stderr.decode())

    def __run_git_push(self):
        self.push_time_stamp = self.get_time_stamp()
        git_response = subprocess.Popen('git push', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = git_response.stdout.read()
        stderr = git_response.stderr.read()
        print("out:", stdout.decode(),stderr.decode())

    def __run_git(self):
        self.__run_git_add()
        self.__run_git_commit()
        self.__run_git_push()

    def run(self):
        while True:
            if (self.get_time_stamp() - self.push_time_stamp) >= self.update_step:
                self.write_file()
                self.__run_git()


if __name__ == "__main__":
    ug_obj = UpdateGit('file_dir',update_step=1)
    ug_obj.run()
