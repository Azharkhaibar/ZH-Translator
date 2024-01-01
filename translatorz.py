import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZHTranslator")

        self.label = tk.Label(root, text="Masukkan teks yang ingin diterjemahkan : ")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.label_language = tk.Label(root, text="Masukkan bahasa tujuan : ")
        self.label_language.pack(pady=10)

        self.entry_language = tk.Entry(root, width=10)
        self.entry_language.pack(pady=10)

        self.translate_button = tk.Button(root, text="Terjemahkan", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def translate_text(self):
        input_text = self.entry.get()
        target_language = self.entry_language.get()

        if input_text and target_language:
            translator = Translator()
            translated_text = translator.translate(input_text, dest=target_language).text
            result_text = f'Teks terjemahan: {translated_text}'
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Masukkan teks dan bahasa tujuan")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
