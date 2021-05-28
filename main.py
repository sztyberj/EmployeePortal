from loadingWindow import LoadingWindow
import asyncio


async def main():
    print ("Czekanie 5 sec do uruchomienia aplikacji. ")
    for _ in range(5):
        await asyncio.sleep(1)
        print (".")
    print ("Finished waiting.")

asyncio.run(main())

runapp = LoadingWindow()




