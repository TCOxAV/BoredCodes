import tkinter as tk
import time

root = tk.Tk()
root.title("Slot Machine")
root.geometry("600x500")

root.update_idletasks()
w = 600
h = 500
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry(f'{w}x{h}+{x}+{y}')

top = tk.Frame(root)
top.pack(pady=10, fill=tk.X, padx=20)

tk.Label(top, text="Type your message:", font=("Courier", 10)).pack(anchor=tk.W)

text_area = tk.Text(top, font=("Courier", 12), height=5, width=50, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True, pady=5)

btn = tk.Button(top, text="SPIN!", font=("Courier", 12), command=lambda: animate())
btn.pack(pady=5)

out_frame = tk.Frame(root)
out_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

out_label = tk.Label(out_frame, text="", font=("Courier", 14), justify=tk.LEFT)
out_label.pack(expand=True)

def animate_line(line, done):
    cur = ""
    for c in line:
        for l in range(ord('a'), ord(c) + 1):
            out_label.config(text="\n".join(done + [cur + chr(l)]))
            root.update()
            time.sleep(0.05)
        cur += c
    return cur

def animate():
    txt = text_area.get("1.0", tk.END).rstrip("\n")
    if not txt.strip():
        return
    
    text_area.config(state="disabled")
    btn.config(state="disabled")
    text_area.config(height=2)
    
    lines = txt.split('\n')
    done = []
    for line in lines:
        if line.strip():
            done.append(animate_line(line, done))
        else:
            done.append("")
    
    out_label.config(text="\n".join(done))
    
    text_area.config(state="normal", height=5)
    text_area.delete("1.0", tk.END)
    btn.config(state="normal")
    text_area.focus()

text_area.focus()
root.mainloop()
