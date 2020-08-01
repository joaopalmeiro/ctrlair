import altair as alt
from typing import Any


def is_namedtuple(obj: Any) -> bool:
    return isinstance(obj, tuple) and hasattr(obj, "_fields")


def is_single_chart(obj):
    return isinstance(obj, alt.Chart)


def is_layered_chart(obj):
    return isinstance(obj, alt.LayerChart)


def is_horizontally_concatenated_chart(obj):
    return isinstance(obj, alt.HConcatChart)


def is_vertically_concatenated_chart(obj):
    return isinstance(obj, alt.VConcatChart)


def is_concatenated_chart(obj):
    return is_horizontally_concatenated_chart(obj) or is_vertically_concatenated_chart(
        obj
    )


def is_repeated_chart(obj):
    return isinstance(obj, alt.RepeatChart)


def is_faceted_chart(obj):
    return isinstance(obj, alt.FacetChart)


def is_compound_chart(obj):
    return (
        is_layered_chart(obj)
        or is_concatenated_chart(obj)
        or is_repeated_chart(obj)
        or is_faceted_chart(obj)
    )