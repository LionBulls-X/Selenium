import customtkinter as ctk
import webbrowser
import random
import time
import threading

BG_DARK = "#0D1317"
ACCENT_GREEN = "#00FF7F"
ACCENT_BLUE = "#1E90FF"
ACCENT_PURPLE = "#FF00FF"
ACCENT_ORANGE = "#FF8C00"

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green") 

class PredictorWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("⚡ DarkTK Oracle PREDICTOR by Dfxit")
        self.geometry("900x650")
        self.configure(fg_color=BG_DARK)
        self.resizable(False, False)
        self.grab_set() 
        
        self.is_running = True
        self.pulse_state = False
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self._create_sidebar()
        self._create_main_panel()
        
        threading.Thread(target=self.start_analysis_simulation, daemon=True).start()

    def _create_sidebar(self):
        sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=15, fg_color="#1A242B")
        sidebar_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")
        sidebar_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(sidebar_frame, text="📊 Аналитика & История", 
                     font=ctk.CTkFont(size=20, weight="bold"), text_color=ACCENT_GREEN).pack(pady=(30, 20))

        success_block = ctk.CTkFrame(sidebar_frame, fg_color="transparent")
        success_block.pack(pady=10, padx=20, fill="x")
        ctk.CTkLabel(success_block, text="Успешность (Прошлые 10)", font=ctk.CTkFont(size=14, weight="normal"), justify="left").pack(side="left")
        self.success_label = ctk.CTkLabel(success_block, text="85%", font=ctk.CTkFont(size=18, weight="bold"), text_color=ACCENT_GREEN)
        self.success_label.pack(side="right")

        avg_block = ctk.CTkFrame(sidebar_frame, fg_color="transparent")
        avg_block.pack(pady=(5, 20), padx=20, fill="x")
        ctk.CTkLabel(avg_block, text="Средний X (Прогноз)", font=ctk.CTkFont(size=14, weight="normal"), justify="left").pack(side="left")
        self.avg_x_label = ctk.CTkLabel(avg_block, text="2.34X", font=ctk.CTkFont(size=18, weight="bold"), text_color=ACCENT_PURPLE)
        self.avg_x_label.pack(side="right")
        
        ctk.CTkFrame(sidebar_frame, height=2, fg_color="#33424A").pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(sidebar_frame, text="⏱️ Последние Сигналы", 
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(20, 10))
        
        self.history_text = ctk.CTkLabel(sidebar_frame, 
                                         text="Раунд 205: 1.77X ✅\nРаунд 204: 1.30X ❌\nРаунд 203: 2.51X ✅\n...",
                                         font=ctk.CTkFont(size=14), justify="left", text_color="#A9B7C6")
        self.history_text.pack(padx=20, pady=10, fill="x", expand=True, anchor="n")

    def _create_main_panel(self):
        main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#1A242B")
        main_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(main_frame, text="🧠 LIVE СИГНАЛ", 
                     font=ctk.CTkFont(size=30, weight="bold", slant="italic"), text_color=ACCENT_GREEN).pack(pady=(30, 10))

        self.signal_block = ctk.CTkFrame(main_frame, corner_radius=25, fg_color="#33424A", border_width=2, border_color="#33424A")
        self.signal_block.pack(fill="both", padx=40, pady=20, expand=True)
        
        self.countdown_label = ctk.CTkLabel(self.signal_block, text="Начало раунда через: 10 сек...", 
                                            font=ctk.CTkFont(size=20, weight="bold"))
        self.countdown_label.pack(pady=(40, 10))
        
        self.forecast_label = ctk.CTkLabel(self.signal_block, text="АНАЛИЗ...", 
                                           font=ctk.CTkFont(family="Consolas", size=90, weight="bold"), text_color="#AAAAAA")
        self.forecast_label.pack(expand=True, fill="both")
        
        ctk.CTkLabel(self.signal_block, text="Софт подключен к серверам анализа. Ожидайте активации...", 
                     font=ctk.CTkFont(size=15), text_color="#999999").pack(pady=(10, 40))

        ctk.CTkButton(main_frame, text="АВТОМАТИЧЕСКИЙ АНАЛИЗ АКТИВЕН 🟢", 
                      fg_color=ACCENT_GREEN, hover_color="#00CC00", 
                      font=ctk.CTkFont(size=18, weight="bold"), 
                      text_color="black", state="disabled", height=50, corner_radius=12).pack(pady=(10, 30), padx=40, fill="x")

    def generate_forecast(self):
        r = random.random()
        if r < 0.45:
            forecast = random.uniform(1.01, 1.5)
            color = ACCENT_ORANGE
            freq = "ЧАСТЫЙ"
        elif r < 0.85:
            forecast = random.uniform(1.5, 2.0)
            color = ACCENT_GREEN
            freq = "НОРМА"
        else:
            forecast = random.uniform(2.0, 5.0)
            color = ACCENT_PURPLE
            freq = "РЕДКИЙ"
        return forecast, color, freq

    def update_forecast(self, forecast, color):
        self.forecast_label.configure(text=f"{forecast:.2f}X", text_color=color)
        self.signal_block.configure(border_color=color)

    def _pulse_signal(self, current_color, count=0):
        if not self.is_running or count >= 10:
            self.signal_block.configure(border_color=current_color)
            return

        if self.pulse_state:
            self.signal_block.configure(border_color="#FFFFFF")
            self.pulse_state = False
        else:
            self.signal_block.configure(border_color=current_color)
            self.pulse_state = True

        self.after(200, lambda: self._pulse_signal(current_color, count + 1))


    def start_analysis_simulation(self):
        while self.is_running:
            # 1. ФАЗА ОЖИДАНИЯ
            wait_time = random.randint(8, 12)
            self.forecast_label.configure(text="⏳ ОЖИДАНИЕ", font=ctk.CTkFont(size=50, weight="bold"), text_color="#A9B7C6")
            self.signal_block.configure(border_color="#33424A")

            for i in range(wait_time, 0, -1):
                if not self.is_running: return
                self.countdown_label.configure(text=f"Начало раунда через: {i} сек...")
                time.sleep(1)

            # 2. ФАЗА АНАЛИЗА
            self.countdown_label.configure(text="ИДЕТ АНАЛИЗ... 🧠")
            self.forecast_label.configure(text="АНАЛИЗ...", font=ctk.CTkFont(size=90, weight="bold"), text_color=ACCENT_BLUE)
            
            analysis_time = random.uniform(2, 4)
            time.sleep(analysis_time)

            # 3. ФАЗА СИГНАЛА
            forecast, color, freq = self.generate_forecast()
            self.update_forecast(forecast, color)
            self.countdown_label.configure(text=f"СИГНАЛ АКТИВЕН ({freq}) ✅")
            
            self._pulse_signal(color)

            time.sleep(10)

    def destroy(self):
        self.is_running = False
        super().destroy()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("GameTactic Pro v1.1 | Главное Меню")
        self.geometry("650x450")
        self.configure(fg_color=BG_DARK)
        self.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(self, text="⚡ GameTactic Pro: Выберите раздел ⚡", 
                     font=ctk.CTkFont(size=26, weight="bold"), text_color=ACCENT_GREEN).pack(pady=(40, 20))

        ctk.CTkButton(self, text="🚀 GIFTUP: Анализ Тактик", 
                      command=self.open_giftup,
                      fg_color=ACCENT_GREEN, hover_color="#00CC00", 
                      font=ctk.CTkFont(size=20, weight="bold"), 
                      text_color="black", height=70, corner_radius=15, 
                      border_width=2, border_color="#33FF33").pack(pady=20, padx=80, fill="x")

        ctk.CTkButton(self, text="⚽ ФУТБОЛЬНЫЙ РАЙ (Мини-Игра)", 
                      command=self.open_football,
                      fg_color=ACCENT_BLUE, hover_color="#007ACC", 
                      font=ctk.CTkFont(size=20, weight="bold"), 
                      text_color="white", height=70, corner_radius=15,
                      border_width=2, border_color="#3399FF").pack(pady=20, padx=80, fill="x")
    
    def open_giftup(self):
        url = "https://t.me/GiftUpRobot?start=6880150992"
        webbrowser.open(url)
        try:
            PredictorWindow(self)
        except Exception as e:
            print(f"Ошибка открытия окна: {e}")

    def open_football(self):
        url = "https://t.me/Doxbingame_bot"
        webbrowser.open(url)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()