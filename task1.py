import random
import webbrowser


def getlink():
    l = ["https://github.com/", "https://www.google.com/", "https://www.linkedin.com/feed/",
         "https://www.youtube.com/",

         ]
    x = random.randint(0, 3)
    print(l[x])
    webbrowser.open(f"{l[x]}")


getlink()
