import graphene
import django_filters
from graphene import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import season, fortniteskins
from graphene import relay



class SeasonType(DjangoObjectType):

    class Meta:
        model = season


class SkinType(DjangoObjectType):

    class Meta:
        model = fortniteskins

class RarityNode(DjangoObjectType):
    """ Rarity = Returns a rarity query all skins in that rarity bracket """
    class Meta:
        model = fortniteskins
        interfaces = (Node, )
        filter_fields = ['rarity']

class PriceNode(DjangoObjectType):
    """PriceNode = Returns a price query """
    class Meta:
        model = fortniteskins
        interfaces = (Node, )
        filter_fields = ['price']



class Query(object):
    all_seasons = graphene.List(SeasonType)
    all_skins = graphene.List(SkinType)
    """ Skins will return one result matching the search"""
    skins = graphene.Field(SkinType,
    						id=graphene.Int(),
    						name = graphene.String(),
    						rarity = graphene.String(),
    						price = graphene.Int(),
    						first_seen = graphene.String()

    	)
    fortniteskins = Node.Field(RarityNode)
    all_rarity = DjangoFilterConnectionField(RarityNode)
    
    skins_price = Node.Field(PriceNode)
    all_price =  DjangoFilterConnectionField(PriceNode)
   

    def resolve_all_seasons(self, info, **kwargs):
        return season.objects.all()

    def resolve_all_skins(self, info, **kwargs):
        return fortniteskins.objects.all()

    def resolve_skins(self, info, **kwargs):
    	id = kwargs.get('id')
    	name = kwargs.get('name')
    	rarity = kwargs.get('rarity')
    	price = kwargs.get('price')
    	first_seen = kwargs.get('first_seen')
    	outfit_img = kwargs.get('outfit_img')

    	if id is not None:
    		return fortniteskins.objects.get(pk=id)

    	if name is not None:
    		return fortniteskins.objects.get(name=name)

    	if rarity is not None:
    		return fortniteskins.objects.get(rarity=rarity)

    	if price is not None:
    		return fortniteskins.objects.get(price=price)

    	if first_seen is not None:
    		return fortniteskins.objects.get(first_seen=first_seen)

    	if outfit_img is not None:
    		return fortniteskins.objects.get(outfit_img=outfit_img)

    	return None





