# Copyright (c) 2023, Noori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name}{self.last_name or ""}'
	def validate(self):
		if self.mobile_number:
			phone_length=len(self.mobile_number)
			if phone_length != 10:
				frappe.throw('Phone number should be 10 digit')
			