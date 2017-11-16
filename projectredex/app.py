import os

from flask import Flask, request
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)


class So(db.Model):
    id_so = db.Column(db.Integer, primary_key=True)
    kernel = db.Column(db.String(100), unique=True)
    release = db.Column(db.String(100), unique=True)
    nodename = db.Column(db.String(100), unique=True)
    kernelv = db.Column(db.String(100), unique=True)
    machine = db.Column(db.String(100), unique=True)
    processor = db.Column(db.String(100), unique=True)
    so = db.Column(db.String(100), unique=True)
    hardware = db.Column(db.String(100), unique=True)

    def __init__(self, kernel, release, nodename, kernelv, machine, processor, so, hardware):
        self.kernel = kernel
        self.release = release
        self.nodename = nodename
        self.kernelv = kernelv
        self.machine = machine
        self.processor = processor
        self.so = so
        self.hardware = hardware

    def __repr__(self):
        return "<So(id_so='%d', kernel='%s', release='%s', nodename='%s', kernelv='%s', machine='%s', processor='%s', so='%s', hardware='%s')>" % (
        self.id_so, self.kernel, self.release, self.nodename, self.kernelv, self.machine, self.processor, self.so, self.hardware)

class Usuario(db.Model):
    id_U = db.Column(db.Integer, primary_key=True)
    Usuarios = db.Column(db.String(100), unique=True)
    UsuarioActivo = db.Column(db.String(100), unique=True)

    def __init__(self, Usuarios, UsuarioActivo):
        self.Usuarios = Usuarios
        self.UsuarioActivo = UsuarioActivo

    def __repr__(self):
        return "<Usuario(id_U='%d', Usuarios='%s', UsuarioActivo='%s')>" % (
        self.id_U, self.Usuarios, self.UsuarioActivo)

class Cpu(db.Model):
    id_Cpu = db.Column(db.Integer, primary_key=True)
    us = db.Column(db.String(100), unique=True)
    sy = db.Column(db.String(100), unique=True)
    idnum = db.Column(db.String(100), unique=True)
    wa = db.Column(db.String(100), unique=True)
    st = db.Column(db.String(100), unique=True)

    def __init__(self, us, sy, idnum, wa, st):
        self.us = us
        self.sy = sy
        self.idnum = idnum
        self.wa = wa
        self.st = st

    def __repr__(self):
        return "<Cpu(id_Cpu='%d', us='%s', sy='%s', idnum='%s', wa='%s', st='%s')>" % (
        self.id_Cpu, self.us, self.sy, self.idnum, self.wa, self.st)

class Memory(db.Model):
    id_Memory = db.Column(db.Integer, primary_key=True)
    swpd = db.Column(db.String(100), unique=True)
    free = db.Column(db.String(100), unique=True)
    buff = db.Column(db.String(100), unique=True)
    cache = db.Column(db.String(100), unique=True)

    def __init__(self, swpd, free, buff, cache):
        self.swpd = swpd
        self.free = free
        self.buff = buff
        self.cache = cache

    def __repr__(self):
        return "<Memory(id_Memory='%d', swpd='%s', free='%s', buff='%s', cache='%s')>" % (
        self.id_Memory, self.swpd, self.free, self.buff, self.cache)

class Swap(db.Model):
    id_Swap = db.Column(db.Integer, primary_key=True)
    si = db.Column(db.String(100), unique=True)
    so = db.Column(db.String(100), unique=True)

    def __init__(self, si, so):
        self.si = si
        self.so = so

    def __repr__(self):
        return "<Swap(id_Swap='%d', si='%s', so='%s')>" % (
        self.id_Swap, self.si, self.so)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/so/show')
def soShow():
    so = So.query.filter(So.id_so == 1).one()
    return render_template('so.html',so = so)

@app.route('/so/update/<string:kernel>/<string:release>/<string:nodename>/<string:kernelv>/<string:machine>/<string:processor>/<string:vso>/<string:hardware>')
def soUpdate(kernel,release,nodename,kernelv,machine,processor,vso,hardware):
    so = So.query.filter(So.id_so == 1).one()
    so.kernel = kernel
    so.release = release
    so.nodename = nodename
    so.kernelv = kernelv
    so.machine = machine
    so.processor = processor
    so.so = vso
    so.hardware = hardware
    db.session.commit()
    return "SO MODIFICADO"

@app.route('/so/update', methods=['POST'])
def soJSONUpdate():
    if request.headers['Content-Type'] == 'application/json':
        if request.json:
            sodata = request.json
            so = So.query.filter(So.id_so == 1).one()
            so.kernel = sodata.get("kernel")
            so.release = sodata.get("release")
            so.nodename = sodata.get("node_name")
            so.kernelv = sodata.get("kernel_version")
            so.machine = sodata.get("machine")
            so.processor = sodata.get("processor")
            so.so = sodata.get("operating_system")
            so.hardware = sodata.get("hardware_platform")
            db.session.commit()
            return "SO MODIFICADO" 
        else:
            return "NO hay Datos del SO"
    else:
        return "Error 415 (Tipo de medio no soportado)"

@app.route('/user/show')
def userShow():
    user = Usuario.query.filter(Usuario.id_U == 1).one()
    return render_template('user.html',user = user)
    
@app.route('/user/update/<string:Usuarios>/<string:UsuarioActivo>')
def userUpdate(Usuarios,UsuarioActivo):
    user = Usuario.query.filter(Usuario.id_U == 1).one()
    user.Usuarios = Usuarios
    user.UsuarioActivo = UsuarioActivo
    db.session.commit()
    return "USUARIO MODIFICADO"
	
@app.route('/user/update', methods=['POST'])
def userJSONUpdate():
    if request.headers['Content-Type'] == 'application/json':
        if request.json:
            userdata = request.json
            user = Usuario.query.filter(Usuario.id_U == 1).one()
            user.Usuarios = userdata.get("users")
            user.UsuarioActivo = userdata.get("loggedin")
            db.session.commit()
            return "USUARIO MODIFICADO" 
        else:
            return "NO hay Datos del Usuario"
    else:
        return "Error 415 (Tipo de medio no soportado)"

@app.route('/mem/show')
def memoryShow():
    memory = Memory.query.filter(Memory.id_Memory == 1).one()
    return render_template('mem.html',memory = memory)
    
@app.route('/mem/update/<string:swpd>/<string:free>/<string:buff>/<string:cache>')
def memoryUpdate(swpd,free,buff,cache):
	memory = Memory.query.filter(Memory.id_Memory == 1).one()
	memory.swpd = swpd
	memory.free = free
	memory.buff = buff
	memory.cache = cache
	db.session.commit()
	return "MEMORIA MODIFICADA"

@app.route('/mem/update', methods=['POST'])
def memoryJSONUpdate():
    if request.headers['Content-Type'] == 'application/json':
        if request.json:
            memorydata = request.json
            memory = Memory.query.filter(Memory.id_Memory == 1).one()
            memory.swpd = memorydata.get("swpd")
            memory.free = memorydata.get("free")
            memory.buff = memorydata.get("buff")
            memory.cache = memorydata.get("cache")
            db.session.commit()
            return "MEMORIA MODIFICADA" 
        else:
            return "NO hay Datos de la Memoria"
    else:
        return "Error 415 (Tipo de medio no soportado)"

@app.route('/swap/show')
def swapShow():
    swap = Swap.query.filter(Swap.id_Swap == 1).one()
    return render_template('swap.html',swap = swap)

@app.route('/swap/update/<string:si>/<string:so>')
def swapUpdate(si,so):
	swap = Swap.query.filter(Swap.id_Swap == 1).one()
	swap.si = si
	swap.so = so
	db.session.commit()
	return "SWAP MODIFICADA"

@app.route('/swap/update', methods=['POST'])
def swapJSONUpdate():
    if request.headers['Content-Type'] == 'application/json':
        if request.json:
            swapdata = request.json
            swap = Swap.query.filter(Swap.id_Swap == 1).one()
            swap.si = swapdata.get("si")
            swap.so = swapdata.get("so")         
            db.session.commit()
            return "SWAP MODIFICADA" 
        else:
            return "NO hay Datos del SWAP"
    else:
        return "Error 415 (Tipo de medio no soportado)"

@app.route('/cpu/show')
def cpuShow():
    cpu = Cpu.query.filter(Cpu.id_Cpu == 1).one()
    return render_template('cpu.html',cpu = cpu)

@app.route('/cpu/update/<string:us>/<string:sy>/<string:idnum>/<string:wa>/<string:st>')
def cpuUpdate(us,sy,idC,wa,st):
	cpu = Cpu.query.filter(Cpu.id_Cpu == 1).one()
	cpu.us = us
	cpu.sy = sy
	cpu.idnum = idnum
	cpu.wa = wa
	cpu.st = st
	db.session.commit()
	return "CPU MODIFICADO"

@app.route('/cpu/update', methods=['POST'])
def cpuJSONUpdate():
    if request.headers['Content-Type'] == 'application/json':
        if request.json:
            cpudata = request.json
            cpu = Cpu.query.filter(Cpu.id_Cpu == 1).one()
            cpu.us = cpudata.get("us")
            cpu.sy = cpudata.get("sy")
            cpu.idnum = cpudata.get("id")
            cpu.wa = cpudata.get("wa")
            cpu.st = cpudata.get("st")
            db.session.commit()
            return "CPU MODIFICADO" 
        else:
            return "NO hay Datos del CPU"
    else:
        return "Error 415 (Tipo de medio no soportado)"
    

@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
    
