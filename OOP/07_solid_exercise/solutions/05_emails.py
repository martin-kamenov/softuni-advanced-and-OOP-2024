from abc import ABC, abstractmethod

class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyMl(IContent):

    def format(self) -> str:
        return '\n'.join(['<myML>', self.text, '</myML>'])


class IProtocol:

    def __init__(self, protocol: str):
        self.protocol = protocol

    def get_protocol(self, identity):
        if self.protocol == 'IM':
            return f"I'm {identity}"

        return identity


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class Email(IEmail):

    def __init__(self, protocol : str):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = self.protocol_format(sender)

    def set_receiver(self, receiver):
        self.__receiver = self.protocol_format(receiver)

    def set_content(self, content: IContent):
        self.__content = content.format()

    def protocol_format(self, identity: str) -> str:
        if self.protocol == 'IM':
            return ''.join(["I'm ", identity])

        return identity

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyMl('Hello, there!')
email.set_content(content)
print(email)


