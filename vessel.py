import xml.etree.ElementTree as ET

class Vessel(object):
    def __init__(self):
        self.id = ""
        self.side = ""
        self.classname = ""
        self.broadType = ""
        self.front_shield = 0
        self.back_shield = 0
        self.description = ""
        self.arcwidth = 0.0
        self.arc_width_extent = 0.0
        self.arc_x = 0.0
        self.arc_x_start = 0.0
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
        vessel_arcwidth = \
        root.find(".//vessel[@uniqueID='" + uid + "']/beam_port").attrib['arcwidth']
        vessel_arc_x = \
        self.root.find(".//vessel[@uniqueID='" + uid + "']/beam_port").attrib['x']

        vessel_front_shield = root.find(".//vessel[@uniqueID='" + uid + "']/shields").attrib['front']
        vessel_back_shield = root.find(".//vessel[@uniqueID='" + uid + "']/shields").attrib['back']

        vessel_arc_width_extent = 360 * float(vessel_arcwidth)
        vessel_arc_width_extent_half = round(vessel_arc_width_extent / 2)
        #print(vessel_arc_width_extent)

        if vessel_arc_x < "0":
            vessel_arc_x_start = round((360 - float(vessel_arc_x))  + (90 + vessel_arc_width_extent_half))
            #print("if:"+vessel_arc_x)
        else:
            vessel_arc_x_start = round((0 + float(vessel_arc_x)) + (90 - vessel_arc_width_extent_half))
            #print("else:" + vessel_arc_x)

        self.front_shield     = vessel_front_shield
        self.back_shield      = vessel_back_shield
        self.arcwidth         = vessel_arcwidth
        self.arc_width_extent = vessel_arc_width_extent
        self.arc_x            = vessel_arc_x
        self.arc_x_start      = vessel_arc_x_start

    def _getOrdData(self):
        root = self.root
        uid = self.id 
        for ord_type in self.ordnance.keys():
            elem = root.find(".//vessel[@uniqueID='" + uid + "']/torpedo_storage[@type='" + ord_type + "']")
            if elem is not None:
                self.ordnance[ord_type] = elem.attrib['amount']


