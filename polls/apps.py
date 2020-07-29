from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = "polls"

    def ready(self):
        import polls.dummy_context
        import polls.notifications
