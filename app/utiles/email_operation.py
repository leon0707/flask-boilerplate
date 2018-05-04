# -*- coding: utf-8 -*-

from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from .. import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, test_email=False, reply_to=None,
               **kwargs):
    """Send email function."""
    app = current_app._get_current_object()
    msg = Message(subject,
                  sender=app.config['MAIL_SENDER'], recipients=[to],
                  reply_to=reply_to)
    msg.body = render_template(
        template + '.txt', test_email=test_email, **kwargs)
    msg.html = render_template(
        template + '.html', test_email=test_email, **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
