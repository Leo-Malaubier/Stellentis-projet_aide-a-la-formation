#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pandas as pd
import os

emplacement_fichier="../fichier_cours/"

def csv_to_excel(file):
    nomSimple=file.split("/")[-1]
    read_file = pd.read_excel(file)
    read_file.to_csv (emplacement_fichier+"csv/"+nomSimple.split('.')[0]+".csv",
                      index = None,
                      header=True)
    df = pd.DataFrame(pd.read_csv(emplacement_fichier+"csv/"+nomSimple.split('.')[0]+".csv"))
