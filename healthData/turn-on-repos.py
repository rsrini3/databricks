# Databricks notebook source
# MAGIC %md
# MAGIC Running this notebook will ensure the Repos feature is enabled. It is idempotent and can be re-run safely.

# COMMAND ----------

# MAGIC %pip install databricks-sdk --upgrade

# COMMAND ----------

dbutils.library.restartPython()

from databricks.sdk.core import ApiClient

client = ApiClient()

# COMMAND ----------

# MAGIC %md
# MAGIC First we check what the current value is. `false` means the feature is disabled. None or `true` means it is enabled.

# COMMAND ----------

client.do("GET", "/api/2.0/workspace-conf", {"keys": "enableProjectTypeInWorkspace"})

# COMMAND ----------

# MAGIC %md
# MAGIC Then we explicitly turn it on

# COMMAND ----------

client.do("PATCH", "/api/2.0/workspace-conf", body={"enableProjectTypeInWorkspace": "true"}, headers={"Content-Type": "application/json"})

# COMMAND ----------

# MAGIC %md
# MAGIC And now we check that the config value is set to `true`. To disable a repo, check that `enableProjectTypeInWorkspace` is true and set it to `false`.

# COMMAND ----------

client.do("GET", "/api/2.0/workspace-conf", {"keys": "enableProjectTypeInWorkspace"})
