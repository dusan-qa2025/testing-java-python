def on_contact(emailService):
    # do some work and then send emails to admin and client
    emailService.send_email("admin@mail.com", "new inquiry", "some text")
    emailService.send_email("client@mail.com", "new inquiry", "some text") 

class EmailServiceSpy():

    is_send_email_was_called = False
    send_email_call_count = 0

    def send_email(to, subject, message):
        is_send_message_was_called = True
        send_email_call_count += 1

    def test_on_contact():
        spy = EmailServiceSpy()
        on_contact(spy)

        if(not(spy.is_send_email_was_called)):
            # Test failed
            pass
        if(spy.send_email_call_count != 2):
            # Test failed
            pass
        else:
            # Test passed
            pass
        