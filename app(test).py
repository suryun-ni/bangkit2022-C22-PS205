from flask import render_template
from flask import Flask, jsonify
app = Flask(__name__)

namaSiswa = [
    { "id":0,
      "nama": "tengku",
      "alamat": "konoha"
    },
    { "id":1,
      "nama": "sasuke",
      "alamat": "konoha"
    },
    { "id":2,
      "nama": "budi tarmiji",
      "alamat": "konoha"
    }
  ]


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/mahasiswa", methods=['GET'])
def get():
    return jsonify({'Mahasiswa':namaSiswa})

@app.route("/mahasiswa/<int:id>",methods=['GET'])
def get_id(id):
    return jsonify({'id':namaSiswa[id]})

@app.route("/mahasiswa", methods=['POST'])
def post():
    addSiswa = {
      "id":3,
      "nama": "Aselole",
      "alamat": "Kirigakure"
    }
    namaSiswa.append(addSiswa)
    return jsonify({'Created':namaSiswa})

@app.route("/mahasiswa/<int:id>",methods=['PUT'])
def update_id(id):
    namaSiswa[id]['nama'] = "jancok"
    return jsonify({'updated':namaSiswa[id]})    

@app.route("/mahasiswa/<int:id>",methods=['DELETE'])
def delete_id(id):
    namaSiswa.remove(namaSiswa[id])
    return jsonify({'deleted':True})

if __name__ == "__main__":
    app.run(debug=True)