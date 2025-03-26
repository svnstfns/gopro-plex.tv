import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import os
from dotenv import load_dotenv

load_dotenv()

EPG_PATH = os.getenv("EPG_PATH", "/www/epg.xml")

now = datetime.datetime.utcnow()
end = now + datetime.timedelta(hours=12)

tv = Element('tv')
channel = SubElement(tv, 'channel', id="gopro")
SubElement(channel, 'display-name').text = "GoPro Hero9"

programme = SubElement(tv, 'programme', start=now.strftime('%Y%m%d%H%M%S') + " +0000",
                       stop=end.strftime('%Y%m%d%H%M%S') + " +0000", channel="gopro")
SubElement(programme, 'title').text = "GoPro Livestream"
SubElement(programme, 'desc').text = "Live von deiner GoPro Kamera"

tree = ElementTree(tv)
tree.write(EPG_PATH, encoding='utf-8', xml_declaration=True)
print(f"EPG geschrieben: {EPG_PATH}")
