import tkinter as tk
from tkinter import Canvas, Label, Button
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageDraw, ImageTk
import io
import matplotlib.pyplot as plt

# 載入預訓練的模型
model = load_model('mnist_model.h5')

# 創建Tkinter應用程序窗口
app = tk.Tk()
app.title("手寫數字辨識")
app.geometry("400x400")  # 設定視窗大小

# 創建一個畫布，用於繪製手寫數字
canvas = Canvas(app, width=300, height=300, bg='black')
canvas.pack()

# 創建一個標籤，用於顯示預測的數字
label = Label(app, text="預測數字: ", font=("TkDefaultFont", 16, "bold"))
label.pack()

# 開始繪製手寫數字
drawing = False

def start_drawing(event):
    global drawing
    drawing = True

def end_drawing(event):
    global drawing
    drawing = False
    predict_digit()

def draw(event):
    if drawing:
        x, y = event.x, event.y
        canvas.create_oval(x, y, x+12, y+12, fill='white', width=0)
        canvas.update()

canvas.bind("<ButtonPress-1>", start_drawing)
canvas.bind("<ButtonRelease-1>", end_drawing)
canvas.bind("<B1-Motion>", draw)

# 清除畫布
def clear_canvas():
    canvas.delete("all")
    label.config(text="預測數字: ")

# 清除按鈕
clear_button = Button(app, text="清除", command=clear_canvas)
clear_button.pack()

def predict_digit():
    image = canvas_to_image(canvas)
    predictions = model.predict(image)
    print(predictions)
    predicted_digit = np.argmax(predictions[0])
    label.config(text=f"預測數字: {predicted_digit}")
    # plt.imshow(image[0, :, :, 0], cmap='gray')
    # plt.show()

def canvas_to_image(canvas):
    # 創建一個空白圖像
    image = Image.new('L', (300, 300), 'black')
    draw = ImageDraw.Draw(image)

    # 獲取畫布上的所有項目
    items = canvas.find_all()

    for item in items:
        item_coords = canvas.coords(item)
        # 提取x和y坐標
        x1, y1, x2, y2 = item_coords
        # 計算橢圓的大小
        size = (x2 - x1, y2 - y1)
        # 在圖像上創建一個白色橢圓
        draw.ellipse([x1, y1, x1 + size[0], y1 + size[1]], fill='white')

    # 調整圖像大小為28x28像素
    image = image.resize((28, 28), Image.ANTIALIAS)

    # 將圖像轉換為NumPy數組
    image_array = np.array(image)

    # 正規化圖像並返回
    image_array = image_array.reshape(1, 28, 28, 1).astype('float32') / 255
    return image_array

app.mainloop()
