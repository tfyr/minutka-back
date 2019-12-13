import graphene
from graphene_django import DjangoObjectType


from minutka.models import Review

class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class Query(graphene.ObjectType):
    reviews = graphene.List(ReviewType)
    def resolve_reviews(self, info, **kwargs):
        return Review.objects.filter(published=True).order_by('-pub_date')


schema = graphene.Schema(
    query=Query,
    #mutation=Mutation,
)