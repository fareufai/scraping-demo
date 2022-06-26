# coding: UTF-8
import amazon


def main():

    # Amazon
    amazon = amazon.Amazon()
    amazon.search_word = "SEARCH WORD"
    amazon.start()


if __name__ == "__main__":
    main()