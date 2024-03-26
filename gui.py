import tkinter as tk
from tkinter import scrolledtext
from predict import make_prediction_with_confidence  # Adjusted import

def start_gui(model, vectorizer):
    window = tk.Tk()
    window.title("Toxic Comment Classifier")

    def on_classify_button_click():
        comment = input_text_area.get("1.0", tk.END).strip()
        prediction, confidence = make_prediction_with_confidence(model, vectorizer, comment)
        categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
        
        if any(prediction[0]):
                prediction_text = "Categories: " + ", ".join([categories[i] for i, pred in enumerate(prediction[0]) if pred == 1])
        else:
                prediction_text = "Your comment is perfectly fine."

            # Now, always append the confidence score to the prediction text
        confidence_text = f"\nConfidence: {confidence*100:.2f}% confident in this assessment."
        prediction_text += confidence_text

        result_display_area.config(state=tk.NORMAL)
        result_display_area.delete('1.0', tk.END)
        result_display_area.insert(tk.END, prediction_text + '\n')
        result_display_area.config(state=tk.DISABLED)

    input_text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    input_text_area.pack(pady=10)

    classify_button = tk.Button(window, text="Classify", command=on_classify_button_click)
    classify_button.pack(pady=5)

    result_display_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    result_display_area.pack(pady=10)
    result_display_area.config(state=tk.DISABLED)

    window.mainloop()
