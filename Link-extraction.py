import pandas as pd

# I use Regular Expression for this problem. We can detect patterns from strings and obtain them with ReGeX with desired expressions.

# Creating DataFrame with Device Type and Access Link
d = {"Device_Type" : ["AXO145", "TRU151", "ZOD231", "YRT326", "LWR245"],
     "Stats_Access_Link" : ["<url>https://xcd32112.smart_meter.com</url>",
                            "<url>https://tXh67.dia_meter.com</url>",
                            "<url>https://yT5495.smart_meter.com</url>",
                            "<url>https://ret323_TRu.crown.com</url>",
                            "<url>https://luwr3243.celcius.com</url>"]}
df = pd.DataFrame(data = d)


# Extracting links according to the detected pattern and Assigning to new column
df["Link"] = df.Stats_Access_Link.str.extract("<url>\w+\W+([\w\d.]+)</url>")
df.head()