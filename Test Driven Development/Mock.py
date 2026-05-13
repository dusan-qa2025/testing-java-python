from unittest.mock import Mock

email_service_mock = Mock()

email_service_mock.send_email("admin@mail.com", "New inquiry", "some text")
email_service_mock.send_email("client@mail.com", "New inquiry", "some text")

assert email_service_mock.send_email.call_count == 2
email_service_mock.send_email.assert_called()

email_service_mock.send_email.assert_called_with("client@mail.com", "New inquiry", "some text")