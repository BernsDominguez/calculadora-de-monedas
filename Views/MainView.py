from tkinter import Tk, Label, Button, Entry, N, S, E, W, StringVar, OptionMenu

class MainView(Tk):
    class Constants:
        title = "Cambio de Moneda"
        heigth = 100
        width = 550
        input_width = 250
        separator_width = 50
        center = N + S + E + W
        left = W
        event = "<Button-1>"
        convert_text = "Convertir"
        separator_text = "▶"
        Currencies = [
            'USD',
            'MXN',
            'JPY',
            'BGN',
            'CZK',
            'DKK',
            'GBP',
            'HUF',
            'PLN',
            'RON',
            'SEK',
            'CHF',
            'NOK',
            'HRK',
            'RUB',
            'TRY',
            'AUD',
            'BRL',
            'CAD',
            'CNY',
            'HKD',
            'IDR',
            'ILS',
            'INR',
            'KRW',
            'MYR',
            'NZD',
            'PHP',
            'SGD',
            'THB',
            'ZAR'
        ]

    def __init__(self, convert_handler = None):
        super().__init__()
        self.__convert_handler = convert_handler
        self.title(self.Constants.title)
        self.maxsize(width = self.Constants.width, height = self.Constants.heigth)
        self.minsize(width = self.Constants.width, height = self.Constants.heigth)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight = True)
        self.grid_rowconfigure(1, weight = True)
        self.grid_rowconfigure(2, weight = True)
        self.grid_columnconfigure(0, minsize = self.Constants.input_width)
        self.grid_columnconfigure(2, minsize = self.Constants.input_width)
        self.grid_columnconfigure(1, minsize = self.Constants.separator_width)

    def __configure_UI(self):
        self.listOne = StringVar(self)
        self.listOne.set(self.Constants.Currencies[0])
        self.dropCurrencyFrom = OptionMenu(self, self.listOne, *self.Constants.Currencies)
        self.dropCurrencyFrom.grid(row = 0, column = 0, sticky = self.Constants.left)

        self.listTwo = StringVar(self)
        self.listTwo.set(self.Constants.Currencies[1])
        self.dropCurrencyTo = OptionMenu(self, self.listTwo, *self.Constants.Currencies)
        self.dropCurrencyTo.grid(row = 0, column = 2, sticky = self.Constants.left)

        separator_label = Label(self)
        separator_label.configure(text = self.Constants.separator_text)
        separator_label.grid(row = 1, column = 1, sticky = self.Constants.center)

        self.__result_label = Label(self)
        self.__result_label.configure(text = "0")
        self.__result_label.grid(row = 1, column = 2, sticky = self.Constants.left)

        self.__convert_button = Button(self)
        self.__convert_button.configure(text = self.Constants.convert_text)
        self.__convert_button.grid(row = 2, column = 2, sticky = self.Constants.center)
        self.__convert_button.bind(self.Constants.event, self.__did_tap_convert)

        vcmd = (self.register(self.__checkNumberOnly), '%d', '%P')
        self.__currency_input = Entry(self, validate = "key", validatecommand = vcmd)
        self.__currency_input.grid(row = 1, column = 0, sticky = self.Constants.center)

    def __did_tap_convert(self, event):
        if self.__convert_handler is None:
            return
        try:
            amount_to_convert = float(self.__currency_input.get())
        except ValueError:
            return
        else:
            self.__convert_handler(self.listOne.get(), self.listTwo.get(), amount_to_convert)

    def update_result(self, text):
        self.__result_label.configure(text = text)


    def __checkNumberOnly(self, action, value_if_allowed):
        if action != '1':
            return True
        try:
            float(value_if_allowed)
        except ValueError:
            return False
        else:
            return True



