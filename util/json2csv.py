import json

with open('Products-FAO.WAPOR_2.json') as fpjson, open('Products-FAO.WAPOR_2.csv', 'w') as fpcsv:
    fpcsv.write('id\tcode\tcaption\tdescription\t'
                'additionalInfo.format\t'
                'additionalInfo.unit\t'
                'additionalInfo.dataType\t'
                'additionalInfo.conversionFactor\t'
                'additionalInfo.noDataValue\t'
                'additionalInfo.spatialResolution\t'
                'additionalInfo.spatialExtent\t'
                'additionalInfo.spatialReferenceSystem\t'
                'additionalInfo.temporalResolution\t'
                'additionalInfo.temporalExtent\t'
                'additionalInfo.nearRealTime\t'
                'additionalInfo.methodology\t'
                'links.href\n')

    data = json.load(fpjson)
    i = 0
    for cube_code in data['response']:
        i += 1
        print(i, 'code: ' + cube_code['code'], end='')
        fpcsv.write('{}\t'.format(i))
        fpcsv.write('{}\t'.format(cube_code['code']).replace(chr(10), ''))
        fpcsv.write('{}\t'.format(cube_code['caption']).replace(chr(10), ''))
        fpcsv.write('{}\t'.format(cube_code['description']).replace(chr(10), ''))

        try:
            code_info = cube_code['additionalInfo']
        except KeyError as err:
            print('\tadditionalInfo', end='')
            fpcsv.write('\t\t\t\t\t\t\t\t\t\t\t\t')
        else:
            fpcsv.write('{}\t'.format(code_info['format']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['unit']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['dataType']).replace(chr(10), ''))
            try:
                fpcsv.write('{}\t'.format(code_info['conversionFactor']).replace(chr(10), ''))
            except KeyError as err:
                print('\tconversionFactor', end='')
                fpcsv.write('\t')
            fpcsv.write('{}\t'.format(code_info['noDataValue']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['spatialResolution']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['spatialExtent']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['spatialReferenceSystem']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['temporalResolution']).replace(chr(10), ''))
            fpcsv.write('{}\t'.format(code_info['temporalExtent']).replace(chr(10), ''))
            try:
                fpcsv.write('{}\t'.format(code_info['nearRealTime']).replace(chr(10), ''))
            except KeyError as err:
                print('\tnearRealTime', end='')
                fpcsv.write('\t')
            fpcsv.write('{}\t'.format(code_info['methodology']).replace(chr(10), ''))

        fpcsv.write('{}'.format(cube_code['links'][0]['href']).replace(chr(10), ''))
        fpcsv.write('\n')
        print(';', end='\n')
