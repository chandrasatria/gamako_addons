# -*- coding: utf-8 -*-
# Copyright (c) 2015, Myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
class custom_method(Document):
	pass

@frappe.whitelist()
def get_data_sales_order(nomor_sales_order):
	data = frappe.db.sql(""" SELECT item_code, item_name, qty FROM `tabSales Order Item` WHERE parent = "{}" """.format(nomor_sales_order))
	return data

@frappe.whitelist()
def get_pe_data(doctype, txt, searchfield, start, page_len, filters):
	data = frappe.db.sql(""" SELECT ur.parent FROM `tabHas Role` ur
		JOIN `tabUser` u ON u.`name` = ur.parent
		WHERE u.enabled = 1
		AND ur.role = "Product Engineering" """)
	return data

@frappe.whitelist()
def get_pe_item(item):
	data = frappe.db.sql(""" 
		SELECT tu.first_name FROM `tabPE Item Relation Detail` pet 
		JOIN `tabUser` tu ON tu.`name` = pet.parent WHERE pet.item_code = "{}" LIMIT 1 """.format(item))
	
	return data