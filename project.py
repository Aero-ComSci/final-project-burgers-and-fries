import tkinter as tk
from PIL import Image, ImageTk
order = []
total= 0



things_list = ["strawberry.png","vanilla.png", "chocolate.png", "hearts.png", "stars.png","rainbow.png","cone.png"]
image_refs = []


cone_price = 1.50
strawberry_price = 2.00
vanilla_price = 2.00
chocolate_price = 2.00
heart_sprinkles_price = 0.75
star_sprinkles_price = 0.75
rainbow_sprinkles_price = 0.75



font=("Comic Sans MS", 15 )

def button_disb():
    buttons[0][0].config(state = "disabled")
    buttons[0][1].config(state = "disabled")
    buttons[0][2].config(state = "disabled")


def on_button_click(row, col):
    global total
    item = buttons[row][col]['text']
    if not item == " ":
        print(f"{item} added to your order!")
        order.append(f"{item} added to your order!")
        tmp = "\n".join(order)
        label1.configure(text=tmp)

    if item == "Strawberry":
        total += strawberry_price
        button_disb()
        ic_flav(0)
    elif item == "Vanilla":
        total += vanilla_price
        button_disb()
        ic_flav(1)
    elif item== "Chocolate":
        total += chocolate_price
        button_disb()
        ic_flav(2)
    elif item == "Heart Sprinkles":
        total += heart_sprinkles_price
        buttons[1][0].config(state = "disabled")
        ic_flav(3)
    elif item == "Star Sprinkles":
        total += star_sprinkles_price
        buttons[1][1].config(state = "disabled")
        ic_flav(4)
    elif item == "Rainbow Sprinkles":
        total += rainbow_sprinkles_price
        buttons[1][2].config(state = "disabled")
        ic_flav(5)
    elif item == "Cone":
        total += cone_price
        buttons[2][1].config(state = "disabled")
        ic_flav(6)

    else:
        total +=0
    tmp = "\n".join(order) + f"\n\nTotal: ${total:.2f}"
    label1.configure(text=tmp)
        
# Create the main window
root = tk.Tk()
root.title("3x3 Grid Interface")
root.configure(bg="#FBC3B8")

canvas = tk.Canvas(root, width=250, height=250, bg="#FBC3B8")
canvas.pack()

def ic_flav(x):
    img_opened = Image.open(things_list[x]).resize((300,250))
    img_disp = ImageTk.PhotoImage(img_opened)
    image_refs.append(img_disp)
    canvas.create_image(125, 125, anchor=tk.CENTER, image=img_disp)




menu_label = tk.Label(root, text="「 MENU 」", font=("Comic Sans MS", 20, "bold"), bg="#FBC3B8", fg="#FCF3C4")
menu_label.pack(pady=(10, 0))

# Create a frame for the grid
grid_frame = tk.Frame(root, bg="#FBC3B8")
grid_frame.pack(pady=10)


# Create a 3x3 grid of buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(grid_frame, text=f"{row},{col}", width=15, height=3,
                           font=font, bg="#FCF3C4", fg="#FBC3B8",
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)
buttons[0][0].config(text="Strawberry")
buttons[0][1].config(text="Vanilla")
buttons[0][2].config(text="Chocolate")

buttons[1][0].config(text="Heart Sprinkles")
buttons[1][1].config(text="Star Sprinkles")
buttons[1][2].config(text="Rainbow Sprinkles")

buttons[2][0].config(text=" ")
buttons[2][1].config(text="Cone")
buttons[2][2].config(text=" ")
# Create two non-writable fields
info_frame = tk.Frame(root, bg="#FBC3B8")
info_frame.pack(pady=10)

label1 = tk.Label(info_frame, text="Start by selecting an item from the menu!", relief="sunken", width=40, anchor="center", font=font, bg="#FCF3C4", fg="#FBC3B8")
label1.pack(pady=5)

label2 = tk.Label(info_frame, text= "hi", relief="sunken", width=30, anchor="center", font=font,bg="#FCF3C4", fg="#FBC3B8")
label2.pack(pady=5)

# Run the application
root.mainloop()