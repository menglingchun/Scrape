// phantom.outputEncoding="gbk";
var page = require('webpage').create(), t;
page.onConsoleMessage = function(msg) {
    console.log('Page title is ' + msg);
};
page.settings.loadImages=false;

t = Date.now();
page.open('http://www.zealer.com', function() {
    if (page.injectJs("jquery-3.1.1.min.js")) {
        var title = page.evaluate(function() {
            return $('ul.index_titleList.clear>li>a')
                .map(function() {
                    return $(this).text();
                })
                .get()
                .join(' , ');
        });
        console.log(title);
        t = Date.now() - t;
        console.log('Load time with Phantom: ' + t + 'msec');
        phantom.exit();
    } else {
        console.log('not working!');    
        t = Date.now() - t;
        console.log('Load time with Phantom: ' + t + 'msec');
        phantom.exit();
    }
});


