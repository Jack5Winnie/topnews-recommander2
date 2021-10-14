# 使用instance文件夾
#   要想加載定義在instance文件夾中的配置變量，你可以使用app.config.from_pyfile()。
#   如果在調用Flask()創建應用時設置了instance_relative_config=True，app.config.from_pyfile()將查看在instance文件夾的特殊文件。
#
#   app = Flask(__name__, instance_relative_config=True)
#   app.config.from_object('config')
#   app.config.from_pyfile('config.py')

# 現在，你可以在instance/config.py中定義變量，一如在config.py。
# 你也應該將instance文件夾加入到版本控制系統的忽略名單中。比如假設你用的是git，你需要在gitignore中新開一行，寫下instance/。

# 密鑰
#   instance文件夾的隱秘屬性使得它成為藏匿密鑰的好地方。你可以在放入應用的密鑰或第三方的API密鑰。
#   假如你的應用是開源的，或者將會是開源的，這會很重要。我們希望其他人去使用他們自己申請的密鑰。

# instance/config.py

API_KEY = "112c9b2a21544785ac573f0221cff7ed"   # NEWS_API_KEY
NEWS_API_KEY = "112c9b2a21544785ac573f0221cff7ed"   # NEWS_API_KEY
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
# STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
# SQLALCHEMY_DATABASE_URI= "postgresql://user:TWljaGHFgiBCYXJ0b3N6a2lld2ljeiEh@localhost/databasename"