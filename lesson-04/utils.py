import time


def calc_time():
    print("calc_time")


def predict(model):
    print("predict", model)



if __name__ == "__main__":
    print("__main__ in utils")
    model = object()
    predict(model)
