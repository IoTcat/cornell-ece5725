from threading import Timer

def timeout(t, cb):
    Timer(t, cb).start()