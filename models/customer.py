class Customer:
    def __init__(self, name, contact_details, registered=False, id= None):
        self.name = name
        self.contact_details = contact_details
        self.registered = registered
        self.id = id
        

        # responsibility of this customer class is to model a customer, not communicate with the database, this is the repositiories concern.

    def registered_with_vet(self):
        self.registered = True
