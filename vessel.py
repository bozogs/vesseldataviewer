import math
import xml.etree.ElementTree as ET

class arcs(object):
    def __init__(self):
        self.arc_width = 0.0
        self.arc_start = 0.0
        self.arc_range = 0
        #self.arc_length = 0.0


class Vessel(object):
    def __init__(self):
        self.id = ""
        self.side = ""
        self.classname = ""
        self.broadType = ""
        self.front_shield = 0
        self.back_shield = 0
        self.description = ""
        self.vessel_arcs = []
        self.ordnance = {
            "trp": 0,
            "nuk": 0,
            "min": 0,
            "emp": 0,
            "shk": 0,
            "bea": 0,
            "pro": 0,
            "tag": 0
        }

    def setup(self, uid, xml_path):
        tree = ET.parse(xml_path)
        if not tree:
            exit("No data")
        self.root = tree.getroot()

        self.id = uid

        self._getArcData()

        self._getOrdData()

        return True

    def _getArcData(self):
        uid = self.id
        root = self.root

        for arc_data in root.findall(".//vessel[@uniqueID='" + uid + "']/beam_port"):

            vessel_arc_width_extent = 360 * float(arc_data.attrib['arcwidth'])
            vessel_arc_width_half = round(vessel_arc_width_extent / 2)
            vessel_data_arc_x = arc_data.attrib['x']
            vessel_data_arc_y = arc_data.attrib['y']
            print(vessel_data_arc_x)
            print("atan2 - " + str(math.atan2(float(vessel_data_arc_x), float(vessel_data_arc_y))))

            vessel_arc_x_start = float(vessel_data_arc_x) - 90
            if vessel_arc_x_start < 0:
                vessel_arc_x_start = vessel_arc_x_start - 360
            else:
                pass

            arc_object = arcs()
            arc_object.arc_width = vessel_arc_width_extent
            arc_object.arc_start = vessel_arc_x_start
            arc_object.arc_range = float(arc_data.attrib['range'])

            self.vessel_arcs.append(arc_object)



    #self.root.find(".//vessel[@uniqueID='" + uid + "']/beam_port").attrib['x']

        vessel_front_shield = root.find(".//vessel[@uniqueID='" + uid + "']/shields").attrib['front']
        vessel_back_shield = root.find(".//vessel[@uniqueID='" + uid + "']/shields").attrib['back']

        #vessel_arc_width_extent = 360 * float(vessel_arcwidth)
        #vessel_arc_width_extent_half = round(vessel_arc_width_extent / 2)
        #print(vessel_arc_width_extent)

        #if vessel_arc_x < "0":
            #vessel_arc_x_start = round((360 - float(vessel_arc_x))  + (90 + vessel_arc_width_extent_half))
            #print("if:"+vessel_arc_x)
        #else:
            #vessel_arc_x_start = round((0 + float(vessel_arc_x)) + (90 - vessel_arc_width_extent_half))
            #print("else:" + vessel_arc_x)

        self.front_shield     = vessel_front_shield
        self.back_shield      = vessel_back_shield
        #self.arcwidth         = vessel_arcwidth
        #self.arc_width_extent = vessel_arc_width_extent
        #self.arc_x            = vessel_arc_x
        #self.arc_x_start      = vessel_arc_x_start

    def _getOrdData(self):
        root = self.root
        uid = self.id 
        for ord_type in self.ordnance.keys():
            elem = root.find(".//vessel[@uniqueID='" + uid + "']/torpedo_storage[@type='" + ord_type + "']")
            if elem is not None:
                self.ordnance[ord_type] = elem.attrib['amount']