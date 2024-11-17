class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, *args):
        if len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
            if start > stop:
                step = -1
            else:
               step = 1
        elif len(args) == 1:
            raise StepValueError
        else:
            raise StepValueError


        if step == 0:
            raise StepValueError
        elif step == None:
            if start > stop:
                step = -1
            else:
                step = 1


        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if ((self.step > 0 and self.pointer > self.stop)
                or (self.step < 0 and self.pointer < self.stop)):
            raise StopIteration
        result = self.pointer
        self.pointer += self.step
        return result


if __name__ == '__main__':
    try:
        iter1 = Iterator(100,200,0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')
    except TypeError as exc:
        print(f'  "Ошибка в исходных данных:", {exc.args} - не указан шаг итерации!')



    iter2 = Iterator(-5,1)
    iter3 = Iterator(6,15,2)
    iter4 = Iterator(5,1,-1)
    iter5 = Iterator(10,1)


    for i in iter2:
        print(i, end=' ')
    print()

    for i in iter3:
        print(i, end=' ')
    print()

    for i in iter4:
        print(i, end=' ')
    print()

    for i in iter5:
        print(i, end=' ')
    print()

    try:
        iter6 = Iterator(10)
        for i in iter6:
            print(i, end=' ')
        print()
    except StepValueError as exc:
        print('Ошибка в исходных данных. Не указан шаг итерации и конечное значение! ')

    try:
        iter7 = Iterator(10,20,1,6,7)
        for i in iter7:
            print(i, end=' ')
        print()
    except StepValueError as exc:
        print('Ошибка в исходных данных. Слишком много аргументов! ')