# from document_management_03.project.document import Document
# from document_management_03.project.category import Category
# from document_management_03.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self,category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self,document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = [el for el in self.categories if el.id == category_id][0]
        current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = [el for el in self.topics if el.id == topic_id][0]
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = [el for el in self.documents if el.id == document_id][0]
        current_document.file_name = new_file_name

    def delete_category(self,category_id):
        current_category = [el for el in self.categories if el.id == category_id][0]
        if current_category in self.categories:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = [el for el in self.topics if el.id == topic_id][0]
        if current_topic in self.topics:
            self.topics.remove(current_topic)

    def delete_document(self,document_id):
        current_document = [el for el in self.documents if el.id == document_id][0]
        if current_document in self.documents:
            self.documents.remove(current_document)

    def get_document(self,document_id):
        current_document = [el for el in self.documents if el.id == document_id][0]
        return current_document

    def __repr__(self):
        result = ''
        for el in self.documents:
            result += f'{str(el)}\n'
        return result

#
# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)

