from . import Notifier
import os
import httplib2
import base64
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from email.mime.text import MIMEText

class GmailNotifier(Notifier):
    """
    Herald notifier that uses GMail to send notifications
    """
    def __init__(self, message, subject="Herald Notification", cc=[], client_secret_file='client_secret.json'):
        """

        :param message: The default message to use in the notification.
        :param subject: The subject line of the email that will be sent to GMail.
        :param cc: List of emails to send the notification to as `cc`.
        :param client_secret_file: The location of the secret file which has the GMail access tokens.
        """
        super().__init__(message)
        self.message = message
        self.subject = subject
        self.cc = cc
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.compose']
        self.CLIENT_SECRET_FILE = client_secret_file
        self.APPLICATION_NAME = 'Herald by Varun Agrawal'
        self.get_credentials()

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'herald-credentials.json')

        store = Storage(credential_path)
        self.credentials = store.get()
        if not self.credentials or self.credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            self.credentials = tools.run_flow(flow, store, None)
            print('Storing credentials to ' + credential_path)

    def notify(self, message=None):
        """
        Send the notification.
        :param message: The message string to use in the notification. If empty, the default message is used.
        :return: None
        """
        if not message:
            message = self.message
        http = self.credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)

        mail = MIMEText(message)
        mail["subject"] = self.subject

        try:
            user = service.users().getProfile(userId="me").execute()
            mail["to"] = user["emailAddress"]
            mail["from"] = user["emailAddress"]
            mail["cc"] =",".join(self.cc)

            mail = {'raw': base64.urlsafe_b64encode(mail.as_string().encode()).decode()}
            message = service.users().messages().send(userId="me", body=mail).execute()
            if message:
                print("Notification sent!")
            else:
                raise ValueError("Error sending message")

        except (Exception,) as ex:
            print(ex)