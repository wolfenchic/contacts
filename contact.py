from flask import Flask, request, redirect, url_for
from flask import render_template



app = Flask(__name__)

contacts= {
    
    1: {'id':1, 'name': 'Nichola', 'phone': '0983944948', 'email': 'wolfe.nichola@gmail.com'},
    2: {'id':2,'name': 'Katie', 'phone': '0233944948', 'email': 'katie@code.com'},
    3:  {'id':3, 'name': 'Richard', 'phone': '0245944948', 'email': 'richard@codeboss.com'}, 
    }
next_id = 4
    
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/contacts", methods=['GET', 'POST'])
def people():
    global next_id
    if request.method == "POST":
        name = request.form.get('name')
        phone = request.form.get('phone')
        
        contacts.update({next_id:{'id': next_id, 'name': name, 'phone': phone}})
        next_id += 1
        
    return render_template("contacts.html", contacts=contacts.values())
    

@app.route("/delete", methods=["POST"])
def delete_id():
    id_to_delete =int(request.form.get('id_to_delete'))
    del(contacts[id_to_delete])
    #return render_template("contacts.html", contacts=contacts.values())
    return redirect(url_for("people"))
    #return render_template("contacts.html", contacts=contacts.values())
    #return redirect(url_for("contacts.html", contacts=contacts.id))

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    
    