# Made by Felipe Barbosa Figueira
class Record:
    def __init__(self, data):
        """Initializer method, demonstrates constructors in OOP."""
        self.ref_number = data['ref_number']
        self.disclosure_group = data['disclosure_group']
        self.title_en = data['title_en']
        self.title_fr = data['title_fr']
        self.name = data['name']
        self.purpose_en = data['purpose_en']
        self.purpose_fr = data['purpose_fr']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.destination_en = data['destination_en']
        self.destination_fr = data['destination_fr']
        self.airfare = data['airfare']
        self.other_transport = data['other_transport']
        self.lodging = data['lodging']
        self.meals = data['meals']
        self.other_expenses = data['other_expenses']
        self.total = data['total']
        self.additional_comments_en = data['additional_comments_en']
        self.additional_comments_fr = data['additional_comments_fr']
        self.owner_org = data['owner_org']
        self.owner_org_title = data['owner_org_title']

    def __str__(self):
        """String representation of the object."""
        return (f"{self.ref_number}, {self.disclosure_group}, {self.title_en}, {self.title_fr}, {self.name}, "
                f"{self.purpose_en}, {self.purpose_fr}, {self.start_date}, {self.end_date}, {self.destination_en}, "
                f"{self.destination_fr}, {self.airfare}, {self.other_transport}, {self.lodging}, {self.meals}, "
                f"{self.other_expenses}, {self.total}, {self.additional_comments_en}, {self.additional_comments_fr}, "
                f"{self.owner_org}, {self.owner_org_title}")
