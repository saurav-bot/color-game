class Subscriber:
    def __init__(self):
        self.obj = {
        "salt":{"white"},
        "banana":{"green", "yellow"},
        "ink" : {"red", "black"},
        "blood":{"red"},
        "sky": {"blue", "black"},
        "apple":{"green", "red"},
        "frog":{"blue", "yellow"}
        }

        self.subscribed = []

def printColor(ans, subs):
    for key in subs.subscribed:
        if ans in subs.obj[key]:
            if key == "frog":
                print(f"I'm Frog! I am {ans} today")
                print()
            else:
                print(f"I'm {key}! I'm sometimes {ans}")
                print()

def main():
    subs = Subscriber()
    while True:
        ans = input("")
        if ans[0] == "+" and ans[1:] not in subs.subscribed:
            subs.subscribed.append(ans[1:])
        elif ans[0] == "-" and ans[1:] in subs.subscribed:
            subs.subscribed.remove(ans[1:])
        elif ans == "list":
            print(subs.subscribed)
        elif ans == "exit":
            break
        else:
            printColor(ans, subs)
            
main()

 