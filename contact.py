from flask import Flask, request
from flask import render_template

app = Flask(__name__)

contacts= {
    
    'Nichola': {'name': 'Nichola', 'phone': '0983944948', 'email': 'wolfe.nichola@gmail.com'},
    'Katie': {'name': 'Katie', 'phone': '0233944948', 'email': 'katie@code.com'},
    'Richard':  {'name': 'Richard', 'phone': '0245944948', 'email': 'richard@codeboss.com'}, 
    }

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/contacts", methods=['GET', 'POST'])
def people():
    if request.method == "POST":
        name = request.form.get('name')
        phone = request.form.get('phone')
        
        contacts.update({
            name:{'name': name, 'phone': phone}})
        
        
    
    return render_template("contacts.html", contacts=contacts.values())

@app.route("/delete", methods=["POST"])
def delete_contact():
    name_to_delete = request.form.get('contact_to_delete')
    
    del(contacts[name_to_delete])
    
    return render_template("contacts.html", contacts=contacts.values())




    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)