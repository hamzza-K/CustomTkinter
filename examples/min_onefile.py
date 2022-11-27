import customtkinter

# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title('minimal example app')
#         self.minsize(500, 400)

#         self.button = customtkinter.CTkButton(master=self,
#                 command=self.button_callback)
#         self.button.pack(padx=30, pady=40)

#     def button_callback(self):
#         print('button pressed')



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x300')
        self.title('small example')
        self.minsize(500, 300)

if __name__ == '__main__':
   app = App()
   app.mainloop()
