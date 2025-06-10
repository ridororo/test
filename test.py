import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("widget")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.photo_background_default = None
        self.photo_background_new_page = None
        self.photo_background_game = None
        self.default_bg_path = "background.png"
        self.new_page_bg_path = "bg2.png"
        self.game_bg_path = "bg3.png"

        try:
            original_bg_image_pil = Image.open(self.default_bg_path)
            resized_bg_image_pil = original_bg_image_pil.resize((self.screen_width, self.screen_height), Image.LANCZOS)
            self.photo_background_default = ImageTk.PhotoImage(resized_bg_image_pil)

            original_new_page_bg_pil = Image.open(self.new_page_bg_path)
            resized_new_page_bg_pil = original_new_page_bg_pil.resize((self.screen_width, self.screen_height), Image.LANCZOS)
            self.photo_background_new_page = ImageTk.PhotoImage(resized_new_page_bg_pil)

            original_game_bg_pil = Image.open(self.game_bg_path)
            resized_game_bg_pil = original_game_bg_pil.resize((self.screen_width, self.screen_height), Image.LANCZOS)
            self.photo_background_game = ImageTk.PhotoImage(resized_game_bg_pil)

            self.bg_label = tk.Label(self.root, image=self.photo_background_default)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.content_bg_color = "#D9F2F4"

        except FileNotFoundError as e:
            print(f"Error: File background tidak ditemukan ({e}). Menggunakan warna latar belakang default.")
            self.content_bg_color = "#D9F2F4"
            self.root.configure(bg=self.content_bg_color)
            self.bg_label = tk.Label(self.root, bg=self.content_bg_color)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_page_widgets = []
        self.about_photo_refs = []
        self.username = ""

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

    def show_game_page(self):
        self.clear_current_page()

        if hasattr(self, 'photo_background_game') and self.photo_background_game:
            self.bg_label.config(image=self.photo_background_game)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)
            print("Peringatan: bg3.png tidak ditemukan, menggunakan warna latar default.")

        home_button = tk.Button(
            self.bg_label,
            text="< Back to Home",
            command=self.show_home_screen,
            font=("Poppins", 12, "bold"),
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        home_button.place(x=20, y=20)
        self.current_page_widgets.append(home_button)
        self.bind_hover_effects(home_button)

        game_info_label = tk.Label(
            self.bg_label,
            text=f"Pilih Aksimu!, {self.username}!",
            font=("Basketball", 22, "bold"),
            bg="#D9F2F4",
            fg="black"
        )
        game_info_label.pack(pady=(100, 20))
        self.current_page_widgets.append(game_info_label)

        # --- BLOK KODE BARU UNTUK TOMBOL AKSI ---
        # Tombol Menanam
        plant_button = tk.Button(
            self.bg_label,
            text="Menanam",
            # command=self.fungsi_menanam, # Ganti dengan fungsi yang sesuai
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        plant_button.pack(pady=5)
        self.current_page_widgets.append(plant_button)
        self.bind_hover_effects(plant_button)

        # Tombol Menyiram
        water_button = tk.Button(
            self.bg_label,
            text="Menyiram",
            # command=self.fungsi_menyiram, # Ganti dengan fungsi yang sesuai
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        water_button.pack(pady=5)
        self.current_page_widgets.append(water_button)
        self.bind_hover_effects(water_button)

        # Tombol Memetik
        harvest_button = tk.Button(
            self.bg_label,
            text="Memetik",
            # command=self.fungsi_memetik, # Ganti dengan fungsi yang sesuai
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        harvest_button.pack(pady=5)
        self.current_page_widgets.append(harvest_button)
        self.bind_hover_effects(harvest_button)
        # --- AKHIR BLOK KODE BARU ---


    def show_home_screen(self):
        self.clear_current_page()

        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        try:
            img = Image.open("sehun.png")
            img = img.resize((400, 250), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.label_gambar = tk.Label(self.bg_label, image=self.photo, bg="#D9F2F4")
        except FileNotFoundError:
            print("Error: sehun.png tidak ditemukan.")
            self.label_gambar = tk.Label(self.bg_label, text="Gambar tidak ditemukan", bg="#D9F2F4")

        self.label_gambar.pack(pady=10)
        self.current_page_widgets.append(self.label_gambar)

        self.start_button = tk.Button(
            self.bg_label,
            text="Start",
            command=self.on_start_button_click,
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        self.start_button.pack(pady=5)
        self.current_page_widgets.append(self.start_button)
        self.bind_hover_effects(self.start_button)

        self.about_button = tk.Button(
            self.bg_label,
            text="About",
            command=self.on_about_button_click,
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        self.about_button.pack(pady=5)
        self.current_page_widgets.append(self.about_button)
        self.bind_hover_effects(self.about_button)

        self.exit_button = tk.Button(
            self.bg_label,
            text="Exit",
            command=self.on_exit_button_click,
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        self.exit_button.pack(pady=5)
        self.current_page_widgets.append(self.exit_button)
        self.bind_hover_effects(self.exit_button)

    def show_new_page(self):
        self.clear_current_page()

        if self.photo_background_new_page:
            self.bg_label.config(image=self.photo_background_new_page)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        label_username = tk.Label(
            self.bg_label,
            text="Masukan Username Anda:",
            font=("Poppins", 16),
            bg=self.content_bg_color,
        )
        label_username.pack(pady=(100, 10))
        self.current_page_widgets.append(label_username)

        self.entry_username = tk.Entry(
            self.bg_label,
            font=("Poppins", 14),
            width=25,
            bd=2,
            relief="flat",
            justify="center"
        )
        self.entry_username.pack(pady=10)
        self.entry_username.configure(highlightbackground="green", highlightcolor="green", highlightthickness=2)
        self.current_page_widgets.append(self.entry_username)

        next_button = tk.Button(
            self.bg_label,
            text="Next",
            command=self.on_next_button_click,
            font=("Poppins", 14),
            width=10,
            height=1,
            bg="#18AEB9",
            fg="white",
            relief="flat",
            activebackground="#14959E"
        )
        next_button.pack(pady=20)
        self.current_page_widgets.append(next_button)

    def on_next_button_click(self):
        username = self.entry_username.get()
        if username.strip():
            self.username = username
            self.show_tanaman_page()
        else:
            messagebox.showwarning("Input Kosong", "Silakan masukkan username terlebih dahulu.")

    def show_tanaman_page(self):
        self.clear_current_page()

        if self.photo_background_new_page:
            self.bg_label.config(image=self.photo_background_new_page)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        label_tanaman = tk.Label(
            self.bg_label,
            text="Masukan Nama Tanaman Yang Akan Ditanam :",
            font=("Poppins", 16),
            fg="darkgreen",
            bg=self.content_bg_color
        )
        label_tanaman.pack(pady=(100, 10))
        self.current_page_widgets.append(label_tanaman)

        self.entry_tanaman = tk.Entry(
            self.bg_label,
            font=("Poppins", 14),
            width=30,
            bd=2,
            relief="flat",
            justify="center"
        )
        self.entry_tanaman.configure(highlightbackground="green", highlightcolor="green", highlightthickness=2)
        self.entry_tanaman.pack(pady=10)
        self.current_page_widgets.append(self.entry_tanaman)

        ok_button = tk.Button(
            self.bg_label,
            text="Ok",
            command=self.on_ok_button_click,
            font=("Poppins", 14),
            width=10,
            height=1,
            bg="#18AEB9",
            fg="white",
            relief="flat",
            activebackground="#14959E"
        )
        ok_button.pack(pady=20)
        self.current_page_widgets.append(ok_button)

    def on_ok_button_click(self):
        if self.entry_tanaman.get().strip():
            self.clear_current_page()
        else:
            messagebox.showwarning("Input Kosong", "Silakan masukkan nama tanaman terlebih dahulu.")
            return
        if self.photo_background_new_page:
            self.bg_label.config(image=self.photo_background_new_page)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        title_label = tk.Label(
            self.bg_label,
            text="Welcome To Garden Heroes!",
            font=("Poppins", 24, "bold"),
            bg=self.content_bg_color,
            fg="black"
        )
        title_label.pack(pady=(80, 20))
        self.current_page_widgets.append(title_label)

        deskripsi_frame = tk.Frame(self.bg_label, bg="#00CFC1", bd=0)
        deskripsi_frame.pack(pady=10)
        self.current_page_widgets.append(deskripsi_frame)

        deskripsi_label = tk.Label(
            deskripsi_frame,
            text="Di game ini, kamu berperan\nsebagai penjaga kebun\nTujuanmu adalah merawat\n"
                 "tanaman dan mendapatkan\nscore sebanyak banyaknya!",
            font=("Poppins", 14),
            bg="#00CFC1",
            fg="white",
            justify="center"
        )
        deskripsi_label.pack(padx=30, pady=20)

        ok_button = tk.Button(
            self.bg_label,
            text="Ok",
            font=("Poppins", 14, "bold"),
            width=10,
            height=1,
            bg="#18AEB9",
            fg="white",
            command=self.show_game_page,
            relief="flat",
            activebackground="#14959E"
        )
        ok_button.pack(pady=30)
        self.current_page_widgets.append(ok_button)

    def show_about_page(self):
        self.clear_current_page()

        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

        about_title_label = tk.Label(self.bg_label, text="About Us", font=("Basketball", 30), bg=self.content_bg_color)
        about_title_label.pack(pady=20)
        self.current_page_widgets.append(about_title_label)

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
                img_pil = Image.open(foto_file)
                img_pil = img_pil.resize((180, 210), Image.LANCZOS)
                photo_tk = ImageTk.PhotoImage(img_pil)
                self.about_photo_refs.append(photo_tk)

                photo_label = tk.Label(person_frame, image=photo_tk, bg=self.content_bg_color)
                photo_label.pack(pady=5)

                name_label = tk.Label(person_frame, text=orang_names[i], font=("Basketball", 14), fg="white", bg="black")
                name_label.pack(pady=2)

            except FileNotFoundError:
                print(f"Error: {foto_file} tidak ditemukan. Menampilkan placeholder.")
                placeholder_label = tk.Label(person_frame, text=f"Foto {i+1}\nTidak Ditemukan",
                                              font=("Arial", 10), width=20, height=10,
                                              bg="lightgray", fg="red")
                placeholder_label.pack(pady=5)

                name_label = tk.Label(person_frame, text=orang_names[i], font=("Arial", 12), bg=self.content_bg_color)
                name_label.pack(pady=2)

        back_button = tk.Button(
            self.bg_label,
            text="Back to Home",
            command=self.show_home_screen,
            font=("Arial", 12),
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
