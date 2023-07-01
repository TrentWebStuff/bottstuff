import json

"""Convert CMS GEM ICD Dump to ICD Code:Desc JSON dump.
    Data downloaded from: https://www.cms.gov/Medicare/Coding/ICD10/2018-ICD-10-CM-and-GEMs.html
"""

# import raw txt
path_import = r'./icd10cm_codes_2018.txt'
with open(path_import, 'r') as _f:
    raw = _f.read()
    _f.close()

# convert raw txt to json
data = []
for rcd in raw.split('\n'):
    if rcd:
        data.append({
            'code': rcd[:8].strip(),
            'desc': rcd[9:],
        })

# export converted json
path_export = './codes_icd10.json'
with open(path_export, 'w') as _f:
    json.dump(data, _f)
    _f.close()
