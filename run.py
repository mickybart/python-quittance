#!/usr/bin/env python
# -*- coding: utf8 -*-

from quittance.config import Config
from quittance.pdf import PDF

rent = Config.load_json("rent.json")
config = Config(rent["address"],
                rent["owner"],
                rent["tenant"],
                rent["currency"],
                rent["rent_price"],
                rent["rent_charge_price"],
                rent["town"],
                rent["signature"])

paid = Config.load_json("paid.json")

pdf = PDF()
pdf.output_pdf(config.getQuittance, paid["date"])

print("Receipt done")
