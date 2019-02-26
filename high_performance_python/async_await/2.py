from types import coroutine

@coroutine
def spam():
    result = yield "somevalue"
    print("result is:", result)

async def foo():
    print("Start foo")
    await spam()
    print("Done foo")

# stacking
async def bar():
    print("Start bar")
    # suspend here
    await foo()
    print("Done foo")

def test1():
    f = spam()
    f # <generator object spam at 0x1026da678>
    f.send(None)
    f.send(42)

def test2():
    b = bar()
    b.send(None)
    b.send(42)

if __name__ == "__main__":
    test2()