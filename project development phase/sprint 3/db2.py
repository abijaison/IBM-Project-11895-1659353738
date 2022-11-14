import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;UID=kpp39792;PWD=TpVTHYT7aXlvLjVz;","","")
print("connection successfully")


sql="""CREATE TABLE login (
    Name varchar(255),
    Email varchar(255),
    Password varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)

sql="""CREATE TABLE Customerdetails (
    Name varchar(255),
    ShopName varchar(255),
    Location varchar(255),
    MobileNumber varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)


"""{% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, messages in messages %}
          <div class="alert alert-{{category}}" ></div>{{messages}}</div>
        {% endfor %}
  {% endif %}  
  {% endwith %} """