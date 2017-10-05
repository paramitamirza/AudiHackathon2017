import csv
import numpy as np
import pandas as pd

csv = np.genfromtxt('../data/prnr_einzeln.csv',delimiter=";",dtype=None)
pnrdata = csv[1:]

#print (pnrdata)
out = open("../data/prnr_clean.csv", "w")

prfam = {}
i = 1

for row in pnrdata:
    prnrstr = row[1]
    for cols in prnrstr[2:].decode('UTF-8').split("~3L~"):
        feat = cols.replace("~3L", "")
        feat = feat.replace("~", "_")
        feat = feat.replace("\"", "")

        feat_fam = feat.split("_")[0]
        if feat_fam not in prfam:
            prfam[feat_fam] = i
            i += 1

print (prfam)

out.write("KNR")
for fam in prfam:
    out.write("," + fam)
out.write("\n")

for row in pnrdata:
    car_id = row[0]
    prnrstr = row[1]
    prnrlist = []
    for i in range(len(prfam) + 1):
        prnrlist.append("")
    prnrlist[0] = car_id.decode('UTF-8')

    for cols in prnrstr[2:].decode('UTF-8').split("~3L~"):
        feat = cols.replace("~3L", "")
        feat = feat.replace("~", "_")
        feat = feat.replace("\"", "")
        fam = feat.split("_")[0]
        feat = feat.split("_")[1]
        prnrlist[prfam[fam]] = feat

    out.write (",".join(prnrlist) + "\n")


out.close()

df = pd.read_csv('pandas_dataframe_importing_csv/example.csv')
