from dataclasses import dataclass
from unittest.mock import Mock
from mail_sender import MailSender, Request

@dataclass
class Response:
    request: Request
    code: int

@dataclass
class User: 
    name: str
    email: str

def test_send_v1():
    def post(url, request):
        return Response(request, 200)
    
    mockHttpClient = Mock(**{'post.side_effect': post})
    message = 'Hello world'
    user = User('toto', 'toto@titi.com')
    mailSender = MailSender(mockHttpClient)
    request = mailSender.send_v1(user, message).request
    assert request.name == user.name
    assert request.email == user.email
    assert request.subject == 'New notification'
    assert request.message == message

def test_send_v2():
    def post(url, request):
        return Response(request, 503)
    
    mockHttpClient = Mock(**{'post.side_effect': post})
    message = 'Hello world'
    user = User('toto', 'toto@titi.com')
    mailSender = MailSender(mockHttpClient)
    request = mailSender.send_v2(user, message).request
    assert request.name == user.name
    assert request.email == user.email
    assert request.subject == 'New notification'
    assert request.message == message