var PLAYER;
var PLAYER_SETTIMEOUT;
var PLAY_NOW;
var GG;



function remove_blue_color() {
    var lis = document.getElementsByTagName('li');
    for (var i=0; i<lis.length; i++) {
        var videoid = lis[i].getAttribute('data-id');
        lis[i].firstChild.nextSibling.style.color = '#444';
    }
}


function toggle(node, e) {
    if (e) {
        e.preventDefault();
    }
    PLAY_NOW = node.getAttribute('data-id');
    function repeat(node) {
        if (node.firstChild.src && PLAY_NOW === node.getAttribute('data-id')) {
            clearTimeout(PLAYER_SETTIMEOUT);
            if (!PLAYER || PLAYER.paused) {
                PLAYER = node.firstChild;
                remove_blue_color();
                PLAYER.nextSibling.style.color = 'blue';
                PLAYER.play();
            } else {
                PLAYER.pause();
                PLAYER.nextSibling.style.color = '#444';
                if (PLAYER !== node.firstChild) {
                    PLAYER = node.firstChild;
                    remove_blue_color();
                    PLAYER.nextSibling.style.color = 'blue';
                    PLAYER.play();
                }
            }
        } else if (PLAY_NOW === node.getAttribute('data-id')) {
            setTimeout(repeat, 0, node);
        }
    }
    repeat(node);
}


function set_audio(node, videoid, autoplay) {
    var xmlhttp = new XMLHttpRequest();
    var url = "/music/src/" + videoid;
    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myArr = JSON.parse(this.responseText);
            node.firstChild.src = myArr.src;
            node.firstChild.nextSibling.style.color = 'black';
            if (autoplay === 'yes') {
                node.firstChild.onended = function () {
                    if (node.nextElementSibling) {
                        toggle(node.nextElementSibling);
                    }
                }
            }
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

var lis = document.getElementsByTagName('li');
var url = new URL(window.location.href);
var autoplay = url.searchParams.get('autoplay');
var autoplay = true;
for (var i=0; i<lis.length; i++) {
    var videoid = lis[i].getAttribute('data-id');
    set_audio(lis[i], videoid, autoplay);
}
