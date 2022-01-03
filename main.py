from automation.sel import automatic
from frontend.frame1 import front


def main():
    # play =automatic()
    # play.scrape()
    create=front()
    create.go()

if __name__ == "__main__":
    main()