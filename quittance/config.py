# Copyright (c) 2018 mickybart
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from .datehelper import DateHelper
import locale

class Config():
    """Config
    
    Permit to handle locale, receipt format etc.
    
    Constructor:
    
    Args:
        address (str): Address of appartment
        owner (str): Owner
        tenant (str): Tenant
        currency (str): Currency (eg: euros, cad, ...)
        rent_price (float): Rent price
        rent_charge_price (float): Rent charge price
        town (str): town name
        signature (str): filename of the signature
    """
    
    quittance = u'''<H1 align="center">Quittance de loyer</H1>
<br>
<br>
<B>Quittance de loyer du mois de :</B> %s
<br>
<br>
<B>Adresse de la location :</B>
<br>
<br>
%s
<br>
Je soussigné %s propriétaire du logement désigné ci-dessus,<br>
déclare avoir reçu de %s<br>
la somme de %s%s au titre du paiement du loyer<br>
et des charges pour la période de location du %s au %s<br>
et lui en donne quittance, sous réserve de tous mes droits.<br>
<br>
<B><U>Détail du règlement</U></B>
<br>
<table border="0" width="100%%">
<thead><tr><th width="40%%"></th><th width="60%%"></th></tr></thead>
<tbody>
<tr><td>Loyer :</td><td>%s%s</td></tr>
<tr><td>Provision pour charges :</td><td>%s%s</td></tr>
<tr><td><B>Total :</B></td><td><B>%s%s</B></td></tr>
<tr><td><br></td><td></td></tr>
<tr><td><B>Date du paiement :</B></td><td>%s</td></tr>
</tbody>
</table>
<br>
Fait à %s, le %s<br>
      <img src="%s" width="100" height="55">
'''

    locale = "fr_FR.UTF-8"

    def __init__(self,
                 address,
                 owner,
                 tenant, 
                 currency, 
                 rent_price, 
                 rent_charge_price, 
                 town, 
                 signature):
        self.address = address
        self.owner = owner
        self.tenant = tenant
        self.currency = currency
        self.rent_price = rent_price
        self.rent_charge_price = rent_charge_price
        self.town = town
        self.signature = signature
        
        if self.locale:
            DateHelper().setLocale(self.locale)
            locale.setlocale(locale.LC_ALL, self.locale)

    def load_json(json_file):
        """Load JSON file
        
        Args:
            json_file (str): filename of a json file
            
        Returns:
            dict: content of the file
        """
        try:
            with open(json_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def getQuittance(self, month_year, begin, end, paid, done):
        """Get the receipt filled
        
        Args:
            month_year (str): the Month Year string
            begin (str): short string for receipt begin date
            end (str): short string for receipt end date
            paid (str): short string for paid date
            done (str): short string for receipt date
        
        Returns:
            str: The receipt
        """
        return self.quittance % (month_year,
                                 self.address,
                                 self.owner,
                                 self.tenant,
                                 locale.format("%.2f", self.rent_price + self.rent_charge_price), self.currency,
                                 begin, end,
                                 locale.format("%.2f", self.rent_price), self.currency,
                                 locale.format("%.2f", self.rent_charge_price), self.currency,
                                 locale.format("%.2f", self.rent_price + self.rent_charge_price), self.currency,
                                 paid,
                                 self.town,
                                 done,
                                 self.signature)
    
