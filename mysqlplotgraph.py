import pandas
import matplotlib.pyplot as plt
from dbpackage import ConnectMySQL as con

# Connect db
connection = con.connectdb()

# Read data
df = pandas.read_sql(
    "SELECT ship_name, freight FROM orders "
    "WHERE ship_country='USA'", connection
)

# Plot graph
df.plot(kind="line", x="ship_name", y="freight")
plt.show()
