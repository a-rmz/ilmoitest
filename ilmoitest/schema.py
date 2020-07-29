import django_ilmoitin.api.schema as django_ilmoitin_schema
import graphene


class Query(django_ilmoitin_schema.Query, graphene.ObjectType):
    foo = graphene.String()

    def resolve_foo(self, info, **kwargs):
        return "foo"


schema = graphene.Schema(query=Query)
