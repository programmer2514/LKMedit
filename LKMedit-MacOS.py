import tkinter as tk
import mido
import ast
import sys
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.wm_title("Launchkey Mini Pad Coloring Tool")
#root.iconbitmap("icon.ico")
root.configure(background="ghost white")
logo = tk.PhotoImage(file="LKMini.gif")
leds = (96, 97, 98, 99, 100, 101, 102, 103, 104, 112, 113, 114, 115, 116, 117, 118, 119, 120)
colors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def update_vpad_color():
    for i in range(18):
        if colors[i] == 0:
            vpad_color = ["snow","snow"]
        if colors[i] == 1:
            vpad_color = ["red3","red3"]
        if colors[i] == 15:
            vpad_color = ["red","red"]
        if colors[i] == 19:
            vpad_color = ["orange3","orange3"]
        if colors[i] == 35:
            vpad_color = ["orange","orange"]
        if colors[i] == 62:
            vpad_color = ["yellow","yellow"]
        if colors[i] == 60:
            vpad_color = ["spring green","spring green"]
        if colors[i] == 16:
            vpad_color = ["SpringGreen3","SpringGreen3"]
        if i == 0:
            p0.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 1:
            p1.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 2:
            p2.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 3:
            p3.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 4:
            p4.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 5:
            p5.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 6:
            p6.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 7:
            p7.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 8:
            p8.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 9:
            p9.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 10:
            p10.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 11:
            p11.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 12:
            p12.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 13:
            p13.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 14:
            p14.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 15:
            p15.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 16:
            p16.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])
        if i == 17:
            p17.configure(bg = vpad_color[0], highlightbackground = vpad_color[1])

def reset_settings(bp=1):
    colors[0] = 0
    colors[1] = 0
    colors[2] = 0
    colors[3] = 0
    colors[4] = 0
    colors[5] = 0
    colors[6] = 0
    colors[7] = 0
    colors[8] = 0
    colors[9] = 0
    colors[10] = 0
    colors[11] = 0
    colors[12] = 0
    colors[13] = 0
    colors[14] = 0
    colors[15] = 0
    colors[16] = 0
    colors[17] = 0
    update_vpad_color()

def write_led(led_id, color_vel):
    midi_out.send(mido.Message('note_on', channel=0, note=led_id, velocity=color_vel))

def apply_settings(bp=1):
    counter = 0
    for led in leds:
        color = colors[counter]
        write_led(led, color)
        counter+=1

def fill_color(color):
    colors[0] = color
    colors[1] = color
    colors[2] = color
    colors[3] = color
    colors[4] = color
    colors[5] = color
    colors[6] = color
    colors[7] = color
    colors[8] = color
    colors[9] = color
    colors[10] = color
    colors[11] = color
    colors[12] = color
    colors[13] = color
    colors[14] = color
    colors[15] = color
    colors[16] = color
    colors[17] = color
    update_vpad_color()

def exit_prog(bp=1):
    try:
        for led in leds:
            write_led(led, 0)
        midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x00]))
        midi_out.close()
    except:
        messagebox.showerror("MIDI Output Not Set!", "MIDI Output Not Set!\nPress OK to exit...")
    file = open("autosave.lkm", "w")
    data = str([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    file.write(data)
    file.close()
    messagebox.showinfo("Launchkey Mini Pad Coloring Tool", "Press OK and close Window...")
    #root.quit()
    #root.destroy()
    #sys.exit()

def exit_prog_save(bp=1):
    file = open("autosave.lkm", "w")
    data = str(colors)
    file.write(data)
    file.close()
    try:
        midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x00]))
        midi_out.close()
    except:
        messagebox.showerror("MIDI Output Not Set!", "MIDI Output Not Set!\nPress OK to exit...")
    messagebox.showinfo("Launchkey Mini Pad Coloring Tool", "Press OK and close Window...")
    #root.quit()
    #root.destroy()
    #sys.exit()

def exit_prog_save_p(bp=1):
    file = open("autosave.lkm", "w")
    data = str(colors)
    file.write(data)
    file.close()
    messagebox.showinfo("Launchkey Mini Pad Coloring Tool", "Press OK and close Window...")
    #root.quit()
    #root.destroy()
    #sys.exit()

def set_button(btn):
    button = btn
    if colors[button] == 0:
        colors[button] = 1
        update_vpad_color()
        return button
    if colors[button] == 1:
        colors[button] = 15
        update_vpad_color()
        return button
    if colors[button] == 15:
        colors[button] = 19
        update_vpad_color()
        return button
    if colors[button] == 19:
        colors[button] = 35
        update_vpad_color()
        return button
    if colors[button] == 35:
        colors[button] = 62
        update_vpad_color()
        return button
    if colors[button] == 62:
        colors[button] = 60
        update_vpad_color()
        return button
    if colors[button] == 60:
        colors[button] = 16
        update_vpad_color()
        return button
    if colors[button] == 16:
        colors[button] = 0
        update_vpad_color()
        return button

def save_file(bp=1):
    file = filedialog.asksaveasfile(mode='w', initialdir="../../configs", defaultextension=".lkm", initialfile='config', filetypes=(("Launchkey Mini Config Files", "*.lkm"),("Configuration Settings","*.ini"),("All Files", "*.*")))
    if file is None:
        return
    data = str(colors)
    file.write(data)
    file.close()

def open_file(bp=1):
    filename = filedialog.askopenfilename(initialdir="../../configs", filetypes = (("Launchkey Mini Config Files", ("*.lkm","*.ini")),("All Files","*.*")))
    if filename: 
        try: 
            file = open(filename, "r")
            data = file.read()
            data = ast.literal_eval(data)
            colors[0] = data[0]
            colors[1] = data[1]
            colors[2] = data[2]
            colors[3] = data[3]
            colors[4] = data[4]
            colors[5] = data[5]
            colors[6] = data[6]
            colors[7] = data[7]
            colors[8] = data[8]
            colors[9] = data[9]
            colors[10] = data[10]
            colors[11] = data[11]
            colors[12] = data[12]
            colors[13] = data[13]
            colors[14] = data[14]
            colors[15] = data[15]
            colors[16] = data[16]
            colors[17] = data[17]
            update_vpad_color()
        except: 
            messagebox.showerror("Open Config File", "Failed to read file \n'%s'"%filename)
            return

def info():
    messagebox.showinfo("Launchkey Mini Pad Coloring Tool", "Launchkey Mini Pad Coloring Tool\nCopyright © 2018 Benjamin Pryor")
    return

def shortcuts():
    messagebox.showinfo("Keyboard Shortcuts:", "Keyboard Shortcuts:\n    File:\n        Ctrl+S = Save As...\n        Ctrl+O = Open...\n        Ctrl+N = New Config\n        Ctrl+Q = Save Changes & Exit\n        Esc = Exit\n    Options:\n        Ctrl+M = Set Output Device\n    Edit:\n        Backspace = Reset\n        Enter = Apply Settings\n    Pads:\n        F1 = Toggle Pad 1\n        F2 = Toggle Pad 2\n        F3 = Toggle Pad 3\n        F4 = Toggle Pad 4\n        F5 = Toggle Pad 5\n        F6 = Toggle Pad 6\n        F7 = Toggle Pad 7\n        F8 = Toggle Pad 8\n        F9 = Toggle Round Button 1\n        1 = Toggle Pad 9\n        2 = Toggle Pad 10\n        3 = Toggle Pad 11\n        4 = Toggle Pad 12\n        5 = Toggle Pad 13\n        6 = Toggle Pad 14\n        7 = Toggle Pad 15\n        8 = Toggle Pad 16\n        9 = Toggle Round Button 2\n")
    return

def set_vbutton(bp):
    if bp.keysym == "F1":
        set_button(0)
    if bp.keysym == "F2":
        set_button(1)
    if bp.keysym == "F3":
        set_button(2)
    if bp.keysym == "F4":
        set_button(3)
    if bp.keysym == "F5":
        set_button(4)
    if bp.keysym == "F6":
        set_button(5)
    if bp.keysym == "F7":
        set_button(6)
    if bp.keysym == "F8":
        set_button(7)
    if bp.keysym == "F9":
        set_button(8)
    if bp.keysym == "1":
        set_button(9)
    if bp.keysym == "2":
        set_button(10)
    if bp.keysym == "3":
        set_button(11)
    if bp.keysym == "4":
        set_button(12)
    if bp.keysym == "5":
        set_button(13)
    if bp.keysym == "6":
        set_button(14)
    if bp.keysym == "7":
        set_button(15)
    if bp.keysym == "8":
        set_button(16)
    if bp.keysym == "9":
        set_button(17)

def set_button_radio(button):
    p0.configure(state=tk.DISABLED)
    p1.configure(state=tk.DISABLED)
    p2.configure(state=tk.DISABLED)
    p3.configure(state=tk.DISABLED)
    p4.configure(state=tk.DISABLED)
    p5.configure(state=tk.DISABLED)
    p6.configure(state=tk.DISABLED)
    p7.configure(state=tk.DISABLED)
    p8.configure(state=tk.DISABLED)
    p9.configure(state=tk.DISABLED)
    p10.configure(state=tk.DISABLED)
    p11.configure(state=tk.DISABLED)
    p12.configure(state=tk.DISABLED)
    p13.configure(state=tk.DISABLED)
    p14.configure(state=tk.DISABLED)
    p15.configure(state=tk.DISABLED)
    p16.configure(state=tk.DISABLED)
    p17.configure(state=tk.DISABLED)
    btnnames = ["Pad 1","Pad 2","Pad 3","Pad 4","Pad 5","Pad 6","Pad 7","Pad 8","Round Button 1","Pad 9","Pad 10","Pad 11","Pad 12","Pad 13","Pad 14","Pad 15","Pad 16","Round Button 2"]
    buttonwin = tk.Toplevel()
    buttonwin.resizable(0,0)
    buttonwin.focus()
    buttonwin.wm_title("Set Color - "+btnnames[button])
    #buttonwin.iconbitmap("icon.ico")
    var = tk.IntVar(buttonwin)
    if colors[button] == 0:
        var.set(0)
    if colors[button] == 1:
        var.set(1)
    if colors[button] == 15:
        var.set(2)
    if colors[button] == 19:
        var.set(3)
    if colors[button] == 35:
        var.set(4)
    if colors[button] == 62:
        var.set(5)
    if colors[button] == 60:
        var.set(6)
    if colors[button] == 16:
        var.set(7)
    var2 = tk.IntVar()
    l1 = tk.Label(buttonwin, text="Please Choose a Color:", justify = tk.CENTER, padx = 20).grid(row=0)
    tk.Radiobutton(buttonwin, text="Off", padx = 20, variable=var, value=0).grid(row=1, sticky="W")
    tk.Radiobutton(buttonwin, text="Dark Red", padx = 20, variable=var, value=1).grid(row=2, sticky="W")
    tk.Radiobutton(buttonwin, text="Red", padx = 20, variable=var, value=2).grid(row=3, sticky="W")
    tk.Radiobutton(buttonwin, text="Dark Orange", padx = 20, variable=var, value=3).grid(row=4, sticky="W")
    tk.Radiobutton(buttonwin, text="Orange", padx = 20, variable=var, value=4).grid(row=5, sticky="W")
    tk.Radiobutton(buttonwin, text="Yellow", padx = 20, variable=var, value=5).grid(row=6, sticky="W")
    tk.Radiobutton(buttonwin, text="Light Green", padx = 20, variable=var, value=6).grid(row=7, sticky="W")
    tk.Radiobutton(buttonwin, text="Green", padx = 20, variable=var, value=7).grid(row=8, sticky="W")
    owb = tk.Button(buttonwin, text="OK", width=20, command=lambda: var2.set(1))
    owb.grid(sticky="S")
    owb.wait_variable(var2)
    if var.get() == 0:
        colors[button] = 0
    if var.get() == 1:
        colors[button] = 1
    if var.get() == 2:
        colors[button] = 15
    if var.get() == 3:
        colors[button] = 19
    if var.get() == 4:
        colors[button] = 35
    if var.get() == 5:
        colors[button] = 62
    if var.get() == 6:
        colors[button] = 60
    if var.get() == 7:
        colors[button] = 16
    update_vpad_color()
    p0.configure(state=tk.ACTIVE)
    p1.configure(state=tk.ACTIVE)
    p2.configure(state=tk.ACTIVE)
    p3.configure(state=tk.ACTIVE)
    p4.configure(state=tk.ACTIVE)
    p5.configure(state=tk.ACTIVE)
    p6.configure(state=tk.ACTIVE)
    p7.configure(state=tk.ACTIVE)
    p8.configure(state=tk.ACTIVE)
    p9.configure(state=tk.ACTIVE)
    p10.configure(state=tk.ACTIVE)
    p11.configure(state=tk.ACTIVE)
    p12.configure(state=tk.ACTIVE)
    p13.configure(state=tk.ACTIVE)
    p14.configure(state=tk.ACTIVE)
    p15.configure(state=tk.ACTIVE)
    p16.configure(state=tk.ACTIVE)
    p17.configure(state=tk.ACTIVE)
    buttonwin.destroy()

def set_button_0(bp):
    p0.configure(relief=tk.SUNKEN)
    set_button_radio(0)
    p0.configure(relief=tk.RAISED)

def set_button_1(bp):
    p1.configure(relief=tk.SUNKEN)
    set_button_radio(1)
    p1.configure(relief=tk.RAISED)

def set_button_2(bp):
    p2.configure(relief=tk.SUNKEN)
    set_button_radio(2)
    p2.configure(relief=tk.RAISED)

def set_button_3(bp):
    p3.configure(relief=tk.SUNKEN)
    set_button_radio(3)
    p3.configure(relief=tk.RAISED)

def set_button_4(bp):
    p4.configure(relief=tk.SUNKEN)
    set_button_radio(4)
    p4.configure(relief=tk.RAISED)

def set_button_5(bp):
    p5.configure(relief=tk.SUNKEN)
    set_button_radio(5)
    p5.configure(relief=tk.RAISED)

def set_button_6(bp):
    p6.configure(relief=tk.SUNKEN)
    set_button_radio(6)
    p6.configure(relief=tk.RAISED)

def set_button_7(bp):
    p7.configure(relief=tk.SUNKEN)
    set_button_radio(7)
    p7.configure(relief=tk.RAISED)

def set_button_8(bp):
    p8.configure(relief=tk.SUNKEN)
    set_button_radio(8)
    p8.configure(relief=tk.RAISED)

def set_button_9(bp):
    p9.configure(relief=tk.SUNKEN)
    set_button_radio(9)
    p9.configure(relief=tk.RAISED)

def set_button_10(bp):
    p10.configure(relief=tk.SUNKEN)
    set_button_radio(10)
    p10.configure(relief=tk.RAISED)

def set_button_11(bp):
    p11.configure(relief=tk.SUNKEN)
    set_button_radio(11)
    p11.configure(relief=tk.RAISED)

def set_button_12(bp):
    p12.configure(relief=tk.SUNKEN)
    set_button_radio(12)
    p12.configure(relief=tk.RAISED)

def set_button_13(bp):
    p13.configure(relief=tk.SUNKEN)
    set_button_radio(13)
    p13.configure(relief=tk.RAISED)

def set_button_14(bp):
    p14.configure(relief=tk.SUNKEN)
    set_button_radio(14)
    p14.configure(relief=tk.RAISED)

def set_button_15(bp):
    p15.configure(relief=tk.SUNKEN)
    set_button_radio(15)
    p15.configure(relief=tk.RAISED)

def set_button_16(bp):
    p16.configure(relief=tk.SUNKEN)
    set_button_radio(16)
    p16.configure(relief=tk.RAISED)

def set_button_17(bp):
    p17.configure(relief=tk.SUNKEN)
    set_button_radio(17)
    p17.configure(relief=tk.RAISED)

def choose_midi_out(bp=1):
    try:
        onames = mido.get_output_names()
    except:
        onames = []
    if len(onames) == 0:
        messagebox.showerror("No Output Devices Found!", "No Output Devices Found!\nMake sure your device is plugged in and try again.")
        return
        #root.quit()
        #root.destroy()
        #sys.exit()
    global midi_out
    outputwin = tk.Toplevel()
    outputwin.resizable(0,0)
    outputwin.wm_title("Choose an Output Device")
    #outputwin.iconbitmap("icon.ico")
    var = tk.IntVar(outputwin)
    var2 = tk.IntVar()
    l1 = tk.Label(outputwin, text="Please Choose an Output Device:", justify = tk.CENTER, padx = 20).grid(row=0)
    for i in range(len(onames)):
        tk.Radiobutton(outputwin, text=onames[i], padx = 20, variable=var, value=i).grid(row=i+1, sticky="W")
    owb = tk.Button(outputwin, text="OK", width=20, command=lambda: var2.set(1))
    owb.grid(sticky="S")
    owb.wait_variable(var2)
    try:
        midiname = onames[var.get()]
        midi_out = mido.open_output(midiname)
        midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))
        outputwin.destroy()
    except:
        messagebox.showerror("Output Device Already Selected!", "Output Device Already Selected!\nSelect a different device and try again.")
        outputwin.destroy()

tk.Label(root, image=logo).grid(sticky="NW")

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New                                     Ctrl+N", command=reset_settings)
filemenu.add_command(label="Save As...                             Ctrl+S", command=save_file)
filemenu.add_command(label="Open...                                Ctrl+O", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Keep Pads On & Exit", command=exit_prog_save_p)
filemenu.add_command(label="Keep Changes & Exit        Ctrl+Q", command=exit_prog_save)
filemenu.add_command(label="Exit                                            Esc", command=exit_prog)

editmenu = tk.Menu(menu)
presetmenu = tk.Menu(editmenu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_cascade(label="Presets", menu=presetmenu)
editmenu.add_separator()
editmenu.add_command(label="Reset                          Backspace", command=reset_settings)
editmenu.add_command(label="Apply Changes                  Enter", command=apply_settings)
presetmenu.add_command(label="Off", command=lambda: fill_color(0))
presetmenu.add_command(label="Dark Red", command=lambda: fill_color(1))
presetmenu.add_command(label="Red", command=lambda: fill_color(15))
presetmenu.add_command(label="Dark Orange", command=lambda: fill_color(19))
presetmenu.add_command(label="Orange", command=lambda: fill_color(35))
presetmenu.add_command(label="Yellow", command=lambda: fill_color(62))
presetmenu.add_command(label="Light Green", command=lambda: fill_color(60))
presetmenu.add_command(label="Green", command=lambda: fill_color(16))

optionsmenu = tk.Menu(menu)
menu.add_cascade(label="Options", menu=optionsmenu)
padsmenu = tk.Menu(optionsmenu)
btnsmenu = tk.Menu(optionsmenu)
optionsmenu.add_cascade(label="Pads        ", menu=padsmenu)
optionsmenu.add_cascade(label="Buttons        ", menu=btnsmenu)
optionsmenu.add_separator()
optionsmenu.add_command(label="Set Output Device            Ctrl+M", command=choose_midi_out)
padsmenu.add_command(label="Configure Pad 1", command=lambda: set_button_radio(0))
padsmenu.add_command(label="Configure Pad 2", command=lambda: set_button_radio(1))
padsmenu.add_command(label="Configure Pad 3", command=lambda: set_button_radio(2))
padsmenu.add_command(label="Configure Pad 4", command=lambda: set_button_radio(3))
padsmenu.add_command(label="Configure Pad 5", command=lambda: set_button_radio(4))
padsmenu.add_command(label="Configure Pad 6", command=lambda: set_button_radio(5))
padsmenu.add_command(label="Configure Pad 7", command=lambda: set_button_radio(6))
padsmenu.add_command(label="Configure Pad 8", command=lambda: set_button_radio(7))
btnsmenu.add_command(label="Configure Round Button 1", command=lambda: set_button_radio(8))
padsmenu.add_command(label="Configure Pad 9", command=lambda: set_button_radio(9))
padsmenu.add_command(label="Configure Pad 10", command=lambda: set_button_radio(10))
padsmenu.add_command(label="Configure Pad 11", command=lambda: set_button_radio(11))
padsmenu.add_command(label="Configure Pad 12", command=lambda: set_button_radio(12))
padsmenu.add_command(label="Configure Pad 13", command=lambda: set_button_radio(13))
padsmenu.add_command(label="Configure Pad 14", command=lambda: set_button_radio(14))
padsmenu.add_command(label="Configure Pad 15", command=lambda: set_button_radio(15))
padsmenu.add_command(label="Configure Pad 16", command=lambda: set_button_radio(16))
btnsmenu.add_command(label="Configure Round Button 2", command=lambda: set_button_radio(17))

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Keyboard Shortcuts", command=shortcuts)
helpmenu.add_separator()
helpmenu.add_command(label="About...", command=info)

tk.Button(root, text="Exit", width=37, command=exit_prog).grid(row=5, sticky="E")
tk.Button(root, text="Apply", width=37, command=apply_settings).grid(row=5, sticky="W")
tk.Button(root, text="Reset", width=37, command=reset_settings).grid(column=0, row=5)
p0 = tk.Button(root, command=lambda: set_button(0))
p0.place(x=129, y=116, height=79, width=80)
p1 = tk.Button(root, command=lambda: set_button(1))
p1.place(x=221, y=116, height=79, width=80)
p2 = tk.Button(root, command=lambda: set_button(2))
p2.place(x=313, y=116, height=79, width=80)
p3 = tk.Button(root, command=lambda: set_button(3))
p3.place(x=405, y=116, height=79, width=80)
p4 = tk.Button(root, command=lambda: set_button(4))
p4.place(x=497, y=116, height=79, width=80)
p5 = tk.Button(root, command=lambda: set_button(5))
p5.place(x=588, y=116, height=79, width=80)
p6 = tk.Button(root, command=lambda: set_button(6))
p6.place(x=679, y=116, height=79, width=80)
p7 = tk.Button(root, command=lambda: set_button(7))
p7.place(x=770, y=116, height=79, width=80)
p9 = tk.Button(root, command=lambda: set_button(9))
p9.place(x=129, y=208, height=79, width=80)
p10 = tk.Button(root, command=lambda: set_button(10))
p10.place(x=221, y=208, height=79, width=80)
p11 = tk.Button(root, command=lambda: set_button(11))
p11.place(x=313, y=208, height=79, width=80)
p12 = tk.Button(root, command=lambda: set_button(12))
p12.place(x=405, y=208, height=79, width=80)
p13 = tk.Button(root, command=lambda: set_button(13))
p13.place(x=497, y=208, height=79, width=80)
p14 = tk.Button(root, command=lambda: set_button(14))
p14.place(x=588, y=208, height=79, width=80)
p15 = tk.Button(root, command=lambda: set_button(15))
p15.place(x=679, y=208, height=79, width=80)
p16 = tk.Button(root, command=lambda: set_button(16))
p16.place(x=770, y=208, height=79, width=80)
p8 = tk.Button(root, command=lambda: set_button(8))
p8.place(x=869, y=123, height=63, width=63)
p17 = tk.Button(root, command=lambda: set_button(17))
p17.place(x=869, y=215, height=63, width=63)
root.resizable(0,0)
#root.protocol("WM_DELETE_WINDOW", exit_prog)
#p0_id = p0.bind('<Button-2>', set_button_0)
#p1_id = p1.bind('<Button-2>', set_button_1)
#p2_id = p2.bind('<Button-2>', set_button_2)
#p3_id = p3.bind('<Button-2>', set_button_3)
#p4_id = p4.bind('<Button-2>', set_button_4)
#p5_id = p5.bind('<Button-2>', set_button_5)
#p6_id = p6.bind('<Button-2>', set_button_6)
#p7_id = p7.bind('<Button-2>', set_button_7)
#p8_id = p8.bind('<Button-2>', set_button_8)
#p9_id = p9.bind('<Button-2>', set_button_9)
#p10_id = p10.bind('<Button-2>', set_button_10)
#p11_id = p11.bind('<Button-2>', set_button_11)
#p12_id = p12.bind('<Button-2>', set_button_12)
#p13_id = p13.bind('<Button-2>', set_button_13)
#p14_id = p14.bind('<Button-2>', set_button_14)
#p15_id = p15.bind('<Button-2>', set_button_15)
#p16_id = p16.bind('<Button-2>', set_button_16)
#p17_id = p17.bind('<Button-2>', set_button_17)
root.bind('<F1>', set_vbutton)
root.bind('<F2>', set_vbutton)
root.bind('<F3>', set_vbutton)
root.bind('<F4>', set_vbutton)
root.bind('<F5>', set_vbutton)
root.bind('<F6>', set_vbutton)
root.bind('<F7>', set_vbutton)
root.bind('<F8>', set_vbutton)
root.bind('<F9>', set_vbutton)
root.bind('1', set_vbutton)
root.bind('2', set_vbutton)
root.bind('3', set_vbutton)
root.bind('4', set_vbutton)
root.bind('5', set_vbutton)
root.bind('6', set_vbutton)
root.bind('7', set_vbutton)
root.bind('8', set_vbutton)
root.bind('9', set_vbutton)
root.bind('<BackSpace>', reset_settings)
root.bind('<Return>', apply_settings)
root.bind('<Escape>', exit_prog)
root.bind('<Control-s>', save_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-q>', exit_prog_save)
root.bind('<Control-n>', reset_settings)
root.bind('<Control-m>', choose_midi_out)

try: 
    file = open("autosave.lkm", "r")
    data = file.read()
    data = ast.literal_eval(data)
    colors[0] = data[0]
    colors[1] = data[1]
    colors[2] = data[2]
    colors[3] = data[3]
    colors[4] = data[4]
    colors[5] = data[5]
    colors[6] = data[6]
    colors[7] = data[7]
    colors[8] = data[8]
    colors[9] = data[9]
    colors[10] = data[10]
    colors[11] = data[11]
    colors[12] = data[12]
    colors[13] = data[13]
    colors[14] = data[14]
    colors[15] = data[15]
    colors[16] = data[16]
    colors[17] = data[17]
    update_vpad_color()
except:
    update_vpad_color()

try:
    midi_out = mido.open_output("MIDIOUT2 (Launchkey Mini) 2")
    midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))
except:
    try:
        midi_out = mido.open_output("Launchkey Mini MIDI 2")
        midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))
    except:
        messagebox.showerror("Launchkey Mini Not Found for Output!", "Launchkey Mini Not Found for Output!\nPlease select a different device or plug it in.")
        choose_midi_out()

update_vpad_color()

root.mainloop()
