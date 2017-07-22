# coding=utf-8
"""Module with API classes."""
import abc


class TableField(object):
  """Represents table field."""

  @property
  def header(self) -> str:
    """Field header"""
    raise NotImplementedError

  def __call__(self, row: object) -> object:
    """
    Extracts and formats data from row.
    """


class FieldReader(object, metaclass=abc.ABCMeta):
  """Object that extracts data from row."""

  @abc.abstractmethod
  def __call__(self, field: TableField, instance) -> object:
    """
    Extract data from row.

    :param field: Field this reader belongs to.
    :param instance: Row instance.
    :return: Cell value
    """
    raise NotImplementedError


class FieldFormatter(object, metaclass=abc.ABCMeta):
  """Formats cell value."""

  @abc.abstractmethod
  def __call__(self, field: TableField, instance) -> object:
    """

    :param field: Field this formatter belongs to.
    :param instance: Cell value.
    :return: formatted value
    """
    raise NotImplementedError


class FieldEmptyCheck(object, metaclass=abc.ABCMeta):
  """
  Checks if field value is empty. If field is empty it will be replaced with default value
  """
  @abc.abstractmethod
  def __call__(self, field: TableField, instance) -> bool:
    """

    :param field: Field this object belongs to.
    :param instance: Extracted cell value (before formatting!)
    :return: true if field IS EMPTY.
    """
    raise NotImplementedError
