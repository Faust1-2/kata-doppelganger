from dataclasses import dataclass
from mail_sender import MailSender, Request

@dataclass
class Response:
    request: Request
    code: int

@dataclass
class User: 
    name: str
    email: str

class MockHttpClient:

    def __init__(self, status) -> None:
        self.code = status

    def post(self, url, request):
        return Response(request, self.code)

def test_send_v1():
    message = 'Hello world'
    user = User('toto', 'toto@titi.com')
    mockHttpClient = MockHttpClient(200)
    mailSender = MailSender(mockHttpClient)
    request = mailSender.send_v1(user, message).request
    assert request.name == user.name
    assert request.email == user.email
    assert request.subject == 'New notification'
    assert request.message == message

def test_send_v2():
    message = 'Hello world'
    user = User('toto', 'toto@titi.com')
    mockHttpClient = MockHttpClient(503)
    mailSender = MailSender(mockHttpClient)
    request = mailSender.send_v2(user, message).request
    assert request.name == user.name
    assert request.email == user.email
    assert request.subject == 'New notification'
    assert request.message == message