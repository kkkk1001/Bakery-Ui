import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        self.sand = Entry(window, width = 10)
        self.cake = Entry(window, width = 10)
        Label(window, text = "샌드위치 (5000원)").grid(column= 0, row = 0)
        Label(window, text = "케이크 (20000원)").grid(column= 0, row = 1)
        self.sand.grid(column = 1, row = 0)
        self.cake.grid(column = 1, row = 1)
        self.btn_order = Button(window, text = "주문하기", command = self.send_order)
        self.btn_order.grid(column = 0,row = 2)
        window.geometry('350x200')

    def send_order(self):
        order_text = ""
        sandnum = self.sand.get()
        cakenum = self.cake.get()
        sachk, cachk = 0,0 
        try:
            int(sandnum)
        except:
            sachk = 1
        try:
            int(cakenum)
        except:
            cachk = 1
        if sachk == 0 and int(sandnum) <= 0:
            sachk = 1
        if cachk == 0 and int(cakenum) <= 0:
            cachk = 1

        if sachk == 1 and cachk == 1:
            return
        elif sachk == 1:
            order_text = self.name +": 케이크(20000원) " + cakenum + "개"
        elif cachk == 1:
            order_text = self.name + ": 샌드위치(5000원) " + sandnum + "개"
        else:
            order_text = self.name + ": 샌드위치(5000원) " + sandnum + "개, 케이크 (20000원) " + cakenum + "개"

        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
