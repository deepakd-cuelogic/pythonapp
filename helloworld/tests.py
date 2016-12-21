from rebar.testing import flatten_to_dict
import django.http
import django.utils.unittest as unittest2
from contacts import forms


class EditContactFormTests(TestCase):

    def test_mismatch_email_is_invalid(self):

        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'bar@example.com'

        bound_form = forms.ContactForm(data=form_data)
        self.assertFalse(bound_form.is_valid())

    def test_same_email_is_valid(self):

        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'foo@example.com'

        bound_form = forms.ContactForm(data=form_data)
        self.assert_(bound_form.is_valid())


    class LocaleMiddlewareTests(unittest2.TestCase):
        """
        LocalMiddleWare test cases.
        """
        def test_request_not_processed(self):
            middleware = LocaleMiddle()
            response = django.http.HttpResponse()
            middleware.process_response(none, response)
            self.assertFalse(response.cookies)
