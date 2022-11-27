import customtkinter
from RadioButtonFrame import RadioButtonFrame

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("RadioButtonFrame test")

        self.radio_button_frame_1 = RadioButtonFrame(self, header_name="RadioButtonFrame 1")
        self.radio_button_frame_1.grid(row=0, column=0, padx=20, pady=20)

        self.frame_1_button = customtkinter.CTkButton(self, text="Print value of frame 1", command=self.print_value_frame_1)
        self.frame_1_button.grid(row=1, column=0, padx=20, pady=10)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Kratzen", text_font=("Roboto", -16))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_callback)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_callback)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_callback)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        # self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def print_value_frame_1(self):
        print(f"Frame 1 value: {self.radio_button_frame_1.get_value()}")

    def sidebar_button_callback(self):
        print("sidebar_button click")

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()