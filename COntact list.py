class ContactList(list):
    def init(self, name1):
        self.name1 = name1
        print(name1)
    
    def search_by_name(self, *name):
        cont = []
        for i in self.name1:
            if self.name1.count(i) > 1:
                cont.append(i)
        prov = [i for i in self.name1 if self.name1.count(i) > 1]
        set1= set(prov)
        print("Список совпадений: ")
        print(set1)
        print(cont)
        

all_contacts = ContactList(['Ivan','Masha', 'Jenya', 'Ivan', 'Ivan' ,'Masha', 'Masha'])
all_contacts.search_by_name('Ivan' 'Masha')