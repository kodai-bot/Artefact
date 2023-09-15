import xml.etree.ElementTree as ET

def create_epcis_capture_event(event_type, epc, location, quantity, business_step, disposition, biz_transaction_list=None, source_dest_list=None):
    # Create the root element and set the namespace
    root = ET.Element('EPCISDocument', {'xmlns': 'urn:epcglobal:epcis:xsd:1'})
    
    # Add the header element
    header = ET.SubElement(root, 'EPCISHeader')
    # Add the extension element
    extension = ET.SubElement(header, 'extension')
    # Add the EPCISMasterData element
    epcis_master_data = ET.SubElement(extension, 'EPCISMasterData')
    
    # Add the event element
    event_element = ET.SubElement(root, 'eventList')
    event = ET.SubElement(event_element, 'ObjectEvent')
    
    # Set the event type
    event.set('eventType', event_type)
    
    # Add the EPC element
    epc_element = ET.SubElement(event, 'epcList')
    epc_node = ET.SubElement(epc_element, 'epc')
    epc_node.text = epc
    
    # Add the eventTime element
    event_time = ET.SubElement(event, 'eventTime')
    event_time.text = '2020-01-01T12:00:00Z'
    
    # Add the eventTimeZoneOffset element
    event_time_offset = ET.SubElement(event, 'eventTimeZoneOffset')
    event_time_offset.text = '+01:00'
    
    # Add the bizLocation element
    biz_location = ET.SubElement(event, 'bizLocation')
    id_element = ET.SubElement(biz_location, 'id')
    id_element.text = location
    
    # Add the bizTransactionList element
    if biz_transaction_list is not None:
        biz_transaction_element = ET.SubElement(event, 'bizTransactionList')
        for biz_transaction in biz_transaction_list:
            biz_transaction_node = ET.SubElement(biz_transaction_element, 'bizTransaction')
            biz_transaction_node.set('type', biz_transaction[0])
            biz_transaction_node.text = biz_transaction[1]
    
    # Add the sourceDestList element
    if source_dest_list is not None:
        source_dest_element = ET.SubElement(event, 'sourceDestList')
        for source_dest in source_dest_list:
            source_dest_node = ET.SubElement(source_dest_element, 'sourceDest')
            source_dest_node.set('type', source_dest[0])
            source_dest_node.text = source_dest[1]
    
       # Add the disposition element
    event.set('disposition', disposition)
    
    # Add the readPoint element
    read_point = ET.SubElement(event, 'readPoint')
    id_element = ET.SubElement(read_point, 'id')
    id_element.text = 'urn:epc:id:sgln:example.com:readpoint'
    
    # Add the businessStep element
    event.set('bizStep', business_step)
    
    # Add the quantity element
    quantity_element = ET.SubElement(event, 'quantity')
    quantity_element.text = str(quantity)
    
    # Return the XML tree as a string
    return ET.tostring(root, encoding='unicode')



    

# Example usage
capture_event = create_epcis_capture_event(
    'OBSERVE',
    'urn:epc:id:sgtin:example.com:product:12345',
    'urn:epc:id:sgln:example.com:location:12345',
    1,
    'urn:epcglobal:cbv:bizstep:receiving',
    'urn:epcglobal:cbv:disp:in_progress',
    biz_transaction_list=[('urn:epcglobal:cbv:bt:po', 'urn:epcglobal:cbv:bt:po_12345')],
    source_dest_list=[('source', 'urn:epc:id:sgln:example.com:supplier')]
)
print(capture_event)

