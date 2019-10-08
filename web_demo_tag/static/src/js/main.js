odoo.define('web_demo_tag.main', function(require) {
"use strict";

    var $ = require('jquery');
    var rpc = require('web.rpc');
    var core = require('web.core');

    // Code from: http://jsfiddle.net/WK_of_Angmar/xgA5C/
    function validStrColour(strToTest) {
        if (strToTest === "") { return false; }
        if (strToTest === "inherit") { return true; }
        if (strToTest === "transparent") { return true; }
        var image = document.createElement("img");
        image.style.color = "rgb(0, 0, 0)";
        image.style.color = strToTest;
        if (image.style.color !== "rgb(0, 0, 0)") { return true; }
        image.style.color = "rgb(255, 255, 255)";
        image.style.color = strToTest;
        return image.style.color !== "rgb(255, 255, 255)";
    }

    core.bus.on('web_client_ready', null, function () {
        var demo_tag = $('<div class="demo_tag"/>');
        $('body').append(demo_tag);
        demo_tag.hide();
        // Get demo_tag data from backend
        rpc.query({
            model: 'web.demo.tag',
            method: 'set_tag',
        }).then(
            function (tag_data) {
                // demo_tag name
                if (tag_data.name && tag_data.name != 'False') {
                    demo_tag.html(tag_data.name);
                    demo_tag.show();
                }
                // demo_tag color
                if (tag_data.color && validStrColour(tag_data.color)) {
                    demo_tag.css('color', tag_data.color);
                }
                // demo_tag background color
                if (tag_data.background_color && validStrColour(tag_data.background_color)) {
                    demo_tag.css('background-color', tag_data.background_color);
                }
            }
        );
    });
});