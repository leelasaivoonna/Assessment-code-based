from noAgrsPackage import fun_file as dec # function decorator
from noAgrsPackage import class_file as dwa
from argsPackage import fun_file as dwia
from argsPackage import class_file as cdwia


@dec.begin_end
def fun2(a, b):
    print(f"We Will win the soccer WC {a} {b}")
fun2(111, 222)

print("-" * 40)

@dwa.StartStop
def fun3(x, y, z):
    print(f"Happy sunday fun3 {x} {y} {z}")

fun3(10, 20, 30)
print("-" * 40)

@dwia.dec_with_arg("sachin", "Suarav", "Rahul")
def fun4(x, y):
    print(f"fun4 ..... {x} {y}")

fun4(88,77)


print("-" * 40)


@cdwia.StartStopwitharguement("Dhoni", "Kohli", "Rohith")
def fun5(x, y):
    print(f"I am from fun5 {x} {y}")
fun5(678, 567)
