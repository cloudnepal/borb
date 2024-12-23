#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Set the text rise, T rise , to rise, which shall be a number expressed in
unscaled text space units. Initial value: 0.
"""
import typing
from decimal import Decimal

from borb.io.read.types import AnyPDFType
from borb.pdf.canvas.operator.canvas_operator import CanvasOperator


class SetTextRise(CanvasOperator):
    """
    Set the text rise, T rise , to rise, which shall be a number expressed in
    unscaled text space units. Initial value: 0.
    """

    #
    # CONSTRUCTOR
    #

    def __init__(self):
        super().__init__("Ts", 1)

    #
    # PRIVATE
    #

    #
    # PUBLIC
    #

    def invoke(
        self,
        canvas_stream_processor: "CanvasStreamProcessor",  # type: ignore [name-defined]
        operands: typing.List[AnyPDFType] = [],
        event_listeners: typing.List["EventListener"] = [],  # type: ignore [name-defined]
    ) -> None:
        """
        Invoke the Ts operator
        :param canvas_stream_processor:     the CanvasStreamProcessor
        :param operands:                    the operands for this CanvasOperator
        :param event_listeners:             the typing.List of EventListener(s) that may be notified
        :return:                            None
        """
        assert isinstance(operands[0], Decimal)
        canvas = canvas_stream_processor.get_canvas()
        canvas.graphics_state.text_rise = operands[0]
