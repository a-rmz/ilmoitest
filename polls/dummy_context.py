from django_ilmoitin.dummy_context import COMMON_CONTEXT, dummy_context

from .models import Animal

dummy_animal = Animal(name="unicorn")

dummy_context.update(
    {COMMON_CONTEXT: {"animal": dummy_animal},}
)
