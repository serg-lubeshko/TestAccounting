import itertools
import operator
from copy import deepcopy
from functools import reduce

from django.db.models import Q
from rest_framework.filters import OrderingFilter


class CustomOrderFilter(OrderingFilter):

    def filter_fields(self, request, queryset, view):
        param_fields = dict(request.query_params)
        try:
            elem = getattr(view, 'custom_filter_fields', None)
            type_elem = getattr(view, 'type', None)
            dict_param = {elem[i]: k[0] for i, k in param_fields.items() if i in elem}
            dict_keys = dict_param.keys()
            for item in dict_keys:
                search_param = dict_param[item]
                if len(item) > 1 and isinstance(item, tuple):
                    list_keys = [i for i in item]
                    filter_query_2 = dict.fromkeys(list_keys, search_param)
                    dcit_in_list = [{k: v} for k, v in filter_query_2.items()]
                    len_dict = len(dcit_in_list)
                    # queryset = self.return_query_use_filter(len_dict, dcit_in_list, queryset)
                else:
                    filter_query = {i: type_elem[i](k) for i, k in dict_param.items() if i in type_elem}
                    search_fields = list(filter_query.keys())
                    for search_field in search_fields:
                        try:
                            for value in (filter_query[search_field].split('%')):
                                queryset = queryset.filter(Q(**{search_field: value}))
                        except:
                            queryset = queryset.filter(**filter_query)
        except (TypeError, ValueError):
            return queryset
        return queryset

    def filter_queryset(self, request, queryset, view):
        queryset = self.filter_fields(request, queryset, view)
        # queryset = super().filter_queryset(request, queryset, view)
        order_fields = []
        ordering_fields = getattr(view, 'custom_order_fields', None)
        ordering_fields_default = getattr(view, 'ordering', None)
        if ordering_fields:
            params = request.query_params.get(self.ordering_param)
            if params:
                fields = [param.strip() for param in params.split(',')]
                ordering = [f for f in fields if f.lstrip('-') in ordering_fields]
                for field in ordering:
                    symbol = "-" if "-" in field else ""
                    order_fields.append(symbol + ordering_fields[field.lstrip('-')])
                if order_fields:
                    # queryset = self.order(queryset, order_fields)
                    queryset = (queryset).order_by(*order_fields)
            elif ordering_fields_default:
                queryset = queryset.order_by(*ordering_fields_default)
        else:
            queryset = queryset.order_by(*ordering_fields_default)
        return queryset
