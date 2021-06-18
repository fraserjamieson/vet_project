class Customer:
    def __init__(self, name, contact_details, id= None):
        self.name = name
        self.contact_details = contact_details
        self.id = id
        

        # responsibility of this customer class is to model a customer, not communicate with the database, this is the repositiories concern.

   
