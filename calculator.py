import sys

stack = []
op1 = []
op2 = []


def main():
    input_value()
    print(stack)
    calculate()
    print(stack)    


def input_value():
    global stack
    global op1
    global op2
    l = False
    while 1:
        print(stack)
        print(op1)
        print(op2)
        val = input()
        if str.isdecimal(val):
            stack.append(val)
            if l:
                l = False
                for i in range(0,len(op1)):
                    print(i)
                    stack.append(op1[len(op1)-i-1])
                op1.clear()
        elif val == "*" or val == "/":
            op1.append(val)
            l = True
        elif val == "+" or val == "-":
            op2.append(val)
        elif val == "=":
            for i in op1:
                stack.append(i)
            op1.clear()
            for i in op2:
                stack.append(i)
            op2.clear()
            return
        else:
            print(val)


def calculate():
    global stack
    while len(stack) != 1:
        for i in range(0,len(stack)):
            print(stack)
            if str.isdecimal(stack[i]):
                continue
            elif stack[i] == "*":
                stack.pop(i)
                nv = int(stack.pop(i-1)) * int(stack.pop(i-2))
                stack.insert(i-2,str(nv))
                break
            elif stack[i] == "/":
                stack.pop(i)
                nv = int(stack.pop(i-1)) / int(stack.pop(i-2))
                stack.insert(i-2,str(nv))
                break
            elif stack[i]=="+":
                stack.pop(i)
                nv = int(stack.pop(i-1)) + int(stack.pop(i-2))
                stack.insert(i-2,str(nv))
                break
            elif stack[i]== "-":
                stack.pop(i)
                nv = int(stack.pop(i-1)) - int(stack.pop(i-2))
                stack.insert(i-2,str(nv))
                break


main()