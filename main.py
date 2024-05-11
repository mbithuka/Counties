import json

data = [
    ['1', 'Mombasa', 'Coast', '212.5', '939,370', '1,208,333', 'Mombasa', 'MSA'],
    ['2', 'Kwale', 'Coast', '8,270.3', '649,931', '866,820', 'Kwale', 'KWL'],
    ['3', 'Kilifi', 'Coast', '12,245.9', '1,109,735', '1,453,787', 'Kilifi', 'KLF'],
    ['4', 'Tana River', 'Coast', '35,375.8', '240,075', '315,943', 'Hola', 'TRV'],
    ['5', 'Lamu', 'Coast', '6,497.7', '101,539', '143,920', 'Lamu', 'LMU'],
    ['6', 'Taita–Taveta', 'Coast', '17,083.9', '284,657', '340,671', 'Wundanyi', 'TVT'],
    ['7', 'Garissa', 'North Eastern', '45,720.2', '623,060', '841,353', 'Garissa', 'GRS'],
    ['8', 'Wajir', 'North Eastern', '55,840.6', '661,941', '781,263', 'Wajir', 'WJR'],
    ['9', 'Mandera', 'North Eastern', '25,797.7', '1,025,756', '867,457', 'Mandera', 'MDR'],
    ['10', 'Marsabit', 'Eastern', '66,923.1', '291,166', '459,785', 'Marsabit', 'MRS'],
    ['11', 'Isiolo', 'Eastern', '25,336.1', '143,294', '268,002', 'Isiolo', 'ISL'],
    ['12', 'Meru', 'Eastern', '7,003.1', '1,356,301', '1,545,714', 'Meru', 'MRU'],
    ['13', 'Tharaka-Nithi', 'Eastern', '2,609.5', '365,330', '393,177', 'Kathwana', 'TNT'],
    ['14', 'Embu', 'Eastern', '2,555.9', '516,212', '608,599', 'Embu', 'EMB'],
    ['15', 'Kitui', 'Eastern', '24,385.1', '1,012,709', '1,136,187', 'Kitui', 'KTU'],
    ['16', 'Machakos', 'Eastern', '5,952.9', '1,098,584', '1,421,932', 'Machakos', 'MCK'],
    ['17', 'Makueni', 'Eastern', '8,008.9', '884,527', '987,653', 'Wote', 'MKN'],
    ['18', 'Nyandarua', 'Central', '3,107.7', '596,268', '638,289', 'Ol Kalou', 'NDR'],
    ['19', 'Nyeri', 'Central', '2,361.0', '693,558', '759,164', 'Nyeri', 'NYR'],
     ['20', 'Kirinyaga', 'Central', '1,205.4', '528,054', '610,411', 'Kerugoya', 'KRG'],
 ['21', "Murang'a", 'Central', '2,325.8', '942,581', '1,056,640', "Murang'a", 'MRG'],
 ['22', 'Kiambu', 'Central', '2,449.2', '1,623,282', '2,417,735', 'Kiambu', 'KMB'],
 ['23', 'Turkana', 'Rift Valley', '98,597.8', '1,100,399', '1,504,976', 'Lodwar', 'TRK'],
 ['24', 'West Pokot', 'Rift Valley', '8,418.2', '512,690', '621,241', 'Kapenguria', 'WPK'],
 ['25', 'Samburu', 'Rift Valley', '20,182.5', '223,947', '310,327', 'Maralal', 'SBR'],
 ['26', 'Trans-Nzoia', 'Rift Valley', '2,469.9', '818,757', '990,341', 'Kitale', 'TNZ'],
 ['27', 'Uasin Gishu', 'Rift Valley', '2,955.3', '894,179', '1,163,186', 'Eldoret', 'UGS'],
 ['28', 'Elgeyo-Marakwet', 'Rift Valley', '3,049.7', '369,998', '454,480', 'Iten', 'EMK'],
 ['29', 'Nandi', 'Rift Valley', '2,884.5', '752,965', '885,711', 'Kapsabet', 'NDI'],
 ['30', 'Baringo', 'Rift Valley', '11,075.3', '555,561', '666,763', 'Kabarnet', 'BRG'],
 ['31', 'Laikipia', 'Rift Valley', '8,696.1', '399,227', '518,560', 'Rumuruti', 'LKP'],
 ['32', 'Nakuru', 'Rift Valley', '7,509.5', '1,603,325', '2,162,202', 'Nakuru[8][9]', 'NKR'],
 ['33', 'Narok', 'Rift Valley', '17,921.2', '850,920', '1,157,873', 'Narok', 'NRK'],
 ['34', 'Kajiado', 'Rift Valley', '21,292.7', '687,312', '1,117,840', 'Kajiado', 'KJD'],
 ['35', 'Kericho', 'Rift Valley', '2,454.5', '752,396', '901,777', 'Kericho', 'KRC'],
 ['36', 'Bomet', 'Rift Valley', '1,997.9', '730,129', '875,689', 'Bomet', 'BMT'],
 ['37', 'Kakamega', 'Western', '3,033.8', '1,660,651', '1,867,579', 'Kakamega', 'KKG'],
 ['38', 'Vihiga', 'Western', '531.3', '554,622', '590,013', 'Mbale', 'VHG'],
 ['39', 'Bungoma', 'Western', '2,206.9', '1,375,063', '1,670,570', 'Bungoma', 'BGM'],
 ['40', 'Busia', 'Western', '1,628.4', '743,946', '893,681', 'Busia', 'BSA'],
 ['41', 'Siaya', 'Nyanza', '2,496.1', '842,304', '993,183', 'Siaya', 'SYA'],
 ['42', 'Kisumu', 'Nyanza', '2,009.5', '968,909', '1,155,574', 'Kisumu', 'KSM'],
 ['43', 'Homa Bay', 'Nyanza', '3,154.7', '963,794', '1,131,950', 'Homa Bay', 'HBY'],
 ['44', 'Migori', 'Nyanza', '2,586.4', '917,170', '1,116,436', 'Migori', 'MGR'],
 ['45', 'Kisii', 'Nyanza', '1,317.9', '1,152,282', '1,266,860', 'Kisii', 'KSI'],
 ['46', 'Nyamira', 'Nyanza', '912.5', '598,252', '605,576', 'Nyamira', 'NMR'],
 ['47', 'Nairobi', 'Nairobi', '694.9', '3,138,369', '4,397,073', 'Nairobi', 'NBI'],

]

formatted_data = []

for item in data:
    formatted_item = {
        "code": item[0],
        "county": item[1],
        "former_province": item[2],
        "area_km2": item[3],
        "population_2009": item[4],
        "population_2019": item[5],
        "capital": item[6],
        "postal_abbreviation": item[7]
    }
    formatted_data.append(formatted_item)

# Convert to JSON
json_data = json.dumps(formatted_data, indent=4)
print(json_data)
