import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class AplikasiTkinter:
    def __init__(self, root):
        self.root = root

        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.default_bg_path = "background.png"
        self.new_page_bg_path = "terbaru.png"

        self.photo_background_default = None
        self.photo_background_new_page = None
        self.content_bg_color = "#D9F2F4"

        try:
            bg_image = Image.open(self.default_bg_path).resize(
                (self.screen_width, self.screen_height), Image.LANCZOS
            )
            self.photo_background_default = ImageTk.PhotoImage(bg_image)

            new_bg_image = Image.open(self.new_page_bg_path).resize(
                (self.screen_width, self.screen_height), Image.LANCZOS
            )
            self.photo_background_new_page = ImageTk.PhotoImage(new_bg_image)

            self.bg_label = tk.Label(self.root, image=self.photo_background_default)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.root.configure(bg=self.content_bg_color)
            self.bg_label = tk.Label(self.root, bg=self.content_bg_color)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_page_widgets = []
        self.about_photo_refs = []

        self.button_normal_bg = "#18AEB9"
        self.button_hover_bg = "#14959E"
        self.button_text_fg = "white"

        self.show_home_screen()

    def clear_current_page(self):
        for widget in self.current_page_widgets:
            if widget.winfo_exists():
                widget.destroy()
        self.current_page_widgets.clear()
        self.about_photo_refs.clear()

    def bind_hover_effects(self, button):
        button.bind("<Enter>", lambda e: button.config(bg=self.button_hover_bg))
        button.bind("<Leave>", lambda e: button.config(bg=self.button_normal_bg))

    def show_home_screen(self):
        self.clear_current_page()

        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        try:
            img = Image.open("sehun.png").resize((400, 250), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            label_gambar = tk.Label(self.bg_label, image=self.photo, bg=self.content_bg_color)
        except FileNotFoundError:
            print("Error: sehun.png tidak ditemukan.")
            label_gambar = tk.Label(self.bg_label, text="Gambar tidak ditemukan", bg=self.content_bg_color)

        label_gambar.pack(pady=10)
        self.current_page_widgets.append(label_gambar)

        start_button = tk.Button(
            self.bg_label,
            text="Start",
            command=self.on_start_button_click,
            font=("Poppins", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        start_button.pack(pady=5)
        self.current_page_widgets.append(start_button)
        self.bind_hover_effects(start_button)

        about_button = tk.Button(
            self.bg_label,
            text="About",
            command=self.on_about_button_click,
            font=("Poppins", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        about_button.pack(pady=5)
        self.current_page_widgets.append(about_button)
        self.bind_hover_effects(about_button)

        exit_button = tk.Button(
            self.bg_label,
            text="Exit",
            command=self.on_exit_button_click,
            font=("Poppins", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        exit_button.pack(pady=5)
        self.current_page_widgets.append(exit_button)
        self.bind_hover_effects(exit_button)

    def show_new_page(self):


        self.clear_current_page()

        if self.photo_background_new_page:
            self.bg_label.config(image=self.photo_background_new_page)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        foto_bendera = "bendera_merah.png"
        foto_bendera2 = "bendera_biru.png"

        try:
            img1 = Image.open("bendera_merah.png").resize((180, 210), Image.LANCZOS)
            foto1 = ImageTk.PhotoImage(img1)
            self.about_photo_refs.append(foto1)

            label1 = tk.Label(self.bg_label, image=foto1, bg=self.content_bg_color)
            label1.pack(side=tk.LEFT, pady=200)
            label1.pack(padx=2) 
            self.current_page_widgets.append(label1)
        except FileNotFoundError:
            print("Error: bendera_merah.png tidak ditemukan.")
            label1 = tk.Label(self.bg_label, text="bendera_merah.png tidak ditemukan", bg=self.content_bg_color)
            label1.pack(pady=5)
            self.current_page_widgets.append(label1)

        
        try:
            img2 = Image.open("bendera_biru.png").resize((180, 210), Image.LANCZOS)
            foto2 = ImageTk.PhotoImage(img2)
            self.about_photo_refs.append(foto2)

            label2 = tk.Label(self.bg_label, image=foto2, bg=self.content_bg_color)
            label2.pack(side=tk.RIGHT, padx=20) 
            label2.pack(pady=10) 
            self.current_page_widgets.append(label2)
        except FileNotFoundError:
            print("Error: bendera_biru.png tidak ditemukan.")
            label2 = tk.Label(self.bg_label, text="bendera_biru.png tidak ditemukan", bg=self.content_bg_color)
            label2.pack(pady=5)
            self.current_page_widgets.append(label2)

        back_button = tk.Button(
            self.bg_label,
            text="Kembali Ke Home",
            command=self.show_home_screen,
            font=("Poppins", 12),
            pady=10,
            bg="#56f895",
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        back_button.pack(side=tk.BOTTOM, pady=20)
        self.current_page_widgets.append(back_button)
        self.bind_hover_effects(back_button)
       

    def show_about_page(self):
        self.clear_current_page()

        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        title_label = tk.Label(self.bg_label, text="About Us", font=("Poppins", 30), bg=self.content_bg_color)
        title_label.pack(pady=20)
        self.current_page_widgets.append(title_label)

        photos_container = tk.Frame(self.bg_label, bg=self.content_bg_color)
        photos_container.pack(pady=10)
        self.current_page_widgets.append(photos_container)

        foto_files = ["foto1.png", "foto2.png", "foto3.png", "foto4.png"]
        orang_names = ["Filuth Ridho Aji", "Rahmad Veri Apriansah", "Zahira Adiah Safa", "Talitha Roihanah Salsabila"]

        for i, foto_file in enumerate(foto_files):
            person_frame = tk.Frame(photos_container, bg="white")
            person_frame.pack(side=tk.LEFT, padx=5, pady=10)
            self.current_page_widgets.append(person_frame)

            try:
                img_pil = Image.open(foto_file).resize((180, 210), Image.LANCZOS)
                photo_tk = ImageTk.PhotoImage(img_pil)
                self.about_photo_refs.append(photo_tk)

                photo_label = tk.Label(person_frame, image=photo_tk, bg=self.content_bg_color)
                photo_label.pack(pady=5)
                self.current_page_widgets.append(photo_label)

                name_label = tk.Label(person_frame, text=orang_names[i], font=("Poppins", 14), fg="black", bg="white")
                name_label.pack(pady=2)
                self.current_page_widgets.append(name_label)

            except FileNotFoundError:
                print(f"Error: {foto_file} tidak ditemukan.")
                placeholder = tk.Label(person_frame, text=f"Foto {i+1}\nTidak Ditemukan",
                                       font=("Arial", 10), width=20, height=10,
                                       bg="lightgray", fg="red")
                placeholder.pack(pady=5)
                self.current_page_widgets.append(placeholder)

                name_label = tk.Label(person_frame, text=orang_names[i], font=("Poppins", 12), bg=self.content_bg_color)
                name_label.pack(pady=2)
                self.current_page_widgets.append(name_label)

        back_button = tk.Button(
            self.bg_label,
            text="Kembali ke Home",
            command=self.show_home_screen,
            font=("Poppins", 12),
            pady=10,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        back_button.pack(pady=20)
        self.current_page_widgets.append(back_button)
        self.bind_hover_effects(back_button)

    def on_start_button_click(self):
        self.show_new_page()

    def on_about_button_click(self):
        self.show_about_page()

    def on_exit_button_click(self):
        if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar dari aplikasi?"):
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()
