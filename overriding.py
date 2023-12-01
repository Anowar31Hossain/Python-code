class phone:
    def __init__(self):
        print("Iam a man")

class samsung(phone):
     def __init__(self):
         super().__init__()
         print("Iam a man2")


s=samsung()