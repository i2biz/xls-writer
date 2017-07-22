# coding=utf-8

from invoke import task


@task
def pep8(ctx):
  ctx.run("pep8 xls_writer xls_writer_test")


@task
def lint(ctx):
  ctx.run("pylint xls_writer xls_writer_test -r n")


@task
def test(ctx):
  ctx.run("py.test -v --cov xls_writer --cov-report=html --cov-report=term-missing xls_writer_test")


@task(pre=[test, pep8, lint])
def check(ctx):
  pass




