# create a class named HelloGitHub
class HelloGitHub:
    # create a function names __init__
    def __init__(self, name):   
        self.name = name
    # create a function names printHello
    def printHello(self):
        print("Hello", self.name)
  
    # create a function names printHello
    def printHello(self, language): 
        if 'en' == language:
            print("Hello", self.name)
        elif 'zh' == language:
            print("你好", self.name)
        elif 'jp' == language:
            print("こんにちは", self.name)
# create a object named hello
hello = HelloGitHub("GitHub")
# call the function printHello
hello.printHello('zh')
