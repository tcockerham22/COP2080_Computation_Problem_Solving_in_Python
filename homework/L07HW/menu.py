import os

class Menu():
    def __init__(self):
        self.options = []

    def addOption(self, option):
        self.options.append(option)

    def run_bash_cmd(self, choice):
        commands = {
            1: "free -h",
            2: "netstat -an",
            3: "free",
        }
        cmd = commands.get(choice)
        if cmd:
            os.system(cmd)

    def getInput(self):
        while(True):
            for i in range(len(self.options)):
                print(f"{i + 1}: {self.options[i]}")
            self.inp = int(input("Enter 1-4: "))
            if (self.inp >= 1 and self.inp <= len(self.options) - 1):
                self.run_bash_cmd(self.inp)
                print()
            elif self.inp == 4:
                break