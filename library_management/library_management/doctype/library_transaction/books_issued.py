import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
    # def before_submit(self):
    #     doc = frappe.new_doc('Library Books Issued')
    #     doc.books_issued=self.article
    #     doc.library_member=self.member_name
    #     doc.member_id=self.library_member
    #     doc.insert()
    #     doc.save()