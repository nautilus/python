# external imports
import graphene
from flask_graphql import GraphQLView, GraphQL
from graphene.contrib.sqlalchemy import SQLAlchemyObjectType
# local imports
from nautilus import db
from nautilus.api.fields import Connection
from nautilus.conventions import getModelString

def init_service(service, schema):
    """ Add GraphQL support to the given Flask app """
    # add default graphql endpoints
    GraphQL(service.app, schema=schema)
    # add the index query per service agreement
    service.app.add_url_rule('/', view_func=GraphQLView.as_view('index', schema=schema))


def create_model_schema(Model):
    """ This function creates a graphql schema that provides a single model """

    # create the schema instance
    schema = graphene.Schema(session = db.session)

    # create a graphene object registered with the schema
    @schema.register
    class ModelObjectType(SQLAlchemyObjectType):
        class Meta:
            model = Model

    class Query(graphene.ObjectType):
        """ the root level query """
        all_models = Connection(ModelObjectType)

        def resolve_all_models(self, args, info):
            return Model.query.all()

    # add the query to the schema
    schema.query = Query

    return schema