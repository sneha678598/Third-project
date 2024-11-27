from app import create_app, db

#from . import main


import os
print(db.engine.table_names())  # This will list all the table names in the database


print("Template folder path:", os.path.abspath('app/templates'))



app = create_app()

@app.before_request
def create_tables():
    db.create_all()  # Create all tables before handling the first request

if __name__ == "__main__":
    app.run(debug=True)