(.venv) ubuvan@ubuvan:~/Py/django_store$ python run.py shell
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.2.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: You can use `%hist` to view history, see the options with `%history?`

In [1]: from catalog.models import Category
   ...:
   ...: # Создаем категории
   ...: electronics = Category.objects.create(name="Электроника", description="Гаджеты")
   ...: clothing = Category.objects.create(name="Одежда", description="Модная одежда")
   ...: food = Category.objects.create(name="Продукты", description="Еда")
   ...:
   ...: # Проверяем
   ...: Category.objects.all()
---------------------------------------------------------------------------
UndefinedTable                            Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     88 else:
---> 89     return self.cursor.execute(sql, params)

UndefinedTable: relation "catalog_category" does not exist
LINE 1: INSERT INTO "catalog_category" ("name", "description") VALUE...
                    ^


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
Cell In[1], line 4
      1 from catalog.models import Category
      3 # Создаем категории
----> 4 electronics = Category.objects.create(name="Электроника", description="Гаджеты")
      5 clothing = Category.objects.create(name="Одежда", description="Модная одежда")
      6 food = Category.objects.create(name="Продукты", description="Еда")

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/manager.py:87, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
     85 @wraps(method)
     86 def manager_method(self, *args, **kwargs):
---> 87     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:658, in QuerySet.create(self, **kwargs)
    656 obj = self.model(**kwargs)
    657 self._for_write = True
--> 658 obj.save(force_insert=True, using=self.db)
    659 return obj

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/base.py:814, in Model.save(self, force_insert, force_update, using, update_fields)
    811     if loaded_fields:
    812         update_fields = frozenset(loaded_fields)
--> 814 self.save_base(
    815     using=using,
    816     force_insert=force_insert,
    817     force_update=force_update,
    818     update_fields=update_fields,
    819 )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/base.py:877, in Model.save_base(self, raw, force_insert, force_update, using, update_fields)
    875     if not raw:
    876         parent_inserted = self._save_parents(cls, using, update_fields)
--> 877     updated = self._save_table(
    878         raw,
    879         cls,
    880         force_insert or parent_inserted,
    881         force_update,
    882         using,
    883         update_fields,
    884     )
    885 # Store the database on which the object was saved
    886 self._state.db = using

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/base.py:1020, in Model._save_table(self, raw, cls, force_insert, force_update, using, update_fields)
   1017     fields = [f for f in fields if f is not meta.auto_field]
   1019 returning_fields = meta.db_returning_fields
-> 1020 results = self._do_insert(
   1021     cls._base_manager, using, fields, returning_fields, raw
   1022 )
   1023 if results:
   1024     for value, field in zip(results[0], returning_fields):

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/base.py:1061, in Model._do_insert(self, manager, using, fields, returning_fields, raw)
   1056 def _do_insert(self, manager, using, fields, returning_fields, raw):
   1057     """
   1058     Do an INSERT. If returning_fields is defined then this method should
   1059     return the newly created data for the model.
   1060     """
-> 1061     return manager._insert(
   1062         [self],
   1063         fields=fields,
   1064         returning_fields=returning_fields,
   1065         using=using,
   1066         raw=raw,
   1067     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/manager.py:87, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
     85 @wraps(method)
     86 def manager_method(self, *args, **kwargs):
---> 87     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:1805, in QuerySet._insert(self, objs, fields, returning_fields, raw, using, on_conflict, update_fields, unique_fields)
   1798 query = sql.InsertQuery(
   1799     self.model,
   1800     on_conflict=on_conflict,
   1801     update_fields=update_fields,
   1802     unique_fields=unique_fields,
   1803 )
   1804 query.insert_values(fields, objs, raw=raw)
-> 1805 return query.get_compiler(using=using).execute_sql(returning_fields)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/sql/compiler.py:1822, in SQLInsertCompiler.execute_sql(self, returning_fields)
   1820 with self.connection.cursor() as cursor:
   1821     for sql, params in self.as_sql():
-> 1822         cursor.execute(sql, params)
   1823     if not self.returning_fields:
   1824         return []

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:102, in CursorDebugWrapper.execute(self, sql, params)
    100 def execute(self, sql, params=None):
    101     with self.debug_sql(sql, params, use_last_executed_query=True):
--> 102         return super().execute(sql, params)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:67, in CursorWrapper.execute(self, sql, params)
     66 def execute(self, sql, params=None):
---> 67     return self._execute_with_wrappers(
     68         sql, params, many=False, executor=self._execute
     69     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:80, in CursorWrapper._execute_with_wrappers(self, sql, params, many, executor)
     78 for wrapper in reversed(self.db.execute_wrappers):
     79     executor = functools.partial(wrapper, executor)
---> 80 return executor(sql, params, many, context)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:84, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     82 def _execute(self, sql, params, *ignored_wrapper_args):
     83     self.db.validate_no_broken_transaction()
---> 84     with self.db.wrap_database_errors:
     85         if params is None:
     86             # params default might be backend specific.
     87             return self.cursor.execute(sql)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py:91, in DatabaseErrorWrapper.__exit__(self, exc_type, exc_value, traceback)
     89 if dj_exc_type not in (DataError, IntegrityError):
     90     self.wrapper.errors_occurred = True
---> 91 raise dj_exc_value.with_traceback(traceback) from exc_value

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     87     return self.cursor.execute(sql)
     88 else:
---> 89     return self.cursor.execute(sql, params)

ProgrammingError: relation "catalog_category" does not exist
LINE 1: INSERT INTO "catalog_category" ("name", "description") VALUE...
                    ^


   ...: )
   ...: Product.objects.create(
   ...:     name="Яблоки",
   ...:     category=food,
   ...:     price=199.99,
   ...:     description="Свежие"
   ...: )
   ...:
   ...: # Проверяем
   ...: Product.objects.all()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[2], line 6
      1 from catalog.models import Product
      3 # Создаем продукты
      4 Product.objects.create(
      5     name="Смартфон",
----> 6     category=electronics,
      7     price=29999.99,
      8     description="Новый флагман"
      9 )
     10 Product.objects.create(
     11     name="Футболка",
     12     category=clothing,
     13     price=1999.99,
     14     description="Хлопок 100%"
     15 )
     16 Product.objects.create(
     17     name="Яблоки",
     18     category=food,
     19     price=199.99,
     20     description="Свежие"
     21 )

NameError: name 'electronics' is not defined

In [3]: Category.objects.all()
Out[3]: ---------------------------------------------------------------------------
UndefinedTable                            Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     88 else:
---> 89     return self.cursor.execute(sql, params)

UndefinedTable: relation "catalog_category" does not exist
LINE 1: ...ry"."name", "catalog_category"."description" FROM "catalog_c...
                                                             ^


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/core/formatters.py:770, in PlainTextFormatter.__call__(self, obj)
    763 stream = StringIO()
    764 printer = pretty.RepresentationPrinter(stream, self.verbose,
    765     self.max_width, self.newline,
    766     max_seq_length=self.max_seq_length,
    767     singleton_pprinters=self.singleton_printers,
    768     type_pprinters=self.type_printers,
    769     deferred_pprinters=self.deferred_printers)
--> 770 printer.pretty(obj)
    771 printer.flush()
    772 return stream.getvalue()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/lib/pretty.py:411, in RepresentationPrinter.pretty(self, obj)
    400                         return meth(obj, self, cycle)
    401                 if (
    402                     cls is not object
    403                     # check if cls defines __repr__
   (...)    409                     and callable(_safe_getattr(cls, "__repr__", None))
    410                 ):
--> 411                     return _repr_pprint(obj, self, cycle)
    413     return _default_pprint(obj, self, cycle)
    414 finally:

File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/lib/pretty.py:786, in _repr_pprint(obj, p, cycle)
    784 """A pprint that just redirects to the normal repr function."""
    785 # Find newlines and replace them with p.break_()
--> 786 output = repr(obj)
    787 lines = output.splitlines()
    788 with p.group():

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:374, in QuerySet.__repr__(self)
    373 def __repr__(self):
--> 374     data = list(self[: REPR_OUTPUT_SIZE + 1])
    375     if len(data) > REPR_OUTPUT_SIZE:
    376         data[-1] = "...(remaining elements truncated)..."

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:398, in QuerySet.__iter__(self)
    383 def __iter__(self):
    384     """
    385     The queryset iterator protocol uses three nested iterators in the
    386     default case:
   (...)    396            - Responsible for turning the rows into model objects.
    397     """
--> 398     self._fetch_all()
    399     return iter(self._result_cache)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:1881, in QuerySet._fetch_all(self)
   1879 def _fetch_all(self):
   1880     if self._result_cache is None:
-> 1881         self._result_cache = list(self._iterable_class(self))
   1882     if self._prefetch_related_lookups and not self._prefetch_done:
   1883         self._prefetch_related_objects()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:91, in ModelIterable.__iter__(self)
     88 compiler = queryset.query.get_compiler(using=db)
     89 # Execute the query. This will also fill compiler.select, klass_info,
     90 # and annotations.
---> 91 results = compiler.execute_sql(
     92     chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
     93 )
     94 select, klass_info, annotation_col_map = (
     95     compiler.select,
     96     compiler.klass_info,
     97     compiler.annotation_col_map,
     98 )
     99 model_cls = klass_info["model"]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/sql/compiler.py:1562, in SQLCompiler.execute_sql(self, result_type, chunked_fetch, chunk_size)
   1560     cursor = self.connection.cursor()
   1561 try:
-> 1562     cursor.execute(sql, params)
   1563 except Exception:
   1564     # Might fail for server-side cursors (e.g. connection closed)
   1565     cursor.close()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:102, in CursorDebugWrapper.execute(self, sql, params)
    100 def execute(self, sql, params=None):
    101     with self.debug_sql(sql, params, use_last_executed_query=True):
--> 102         return super().execute(sql, params)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:67, in CursorWrapper.execute(self, sql, params)
     66 def execute(self, sql, params=None):
---> 67     return self._execute_with_wrappers(
     68         sql, params, many=False, executor=self._execute
     69     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:80, in CursorWrapper._execute_with_wrappers(self, sql, params, many, executor)
     78 for wrapper in reversed(self.db.execute_wrappers):
     79     executor = functools.partial(wrapper, executor)
---> 80 return executor(sql, params, many, context)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:84, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     82 def _execute(self, sql, params, *ignored_wrapper_args):
     83     self.db.validate_no_broken_transaction()
---> 84     with self.db.wrap_database_errors:
     85         if params is None:
     86             # params default might be backend specific.
     87             return self.cursor.execute(sql)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py:91, in DatabaseErrorWrapper.__exit__(self, exc_type, exc_value, traceback)
     89 if dj_exc_type not in (DataError, IntegrityError):
     90     self.wrapper.errors_occurred = True
---> 91 raise dj_exc_value.with_traceback(traceback) from exc_value

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     87     return self.cursor.execute(sql)
     88 else:
---> 89     return self.cursor.execute(sql, params)

ProgrammingError: relation "catalog_category" does not exist
LINE 1: ...ry"."name", "catalog_category"."description" FROM "catalog_c...
                                                             ^


In [4]: Product.objects.all()
   ...:
Out[4]: ---------------------------------------------------------------------------
UndefinedTable                            Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     88 else:
---> 89     return self.cursor.execute(sql, params)

UndefinedTable: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/core/formatters.py:770, in PlainTextFormatter.__call__(self, obj)
    763 stream = StringIO()
    764 printer = pretty.RepresentationPrinter(stream, self.verbose,
    765     self.max_width, self.newline,
    766     max_seq_length=self.max_seq_length,
    767     singleton_pprinters=self.singleton_printers,
    768     type_pprinters=self.type_printers,
    769     deferred_pprinters=self.deferred_printers)
--> 770 printer.pretty(obj)
    771 printer.flush()
    772 return stream.getvalue()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/lib/pretty.py:411, in RepresentationPrinter.pretty(self, obj)
    400                         return meth(obj, self, cycle)
    401                 if (
    402                     cls is not object
    403                     # check if cls defines __repr__
   (...)    409                     and callable(_safe_getattr(cls, "__repr__", None))
    410                 ):
--> 411                     return _repr_pprint(obj, self, cycle)
    413     return _default_pprint(obj, self, cycle)
    414 finally:

File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/lib/pretty.py:786, in _repr_pprint(obj, p, cycle)
    784 """A pprint that just redirects to the normal repr function."""
    785 # Find newlines and replace them with p.break_()
--> 786 output = repr(obj)
    787 lines = output.splitlines()
    788 with p.group():

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:374, in QuerySet.__repr__(self)
    373 def __repr__(self):
--> 374     data = list(self[: REPR_OUTPUT_SIZE + 1])
    375     if len(data) > REPR_OUTPUT_SIZE:
    376         data[-1] = "...(remaining elements truncated)..."

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:398, in QuerySet.__iter__(self)
    383 def __iter__(self):
    384     """
    385     The queryset iterator protocol uses three nested iterators in the
    386     default case:
   (...)    396            - Responsible for turning the rows into model objects.
    397     """
--> 398     self._fetch_all()
    399     return iter(self._result_cache)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:1881, in QuerySet._fetch_all(self)
   1879 def _fetch_all(self):
   1880     if self._result_cache is None:
-> 1881         self._result_cache = list(self._iterable_class(self))
   1882     if self._prefetch_related_lookups and not self._prefetch_done:
   1883         self._prefetch_related_objects()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:91, in ModelIterable.__iter__(self)
     88 compiler = queryset.query.get_compiler(using=db)
     89 # Execute the query. This will also fill compiler.select, klass_info,
     90 # and annotations.
---> 91 results = compiler.execute_sql(
     92     chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
     93 )
     94 select, klass_info, annotation_col_map = (
     95     compiler.select,
     96     compiler.klass_info,
     97     compiler.annotation_col_map,
     98 )
     99 model_cls = klass_info["model"]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/sql/compiler.py:1562, in SQLCompiler.execute_sql(self, result_type, chunked_fetch, chunk_size)
   1560     cursor = self.connection.cursor()
   1561 try:
-> 1562     cursor.execute(sql, params)
   1563 except Exception:
   1564     # Might fail for server-side cursors (e.g. connection closed)
   1565     cursor.close()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:102, in CursorDebugWrapper.execute(self, sql, params)
    100 def execute(self, sql, params=None):
    101     with self.debug_sql(sql, params, use_last_executed_query=True):
--> 102         return super().execute(sql, params)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:67, in CursorWrapper.execute(self, sql, params)
     66 def execute(self, sql, params=None):
---> 67     return self._execute_with_wrappers(
     68         sql, params, many=False, executor=self._execute
     69     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:80, in CursorWrapper._execute_with_wrappers(self, sql, params, many, executor)
     78 for wrapper in reversed(self.db.execute_wrappers):
     79     executor = functools.partial(wrapper, executor)
---> 80 return executor(sql, params, many, context)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:84, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     82 def _execute(self, sql, params, *ignored_wrapper_args):
     83     self.db.validate_no_broken_transaction()
---> 84     with self.db.wrap_database_errors:
     85         if params is None:
     86             # params default might be backend specific.
     87             return self.cursor.execute(sql)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py:91, in DatabaseErrorWrapper.__exit__(self, exc_type, exc_value, traceback)
     89 if dj_exc_type not in (DataError, IntegrityError):
     90     self.wrapper.errors_occurred = True
---> 91 raise dj_exc_value.with_traceback(traceback) from exc_value

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     87     return self.cursor.execute(sql)
     88 else:
---> 89     return self.cursor.execute(sql, params)

ProgrammingError: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


In [5]: Product.objects.filter(category__name="Электроника")
Out[5]: ---------------------------------------------------------------------------
UndefinedTable                            Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     88 else:
---> 89     return self.cursor.execute(sql, params)

UndefinedTable: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/core/formatters.py:770, in PlainTextFormatter.__call__(self, obj)
    763 stream = StringIO()
    764 printer = pretty.RepresentationPrinter(stream, self.verbose,
    765     self.max_width, self.newline,
    766     max_seq_length=self.max_seq_length,
    767     singleton_pprinters=self.singleton_printers,
    768     type_pprinters=self.type_printers,
    769     deferred_pprinters=self.deferred_printers)
--> 770 printer.pretty(obj)
    771 printer.flush()
    772 return stream.getvalue()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/lib/pretty.py:411, in RepresentationPrinter.pretty(self, obj)
    400                         return meth(obj, self, cycle)
    401                 if (
    402                     cls is not object
    403                     # check if cls defines __repr__
   (...)    409                     and callable(_safe_getattr(cls, "__repr__", None))
    410                 ):
--> 411                     return _repr_pprint(obj, self, cycle)
    413     return _default_pprint(obj, self, cycle)
    414 finally:

File ~/Py/django_store/.venv/lib/python3.12/site-packages/IPython/lib/pretty.py:786, in _repr_pprint(obj, p, cycle)
    784 """A pprint that just redirects to the normal repr function."""
    785 # Find newlines and replace them with p.break_()
--> 786 output = repr(obj)
    787 lines = output.splitlines()
    788 with p.group():

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:374, in QuerySet.__repr__(self)
    373 def __repr__(self):
--> 374     data = list(self[: REPR_OUTPUT_SIZE + 1])
    375     if len(data) > REPR_OUTPUT_SIZE:
    376         data[-1] = "...(remaining elements truncated)..."

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:398, in QuerySet.__iter__(self)
    383 def __iter__(self):
    384     """
    385     The queryset iterator protocol uses three nested iterators in the
    386     default case:
   (...)    396            - Responsible for turning the rows into model objects.
    397     """
--> 398     self._fetch_all()
    399     return iter(self._result_cache)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:1881, in QuerySet._fetch_all(self)
   1879 def _fetch_all(self):
   1880     if self._result_cache is None:
-> 1881         self._result_cache = list(self._iterable_class(self))
   1882     if self._prefetch_related_lookups and not self._prefetch_done:
   1883         self._prefetch_related_objects()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:91, in ModelIterable.__iter__(self)
     88 compiler = queryset.query.get_compiler(using=db)
     89 # Execute the query. This will also fill compiler.select, klass_info,
     90 # and annotations.
---> 91 results = compiler.execute_sql(
     92     chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
     93 )
     94 select, klass_info, annotation_col_map = (
     95     compiler.select,
     96     compiler.klass_info,
     97     compiler.annotation_col_map,
     98 )
     99 model_cls = klass_info["model"]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/sql/compiler.py:1562, in SQLCompiler.execute_sql(self, result_type, chunked_fetch, chunk_size)
   1560     cursor = self.connection.cursor()
   1561 try:
-> 1562     cursor.execute(sql, params)
   1563 except Exception:
   1564     # Might fail for server-side cursors (e.g. connection closed)
   1565     cursor.close()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:102, in CursorDebugWrapper.execute(self, sql, params)
    100 def execute(self, sql, params=None):
    101     with self.debug_sql(sql, params, use_last_executed_query=True):
--> 102         return super().execute(sql, params)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:67, in CursorWrapper.execute(self, sql, params)
     66 def execute(self, sql, params=None):
---> 67     return self._execute_with_wrappers(
     68         sql, params, many=False, executor=self._execute
     69     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:80, in CursorWrapper._execute_with_wrappers(self, sql, params, many, executor)
     78 for wrapper in reversed(self.db.execute_wrappers):
     79     executor = functools.partial(wrapper, executor)
---> 80 return executor(sql, params, many, context)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:84, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     82 def _execute(self, sql, params, *ignored_wrapper_args):
     83     self.db.validate_no_broken_transaction()
---> 84     with self.db.wrap_database_errors:
     85         if params is None:
     86             # params default might be backend specific.
     87             return self.cursor.execute(sql)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py:91, in DatabaseErrorWrapper.__exit__(self, exc_type, exc_value, traceback)
     89 if dj_exc_type not in (DataError, IntegrityError):
     90     self.wrapper.errors_occurred = True
---> 91 raise dj_exc_value.with_traceback(traceback) from exc_value

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     87     return self.cursor.execute(sql)
     88 else:
---> 89     return self.cursor.execute(sql, params)

ProgrammingError: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


In [6]: phone = Product.objects.get(name="Смартфон")
   ...: phone.price = 25999.99
   ...: phone.save()
   ...: Product.objects.get(name="Смартфон").price
---------------------------------------------------------------------------
UndefinedTable                            Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     88 else:
---> 89     return self.cursor.execute(sql, params)

UndefinedTable: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
Cell In[6], line 1
----> 1 phone = Product.objects.get(name="Смартфон")
      2 phone.price = 25999.99
      3 phone.save()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/manager.py:87, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
     85 @wraps(method)
     86 def manager_method(self, *args, **kwargs):
---> 87     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:633, in QuerySet.get(self, *args, **kwargs)
    631     limit = MAX_GET_RESULTS
    632     clone.query.set_limits(high=limit)
--> 633 num = len(clone)
    634 if num == 1:
    635     return clone._result_cache[0]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:380, in QuerySet.__len__(self)
    379 def __len__(self):
--> 380     self._fetch_all()
    381     return len(self._result_cache)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:1881, in QuerySet._fetch_all(self)
   1879 def _fetch_all(self):
   1880     if self._result_cache is None:
-> 1881         self._result_cache = list(self._iterable_class(self))
   1882     if self._prefetch_related_lookups and not self._prefetch_done:
   1883         self._prefetch_related_objects()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:91, in ModelIterable.__iter__(self)
     88 compiler = queryset.query.get_compiler(using=db)
     89 # Execute the query. This will also fill compiler.select, klass_info,
     90 # and annotations.
---> 91 results = compiler.execute_sql(
     92     chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
     93 )
     94 select, klass_info, annotation_col_map = (
     95     compiler.select,
     96     compiler.klass_info,
     97     compiler.annotation_col_map,
     98 )
     99 model_cls = klass_info["model"]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/sql/compiler.py:1562, in SQLCompiler.execute_sql(self, result_type, chunked_fetch, chunk_size)
   1560     cursor = self.connection.cursor()
   1561 try:
-> 1562     cursor.execute(sql, params)
   1563 except Exception:
   1564     # Might fail for server-side cursors (e.g. connection closed)
   1565     cursor.close()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:102, in CursorDebugWrapper.execute(self, sql, params)
    100 def execute(self, sql, params=None):
    101     with self.debug_sql(sql, params, use_last_executed_query=True):
--> 102         return super().execute(sql, params)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:67, in CursorWrapper.execute(self, sql, params)
     66 def execute(self, sql, params=None):
---> 67     return self._execute_with_wrappers(
     68         sql, params, many=False, executor=self._execute
     69     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:80, in CursorWrapper._execute_with_wrappers(self, sql, params, many, executor)
     78 for wrapper in reversed(self.db.execute_wrappers):
     79     executor = functools.partial(wrapper, executor)
---> 80 return executor(sql, params, many, context)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:84, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     82 def _execute(self, sql, params, *ignored_wrapper_args):
     83     self.db.validate_no_broken_transaction()
---> 84     with self.db.wrap_database_errors:
     85         if params is None:
     86             # params default might be backend specific.
     87             return self.cursor.execute(sql)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py:91, in DatabaseErrorWrapper.__exit__(self, exc_type, exc_value, traceback)
     89 if dj_exc_type not in (DataError, IntegrityError):
     90     self.wrapper.errors_occurred = True
---> 91 raise dj_exc_value.with_traceback(traceback) from exc_value

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     87     return self.cursor.execute(sql)
     88 else:
---> 89     return self.cursor.execute(sql, params)

ProgrammingError: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


In [7]: Product.objects.get(name="Яблоки").delete()
   ...: Product.objects.all().delete()
---------------------------------------------------------------------------
UndefinedTable                            Traceback (most recent call last)
File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     88 else:
---> 89     return self.cursor.execute(sql, params)

UndefinedTable: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
Cell In[7], line 1
----> 1 Product.objects.get(name="Яблоки").delete()
      2 Product.objects.all()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/manager.py:87, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
     85 @wraps(method)
     86 def manager_method(self, *args, **kwargs):
---> 87     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:633, in QuerySet.get(self, *args, **kwargs)
    631     limit = MAX_GET_RESULTS
    632     clone.query.set_limits(high=limit)
--> 633 num = len(clone)
    634 if num == 1:
    635     return clone._result_cache[0]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:380, in QuerySet.__len__(self)
    379 def __len__(self):
--> 380     self._fetch_all()
    381     return len(self._result_cache)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:1881, in QuerySet._fetch_all(self)
   1879 def _fetch_all(self):
   1880     if self._result_cache is None:
-> 1881         self._result_cache = list(self._iterable_class(self))
   1882     if self._prefetch_related_lookups and not self._prefetch_done:
   1883         self._prefetch_related_objects()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/query.py:91, in ModelIterable.__iter__(self)
     88 compiler = queryset.query.get_compiler(using=db)
     89 # Execute the query. This will also fill compiler.select, klass_info,
     90 # and annotations.
---> 91 results = compiler.execute_sql(
     92     chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
     93 )
     94 select, klass_info, annotation_col_map = (
     95     compiler.select,
     96     compiler.klass_info,
     97     compiler.annotation_col_map,
     98 )
     99 model_cls = klass_info["model"]

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/models/sql/compiler.py:1562, in SQLCompiler.execute_sql(self, result_type, chunked_fetch, chunk_size)
   1560     cursor = self.connection.cursor()
   1561 try:
-> 1562     cursor.execute(sql, params)
   1563 except Exception:
   1564     # Might fail for server-side cursors (e.g. connection closed)
   1565     cursor.close()

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:102, in CursorDebugWrapper.execute(self, sql, params)
    100 def execute(self, sql, params=None):
    101     with self.debug_sql(sql, params, use_last_executed_query=True):
--> 102         return super().execute(sql, params)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:67, in CursorWrapper.execute(self, sql, params)
     66 def execute(self, sql, params=None):
---> 67     return self._execute_with_wrappers(
     68         sql, params, many=False, executor=self._execute
     69     )

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:80, in CursorWrapper._execute_with_wrappers(self, sql, params, many, executor)
     78 for wrapper in reversed(self.db.execute_wrappers):
     79     executor = functools.partial(wrapper, executor)
---> 80 return executor(sql, params, many, context)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:84, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     82 def _execute(self, sql, params, *ignored_wrapper_args):
     83     self.db.validate_no_broken_transaction()
---> 84     with self.db.wrap_database_errors:
     85         if params is None:
     86             # params default might be backend specific.
     87             return self.cursor.execute(sql)

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py:91, in DatabaseErrorWrapper.__exit__(self, exc_type, exc_value, traceback)
     89 if dj_exc_type not in (DataError, IntegrityError):
     90     self.wrapper.errors_occurred = True
---> 91 raise dj_exc_value.with_traceback(traceback) from exc_value

File ~/Py/django_store/.venv/lib/python3.12/site-packages/django/db/backends/utils.py:89, in CursorWrapper._execute(self, sql, params, *ignored_wrapper_args)
     87     return self.cursor.execute(sql)
     88 else:
---> 89     return self.cursor.execute(sql, params)

ProgrammingError: relation "catalog_product" does not exist
LINE 1: ..."created_at", "catalog_product"."updated_at" FROM "catalog_p...
                                                             ^


In [8]:
