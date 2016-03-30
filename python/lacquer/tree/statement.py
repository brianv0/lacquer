from .node import Node


class Statement(Node):
    def __init__(self, line=None, pos=None):
        super(Statement, self).__init__(line, pos)

    def accept(self, visitor, context):
        visitor.visit_statement(self, context)

    
class Delete(Statement):
    def __init__(self, line=None, pos=None, table=None, where=None):
        super(Delete, self).__init__(line, pos)
        self.table = table
        self.where = where

    def accept(self, visitor, context):
        visitor.visit_delete(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("table", table.getName()).add("where", where).toString();
        """
        pass

    
class Query(Statement):
    def __init__(self, line=None, pos=None, with_=None, query_body=None, order_by=None, limit=None):
        super(Query, self).__init__(line, pos)
        self.with_ = with_
        self.query_body = query_body
        self.order_by = order_by
        self.limit = limit
        # self.approximate = approximate

    def accept(self, visitor, context):
        visitor.visit_query(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("with", with.orNull())
            .add("queryBody", queryBody).add("orderBy", orderBy).add("limit", limit.orNull())
            #.add("approximate", approximate.orNull()).#omitNullValues().toString();
        """
        pass

    
class Insert(Statement):
    def __init__(self, line=None, pos=None, target=None, query=None, columns=None):
        super(Insert, self).__init__(line, pos)
        self.target = target
        self.query = query
        self.columns = columns

    def accept(self, visitor, context):
        visitor.visit_insert(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).
            add("target", target).add("columns", columns).add("query", query).toString();
        """
        pass

    
class ShowColumns(Statement):
    def __init__(self, line=None, pos=None, table=None):
        super(ShowColumns, self).__init__(line, pos)
        self.table = table

    def accept(self, visitor, context):
        visitor.visit_show_columns(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("table", table).toString();
        """
        pass


class RenameTable(Statement):
    def __init__(self, line=None, pos=None, source=None, target=None):
        super(RenameTable, self).__init__(line, pos)
        self.source = source
        self.target = target

    def accept(self, visitor, context):
        visitor.visit_rename_table(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("source", source).add("target", target).toString();
        """
        pass


class CreateTable(Statement):
    def __init__(self, line=None, pos=None, name=None, elements=None, not_exists=None, properties=None):
        super(CreateTable, self).__init__(line, pos)
        self.name = name
        self.elements = elements
        self.not_exists = not_exists
        self.properties = properties

    def is_not_exists(self):
        pass

    def accept(self, visitor, context):
        visitor.visit_create_table(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("name", name)
            .add("elements", elements).add("notExists", notExists).add("properties", properties).toString();
        """
        pass

    
class DropView(Statement):
    def __init__(self, line=None, pos=None, name=None, exists=None):
        super(DropView, self).__init__(line, pos)
        self.name = name
        self.exists = exists

    def is_exists(self):
        pass

    def accept(self, visitor, context):
        visitor.visit_drop_view(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("name", name).add("exists", exists).toString();
        """
        pass


class Rollback(Statement):
    def __init__(self, line=None, pos=None):
        super(Rollback, self).__init__(line, pos)

    def accept(self, visitor, context):
        visitor.visit_rollback(self, context)

    def __str__(self):
        """
        return "ROLLBACK";
        """
        pass


class ShowSession(Statement):
    def __init__(self, line=None, pos=None):
        super(ShowSession, self).__init__(line, pos)

    def accept(self, visitor, context):
        visitor.visit_show_session(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).toString();
        """
        pass


class Call(Statement):
    def __init__(self, line=None, pos=None, name=None, arguments=None):
        super(Call, self).__init__(line, pos)
        self.name = name
        self.arguments = arguments

    def accept(self, visitor, context):
        visitor.visit_call(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("name", name).add("arguments", arguments).toString();
        """
        pass


class Use(Statement):
    def __init__(self, line=None, pos=None, catalog=None, schema=None):
        super(Use, self).__init__(line, pos)
        self.catalog = catalog
        self.schema = schema

    def accept(self, visitor, context):
        visitor.visit_use(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).toString();
        """
        pass

    
class ShowPartitions(Statement):
    def __init__(self, line=None, pos=None, table=None, where=None, order_by=None, limit=None):
        super(ShowPartitions, self).__init__(line, pos)
        self.table = table
        self.where = where
        self.order_by = order_by
        self.limit = limit

    def accept(self, visitor, context):
        visitor.visit_show_partitions(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this)
            .add("table", table).add("where", where).add("orderBy", orderBy).add("limit", limit).toString();
        """
        pass


class ShowCatalogs(Statement):
    def __init__(self, line=None, pos=None):
        super(ShowCatalogs, self).__init__(line, pos)

    def accept(self, visitor, context):
        visitor.visit_show_catalogs(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).toString();
        """
        pass


class StartTransaction(Statement):
    def __init__(self, line=None, pos=None, transaction_modes=None):
        super(StartTransaction, self).__init__(line, pos)
        self.transaction_modes = transaction_modes

    def accept(self, visitor, context):
        visitor.visit_start_transaction(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("transactionModes", transactionModes).toString();
        """
        pass


class CreateView(Statement):
    def __init__(self, line=None, pos=None, name=None, query=None, replace=None):
        super(CreateView, self).__init__(line, pos)
        self.name = name
        self.query = query
        self.replace = replace

    def is_replace(self):
        pass

    def accept(self, visitor, context):
        visitor.visit_create_view(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this)
            .add("name", name).add("query", query).add("replace", replace).toString();
        """
        pass


class SetSession(Statement):
    def __init__(self, line=None, pos=None, name=None, value=None):
        super(SetSession, self).__init__(line, pos)
        self.name = name
        self.value = value

    def accept(self, visitor, context):
        visitor.visit_set_session(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("name", name).add("value", value).toString();
        """
        pass


class CreateTableAsSelect(Statement):
    def __init__(self, line=None, pos=None, name=None, query=None, properties=None, with_data=None):
        super(CreateTableAsSelect, self).__init__(line, pos)
        self.name = name
        self.query = query
        self.properties = properties
        self.with_data = with_data

    def is_with_data(self):
        pass

    def accept(self, visitor, context):
        visitor.visit_create_table_as_select(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).
             add("name", name).add("query", query).add("properties", properties).add("withData", withData).toString();
        """
        pass


class RenameColumn(Statement):
    def __init__(self, line=None, pos=None, table=None, source=None, target=None):
        super(RenameColumn, self).__init__(line, pos)
        self.table = table
        self.source = source
        self.target = target

    def accept(self, visitor, context):
        visitor.visit_rename_column(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).
            add("table", table).add("source", source).add("target", target).toString();
        """
        pass


class ResetSession(Statement):
    def __init__(self, line=None, pos=None, name=None):
        super(ResetSession, self).__init__(line, pos)
        self.name = name

    def accept(self, visitor, context):
        visitor.visit_reset_session(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("name", name).toString();
        """
        pass


class ShowSchemas(Statement):
    def __init__(self, line=None, pos=None, catalog=None):
        super(ShowSchemas, self).__init__(line, pos)
        self.catalog = catalog

    def accept(self, visitor, context):
        visitor.visit_show_schemas(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).toString();
        """
        pass


class DropTable(Statement):
    def __init__(self, line=None, pos=None, table_name=None, exists=None):
        super(DropTable, self).__init__(line, pos)
        self.table_name = table_name
        self.exists = exists

    def is_exists(self):
        pass

    def accept(self, visitor, context):
        visitor.visit_drop_table(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("tableName", tableName).add("exists", exists).toString();
        """
        pass


class ShowTables(Statement):
    def __init__(self, line=None, pos=None, schema=None, like_pattern=None):
        super(ShowTables, self).__init__(line, pos)
        self.schema = schema
        self.like_pattern = like_pattern

    def accept(self, visitor, context):
        visitor.visit_show_tables(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("schema", schema).add("likePattern", likePattern).toString();
        """
        pass


class Explain(Statement):
    def __init__(self, line=None, pos=None, statement=None, options=None):
        super(Explain, self).__init__(line, pos)
        self.statement = statement
        self.options = options

    def accept(self, visitor, context):
        visitor.visit_explain(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("statement", statement).add("options", options).toString();
        """
        pass


class AddColumn(Statement):
    def __init__(self, line=None, pos=None, name=None, column=None):
        super(AddColumn, self).__init__(line, pos)
        self.name = name
        self.column = column

    def accept(self, visitor, context):
        visitor.visit_add_column(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).add("name", name).add("column", column).toString();
        """
        pass


class Commit(Statement):
    def __init__(self, line=None, pos=None):
        super(Commit, self).__init__(line, pos)

    def accept(self, visitor, context):
        visitor.visit_commit(self, context)

    def __str__(self):
        """
        return "COMMIT";
        """
        pass


class ShowFunctions(Statement):
    def __init__(self, line=None, pos=None):
        super(ShowFunctions, self).__init__(line, pos)

    def accept(self, visitor, context):
        visitor.visit_show_functions(self, context)

    def __str__(self):
        """
        return MoreObjects.toStringHelper(this).toString();
        """
        pass
