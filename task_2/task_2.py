'''
Задание 2: Написать функцию, которая получает из Сети код страниц из списка
и сохраняет его (код) на диск.
'''

import time
import random
import asyncio
import aiohttp
import aiofiles

urls = ['http://google.com/' for _ in range(100)]


def generate_filename() -> str:
    temp = str(int(time.time()))
    for _ in range(5):
        temp += chr(random.randint(65, 75))
    return f"{temp}.html"


async def download_site(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            filename = generate_filename()
            html = response.text

            async with aiofiles.open(filename, mode='w') as file:
                await file.write(str(html))


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download_site(url=url)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    print(f"time: {(time.perf_counter() - start):.03f}")
