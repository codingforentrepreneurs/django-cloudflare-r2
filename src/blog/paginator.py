# services.py

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def paginate_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    return {
        "object_list": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator,
        "page_obj": page_obj,
    }
