# -*- coding: utf-8 -*-

class CustomerPortal(CustomerPortal):
    def __init__(self):
        super(CustomerPortal, self).__init__()
        OPTIONAL_BILLING_FIELDS.append("lcc")