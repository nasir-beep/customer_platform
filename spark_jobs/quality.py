from pyspark.sql.functions import col

def remove_null_ids(df, column_name):
    """
    Remove rows where the ID column is null.
    """
    return df.filter(col(column_name).isNotNull())


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    return df.dropDuplicates()


def count_rows(df):
    """
    Return the number of rows.
    """
    return df.count()

from pyspark.sql.functions import col

def count_nulls(df, column_name):
    return df.filter(col(column_name).isNull()).count()


def count_duplicates(df):
    return df.count() - df.dropDuplicates().count()