class Countdown:
    def __init__(self,count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            val = self.count
            self.count -=1
            return val
        else:
            raise StopIteration
            
        

number = Countdown(10)
for i in number:
    print(i)


class NumberRange:
    def __init__(self,start,end):
        self.current = start
        self.end = end
        self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current  += self.step
            return val

        else:
            raise StopIteration


n = NumberRange(1,5)

for i in n:
    print(i)