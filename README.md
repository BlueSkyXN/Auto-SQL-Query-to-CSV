# Auto-SQL-Query-to-CSV
辅助自动化操作，实现SQL查询转为CSV表

# 参考命令

E:\Downloads\Auto-SQL-Query-to-CSV.exe E:\Downloads\PySQL-Query.txt E:\Downloads\PySQL-Info.txt E:\Downloads\output.csv

## 警告

pandas\io\sql.py:832: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.

这个警告信息的意义是提醒开发者，pandas库在执行SQL查询时，使用的连接方式可能未经过全面的测试。警告信息建议使用SQLAlchemy库提供的连接方式，因为它是经过广泛测试和使用的。

警告本身并不会影响脚本的功能或导致错误。大多数情况下，pandas仍然可以正常使用DBAPI2连接执行SQL查询，并将结果返回为DataFrame对象。警告只是提醒你可能会遇到一些未知的问题，因为pandas库无法保证对所有DBAPI2连接的兼容性和稳定性。

如果你的脚本运行正常并且查询结果正确，那么这个警告本身并没有太大影响。然而，如果你遇到了与连接或执行SQL查询相关的问题，警告可能是一个线索，提示你使用SQLAlchemy连接方式来确保更好的兼容性和稳定性。

总结起来，警告信息只是提醒你使用SQLAlchemy连接方式来替代底层的DBAPI2连接，以获得更好的支持和兼容性。如果你的脚本运行正常，你可以选择忽略这个警告。但如果你遇到了问题，可以尝试使用SQLAlchemy连接方式来解决。
