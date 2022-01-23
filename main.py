import tkinter
import turtle
import xml.etree.ElementTree as ET
import tkinter as tk
from classes import vessel
from turtle import *
from tkinter import ttk
from tkinter import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk

background_colour = "#182039"
title_text_colour = "#F6D365"

tree = ET.parse("vesselData.xml")
root = tree.getroot()

#create variables
vessel_uniqueID = ""
vessel_side = ""
vessel_classname = ""
vessel_broadType = ""
vessel_front_shield = 0
vessel_back_shield = 0
vessel_description = ""
vessel_arcwidth = 0.0
vessel_arc_width_extent = 0.0
vessel_arc_x = 0.0
vessel_arc_x_start = 0.0
label_uniqueID = ""
label_classname = ""
label_broadType = ""
label_side = ""
label_front_shield_value_text = ""
label_rear_shield_value_text = ""
label_vessel_homing_count = ""
label_vessel_nuke_count = ""
label_vessel_mine_count = ""
label_vessel_emp_count = ""
label_vessel_shock_count = ""
label_vessel_beacon_count = ""
label_vessel_probe_count = ""
label_vessel_tag_count = ""

ordnance_database = {
    "trp": "Homing",
    "nuk": "Nuke",
    "min": "Mine",
    "emp": "Emp",
    "shk": "P Shock",
    "bea": "Beacon",
    "pro": "Probe",
    "tag": "Tag"
}

ship_ordnance = []
all_labels = []

#key down function
def submit_uniqueID():
    ship_ordnance.clear()
    all_labels.clear()
    entered_text=textentry.get()
    for vessels in root.findall(".//vessel[@uniqueID='" + entered_text + "']"):

        #global allows classes outside of function to be used within
        global label_uniqueID
        global label_side
        global label_classname
        global label_broadType
        global label_front_shield_value_text
        global label_rear_shield_value_text
        global label_vessel_homing_count
        global label_vessel_nuke_count
        global label_vessel_mine_count
        global label_vessel_emp_count
        global label_vessel_shock_count
        global label_vessel_beacon_count
        global label_vessel_probe_count
        global label_vessel_tag_count
        global vessel_description
        global vessel_arcwidth
        global vessel_arc_width_extent
        global vessel_arc_x
        global vessel_arc_x_start
        global vessel_back_shield
        global vessel_front_shield

        def ordnance_data(type, entered_text):
            count = \
                root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='" + type + "']").attrib[
                    'amount']
            return count

        for k,v in ordnance_database.items():
            a = ordnance_data(k, entered_text)
            ship_ordnance.append(a)


        row = 7
        step = 0
        for k,v in ordnance_database.items():
                print(k)
                print(v)
                name = v
                label = ttk.Label(window, text=(name + ": " + str(ship_ordnance[step])), background=background_colour, foreground="white", font="none 10")
                label.grid(row=row, column=0, sticky=W, columnspan=2)
                all_labels.append(label)
                row += 1
                step += 1

        vessel_arcwidth = \
        root.find(".//vessel[@uniqueID='" + entered_text + "']/beam_port").attrib['arcwidth']
        vessel_arc_x = \
        root.find(".//vessel[@uniqueID='" + entered_text + "']/beam_port").attrib['x']

        vessel_front_shield = root.find(".//vessel[@uniqueID='" + entered_text + "']/shields").attrib['front']
        vessel_back_shield = root.find(".//vessel[@uniqueID='" + entered_text + "']/shields").attrib['back']

        vessel_arc_width_extent = 360 * float(vessel_arcwidth)
        vessel_arc_width_extent_half = round(vessel_arc_width_extent / 2)
        print(vessel_arc_width_extent)

        if vessel_arc_x < "0":
            vessel_arc_x_start = round((360 - float(vessel_arc_x))  + (90 + vessel_arc_width_extent_half))
            print("if:"+vessel_arc_x)
        else:
            vessel_arc_x_start = round((0 + float(vessel_arc_x)) + (90 - vessel_arc_width_extent_half))
            print("else:" + vessel_arc_x)

        print(vessel_arc_x_start)


        #overwrites existing labels
        #label_uniqueID.configure(text="Unique ID: " + vessel_uniqueID)
        #label_side.configure(text="Side: " + vessel_side)
        label_classname.configure(text=vessel_classname)
        label_description.configure(text=vessel_description)
        #label_broadType.configure(text="broadType: " + vessel_broadType)
        label_front_shield_value_text.configure(text=vessel_front_shield)
        label_rear_shield_value_text.configure(text=vessel_back_shield)
        arc_canvas.coords(100, 100, 300, 300)
        arc_canvas.itemconfig(arc, start=vessel_arc_x_start, extent=vessel_arc_width_extent)

#100, 100, 300, 300, start=0, extent=vessel_arc_width_extent
#Window Information
window = Tk()
window.title("Vessel Data Viewer")
window.configure(background=background_colour)

#Testing the SVg reader
drawing = svg2rlg("nemesis.svg")
renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
img = Image.open('temp.png').resize((100, 50))
img = img.convert("RGBA")
img_data = img.getdata()
newData = []
#print(img_data)

#Converting the png background to transparent
for item in img_data:
    if item[0] == 255 and item [1] == 255 and item[2] ==255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)

img_data_post = img.getdata()
pimg = ImageTk.PhotoImage(img)

#Ship name and desc
label_classname = ttk.Label(window, width="50", anchor="center")
label_classname.grid(row=2, column=0, sticky=W, columnspan=5)
label_classname.configure(text=vessel_classname, background=background_colour, foreground=title_text_colour, font="none 16 bold")
label_description = ttk.Label(window, anchor="center", justify=CENTER)
label_description.grid(row=3, column=0, stick=W, columnspan=5)
label_description.configure(text=vessel_description, background=background_colour, foreground="white", font="none 8 bold", wraplength="500")

#shields
label_shields_title = ttk.Label(window, width="40%", anchor="center")
label_shields_title.grid(row=4, column=0, stick=W, columnspan=2)
label_shields_title.configure(text="SHIELDS", background=background_colour, foreground=title_text_colour, font="none 14 bold")

shield_frame = Frame (window, background=background_colour)
shield_frame.grid(column=0, row=5, columnspan=2)

#shield 0,0
label_rear_shield_value_text_title = ttk.Label(shield_frame)
label_rear_shield_value_text_title.grid(row=0, column=0)
label_rear_shield_value_text_title.configure(text="Rear", background=background_colour, foreground=title_text_colour, font="none 8")

#shield 1,0
label_rear_shield_value_text = ttk.Label(shield_frame)
label_rear_shield_value_text.grid(row=1, column=0)
label_rear_shield_value_text.configure(text=vessel_back_shield, background=background_colour, foreground="white", font="none 8 bold")

photo2 = (Image.open("lightcruiser_yellow_small.png"))
resized_image = photo2.resize((100,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Label (shield_frame, image=new_image, bg=background_colour) .grid(row=0, column=1, sticky=W, rowspan=2)

#shield 0,2
label_front_shield_value_text_title = ttk.Label(shield_frame)
label_front_shield_value_text_title.grid(row=0, column=2)
label_front_shield_value_text_title.configure(text="Front", background=background_colour, foreground=title_text_colour, font="none 8")

#shield 1,2
label_front_shield_value_text = ttk.Label(shield_frame)
label_front_shield_value_text.grid(row=1, column=2)
label_front_shield_value_text.configure(text=vessel_front_shield, background=background_colour, foreground="white", font="none 8 bold")

#weapons
label_weapons_title = ttk.Label(window, width="40%", anchor="center")
label_weapons_title.grid(row=6, column=0, sticky=W, columnspan=5)
label_weapons_title.configure(text="WEAPONS", background=background_colour, foreground=title_text_colour, font="none 14 bold")

#arc frame

arc_frame = Frame (window, background=background_colour)
arc_frame.grid(column=3, row=7, columnspan=3, rowspan=8)

arc_canvas = tkinter.Canvas(master=arc_frame, width=400, height=400)
arc_canvas.grid(padx=2, pady=2, row=0, column=0, columnspan=10)
arc = arc_canvas.create_arc(100, 100, 300, 300, start=vessel_arc_x_start, extent=vessel_arc_width_extent)

#Adding elements to the window
photo1 = PhotoImage(file="TSN_Emblem.png")
Label (window, image=photo1, bg=background_colour) .grid(row=0, column=0, sticky=W, columnspan=2)
Label (window, text="Vessel Data Viewer for Artemis 2.7+", bg=background_colour, fg="white", font="none 12 bold") .grid(row=0, column=2, sticky=W, columnspan=3)
Label (window, text="by Lt. Garion", bg=background_colour, fg="white", font="none 8") .grid(row=0, column=2, sticky=S, columnspan=3)

#User Input
Label (window, text="Enter a uniqueID:", bg=background_colour, fg="white", font="none 10") .grid(row=1, column=0, stick=E)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=1, column=1, sticky=W)

#Submit button
Button(window, text="SUBMIT", width = 6, command=submit_uniqueID) .grid(row=1, column=2, sticky=E)

window.mainloop()