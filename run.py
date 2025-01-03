import multiprocessing
import subprocess

# To run Jarvis
def startAlexa():
    # Code for process 1
    print("Process 1 is running.")
    from main import start
    start()

# To run hotword
def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()


# Start both processes
if __name__ == '__main__':
    # Create processes for Jarvis and hotword listening
    p1 = multiprocessing.Process(target=startAlexa)
    p2 = multiprocessing.Process(target=listenHotword)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for p1 to finish
    p1.join()

    # Check if p2 is still alive and terminate if necessary
    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped.")
