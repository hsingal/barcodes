import xml.etree.ElementTree as ET
import datetime

def main():
    
    #One Product Pallet
    template_xml_file_name = "<insert xml file name>"
    
    doc = ET.parse(template_xml_file_name)

    root = doc.getroot()
   
    file_obj = open("bar_code_sequence.txt", "r+")
    init_bar_code=int(file_obj.read())

    
    file_obj.seek(0)


    for element in root.iter('ItemBarcode'):
        init_bar_code = init_bar_code + 1
        element.text = "0" + str(init_bar_code)


    #skip = False  #flag to skip alternate itemnumbers in xml file

    #logic to set 'ItemNbr' xml tag blank for every alternate element
    #for element in root.iter('ItemNbr'):
    #    if(skip):
    #          element.text=""
    #    skip = not skip   #toggle skip flag 

    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%Y%m%d%H%M%S")

    updated_file_name = template_xml_file_name[0:len(template_xml_file_name)-18] + string_date + ".xml"

    print(updated_file_name)
    
    doc.write(updated_file_name)     
    
    
    file_obj.write(str(init_bar_code))

    file_obj.close()

if __name__ =="__main__":
    main()
