import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DelayCalcPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Studio Time Calc")
        self.geometry("450x600")
        
        # This makes the app responsive
        self.grid_columnconfigure(0, weight=1)

        # --- HEADER ---
        self.header = ctk.CTkLabel(self, text="TIME CALCULATOR", font=("Arial", 22, "bold"))
        self.header.grid(row=0, column=0, pady=(20, 10))

        # --- INPUT SECTION ---
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.bpm_label = ctk.CTkLabel(self.input_frame, text="BPM:", font=("Arial", 14))
        self.bpm_label.pack(side="left", padx=10, pady=15)
        
        self.bpm_entry = ctk.CTkEntry(self.input_frame, width=100, placeholder_text="120")
        self.bpm_entry.pack(side="left", padx=10)
        
        # 1. BIND ENTER KEY: This makes the "Enter" key trigger the calculation
        self.bpm_entry.bind("<Return>", lambda event: self.update_ui())

        self.calc_button = ctk.CTkButton(self.input_frame, text="Calculate", width=80, command=self.update_ui)
        self.calc_button.pack(side="right", padx=10)

        # --- RESULTS SECTION ---
        self.results_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.results_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.results_frame.grid_columnconfigure(0, weight=1)

    def create_result_row(self, label_text, value, row_idx):
        """Creates a row with a copy button that gives feedback"""
        frame = ctk.CTkFrame(self.results_frame)
        frame.grid(row=row_idx, column=0, pady=5, sticky="ew")
        
        lbl = ctk.CTkLabel(frame, text=label_text, font=("Arial", 13))
        lbl.pack(side="left", padx=10)
        
        val_str = f"{value:.2f} ms"
        val_lbl = ctk.CTkLabel(frame, text=val_str, font=("Consolas", 14, "bold"), text_color="#1f93ff")
        val_lbl.pack(side="right", padx=(0, 10))
        
        # 2. UPDATED COPY BUTTON: Using "COPY" text for clarity
        copy_btn = ctk.CTkButton(frame, text="COPY", width=50, height=25, 
                                 fg_color="gray20", hover_color="gray30", font=("Arial", 10, "bold"))
        
        # We use a command that handles the feedback
        copy_btn.configure(command=lambda: self.copy_to_clipboard(value, copy_btn))
        copy_btn.pack(side="right", padx=5)

    def copy_to_clipboard(self, value, button_widget):
        """Copies value and changes button text briefly"""
        self.clipboard_clear()
        self.clipboard_append(f"{value:.2f}")
        
        # Change button state to show success
        button_widget.configure(text="DONE!", fg_color="#2eb85c")
        
        # Reset the button after 1 second
        self.after(1000, lambda: button_widget.configure(text="COPY", fg_color="gray20"))

    def update_ui(self):
        try:
            # Clear previous results
            for widget in self.results_frame.winfo_children():
                widget.destroy()

            bpm_text = self.bpm_entry.get()
            if not bpm_text: return # Don't do anything if empty
            
            bpm = float(bpm_text)
            quarter = 60000 / bpm
            
            data = [
                ("1/4 Note", quarter),
                ("1/8 Note", quarter / 2),
                ("1/16 Note", quarter / 4),
                ("1/32 Note", quarter / 8),
                ("Pre-Delay (1/64)", quarter / 16),
                ("Reverb Decay (1 Bar)", quarter * 4)
            ]

            for i, (name, val) in enumerate(data):
                self.create_result_row(name, val, i)

        except ValueError:
            error_lbl = ctk.CTkLabel(self.results_frame, text="Invalid BPM - Numbers only!", text_color="#ff4d4d")
            error_lbl.grid(row=0, column=0, pady=20)

if __name__ == "__main__":
    app = DelayCalcPro()
    app.mainloop()