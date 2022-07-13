from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import celery


class NewTask(celery.Task):

    def order_task(order_form, order, cart):
        subject = 'New Order'
        html_message = render_to_string("email_template.html",
                                        {'order_form': order_form, 'order': order, 'cart': cart})
        plain_message = strip_tags(html_message)
        mail_sent = send_mail(subject, plain_message, 'support@gamemaxstore.herokuapp.com', [order_form.email],
                              html_message=html_message)
        return mail_sent
