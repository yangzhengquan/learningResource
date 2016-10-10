var express = require('express');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);

var sockets = {};

server.listen(8088);
app.use(express.static('static'))
    /*app.get('/', function (req, res) {
      res.sendfile(__dirname + '/index.html');
    });*/
app.get('/onlineLen', function(req, res) {
    res.send({ 'idLen': Object.keys(sockets).length });
});
app.get('/onlineIds', function(req, res) {
    var s = {};
    Object.keys(sockets).forEach(function(v, k) {
        s[v] = Object.keys(sockets[v]);
    });
    res.send(s);
});
app.get('/push', function(req, res) {

    var data = {
        k: req.query.k,
        from: req.query.from,
        to: req.query.to,
    }
    handlerMsg(data, 'socket', true);
    res.send('ok');
});

io.on('connection', function(socket) {
    //socket.emit('message', { k: 'hi client' });
    socket.on('message', function(data) {
        try {
            handlerMsg(data, socket);
        } catch (e) {
            console.log('error:')
            console.error(e);

        }

        socket.on('disconnect', function(e) {
            console.log('disconnect', socket.from, socket.id)
            var socketFrom = sockets[socket.from];
            delete socketFrom[socket.id];
            if (Object.keys(socketFrom).length === 0) {
                delete sockets[socket.from];
            }
        });

    });



});
//刷新浏览器时socket是相同的
function handlerMsg(data, socket, isget) {
	console.log(data)
    if (!data.from && !isget) {
        socket.emit('message', {
            k: 'from字段为必填！'
        });
        return;
    }
    data.to = data.to ? data.to.split(',') : data.from.split(',');
    if (!isget) {
        if (!sockets[data.from]) { sockets[data.from] = {}; }
        socket.from = data.from;
        sockets[data.from][socket.id] = socket;
    }

    if (data.to[0] === 'all') {
        io.emit('message', data);
        return;
    }
    //socket.emit('message',data);
    data.to.forEach(function(v, k) {
            var toIdsSockets = sockets[v];
            if (!toIdsSockets && !isget) {
                socket.emit('message', { k: 'id=' + v + '的用户不在线。' });
                return;
            }
            Object.keys(toIdsSockets).forEach(function(v2, k2) {
                toIdsSockets[v2].emit('message', data);
            })
        })
}
