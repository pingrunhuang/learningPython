import asyncssh
import asyncio

async def run_command(host, command):
    async with asyncssh.connect(host) as conn:
        result = await conn.run(command)
        return result.stdout

loop = asyncio.get_event_loop()

def serial_test():
    out = [loop.run_until_complete(
        run_command("n301.shanshu", "echo hello world %d" % i) for i in range(200)
    )]
    print(out)

def parrallel_test():
    # asyncio.gather: pass all coroutines(function) and wait to be finished
    out = loop.run_until_complete(
        asyncio.gather(
            *[run_command('n301.shanshu', 'echo hello world %d' % i) for i in range(200)]
        )
    )
    print(out)

if __name__ == '__main__':
    parrallel_test()