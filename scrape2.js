// phantom.outputEncoding="gbk";
var page = require('webpage').create(), t;
page.onConsoleMessage = function(msg) {
    console.log('Page title is ' + msg);
};
page.settings.loadImages=false;

t = Date.now();
page.open('http://www.autohome.com.cn/suv/#pvareaid=103451', function() {
    if (page.injectJs("jquery-3.1.1.min.js")) {
        var title = page.evaluate(function() {
            return $(".tab-content-item.current .uibox li[id^='s']")
                .filter(function() {
                    return $(this).find("div:first>a").text() != undefined;
                })
                .map(function() {
                    var carid = $(this).attr("id"),
                    // var price = $(this).text();
                    // var name = $(this).find("h4").text();
                    // return {carid: [name, price]};
                    return carid;
                })
                .get().length;
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


