
'''


vesselList = [
]

for vessels in root.findall("./vessel"):

    vessel_uniqueID = root.find('./vessel').attrib['uniqueID']
    vessel_side = root.find('./vessel').attrib['side']
    vessel_classname = root.find('./vessel').attrib['classname']
    vessel_broadType = root.find('./vessel').attrib['broadType']

    vessel_add_list = vessel(vessel_uniqueID, vessel_side, vessel_classname, vessel_broadType)

    vesselList.append(vessel_add_list)
'''


#vessel class
#uniqueID, side, classname, broadType

#--- Find single vessel ---
#search = input("Enter an ID...")
#for vessels in root.findall(".//vessel[@uniqueID='"+search+"']"):
#    print(vessels.attrib)

#Gets the "vessel"
#print(root[23].tag)

#Gets the unique ID
#print(root[100].attrib['uniqueID'])

#for child in root:
#    print(child.tag, child.attrib)

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

#Outputs a list of the ships!
#for vessels in root.iter('vessel'):
#    print(vessels.attrib)

#for vessels in root.findall("./[uniqueID='7703']"):
#    print(vessels.attrib)

# print(ship_ordnance)

# finds the data
# vessel_uniqueID = root.find("./vessel[@uniqueID='"+entered_text+"']").attrib['uniqueID']
# vessel_side = root.find("./vessel[@uniqueID='" + entered_text + "']").attrib['side']
# vessel_classname = root.find("./vessel[@uniqueID='" + entered_text + "']").attrib['classname']
# vessel_description = root.find("./vessel[@uniqueID='" + entered_text +"']/long_desc").attrib['text']
# vessel_broadType = root.find("./vessel[@uniqueID='" + entered_text + "']").attrib['broadType']


# vessel_homing_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='trp']").attrib['amount']
# vessel_nuke_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='nuk']").attrib['amount']
# vessel_mine_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='min']").attrib['amount']
# vessel_emp_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='emp']").attrib['amount']
# vessel_shock_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='shk']").attrib['amount']
# vessel_beacon_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='bea']").attrib['amount']
# vessel_probe_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='pro']").attrib['amount']
# vessel_tag_count = \
# root.find(".//vessel[@uniqueID='" + entered_text + "']/torpedo_storage[@type='tag']").attrib['amount']

'''
label_vessel_homing_count = \
ttk.Label(window, text="Homings: " + vessel_homing_count, background=background_colour, foreground="white", font="none 10")
label_vessel_homing_count.grid(row=7, column=0, sticky=W, columnspan=2)
label_vessel_nuke_count = \
ttk.Label(window, text="Nukes: " + vessel_nuke_count, background=background_colour, foreground="white", font="none 10")
label_vessel_nuke_count.grid(row=8, column=0, sticky=W, columnspan=2)
label_vessel_mine_count = \
ttk.Label(window, text="Mines: " + vessel_mine_count, background=background_colour, foreground="white", font="none 10")
label_vessel_mine_count.grid(row=9, column=0, sticky=W, columnspan=2)
label_vessel_emp_count = \
ttk.Label(window, text="EMPs: " + vessel_emp_count, background=background_colour, foreground="white", font="none 10")
label_vessel_emp_count.grid(row=10, column=0, sticky=W, columnspan=2)
label_vessel_shock_count = \
ttk.Label(window, text="P Shocks: " + vessel_shock_count, background=background_colour, foreground="white", font="none 10")
label_vessel_shock_count.grid(row=11, column=0, sticky=W, columnspan=2)
label_vessel_beacon_count = \
ttk.Label(window, text="Beacons: " + vessel_beacon_count, background=background_colour, foreground="white", font="none 10")
label_vessel_beacon_count.grid(row=12, column=0, sticky=W, columnspan=2)
label_vessel_probe_count = \
ttk.Label(window, text="Probes: " + vessel_beacon_count, background=background_colour, foreground="white", font="none 10")
label_vessel_probe_count.grid(row=13, column=0, sticky=W, columnspan=2)
label_vessel_tag_count = \
ttk.Label(window, text="Tags: " + vessel_beacon_count, background=background_colour, foreground="white", font="none 10")
label_vessel_tag_count.grid(row=14, column=0, sticky=W, columnspan=2)
'''

# label_vessel_homing_count.configure(text="Homings: " + vessel_homing_count)
# label_vessel_nuke_count.configure(text="Nukes: " + vessel_nuke_count)
# label_vessel_mine_count.configure(text="Mines: " + vessel_mine_count)
# label_vessel_emp_count.configure(text="EMPs: " + vessel_emp_count)
# label_vessel_shock_count.configure(text="P Shocks: " + vessel_shock_count)
# label_vessel_beacon_count.configure(text="Beacons: " + vessel_beacon_count)
# label_vessel_probe_count.configure(text="Probes: " + vessel_probe_count)
# label_vessel_tag_count.configure(text="Tag: " + vessel_tag_count)