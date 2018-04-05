import xml.etree.ElementTree as ET
import datetime

def main():
    
    #MIXED PALLET
    template_xml_file_name = "BINDAREE_DESADV_MIXED_20180405130626.xml"
    doc = ET.parse(template_xml_file_name)

    root = doc.getroot()

    for element in root.iter('ItemBarcode'):
        existing_bar_code = element.text.lstrip('0')  #python considers the number as octal if it starts with zero
        bar_code_int = int(existing_bar_code) + 1
        element.text = "0" + str(bar_code_int)

    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%Y%m%d%H%M%S")

    updated_file_name = template_xml_file_name[0:len(template_xml_file_name)-18] + "MIXED" + string_date + ".xml"

    print(updated_file_name)
    
    doc.write(updated_file_name)     
    

if __name__ =="__main__":
    main()