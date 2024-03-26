import tkinter as tk
from tkinter import scrolledtext, Toplevel, Label
from PIL import Image, ImageTk
from predict import make_prediction_with_confidence

def start_gui(model, vectorizer):
    window = tk.Tk()
    window.title("Toxic Comment Classifier")

    
    pie_image = Image.open('PieChart1.png')
    bar_image = Image.open('Barchart1.png')
    line_image = Image.open('LineGraph.png')

   
    pie_photo = ImageTk.PhotoImage(pie_image)
    bar_photo = ImageTk.PhotoImage(bar_image)
    line_photo = ImageTk.PhotoImage(line_image)

    
    def show_image(image):
        top = Toplevel(window)
        top.title("Chart")
        img_label = Label(top, image=image)
        img_label.pack()

    def on_classify_button_click():
        comment = input_text_area.get("1.0", tk.END).strip()
        prediction, confidence = make_prediction_with_confidence(model, vectorizer, comment)
        categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
        
        if any(prediction[0]):
            prediction_text = "Categories: " + ", ".join([categories[i] for i, pred in enumerate(prediction[0]) if pred == 1])
        else:
            prediction_text = "Your comment is perfectly fine."
        
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

    
    pie_button = tk.Button(window, text="Pie Chart % /of Types of Comments", command=lambda: show_image(pie_photo))
    pie_button.pack()

    bar_button = tk.Button(window, text="Bar Graph Count of Types of Comments", command=lambda: show_image(bar_photo))
    bar_button.pack()

    line_button = tk.Button(window, text="Line Graph of Toxic vs Acceptable Comments", command=lambda: show_image(line_photo))
    line_button.pack()

    window.mainloop()
