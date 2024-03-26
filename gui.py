import tkinter as tk
from tkinter import scrolledtext
from predict import make_prediction  # make sure this function can handle the model and vectorizer

def start_gui(model, vectorizer):
    window = tk.Tk()
    window.title("Toxic Comment Classifier")

    # Setup the GUI layout here
    # Include an input area for comments, a button to submit, and an area to display predictions
    
    # Example of a function to handle button click event
    def on_classify_button_click():
        comment = input_text_area.get("1.0", tk.END).strip()
        prediction = make_prediction(model, vectorizer, comment)
        result_display_area.config(state=tk.NORMAL)  # Enable the widget before inserting
        result_display_area.insert(tk.END, str(prediction) + '\n')
        result_display_area.config(state=tk.DISABLED)

    # Example components
    input_text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    input_text_area.pack(pady=10)

    classify_button = tk.Button(window, text="Classify", command=on_classify_button_click)
    classify_button.pack(pady=5)

    result_display_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    result_display_area.pack(pady=10)
    result_display_area.config(state=tk.DISABLED)

    window.mainloop()
