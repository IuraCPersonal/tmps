from adapter.Adapter import *

def main():
    # Plug in
    socket  = Port()
    adapter = Adapter(socket)
    airpods  = Airpods(adapter)

    # Make coffee
    airpods.charge()

    return 0

if __name__ == "__main__":
    main()