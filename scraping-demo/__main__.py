# coding: UTF-8
import amazon


def main():

    # Amazon
    amzn = amazon.Amazon()
    amzn.search_word = "SEARCH WORD"
    amzn.start()


if __name__ == "__main__":
    main()
