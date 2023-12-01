class phone:
    def call(self):
        print("You can call")

    def message(self):
        print("you can message")

    def photo(self):
        print("you  can take photo")


class samsung(phone):
    def call(self):
        print("YOu can call")

    def message(self):
        print("ypu can message")


p=phone()
s=samsung()

s.message()
s.call()
s.photo()
print(issubclass(samsung,phone))