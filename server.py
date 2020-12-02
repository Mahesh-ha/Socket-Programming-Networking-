from socket import *
import math


class eq:
    def getandreplace(self):
        """replace x, /, e, \u00b2, log, ln, ^,! with *, /, math.exp, **2, math.log10 , math.log, ** ,math.factorial
        respectively """
        self.newtext = self.name.replace('/', '/')
        self.newtext = self.newtext.replace('x', '*')
        self.newtext = self.newtext.replace('e', 'math.exp')
        self.newtext = self.newtext.replace('\u00b2', '**2')
        self.newtext = self.newtext.replace('log', 'math.log10')
        self.newtext = self.newtext.replace('ln', 'math.log')
        self.newtext = self.newtext.replace('^', '**')
        self.newtext = self.newtext.replace('!', 'math.factorial')

    def __init__(self, name):
        """when the equal button is pressed"""
        print(name)
        self.name = name
        self.eg = list(self.name)
        self.eg.append('end')
        self.n = len(self.eg) - 1  # length of the expression
        self.n2 = 0
        while self.eg[self.n2] != 'end':
            self.n1 = self.n2
            print(self.eg)
            while self.n1 < self.n and self.eg[self.n1] != '!':
                self.n1 = self.n1 + 1
            if self.n1 == self.n:
                break
            self.n3 = self.n1    # pos of the !
            if self.eg[self.n1] == '!':
                del (self.eg[self.n1])
                self.n = self.n - 1

                if self.eg[self.n1 - 1] == ')':
                    while self.n1 > 0 and self.eg[self.n1 - 1] != '(':
                        self.n1 = self.n1 - 1
                    if self.eg[self.n1 - 1] == '(':
                        self.eg.insert(self.n1 - 1, '!')
                        self.n += 1
                        self.n2 = self.n3 + 1
                else:
                    self.eg.insert(self.n1, ')')
                    while (self.n1 > 0) and self.eg[self.n1 - 1] not in '(+-/x':
                        self.n1 = self.n1 - 1

                    self.eg.insert(self.n1, '!(')
                    self.n = self.n + 2
                    self.n2 = self.n3 + 2

        self.name = "".join(self.eg)
        self.name = self.name.replace('end', '')
        self.getandreplace()
        print(self.newtext)

        try:
            # evaluate the expression using the eval function
            self.value = eval(self.newtext)
        except (NameError, TypeError, ZeroDivisionError, ValueError):
            self.value = 'Invalid Input!'
        except SyntaxError:
            self.value = 'SyntaxError!'


serverPort = 1206
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    sol = eq(sentence)
    connectionSocket.send(str(sol.value).encode())
    print(sol.value)
    connectionSocket.close()
