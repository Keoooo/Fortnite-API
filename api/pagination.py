from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class GetLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 20
	max_limit = 100
