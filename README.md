# Herald

Programmatically send notifications!

## About

Have you ever been in a situation where you've been simply twiddling your thumbs, waiting for your program to finish compiling/running? Are you into Deep Learning and need a way to notify yourself when your program crashes or is done learning to do the impossible?

Then _Herald_ is for you!

With a simple, extensible and pythonic interface, you can get setup with a programmatic way of notifying yourself and/or your teammates about different events in your code.

The following platforms are currently supported:

- GMail
- Twilio

Need to use it with a custom platform? You can easily write your own `notifier` and plug it in to handle that, making _Herald_ infinitely extensible.

## Installation

The easy `pip install herald-notify`.

## Usage

The primary way to use _Herald_ is like a context manager. E.g.

```python
import herald
from herald import notifiers

# Send yourself a mail in Gmail to notify you
# Assumes your Gmail tokens have been set up properly
notifier = notifiers.GmailNotifier()

with Herald(notifier, message="Model Trained!"):
    # super long running process
    train_model()
    ...

```

You should get an email in your registered Gmail account at the end of the program.

You can also specify notifications at arbitrary points via the `notifier` call:

```python
import herald
from herald import notifiers

notifier = notifiers.TerminalNotifier("Whoop de doo!")

notifier.notify("A new custom message")

# Send the original message from the constructor
notifier.notify()
```

## Contributing

If you find bugs, please feel free to submit an Issue, or even better, a Pull Request!

### Development

To set up your dev environment, perform the following steps:
 - Clone _Herald_
 - Inside the root directory, run `pipenv shell` to open a shell.
 - Finally run `pipenv install` to install all the dependencies.

At this point, you should be good to go!

### Testing

WIP
