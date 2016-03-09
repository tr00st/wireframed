(
    function() {
        var styleCSS="\
* {\
    background:rgba(0,0,0,0.02)!important;\
    color:black!important;\
    font-family:'Comic Sans MS',Arial!important;\
    font-size:110%;\
    padding:2px;\
    margin:-3px;\
}\
input,textarea,select,button,a {\
    border:1px dashed black!important;\
    padding:2px;\
    margin:-3px;\
}\
body,html,div{\
    padding:0;\
    margin:0;\
}";
        var styleNode=document.createElement("style");
        styleNode.innerText=styleCSS;
        document.head.appendChild(styleNode);
    }
)()

