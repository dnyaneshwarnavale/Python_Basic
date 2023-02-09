def searcher():
    import time
    # some 4 seconds time cinsuming task
    book="This is book on harry and coded with haryy and good"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print ("your text is in the book")
        else:
            print("text is not in the book")

search=searcher()
next(search)
search.send("harry")
input("press any key")
search.send("harry and")
input("press any key")
search.send("good")
input("press any key")
search.send("like")
input("press any key")
search.send("football")
