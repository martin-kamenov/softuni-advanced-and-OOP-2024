from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        return self.__add_object(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        return self.__add_object(topic, self.topics)

    def add_document(self, document: Document) -> None:
        return self.__add_object(document, self.documents)


    def edit_category(self, category_id: int, new_name: str) -> None:
        return self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        return self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name: str) -> None:
        return self.__edit_object(document_id, self.documents, new_file_name)


    def delete_category(self, category_id: int) -> None:
        return self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id: int) -> None:
        return self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id: int) -> None:
        return self.__delete_object(document_id, self.documents)


    def get_document(self, document_id) -> None:
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])

    @staticmethod
    def __add_object(object_, objects_collection) -> None:
        if object_ not in objects_collection:
            objects_collection.append(object_)

    def __edit_object(self, object_id, objects_collection, *new_values) -> None:
        current_object = self.__find_object(object_id, objects_collection)

        if current_object:
            current_object.edit(*new_values)

    def __delete_object(self, object_id, objects_collection) -> None:
        current_object = self.__find_object(object_id, objects_collection)

        if current_object and current_object in objects_collection:
            objects_collection.remove(current_object)

    @staticmethod
    def __find_object(object_id, objects_collection) -> 'Document' or None:
        return next((o for o in objects_collection if o.id == object_id), None)