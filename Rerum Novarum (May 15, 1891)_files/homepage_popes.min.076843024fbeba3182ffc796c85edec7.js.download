window.Modernizr=function(au,at,ar){function R(b){ak.cssText=b
}function Q(d,c){return R(ag.join(d+";")+(c||""))
}function P(d,c){return typeof d===c
}function O(d,c){return !!~(""+d).indexOf(c)
}function N(f,c){for(var h in f){var g=f[h];
if(!O(g,"-")&&ak[g]!==ar){return c=="pfx"?g:!0
}}return !1
}function M(g,c,j){for(var i in g){var h=c[g[i]];
if(h!==ar){return j===!1?g[i]:P(h,"function")?h.bind(j||c):h
}}return !1
}function L(g,f,j){var i=g.charAt(0).toUpperCase()+g.slice(1),h=(g+" "+ae.join(i+" ")+i).split(" ");
return P(f,"string")||P(f,"undefined")?N(h,f):(h=(g+" "+ad.join(i+" ")+i).split(" "),M(h,f,j))
}var aq="2.6.2",ap={},ao=!0,an=at.documentElement,am="modernizr",al=at.createElement(am),ak=al.style,aj,ai=":)",ah={}.toString,ag=" -webkit- -moz- -o- -ms- ".split(" "),af="Webkit Moz O ms",ae=af.split(" "),ad=af.toLowerCase().split(" "),ac={svg:"http://www.w3.org/2000/svg"},ab={},aa={},Z={},Y=[],X=Y.slice,W,V=function(x,w,u,t){var r,q,p,o,h=at.createElement("div"),g=at.body,b=g||at.createElement("body");
if(parseInt(u,10)){while(u--){p=at.createElement("div"),p.id=t?t[u]:am+(u+1),h.appendChild(p)
}}return r=["&#173;",'<style id="s',am,'">',x,"</style>"].join(""),h.id=am,(g?h:b).innerHTML+=r,b.appendChild(h),g||(b.style.background="",b.style.overflow="hidden",o=an.style.overflow,an.style.overflow="hidden",an.appendChild(b)),q=w(h,x),g?h.parentNode.removeChild(h):(b.parentNode.removeChild(b),an.style.overflow=o),!!q
},U=function(a){var f=au.matchMedia||au.msMatchMedia;
if(f){return f(a).matches
}var e;
return V("@media "+a+" { #"+am+" { position: absolute; } }",function(c){e=(au.getComputedStyle?getComputedStyle(c,null):c.currentStyle)["position"]=="absolute"
}),e
},T={}.hasOwnProperty,S;
!P(T,"undefined")&&!P(T.call,"undefined")?S=function(d,c){return T.call(d,c)
}:S=function(d,c){return c in d&&P(d.constructor.prototype[c],"undefined")
},Function.prototype.bind||(Function.prototype.bind=function(a){var h=this;
if(typeof h!="function"){throw new TypeError
}var g=X.call(arguments,1),f=function(){if(this instanceof f){var b=function(){};
b.prototype=h.prototype;
var d=new b,c=h.apply(d,g.concat(X.call(arguments)));
return Object(c)===c?c:d
}return h.apply(a,g.concat(X.call(arguments)))
};
return f
}),ab.flexbox=function(){return L("flexWrap")
},ab.flexboxlegacy=function(){return L("boxDirection")
},ab.rgba=function(){return R("background-color:rgba(150,255,150,.5)"),O(ak.backgroundColor,"rgba")
},ab.hsla=function(){return R("background-color:hsla(120,40%,100%,.5)"),O(ak.backgroundColor,"rgba")||O(ak.backgroundColor,"hsla")
},ab.multiplebgs=function(){return R("background:url(https://),url(https://),red url(https://)"),/(url\s*\(.*?){3}/.test(ak.background)
},ab.backgroundsize=function(){return L("backgroundSize")
},ab.borderimage=function(){return L("borderImage")
},ab.borderradius=function(){return L("borderRadius")
},ab.boxshadow=function(){return L("boxShadow")
},ab.textshadow=function(){return at.createElement("div").style.textShadow===""
},ab.opacity=function(){return Q("opacity:.55"),/^0.55$/.test(ak.opacity)
},ab.cssanimations=function(){return L("animationName")
},ab.csscolumns=function(){return L("columnCount")
},ab.cssgradients=function(){var e="background-image:",d="gradient(linear,left top,right bottom,from(#9f9),to(white));",f="linear-gradient(left top,#9f9, white);";
return R((e+"-webkit- ".split(" ").join(d+e)+ag.join(f+e)).slice(0,-e.length)),O(ak.backgroundImage,"gradient")
},ab.cssreflections=function(){return L("boxReflect")
},ab.csstransforms=function(){return !!L("transform")
},ab.csstransforms3d=function(){var b=!!L("perspective");
return b&&"webkitPerspective" in an.style&&V("@media (transform-3d),(-webkit-transform-3d){#modernizr{left:9px;position:absolute;height:3px;}}",function(a,d){b=a.offsetLeft===9&&a.offsetHeight===3
}),b
},ab.csstransitions=function(){return L("transition")
},ab.fontface=function(){var b;
return V('@font-face {font-family:"font";src:url("https://")}',function(k,j){var i=at.getElementById("smodernizr"),h=i.sheet||i.styleSheet,a=h?h.cssRules&&h.cssRules[0]?h.cssRules[0].cssText:h.cssText||"":"";
b=/src/i.test(a)&&a.indexOf(j.split(" ")[0])===0
}),b
},ab.generatedcontent=function(){var b;
return V(["#",am,"{font:0/0 a}#",am,':after{content:"',ai,'";visibility:hidden;font:3px/1 a}'].join(""),function(a){b=a.offsetHeight>=3
}),b
},ab.video=function(){var b=at.createElement("video"),f=!1;
try{if(f=!!b.canPlayType){f=new Boolean(f),f.ogg=b.canPlayType('video/ogg; codecs="theora"').replace(/^no$/,""),f.h264=b.canPlayType('video/mp4; codecs="avc1.42E01E"').replace(/^no$/,""),f.webm=b.canPlayType('video/webm; codecs="vp8, vorbis"').replace(/^no$/,"")
}}catch(e){}return f
},ab.audio=function(){var b=at.createElement("audio"),f=!1;
try{if(f=!!b.canPlayType){f=new Boolean(f),f.ogg=b.canPlayType('audio/ogg; codecs="vorbis"').replace(/^no$/,""),f.mp3=b.canPlayType("audio/mpeg;").replace(/^no$/,""),f.wav=b.canPlayType('audio/wav; codecs="1"').replace(/^no$/,""),f.m4a=(b.canPlayType("audio/x-m4a;")||b.canPlayType("audio/aac;")).replace(/^no$/,"")
}}catch(e){}return f
},ab.svg=function(){return !!at.createElementNS&&!!at.createElementNS(ac.svg,"svg").createSVGRect
};
for(var K in ab){S(ab,K)&&(W=K.toLowerCase(),ap[W]=ab[K](),Y.push((ap[W]?"":"no-")+W))
}return ap.addTest=function(e,c){if(typeof e=="object"){for(var f in e){S(e,f)&&ap.addTest(f,e[f])
}}else{e=e.toLowerCase();
if(ap[e]!==ar){return ap
}c=typeof c=="function"?c():c,typeof ao!="undefined"&&ao&&(an.className+=" "+(c?"":"no-")+e),ap[e]=c
}return ap
},R(""),al=aj=null,ap._version=aq,ap._prefixes=ag,ap._domPrefixes=ad,ap._cssomPrefixes=ae,ap.mq=U,ap.testProp=function(b){return N([b])
},ap.testAllProps=L,ap.testStyles=V,an.className=an.className.replace(/(^|\s)no-js(\s|$)/,"$1$2")+(ao?" js "+Y.join(" "):""),ap
}(this,this.document),function(Z,Y){function P(f,e){var h=f.createElement("p"),g=f.getElementsByTagName("head")[0]||f.documentElement;
return h.innerHTML="x<style>"+e+"</style>",g.insertBefore(h.lastChild,g.firstChild)
}function O(){var b=I.elements;
return typeof b=="string"?b.split(" "):b
}function N(d){var c=R[d[T]];
return c||(c={},S++,d[T]=S,R[S]=c),c
}function M(b,h,e){h||(h=Y);
if(Q){return h.createElement(b)
}e||(e=N(h));
var d;
return e.cache[b]?d=e.cache[b].cloneNode():V.test(b)?d=(e.cache[b]=e.createElem(b)).cloneNode():d=e.createElem(b),d.canHaveChildren&&!W.test(b)?e.frag.appendChild(d):d
}function L(b,l){b||(b=Y);
if(Q){return b.createDocumentFragment()
}l=l||N(b);
var k=l.frag.cloneNode(),j=0,i=O(),h=i.length;
for(;
j<h;
j++){k.createElement(i[j])
}return k
}function K(d,c){c.cache||(c.cache={},c.createElem=d.createElement,c.createFrag=d.createDocumentFragment,c.frag=c.createFrag()),d.createElement=function(a){return I.shivMethods?M(a,d,c):c.createElem(a)
},d.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+O().join().replace(/\w+/g,function(b){return c.createElem(b),c.frag.createElement(b),'c("'+b+'")'
})+");return n}")(I,c.frag)
}function J(b){b||(b=Y);
var d=N(b);
return I.shivCSS&&!U&&!d.hasCSS&&(d.hasCSS=!!P(b,"article,aside,figcaption,figure,footer,header,hgroup,nav,section{display:block}mark{background:#FF0;color:#000}")),Q||K(b,d),b
}function E(h){var g,l=h.getElementsByTagName("*"),k=l.length,j=RegExp("^(?:"+O().join("|")+")$","i"),i=[];
while(k--){g=l[k],j.test(g.nodeName)&&i.push(g.applyElement(D(g)))
}return i
}function D(g){var f,j=g.attributes,i=j.length,h=g.ownerDocument.createElement(G+":"+g.nodeName);
while(i--){f=j[i],f.specified&&h.setAttribute(f.nodeName,f.nodeValue)
}return h.style.cssText=g.style.cssText,h
}function C(h){var g,l=h.split("{"),k=l.length,j=RegExp("(^|[\\s,>+~])("+O().join("|")+")(?=[[\\s,>+~#.:]|$)","gi"),i="$1"+G+"\\:$2";
while(k--){g=l[k]=l[k].split("}"),g[g.length-1]=g[g.length-1].replace(j,i),l[k]=g.join("}")
}return l.join("{")
}function B(d){var c=d.length;
while(c--){d[c].removeNode()
}}function A(i){function j(){clearTimeout(m._removeSheetTimer),h&&h.removeNode(!0),h=null
}var h,n,m=N(i),l=i.namespaces,k=i.parentWindow;
return !F||i.printShived?i:(typeof l[G]=="undefined"&&l.add(G),k.attachEvent("onbeforeprint",function(){j();
var r,q,p,o=i.styleSheets,g=[],c=o.length,b=Array(c);
while(c--){b[c]=o[c]
}while(p=b.pop()){if(!p.disabled&&H.test(p.media)){try{r=p.imports,q=r.length
}catch(a){q=0
}for(c=0;
c<q;
c++){b.push(r[c])
}try{g.push(p.cssText)
}catch(a){}}}g=C(g.reverse().join("")),n=E(i),h=P(i,g)
}),k.attachEvent("onafterprint",function(){B(n),clearTimeout(m._removeSheetTimer),m._removeSheetTimer=setTimeout(j,500)
}),i.printShived=!0,i)
}var X=Z.html5||{},W=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,V=/^<|^(?:a|b|button|code|div|fieldset|form|h1|h2|h3|h4|h5|h6|i|iframe|img|input|label|li|link|ol|option|p|param|q|script|select|span|strong|style|table|tbody|td|textarea|tfoot|th|thead|tr|ul)$/i,U,T="_html5shiv",S=0,R={},Q;
(function(){try{var b=Y.createElement("a");
b.innerHTML="<xyz></xyz>",U="hidden" in b,Q=b.childNodes.length==1||function(){Y.createElement("a");
var c=Y.createDocumentFragment();
return typeof c.cloneNode=="undefined"||typeof c.createDocumentFragment=="undefined"||typeof c.createElement=="undefined"
}()
}catch(d){U=!0,Q=!0
}})();
var I={elements:X.elements||"abbr article aside audio bdi canvas data datalist details figcaption figure footer header hgroup mark meter nav output progress section summary time video",shivCSS:X.shivCSS!==!1,supportsUnknownElements:Q,shivMethods:X.shivMethods!==!1,type:"default",shivDocument:J,createElement:M,createDocumentFragment:L};
Z.html5=I,J(Y);
var H=/^$|\b(?:all|print)\b/,G="html5shiv",F=!Q&&function(){var a=Y.documentElement;
return typeof Y.namespaces!="undefined"&&typeof Y.parentWindow!="undefined"&&typeof a.applyElement!="undefined"&&typeof a.removeNode!="undefined"&&typeof Z.attachEvent!="undefined"
}();
I.type+=" print",I.shivPrint=A,A(Y)
}(this,document),function(ad,ac,ab){function aa(b){return"[object Function]"==P.call(b)
}function Z(b){return"string"==typeof b
}function Y(){}function X(b){return !b||"loaded"==b||"complete"==b||"uninitialized"==b
}function W(){var b=O.shift();
M=1,b?b.t?R(function(){("c"==b.t?L.injectCss:L.injectJs)(b.s,0,b.a,b.x,b.e,1)
},0):(b(),W()):M=0
}function V(y,x,w,t,q,p,n){function m(a){if(!g&&X(h.readyState)&&(z.r=g=1,!M&&W(),h.onload=h.onreadystatechange=null,a)){"img"!=y&&R(function(){I.removeChild(h)
},50);
for(var c in D[x]){D[x].hasOwnProperty(c)&&D[x][c].onload()
}}}var n=n||L.errorTimeout,h=ac.createElement(y),g=0,b=0,z={t:w,s:x,e:q,a:p,x:n};
1===D[x]&&(b=1,D[x]=[]),"object"==y?h.data=x:(h.src=x,h.type=y),h.width=h.height="0",h.onerror=h.onload=h.onreadystatechange=function(){m.call(this,b)
},O.splice(t,0,z),"img"!=y&&(b||2===D[x]?(I.insertBefore(h,J?null:Q),R(m,n)):D[x].push(h))
}function U(g,e,j,i,h){return M=0,e=e||"j",Z(g)?V("c"==e?G:H,g,e,this.i++,j,i,h):(O.splice(this.i++,0,g),1==O.length&&W()),this
}function T(){var b=L;
return b.loader={load:U,i:0},b
}var S=ac.documentElement,R=ad.setTimeout,Q=ac.getElementsByTagName("script")[0],P={}.toString,O=[],M=0,K="MozAppearance" in S.style,J=K&&!!ac.createRange().compareNode,I=J?S:Q.parentNode,S=ad.opera&&"[object Opera]"==P.call(ad.opera),S=!!ac.attachEvent&&!S,H=K?"object":S?"script":"img",G=S?"script":H,F=Array.isArray||function(b){return"[object Array]"==P.call(b)
},E=[],D={},C={timeout:function(d,c){return c.length&&(d.timeout=c[0]),d
}},N,L;
L=function(e){function c(i){var i=i.split("!"),h=E.length,q=i.pop(),p=i.length,q={url:q,origUrl:q,prefixes:i},o,l,j;
for(l=0;
l<p;
l++){j=i[l].split("="),(o=C[j.shift()])&&(q=o(q,j))
}for(l=0;
l<h;
l++){q=E[l](q)
}return q
}function n(b,t,r,q,p){var o=c(b),l=o.autoCallback;
o.url.split(".").pop().split("?").shift(),o.bypass||(t&&(t=aa(t)?t:t[b]||t[q]||t[b.split("/").pop().split("?")[0]]),o.instead?o.instead(b,t,r,q,p):(D[o.url]?o.noexec=!0:D[o.url]=1,r.load(o.url,o.forceCSS||!o.forceJS&&"css"==o.url.split(".").pop().split("?").shift()?"c":ab,o.noexec,o.attrs,o.timeout),(aa(t)||aa(l))&&r.load(function(){T(),t&&t(o.origUrl,p,q),l&&l(o.origUrl,p,q),D[o.url]=2
})))
}function m(y,x){function w(b,h){if(b){if(Z(b)){h||(r=function(){var i=[].slice.call(arguments);
q.apply(this,i),p()
}),n(b,r,x,0,u)
}else{if(Object(b)===b){for(g in o=function(){var a=0,i;
for(i in b){b.hasOwnProperty(i)&&a++
}return a
}(),b){b.hasOwnProperty(g)&&(!h&&!--o&&(aa(r)?r=function(){var i=[].slice.call(arguments);
q.apply(this,i),p()
}:r[g]=function(i){return function(){var a=[].slice.call(arguments);
i&&i.apply(this,a),p()
}
}(q[g])),n(b[g],r,x,g,u))
}}}}else{!h&&p()
}}var u=!!y.test,t=y.load||y.both,r=y.callback||Y,q=r,p=y.complete||Y,o,g;
w(u?y.yep:y.nope,!!t),t&&w(t)
}var k,f,d=this.yepnope.loader;
if(Z(e)){n(e,0,d,0)
}else{if(F(e)){for(k=0;
k<e.length;
k++){f=e[k],Z(f)?n(f,0,d,0):F(f)?L(f):Object(f)===f&&m(f,d)
}}else{Object(e)===e&&m(e,d)
}}},L.addPrefix=function(d,c){C[d]=c
},L.addFilter=function(b){E.push(b)
},L.errorTimeout=10000,null==ac.readyState&&ac.addEventListener&&(ac.readyState="loading",ac.addEventListener("DOMContentLoaded",N=function(){ac.removeEventListener("DOMContentLoaded",N,0),ac.readyState="complete"
},0)),ad.yepnope=T(),ad.yepnope.executeStack=W,ad.yepnope.injectJs=function(r,q,p,n,m,h){var g=ac.createElement("script"),f,b,n=n||L.errorTimeout;
g.src=r;
for(b in p){g.setAttribute(b,p[b])
}q=h?W:q||Y,g.onreadystatechange=g.onload=function(){!f&&X(g.readyState)&&(f=1,q(),g.onload=g.onreadystatechange=null)
},R(function(){f||(f=1,q(1))
},n),m?g.onload():Q.parentNode.insertBefore(g,Q)
},ad.yepnope.injectCss=function(b,n,m,l,k,h){var l=ac.createElement("link"),f,n=h?W:n||Y;
l.href=b,l.rel="stylesheet",l.type="text/css";
for(f in m){l.setAttribute(f,m[f])
}k||(Q.parentNode.insertBefore(l,Q),R(n,0))
}
}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))
},Modernizr.addTest("mediaqueries",Modernizr.mq("only all"));
!function(L,K){function J(a){a=L.extend({},u,a||{}),null===y&&(y=L("body"));
for(var h=L(this),g=0,d=h.length;
d>g;
g++){I(h.eq(g),a)
}return h
}function I(f,e){if(!f.hasClass(x.base)){e=L.extend({},e,f.data(z+"-options"));
var b="";
b+='<div class="'+x.bar+'">',b+='<div class="'+x.track+'">',b+='<div class="'+x.handle+'">',b+="</div></div></div>",e.paddingRight=parseInt(f.css("padding-right"),10),e.paddingBottom=parseInt(f.css("padding-bottom"),10),f.addClass([x.base,e.customClass].join(" ")).wrapInner('<div class="'+x.content+'" />').prepend(b),e.horizontal&&f.addClass(x.isHorizontal);
var a=L.extend({$scroller:f,$content:f.find(A(x.content)),$bar:f.find(A(x.bar)),$track:f.find(A(x.track)),$handle:f.find(A(x.handle))},e);
a.trackMargin=parseInt(a.trackMargin,10),a.$content.on("scroll."+z,a,H),a.$scroller.on(w.start,A(x.track),a,G).on(w.start,A(x.handle),a,F).data(z,a),t.reset.apply(f),L(K).one("load",function(){t.reset.apply(f)
})
}}function H(i){i.preventDefault(),i.stopPropagation();
var h=i.data,n={};
if(h.horizontal){var m=h.$content.scrollLeft();
0>m&&(m=0);
var l=m/h.scrollRatio;
l>h.handleBounds.right&&(l=h.handleBounds.right),n={left:l}
}else{var k=h.$content.scrollTop();
0>k&&(k=0);
var j=k/h.scrollRatio;
j>h.handleBounds.bottom&&(j=h.handleBounds.bottom),n={top:j}
}h.$handle.css(n)
}function G(i){i.preventDefault(),i.stopPropagation();
var h=i.data,n=i.originalEvent,m=h.$track.offset(),l="undefined"!=typeof n.targetTouches?n.targetTouches[0]:null,k=l?l.pageX:i.clientX,j=l?l.pageY:i.clientY;
h.horizontal?(h.mouseStart=k,h.handleLeft=k-m.left-h.handleWidth/2,B(h,h.handleLeft)):(h.mouseStart=j,h.handleTop=j-m.top-h.handleHeight/2,B(h,h.handleTop)),E(h)
}function F(h){h.preventDefault(),h.stopPropagation();
var g=h.data,l=h.originalEvent,k="undefined"!=typeof l.targetTouches?l.targetTouches[0]:null,j=k?k.pageX:h.clientX,i=k?k.pageY:h.clientY;
g.horizontal?(g.mouseStart=j,g.handleLeft=parseInt(g.$handle.css("left"),10)):(g.mouseStart=i,g.handleTop=parseInt(g.$handle.css("top"),10)),E(g)
}function E(b){b.$content.off(A(z)),y.on(w.move,b,D).on(w.end,b,C)
}function D(j){j.preventDefault(),j.stopPropagation();
var i=j.data,p=j.originalEvent,o=0,n=0,m="undefined"!=typeof p.targetTouches?p.targetTouches[0]:null,l=m?m.pageX:j.clientX,k=m?m.pageY:j.clientY;
i.horizontal?(n=i.mouseStart-l,o=i.handleLeft-n):(n=i.mouseStart-k,o=i.handleTop-n),B(i,o)
}function C(d){d.preventDefault(),d.stopPropagation();
var c=d.data;
c.$content.on("scroll.scroller",c,H),y.off(".scroller")
}function B(g,f){var j={};
if(g.horizontal){f<g.handleBounds.left&&(f=g.handleBounds.left),f>g.handleBounds.right&&(f=g.handleBounds.right);
var i=Math.round(f*g.scrollRatio);
j={left:f},g.$content.scrollLeft(i)
}else{f<g.handleBounds.top&&(f=g.handleBounds.top),f>g.handleBounds.bottom&&(f=g.handleBounds.bottom);
var h=Math.round(f*g.scrollRatio);
j={top:f},g.$content.scrollTop(h)
}g.$handle.css(j)
}function A(b){return"."+b
}var z="scroller",y=null,x={base:"scroller",content:"scroller-content",bar:"scroller-bar",track:"scroller-track",handle:"scroller-handle",isHorizontal:"scroller-horizontal",isSetup:"scroller-setup",isActive:"scroller-active"},w={start:"touchstart."+z+" mousedown."+z,move:"touchmove."+z+" mousemove."+z,end:"touchend."+z+" mouseup."+z},u={customClass:"",duration:0,handleSize:0,horizontal:!1,trackMargin:0},t={defaults:function(a){return u=L.extend(u,a||{}),"object"==typeof this?L(this):!0
},destroy:function(){return L(this).each(function(a,f){var e=L(f).data(z);
e&&(e.$scroller.removeClass([e.customClass,x.base,x.isActive].join(" ")),e.$bar.remove(),e.$content.contents().unwrap(),e.$content.off(A(z)),e.$scroller.off(A(z)).removeData(z))
})
},scroll:function(a,d){return L(this).each(function(){var k=L(this).data(z),j=d||u.duration;
if("number"!=typeof a){var i=L(a);
if(i.length>0){var c=i.position();
a=k.horizontal?c.left+k.$content.scrollLeft():c.top+k.$content.scrollTop()
}else{a=k.$content.scrollTop()
}}var b=k.horizontal?{scrollLeft:a}:{scrollTop:a};
k.$content.stop().animate(b,j)
})
},reset:function(){return L(this).each(function(){var a=L(this).data(z);
if(a){a.$scroller.addClass(x.isSetup);
var p={},o={},n={},m=0,l=!0;
if(a.horizontal){a.barHeight=a.$content[0].offsetHeight-a.$content[0].clientHeight,a.frameWidth=a.$content.outerWidth(),a.trackWidth=a.frameWidth-2*a.trackMargin,a.scrollWidth=a.$content[0].scrollWidth,a.ratio=a.trackWidth/a.scrollWidth,a.trackRatio=a.trackWidth/a.scrollWidth,a.handleWidth=a.handleSize>0?a.handleSize:a.trackWidth*a.trackRatio,a.scrollRatio=(a.scrollWidth-a.frameWidth)/(a.trackWidth-a.handleWidth),a.handleBounds={left:0,right:a.trackWidth-a.handleWidth},a.$content.css({paddingBottom:a.barHeight+a.paddingBottom});
var k=a.$content.scrollLeft();
m=k*a.ratio,l=a.scrollWidth<=a.frameWidth,p={width:a.frameWidth},o={width:a.trackWidth,marginLeft:a.trackMargin,marginRight:a.trackMargin},n={width:a.handleWidth}
}else{a.barWidth=a.$content[0].offsetWidth-a.$content[0].clientWidth,a.frameHeight=a.$content.outerHeight(),a.trackHeight=a.frameHeight-2*a.trackMargin,a.scrollHeight=a.$content[0].scrollHeight,a.ratio=a.trackHeight/a.scrollHeight,a.trackRatio=a.trackHeight/a.scrollHeight,a.handleHeight=a.handleSize>0?a.handleSize:a.trackHeight*a.trackRatio,a.scrollRatio=(a.scrollHeight-a.frameHeight)/(a.trackHeight-a.handleHeight),a.handleBounds={top:0,bottom:a.trackHeight-a.handleHeight};
var j=a.$content.scrollTop();
m=j*a.ratio,l=a.scrollHeight<=a.frameHeight,p={height:a.frameHeight},o={height:a.trackHeight,marginBottom:a.trackMargin,marginTop:a.trackMargin},n={height:a.handleHeight}
}l?a.$scroller.removeClass(x.isActive):a.$scroller.addClass(x.isActive),a.$bar.css(p),a.$track.css(o),a.$handle.css(n),B(a,m),a.$scroller.removeClass(x.isSetup)
}})
}};
L.fn[z]=function(b){return t[b]?t[b].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof b&&b?this:J.apply(this,arguments)
},L[z]=function(b){"defaults"===b&&t.defaults.apply(this,Array.prototype.slice.call(arguments,1))
}
}(jQuery);
/*! Lazy Load 1.9.3 - MIT license - Copyright 2010-2013 Mika Tuupola */
!function(g,f,j,i){var h=g(f);
g.fn.lazyload=function(e){function d(){var k=0;
b.each(function(){var l=g(this);
if(!a.skip_invisible||l.is(":visible")){if(g.abovethetop(this,a)||g.leftofbegin(this,a)){}else{if(g.belowthefold(this,a)||g.rightoffold(this,a)){if(++k>a.failure_limit){return !1
}}else{l.trigger("appear"),k=0
}}}})
}var c,b=this,a={threshold:0,failure_limit:0,event:"scroll",effect:"show",container:f,data_attribute:"original",skip_invisible:!0,appear:null,load:null,placeholder:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC"};
return e&&(i!==e.failurelimit&&(e.failure_limit=e.failurelimit,delete e.failurelimit),i!==e.effectspeed&&(e.effect_speed=e.effectspeed,delete e.effectspeed),g.extend(a,e)),c=a.container===i||a.container===f?h:g(a.container),0===a.event.indexOf("scroll")&&c.bind(a.event,function(){return d()
}),this.each(function(){var k=this,l=g(k);
k.loaded=!1,(l.attr("src")===i||l.attr("src")===!1)&&l.is("img")&&l.attr("src",a.placeholder),l.one("appear",function(){if(!this.loaded){if(a.appear){var m=b.length;
a.appear.call(k,m,a)
}g("<img />").bind("load",function(){var p=l.attr("data-"+a.data_attribute);
l.hide(),l.is("img")?l.attr("src",p):l.css("background-image","url('"+p+"')"),l[a.effect](a.effect_speed),k.loaded=!0;
var o=g.grep(b,function(q){return !q.loaded
});
if(b=g(o),a.load){var n=b.length;
a.load.call(k,n,a)
}}).attr("src",l.attr("data-"+a.data_attribute))
}}),0!==a.event.indexOf("scroll")&&l.bind(a.event,function(){k.loaded||l.trigger("appear")
})
}),h.bind("resize",function(){d()
}),/(?:iphone|ipod|ipad).*os 5/gi.test(navigator.appVersion)&&h.bind("pageshow",function(k){k.originalEvent&&k.originalEvent.persisted&&b.each(function(){g(this).trigger("appear")
})
}),g(j).ready(function(){d()
}),this
},g.belowthefold=function(d,b){var a;
return a=b.container===i||b.container===f?(f.innerHeight?f.innerHeight:h.height())+h.scrollTop():g(b.container).offset().top+g(b.container).height(),a<=g(d).offset().top-b.threshold
},g.rightoffold=function(d,b){var a;
return a=b.container===i||b.container===f?h.width()+h.scrollLeft():g(b.container).offset().left+g(b.container).width(),a<=g(d).offset().left-b.threshold
},g.abovethetop=function(d,b){var a;
return a=b.container===i||b.container===f?h.scrollTop():g(b.container).offset().top,a>=g(d).offset().top+b.threshold+g(d).height()
},g.leftofbegin=function(d,b){var a;
return a=b.container===i||b.container===f?h.scrollLeft():g(b.container).offset().left,a>=g(d).offset().left+b.threshold+g(d).width()
},g.inviewport=function(a,d){return !(g.rightoffold(a,d)||g.leftofbegin(a,d)||g.belowthefold(a,d)||g.abovethetop(a,d))
},g.extend(g.expr[":"],{"below-the-fold":function(a){return g.belowthefold(a,{threshold:0})
},"above-the-top":function(a){return !g.belowthefold(a,{threshold:0})
},"right-of-screen":function(a){return g.rightoffold(a,{threshold:0})
},"left-of-screen":function(a){return !g.rightoffold(a,{threshold:0})
},"in-viewport":function(a){return g.inviewport(a,{threshold:0})
},"above-the-fold":function(a){return !g.belowthefold(a,{threshold:0})
},"right-of-fold":function(a){return g.rightoffold(a,{threshold:0})
},"left-of-fold":function(a){return !g.rightoffold(a,{threshold:0})
}})
}(jQuery,window,document);
/*!
 * instaFilta
 * Description: "jQuery plugin for performing in-page filtering"
 * Version: "1.1.0"
 * Homepage: https://github.com/chromawoods/instaFilta
 * Author: Andreas Larsson <andreas@chromawoods.com> (http://chromawoods.com)
 * Modified: Davide Di Giulio for Vatican.va - 20141212 (added callback as parameter)
 */
(function(a){a.fn.instaFilta=function(j){var e=a.extend({targets:".instafilta-target",sections:".instafilta-section",matchCssClass:"instafilta-match",markMatches:false,hideEmptySections:true,beginsWith:false,caseSensitive:false,typeDelay:0,callback:null},j);
var d,b=a(e.targets),f=a(e.sections),c="";
var h=function(){f.each(function(){var k=a(this);
k.toggle(!!(k.find('[data-instafilta-hide="false"]').length))
})
};
var g=function(k){k=e.caseSensitive?k:k.toLowerCase();
if(c===k){return false
}else{c=k
}if(!k){b.attr("data-instafilta-hide","false").show();
f.show()
}b.each(function(){var m=a(this),p=m.text(),l=e.caseSensitive?p:p.toLowerCase(),o=l.indexOf(k),n=null;
if(!m.data("originalText")){m.data("originalText",p)
}else{m.html(m.data("originalText"))
}if(o>=0&&e.markMatches){n=p.substring(o,o+k.length);
m.html(p.replace(n,'<span class="'+e.matchCssClass+'">'+n+"</span>"))
}m.attr("data-instafilta-hide",(e.beginsWith&&o!==0)||o<0?"true":"false")
});
b.filter('[data-instafilta-hide="true"]').hide();
b.filter('[data-instafilta-hide="false"]').show();
e.hideEmptySections&&h()
};
var i=function(){var k=a(this);
clearTimeout(d);
d=setTimeout(function(){g(k.val());
if(e.callback!=null){e.callback(k)
}},e.typeDelay)
};
return a(this).on("keyup",i)
}
}(jQuery));
!function(b){"function"==typeof define&&define.amd?define(["jquery"],b):"object"==typeof exports?module.exports=b:b(jQuery)
}(function(x){function w(B){var A=B||window.event,z=n.call(arguments,1),y=0,k=0,i=0,f=0,e=0,d=0;
if(B=x.event.fix(A),B.type="mousewheel","detail" in A&&(i=-1*A.detail),"wheelDelta" in A&&(i=A.wheelDelta),"wheelDeltaY" in A&&(i=A.wheelDeltaY),"wheelDeltaX" in A&&(k=-1*A.wheelDeltaX),"axis" in A&&A.axis===A.HORIZONTAL_AXIS&&(k=-1*i,i=0),y=0===i?k:i,"deltaY" in A&&(i=-1*A.deltaY,y=i),"deltaX" in A&&(k=A.deltaX,0===i&&(y=-1*k)),0!==i||0!==k){if(1===A.deltaMode){var c=x.data(this,"mousewheel-line-height");
y*=c,i*=c,k*=c
}else{if(2===A.deltaMode){var a=x.data(this,"mousewheel-page-height");
y*=a,i*=a,k*=a
}}if(f=Math.max(Math.abs(i),Math.abs(k)),(!q||q>f)&&(q=f,t(A,f)&&(q/=40)),t(A,f)&&(y/=40,k/=40,i/=40),y=Math[y>=1?"floor":"ceil"](y/q),k=Math[k>=1?"floor":"ceil"](k/q),i=Math[i>=1?"floor":"ceil"](i/q),l.settings.normalizeOffset&&this.getBoundingClientRect){var C=this.getBoundingClientRect();
e=B.clientX-C.left,d=B.clientY-C.top
}return B.deltaX=k,B.deltaY=i,B.deltaFactor=q,B.offsetX=e,B.offsetY=d,B.deltaMode=0,z.unshift(B,y,k,i),r&&clearTimeout(r),r=setTimeout(u,200),(x.event.dispatch||x.event.handle).apply(this,z)
}}function u(){q=null
}function t(d,c){return l.settings.adjustOldDeltas&&"mousewheel"===d.type&&c%120===0
}var r,q,p=["wheel","mousewheel","DOMMouseScroll","MozMousePixelScroll"],o="onwheel" in document||document.documentMode>=9?["wheel"]:["mousewheel","DomMouseScroll","MozMousePixelScroll"],n=Array.prototype.slice;
if(x.event.fixHooks){for(var m=p.length;
m;
){x.event.fixHooks[p[--m]]=x.event.mouseHooks
}}var l=x.event.special.mousewheel={version:"3.1.12",setup:function(){if(this.addEventListener){for(var a=o.length;
a;
){this.addEventListener(o[--a],w,!1)
}}else{this.onmousewheel=w
}x.data(this,"mousewheel-line-height",l.getLineHeight(this)),x.data(this,"mousewheel-page-height",l.getPageHeight(this))
},teardown:function(){if(this.removeEventListener){for(var a=o.length;
a;
){this.removeEventListener(o[--a],w,!1)
}}else{this.onmousewheel=null
}x.removeData(this,"mousewheel-line-height"),x.removeData(this,"mousewheel-page-height")
},getLineHeight:function(a){var f=x(a),e=f["offsetParent" in x.fn?"offsetParent":"parent"]();
return e.length||(e=x("body")),parseInt(e.css("fontSize"),10)||parseInt(f.css("fontSize"),10)||16
},getPageHeight:function(a){return x(a).height()
},settings:{adjustOldDeltas:!0,normalizeOffset:!0}};
x.fn.extend({mousewheel:function(b){return b?this.bind("mousewheel",b):this.trigger("mousewheel")
},unmousewheel:function(b){return this.unbind("mousewheel",b)
}})
});
!function(d,c,b){!function(e){var f="function"==typeof define&&define.amd,g="https:"==b.location.protocol?"https:":"http:",a="cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.12/jquery.mousewheel.min.js";
f||d.event.special.mousewheel||d("head").append(decodeURI("%3Cscript src="+g+"//"+a+"%3E%3C/script%3E")),e()
}(function(){var aM="mCustomScrollbar",aN="mCS",aS=".mCustomScrollbar",aI={setTop:0,setLeft:0,axis:"y",scrollbarPosition:"inside",scrollInertia:950,autoDraggerLength:!0,alwaysShowScrollbar:0,snapOffset:0,mouseWheel:{enable:!0,scrollAmount:"auto",axis:"y",deltaFactor:"auto",disableOver:["select","option","keygen","datalist","textarea"]},scrollButtons:{scrollType:"stepless",scrollAmount:"auto"},keyboard:{enable:!0,scrollType:"stepless",scrollAmount:"auto"},contentTouchScroll:25,advanced:{autoScrollOnFocus:"input,textarea,select,button,datalist,keygen,a[tabindex],area,object,[contenteditable='true']",updateOnContentResize:!0,updateOnImageLoad:!0},theme:"light",callbacks:{onTotalScrollOffset:0,onTotalScrollBackOffset:0,alwaysTriggerOffsets:!0}},aP=0,aH={},aY=c.attachEvent&&!c.addEventListener?1:0,aX=!1,aG=["mCSB_dragger_onDrag","mCSB_scrollTools_onDrag","mCS_img_loaded","mCS_disabled","mCS_destroyed","mCS_no_scrollbar","mCS-autoHide","mCS-dir-rtl","mCS_no_scrollbar_y","mCS_no_scrollbar_x","mCS_y_hidden","mCS_x_hidden","mCSB_draggerContainer","mCSB_buttonUp","mCSB_buttonDown","mCSB_buttonLeft","mCSB_buttonRight"],aW={init:function(g){var g=d.extend(!0,{},aI,g),f=aT.call(this);
if(g.live){var h=g.liveSelector||this.selector||aS,i=d(h);
if("off"===g.live){return void aL(h)
}aH[h]=setTimeout(function(){i.mCustomScrollbar(g),"once"===g.live&&i.length&&aL(h)
},500)
}else{aL(h)
}return g.setWidth=g.set_width?g.set_width:g.setWidth,g.setHeight=g.set_height?g.set_height:g.setHeight,g.axis=g.horizontalScroll?"x":aU(g.axis),g.scrollInertia=g.scrollInertia>0&&g.scrollInertia<17?17:g.scrollInertia,"object"!=typeof g.mouseWheel&&1==g.mouseWheel&&(g.mouseWheel={enable:!0,scrollAmount:"auto",axis:"y",preventDefault:!1,deltaFactor:"auto",normalizeDelta:!1,invert:!1}),g.mouseWheel.scrollAmount=g.mouseWheelPixels?g.mouseWheelPixels:g.mouseWheel.scrollAmount,g.mouseWheel.normalizeDelta=g.advanced.normalizeMouseWheelDelta?g.advanced.normalizeMouseWheelDelta:g.mouseWheel.normalizeDelta,g.scrollButtons.scrollType=aF(g.scrollButtons.scrollType),aO(g),d(f).each(function(){var j=d(this);
if(!j.data(aN)){j.data(aN,{idx:++aP,opt:g,scrollRatio:{y:null,x:null},overflowed:null,contentReset:{y:null,x:null},bindEvents:!1,tweenRunning:!1,sequential:{},langDir:j.css("direction"),cbOffsets:null,trigger:null});
var n=j.data(aN),k=n.opt,m=j.data("mcs-axis"),l=j.data("mcs-scrollbar-position"),p=j.data("mcs-theme");
m&&(k.axis=m),l&&(k.scrollbarPosition=l),p&&(k.theme=p,aO(k)),aD.call(this),d("#mCSB_"+n.idx+"_container img:not(."+aG[2]+")").addClass(aG[2]),aW.update.call(null,j)
}})
},update:function(g,f){var h=g||aT.call(this);
return d(h).each(function(){var m=d(this);
if(m.data(aN)){var q=m.data(aN),k=q.opt,p=d("#mCSB_"+q.idx+"_container"),j=[d("#mCSB_"+q.idx+"_dragger_vertical"),d("#mCSB_"+q.idx+"_dragger_horizontal")];
if(!p.length){return
}q.tweenRunning&&ab(m),m.hasClass(aG[3])&&m.removeClass(aG[3]),m.hasClass(aG[4])&&m.removeClass(aG[4]),aZ.call(this),af.call(this),"y"===k.axis||k.advanced.autoExpandHorizontalScroll||p.css("width",a0(p.children())),q.overflowed=ad.call(this),ap.call(this),k.autoDraggerLength&&ax.call(this),aC.call(this),al.call(this);
var n=[Math.abs(p[0].offsetTop),Math.abs(p[0].offsetLeft)];
"x"!==k.axis&&(q.overflowed[0]?j[0].height()>j[0].parent().height()?aQ.call(this):(ah(m,n[0].toString(),{dir:"y",dur:0,overwrite:"none"}),q.contentReset.y=null):(aQ.call(this),"y"===k.axis?aj.call(this):"yx"===k.axis&&q.overflowed[1]&&ah(m,n[1].toString(),{dir:"x",dur:0,overwrite:"none"}))),"y"!==k.axis&&(q.overflowed[1]?j[1].width()>j[1].parent().width()?aQ.call(this):(ah(m,n[1].toString(),{dir:"x",dur:0,overwrite:"none"}),q.contentReset.x=null):(aQ.call(this),"x"===k.axis?aj.call(this):"yx"===k.axis&&q.overflowed[0]&&ah(m,n[0].toString(),{dir:"y",dur:0,overwrite:"none"}))),f&&q&&(2===f&&k.callbacks.onImageLoad&&"function"==typeof k.callbacks.onImageLoad?k.callbacks.onImageLoad.call(this):3===f&&k.callbacks.onSelectorChange&&"function"==typeof k.callbacks.onSelectorChange?k.callbacks.onSelectorChange.call(this):k.callbacks.onUpdate&&"function"==typeof k.callbacks.onUpdate&&k.callbacks.onUpdate.call(this)),t.call(this)
}})
},scrollTo:function(g,f){if("undefined"!=typeof g&&null!=g){var h=aT.call(this);
return d(h).each(function(){var q=d(this);
if(q.data(aN)){var k=q.data(aN),n=k.opt,j={trigger:"external",scrollInertia:n.scrollInertia,scrollEasing:"mcsEaseInOut",moveDragger:!1,timeout:60,callbacks:!0,onStart:!0,onUpdate:!0,onComplete:!0},m=d.extend(!0,{},j,f),u=aR.call(this,g),p=m.scrollInertia>0&&m.scrollInertia<17?17:m.scrollInertia;
u[0]=e.call(this,u[0],"y"),u[1]=e.call(this,u[1],"x"),m.moveDragger&&(u[0]*=k.scrollRatio.y,u[1]*=k.scrollRatio.x),m.dur=p,setTimeout(function(){null!==u[0]&&"undefined"!=typeof u[0]&&"x"!==n.axis&&k.overflowed[0]&&(m.dir="y",m.overwrite="all",ah(q,u[0].toString(),m)),null!==u[1]&&"undefined"!=typeof u[1]&&"y"!==n.axis&&k.overflowed[1]&&(m.dir="x",m.overwrite="none",ah(q,u[1].toString(),m))
},m.timeout)
}})
}},stop:function(){var f=aT.call(this);
return d(f).each(function(){var g=d(this);
g.data(aN)&&ab(g)
})
},disable:function(g){var f=aT.call(this);
return d(f).each(function(){var h=d(this);
if(h.data(aN)){h.data(aN);
t.call(this,"remove"),aj.call(this),g&&aQ.call(this),ap.call(this,!0),h.addClass(aG[3])
}})
},destroy:function(){var f=aT.call(this);
return d(f).each(function(){var h=d(this);
if(h.data(aN)){var j=h.data(aN),m=j.opt,g=d("#mCSB_"+j.idx),k=d("#mCSB_"+j.idx+"_container"),n=d(".mCSB_"+j.idx+"_scrollbar");
m.live&&aL(m.liveSelector||d(f).selector),t.call(this,"remove"),aj.call(this),aQ.call(this),h.removeData(aN),a(this,"mcs"),n.remove(),k.find("img."+aG[2]).removeClass(aG[2]),g.replaceWith(k.contents()),h.removeClass(aM+" _"+aN+"_"+j.idx+" "+aG[6]+" "+aG[7]+" "+aG[5]+" "+aG[3]).addClass(aG[4])
}})
}},aT=function(){return"object"!=typeof d(this)||d(this).length<1?aS:this
},aO=function(h){var f=["rounded","rounded-dark","rounded-dots","rounded-dots-dark"],k=["rounded-dots","rounded-dots-dark","3d","3d-dark","3d-thick","3d-thick-dark","inset","inset-dark","inset-2","inset-2-dark","inset-3","inset-3-dark"],l=["minimal","minimal-dark"],g=["minimal","minimal-dark"],j=["minimal","minimal-dark"];
h.autoDraggerLength=d.inArray(h.theme,f)>-1?!1:h.autoDraggerLength,h.autoExpandScrollbar=d.inArray(h.theme,k)>-1?!1:h.autoExpandScrollbar,h.scrollButtons.enable=d.inArray(h.theme,l)>-1?!1:h.scrollButtons.enable,h.autoHideScrollbar=d.inArray(h.theme,g)>-1?!0:h.autoHideScrollbar,h.scrollbarPosition=d.inArray(h.theme,j)>-1?"outside":h.scrollbarPosition
},aL=function(f){aH[f]&&(clearTimeout(aH[f]),a(aH,f))
},aU=function(f){return"yx"===f||"xy"===f||"auto"===f?"yx":"x"===f||"horizontal"===f?"x":"y"
},aF=function(f){return"stepped"===f||"pixels"===f||"step"===f||"click"===f?"stepped":"stepless"
},aD=function(){var B=d(this),A=B.data(aN),q=A.opt,j=q.autoExpandScrollbar?" "+aG[1]+"_expand":"",o=["<div id='mCSB_"+A.idx+"_scrollbar_vertical' class='mCSB_scrollTools mCSB_"+A.idx+"_scrollbar mCS-"+q.theme+" mCSB_scrollTools_vertical"+j+"'><div class='"+aG[12]+"'><div id='mCSB_"+A.idx+"_dragger_vertical' class='mCSB_dragger' style='position:absolute;' oncontextmenu='return false;'><div class='mCSB_dragger_bar' /></div><div class='mCSB_draggerRail' /></div></div>","<div id='mCSB_"+A.idx+"_scrollbar_horizontal' class='mCSB_scrollTools mCSB_"+A.idx+"_scrollbar mCS-"+q.theme+" mCSB_scrollTools_horizontal"+j+"'><div class='"+aG[12]+"'><div id='mCSB_"+A.idx+"_dragger_horizontal' class='mCSB_dragger' style='position:absolute;' oncontextmenu='return false;'><div class='mCSB_dragger_bar' /></div><div class='mCSB_draggerRail' /></div></div>"],C="yx"===q.axis?"mCSB_vertical_horizontal":"x"===q.axis?"mCSB_horizontal":"mCSB_vertical",z="yx"===q.axis?o[0]+o[1]:"x"===q.axis?o[1]:o[0],y="yx"===q.axis?"<div id='mCSB_"+A.idx+"_container_wrapper' class='mCSB_container_wrapper' />":"",x=q.autoHideScrollbar?" "+aG[6]:"",u="x"!==q.axis&&"rtl"===A.langDir?" "+aG[7]:"";
q.setWidth&&B.css("width",q.setWidth),q.setHeight&&B.css("height",q.setHeight),q.setLeft="y"!==q.axis&&"rtl"===A.langDir?"989999px":q.setLeft,B.addClass(aM+" _"+aN+"_"+A.idx+x+u).wrapInner("<div id='mCSB_"+A.idx+"' class='mCustomScrollBox mCS-"+q.theme+" "+C+"'><div id='mCSB_"+A.idx+"_container' class='mCSB_container' style='position:relative; top:"+q.setTop+"; left:"+q.setLeft+";' dir="+A.langDir+" /></div>");
var n=d("#mCSB_"+A.idx),k=d("#mCSB_"+A.idx+"_container");
"y"===q.axis||q.advanced.autoExpandHorizontalScroll||k.css("width",a0(k.children())),"outside"===q.scrollbarPosition?("static"===B.css("position")&&B.css("position","relative"),B.css("overflow","visible"),n.addClass("mCSB_outside").after(z)):(n.addClass("mCSB_inside").append(z),k.wrap(y)),aE.call(this);
var w=[d("#mCSB_"+A.idx+"_dragger_vertical"),d("#mCSB_"+A.idx+"_dragger_horizontal")];
w[0].css("min-height",w[0].height()),w[1].css("min-width",w[1].width())
},a0=function(f){return Math.max.apply(Math,f.map(function(){return d(this).outerWidth(!0)
}).get())
},af=function(){var h=d(this),f=h.data(aN),j=f.opt,g=d("#mCSB_"+f.idx+"_container");
j.advanced.autoExpandHorizontalScroll&&"y"!==j.axis&&g.css({position:"absolute",width:"auto"}).wrap("<div class='mCSB_h_wrapper' style='position:relative; left:0; width:999999px;' />").css({width:Math.ceil(g[0].getBoundingClientRect().right+0.4)-Math.floor(g[0].getBoundingClientRect().left),position:"relative"}).unwrap()
},aE=function(){var j=d(this),g=j.data(aN),n=g.opt,h=d(".mCSB_"+g.idx+"_scrollbar:first"),m=aV(n.scrollButtons.tabindex)?"tabindex='"+n.scrollButtons.tabindex+"'":"",f=["<a href='#' class='"+aG[13]+"' oncontextmenu='return false;' "+m+" />","<a href='#' class='"+aG[14]+"' oncontextmenu='return false;' "+m+" />","<a href='#' class='"+aG[15]+"' oncontextmenu='return false;' "+m+" />","<a href='#' class='"+aG[16]+"' oncontextmenu='return false;' "+m+" />"],k=["x"===n.axis?f[2]:f[0],"x"===n.axis?f[3]:f[1],f[2],f[3]];
n.scrollButtons.enable&&h.prepend(k[0]).append(k[1]).next(".mCSB_scrollTools").prepend(k[2]).append(k[3])
},aZ=function(){var j=d(this),g=j.data(aN),n=d("#mCSB_"+g.idx),h=j.css("max-height")||"none",m=-1!==h.indexOf("%"),f=j.css("box-sizing");
if("none"!==h){var k=m?j.parent().height()*parseInt(h)/100:parseInt(h);
"border-box"===f&&(k-=j.innerHeight()-j.height()+(j.outerHeight()-j.innerHeight())),n.css("max-height",Math.round(k))
}},ax=function(){var p=d(this),m=p.data(aN),g=d("#mCSB_"+m.idx),j=d("#mCSB_"+m.idx+"_container"),f=[d("#mCSB_"+m.idx+"_dragger_vertical"),d("#mCSB_"+m.idx+"_dragger_horizontal")],h=[g.height()/j.outerHeight(!1),g.width()/j.outerWidth(!1)],q=[parseInt(f[0].css("min-height")),Math.round(h[0]*f[0].parent().height()),parseInt(f[1].css("min-width")),Math.round(h[1]*f[1].parent().width())],k=aY&&q[1]<q[0]?q[0]:q[1],n=aY&&q[3]<q[2]?q[2]:q[3];
f[0].css({height:k,"max-height":f[0].parent().height()-10}).find(".mCSB_dragger_bar").css({"line-height":q[0]+"px"}),f[1].css({width:n,"max-width":f[1].parent().width()-10})
},aC=function(){var j=d(this),g=j.data(aN),n=d("#mCSB_"+g.idx),h=d("#mCSB_"+g.idx+"_container"),m=[d("#mCSB_"+g.idx+"_dragger_vertical"),d("#mCSB_"+g.idx+"_dragger_horizontal")],f=[h.outerHeight(!1)-n.height(),h.outerWidth(!1)-n.width()],k=[f[0]/(m[0].parent().height()-m[0].height()),f[1]/(m[1].parent().width()-m[1].width())];
g.scrollRatio={y:k[0],x:k[1]}
},ay=function(h,g,f){var i=f?aG[0]+"_expanded":"",j=h.closest(".mCSB_scrollTools");
"active"===g?(h.toggleClass(aG[0]+" "+i),j.toggleClass(aG[1]),h[0]._draggable=h[0]._draggable?0:1):h[0]._draggable||("hide"===g?(h.removeClass(aG[0]),j.removeClass(aG[1])):(h.addClass(aG[0]),j.addClass(aG[1])))
},ad=function(){var j=d(this),g=j.data(aN),m=d("#mCSB_"+g.idx),h=d("#mCSB_"+g.idx+"_container"),k=null==g.overflowed?h.height():h.outerHeight(!1),f=null==g.overflowed?h.width():h.outerWidth(!1);
return[k>m.height(),f>m.width()]
},aQ=function(){var j=d(this),g=j.data(aN),n=g.opt,h=d("#mCSB_"+g.idx),m=d("#mCSB_"+g.idx+"_container"),f=[d("#mCSB_"+g.idx+"_dragger_vertical"),d("#mCSB_"+g.idx+"_dragger_horizontal")];
if(ab(j),("x"!==n.axis&&!g.overflowed[0]||"y"===n.axis&&g.overflowed[0])&&(f[0].add(m).css("top",0),ah(j,"_resetY")),"y"!==n.axis&&!g.overflowed[1]||"x"===n.axis&&g.overflowed[1]){var k=dx=0;
"rtl"===g.langDir&&(k=h.width()-m.outerWidth(!1),dx=Math.abs(k/g.scrollRatio.x)),m.css("left",k),f[1].css("left",dx),ah(j,"_resetX")
}},al=function(){function h(){j=setTimeout(function(){d.event.special.mousewheel?(clearTimeout(j),aa.call(f[0])):h()
},100)
}var f=d(this),k=f.data(aN),g=k.opt;
if(!k.bindEvents){if(av.call(this),g.contentTouchScroll&&aw.call(this),am.call(this),g.mouseWheel.enable){var j;
h()
}ai.call(this),aq.call(this),g.advanced.autoScrollOnFocus&&aB.call(this),g.scrollButtons.enable&&ac.call(this),g.keyboard.enable&&au.call(this),k.bindEvents=!0
}},aj=function(){var h=d(this),m=h.data(aN),g=m.opt,k=aN+"_"+m.idx,f=".mCSB_"+m.idx+"_scrollbar",j=d("#mCSB_"+m.idx+",#mCSB_"+m.idx+"_container,#mCSB_"+m.idx+"_container_wrapper,"+f+" ."+aG[12]+",#mCSB_"+m.idx+"_dragger_vertical,#mCSB_"+m.idx+"_dragger_horizontal,"+f+">a"),n=d("#mCSB_"+m.idx+"_container");
g.advanced.releaseDraggableSelectors&&j.add(d(g.advanced.releaseDraggableSelectors)),m.bindEvents&&(d(b).unbind("."+k),j.each(function(){d(this).unbind("."+k)
}),clearTimeout(h[0]._focusTimeout),a(h[0],"_focusTimeout"),clearTimeout(m.sequential.step),a(m.sequential,"step"),clearTimeout(n[0].onCompleteTimeout),a(n[0],"onCompleteTimeout"),m.bindEvents=!1)
},ap=function(j){var g=d(this),n=g.data(aN),h=n.opt,m=d("#mCSB_"+n.idx+"_container_wrapper"),f=m.length?m:d("#mCSB_"+n.idx+"_container"),k=[d("#mCSB_"+n.idx+"_scrollbar_vertical"),d("#mCSB_"+n.idx+"_scrollbar_horizontal")],p=[k[0].find(".mCSB_dragger"),k[1].find(".mCSB_dragger")];
"x"!==h.axis&&(n.overflowed[0]&&!j?(k[0].add(p[0]).add(k[0].children("a")).css("display","block"),f.removeClass(aG[8]+" "+aG[10])):(h.alwaysShowScrollbar?(2!==h.alwaysShowScrollbar&&p[0].add(k[0].children("a")).css("display","none"),f.removeClass(aG[10])):(k[0].css("display","none"),f.addClass(aG[10])),f.addClass(aG[8]))),"y"!==h.axis&&(n.overflowed[1]&&!j?(k[1].add(p[1]).add(k[1].children("a")).css("display","block"),f.removeClass(aG[9]+" "+aG[11])):(h.alwaysShowScrollbar?(2!==h.alwaysShowScrollbar&&p[1].add(k[1].children("a")).css("display","none"),f.removeClass(aG[11])):(k[1].css("display","none"),f.addClass(aG[11])),f.addClass(aG[9]))),n.overflowed[0]||n.overflowed[1]?g.removeClass(aG[5]):g.addClass(aG[5])
},ag=function(h){var g=h.type;
switch(g){case"pointerdown":case"MSPointerDown":case"pointermove":case"MSPointerMove":case"pointerup":case"MSPointerUp":return[h.originalEvent.pageY,h.originalEvent.pageX,!1];
case"touchstart":case"touchmove":case"touchend":var f=h.originalEvent.touches[0]||h.originalEvent.changedTouches[0],i=h.originalEvent.touches.length||h.originalEvent.changedTouches.length;
return[f.pageY,f.pageX,i>1];
default:return[h.pageY,h.pageX,!1]
}},av=function(){function D(h){var g=k.find("iframe");
if(g.length){var f=h?"auto":"none";
g.css("pointer-events",f)
}}function n(i,g,f,l){if(k[0].idleTimer=A.scrollInertia<233?250:0,x.attr("id")===q[1]){var m="x",h=(x[0].offsetLeft-g+l)*C.scrollRatio.x
}else{var m="y",h=(x[0].offsetTop-i+f)*C.scrollRatio.y
}ah(E,h.toString(),{dir:m,drag:!0})
}var x,j,w,E=d(this),C=E.data(aN),A=C.opt,y=aN+"_"+C.idx,q=["mCSB_"+C.idx+"_dragger_vertical","mCSB_"+C.idx+"_dragger_horizontal"],k=d("#mCSB_"+C.idx+"_container"),z=d("#"+q[0]+",#"+q[1]),B=A.advanced.releaseDraggableSelectors?z.add(d(A.advanced.releaseDraggableSelectors)):z;
z.bind("mousedown."+y+" touchstart."+y+" pointerdown."+y+" MSPointerDown."+y,function(r){if(r.stopImmediatePropagation(),r.preventDefault(),aA(r)){aX=!0,aY&&(b.onselectstart=function(){return !1
}),D(!1),ab(E),x=d(this);
var F=x.offset(),g=ag(r)[0]-F.top,i=ag(r)[1]-F.left,f=x.height()+F.top,l=x.width()+F.left;
f>g&&g>0&&l>i&&i>0&&(j=g,w=i),ay(x,"active",A.autoExpandScrollbar)
}}).bind("touchmove."+y,function(h){h.stopImmediatePropagation(),h.preventDefault();
var g=x.offset(),f=ag(h)[0]-g.top,i=ag(h)[1]-g.left;
n(j,w,f,i)
}),d(b).bind("mousemove."+y+" pointermove."+y+" MSPointerMove."+y,function(h){if(x){var g=x.offset(),f=ag(h)[0]-g.top,i=ag(h)[1]-g.left;
if(j===f){return
}n(j,w,f,i)
}}).add(B).bind("mouseup."+y+" touchend."+y+" pointerup."+y+" MSPointerUp."+y,function(){x&&(ay(x,"active",A.autoExpandScrollbar),x=null),aX=!1,aY&&(b.onselectstart=null),D(!0)
})
},aw=function(){function F(h,g){var f=[1.5*g,2*g,g/1.5,g/2];
return h>90?g>4?f[0]:f[3]:h>60?g>3?f[3]:f[2]:h>30?g>8?f[1]:g>6?f[0]:g>4?g:f[2]:g>8?g:f[3]
}function X(k,h,f,l,m,g){k&&ah(R,k.toString(),{dur:h,scrollEasing:f,dir:l,overwrite:m,drag:g})
}var L,P,I,N,G,V,E,U,Q,M,K,R=d(this),D=R.data(aN),z=D.opt,Y=aN+"_"+D.idx,n=d("#mCSB_"+D.idx),A=d("#mCSB_"+D.idx+"_container"),W=[d("#mCSB_"+D.idx+"_dragger_vertical"),d("#mCSB_"+D.idx+"_dragger_horizontal")],H=[],q=[],J=0,j="yx"===z.axis?"none":"all",O=[];
A.bind("touchstart."+Y+" pointerdown."+Y+" MSPointerDown."+Y,function(g){if(aK(g)&&!aX&&!ag(g)[2]){var f=A.offset();
L=ag(g)[0]-f.top,P=ag(g)[1]-f.left,O=[ag(g)[0],ag(g)[1]]
}}).bind("touchmove."+Y+" pointermove."+Y+" MSPointerMove."+Y,function(p){if(aK(p)&&!aX&&!ag(p)[2]){p.stopImmediatePropagation(),V=ao();
var x=n.offset(),i=ag(p)[0]-x.top,g=ag(p)[1]-x.left,k="mcsLinearOut";
if(H.push(i),q.push(g),O[2]=Math.abs(ag(p)[0]-O[0]),O[3]=Math.abs(ag(p)[1]-O[1]),D.overflowed[0]){var y=W[0].parent().height()-W[0].height(),w=L-i>0&&i-L>-(y*D.scrollRatio.y)&&(2*O[3]<O[2]||"yx"===z.axis)
}if(D.overflowed[1]){var o=W[1].parent().width()-W[1].width(),m=P-g>0&&g-P>-(o*D.scrollRatio.x)&&(2*O[2]<O[3]||"yx"===z.axis)
}(w||m)&&p.preventDefault(),M="yx"===z.axis?[L-i,P-g]:"x"===z.axis?[null,P-g]:[L-i,null],A[0].idleTimer=250,D.overflowed[0]&&X(M[0],J,k,"y","all",!0),D.overflowed[1]&&X(M[1],J,k,"x",j,!0)
}}),n.bind("touchstart."+Y+" pointerdown."+Y+" MSPointerDown."+Y,function(g){if(aK(g)&&!aX&&!ag(g)[2]){g.stopImmediatePropagation(),ab(R),G=ao();
var f=n.offset();
I=ag(g)[0]-f.top,N=ag(g)[1]-f.left,H=[],q=[]
}}).bind("touchend."+Y+" pointerup."+Y+" MSPointerUp."+Y,function(u){if(aK(u)&&!aX&&!ag(u)[2]){u.stopImmediatePropagation(),E=ao();
var h=n.offset(),l=ag(u)[0]-h.top,p=ag(u)[1]-h.left;
if(!(E-V>30)){Q=1000/(E-G);
var r="mcsEaseOut",y=2.5>Q,x=y?[H[H.length-2],q[q.length-2]]:[0,0];
U=y?[l-x[0],p-x[1]]:[l-I,p-N];
var f=[Math.abs(U[0]),Math.abs(U[1])];
Q=y?[Math.abs(U[0]/4),Math.abs(U[1]/4)]:[Q,Q];
var m=[Math.abs(A[0].offsetTop)-U[0]*F(f[0]/Q[0],Q[0]),Math.abs(A[0].offsetLeft)-U[1]*F(f[1]/Q[1],Q[1])];
M="yx"===z.axis?[m[0],m[1]]:"x"===z.axis?[null,m[1]]:[m[0],null],K=[4*f[0]+z.scrollInertia,4*f[1]+z.scrollInertia];
var w=parseInt(z.contentTouchScroll)||0;
M[0]=f[0]>w?M[0]:0,M[1]=f[1]>w?M[1]:0,D.overflowed[0]&&X(M[0],K[0],r,"y",j,!1),D.overflowed[1]&&X(M[1],K[1],r,"x",j,!1)
}}})
},am=function(){function j(){return c.getSelection?c.getSelection().toString():b.selection&&"Control"!=b.selection.type?b.selection.createRange().text:0
}function p(i,h,f){y.type=f&&g?"stepped":"stepless",y.scrollAmount=10,aJ(n,i,h,"mcsLinearOut",f?60:null)
}var g,n=d(this),z=n.data(aN),x=z.opt,y=z.sequential,w=aN+"_"+z.idx,q=d("#mCSB_"+z.idx+"_container"),k=q.parent();
q.bind("mousedown."+w,function(){g||(g=1,aX=!0)
}).add(b).bind("mousemove."+w,function(i){if(g&&j()){var h=q.offset(),f=ag(i)[0]-h.top+q[0].offsetTop,l=ag(i)[1]-h.left+q[0].offsetLeft;
f>0&&f<k.height()&&l>0&&l<k.width()?y.step&&p("off",null,"stepped"):("x"!==x.axis&&z.overflowed[0]&&(0>f?p("on",38):f>k.height()&&p("on",40)),"y"!==x.axis&&z.overflowed[1]&&(0>l?p("on",37):l>k.width()&&p("on",39)))
}}).bind("mouseup."+w,function(){g&&(g=0,p("off",null)),aX=!1
})
},aa=function(){function p(r){var l=null;
try{var i=r.contentDocument||r.contentWindow.document;
l=i.body.innerHTML
}catch(u){}return null!==l
}var m=d(this),g=m.data(aN);
if(g){var j=g.opt,f=aN+"_"+g.idx,h=d("#mCSB_"+g.idx),q=[d("#mCSB_"+g.idx+"_dragger_vertical"),d("#mCSB_"+g.idx+"_dragger_horizontal")],k=d("#mCSB_"+g.idx+"_container").find("iframe"),n=h;
k.length&&k.each(function(){var i=this;
p(i)&&(n=n.add(d(i).contents().find("body")))
}),n.bind("mousewheel."+f,function(C,o){if(ab(m),!az(m,C.target)){var i="auto"!==j.mouseWheel.deltaFactor?parseInt(j.mouseWheel.deltaFactor):aY&&C.deltaFactor<100?100:C.deltaFactor||100;
if("x"===j.axis||"x"===j.mouseWheel.axis){var A="x",B=[Math.round(i*g.scrollRatio.x),parseInt(j.mouseWheel.scrollAmount)],z="auto"!==j.mouseWheel.scrollAmount?B[1]:B[0]>=h.width()?0.9*h.width():B[0],x=Math.abs(d("#mCSB_"+g.idx+"_container")[0].offsetLeft),w=q[1][0].offsetLeft,l=q[1].parent().width()-q[1].width(),y=C.deltaX||C.deltaY||o
}else{var A="y",B=[Math.round(i*g.scrollRatio.y),parseInt(j.mouseWheel.scrollAmount)],z="auto"!==j.mouseWheel.scrollAmount?B[1]:B[0]>=h.height()?0.9*h.height():B[0],x=Math.abs(d("#mCSB_"+g.idx+"_container")[0].offsetTop),w=q[0][0].offsetTop,l=q[0].parent().height()-q[0].height(),y=C.deltaY||o
}"y"===A&&!g.overflowed[0]||"x"===A&&!g.overflowed[1]||(j.mouseWheel.invert&&(y=-y),j.mouseWheel.normalizeDelta&&(y=0>y?-1:1),(y>0&&0!==w||0>y&&w!==l||j.mouseWheel.preventDefault)&&(C.stopImmediatePropagation(),C.preventDefault()),ah(m,(x-y*z).toString(),{dir:A}))
}})
}},az=function(h,f){var k=f.nodeName.toLowerCase(),g=h.data(aN).opt.mouseWheel.disableOver,j=["select","textarea"];
return d.inArray(k,g)>-1&&!(d.inArray(k,j)>-1&&!d(f).is(":focus"))
},ai=function(){var j=d(this),g=j.data(aN),m=aN+"_"+g.idx,h=d("#mCSB_"+g.idx+"_container"),k=h.parent(),f=d(".mCSB_"+g.idx+"_scrollbar ."+aG[12]);
f.bind("touchstart."+m+" pointerdown."+m+" MSPointerDown."+m,function(){aX=!0
}).bind("touchend."+m+" pointerup."+m+" MSPointerUp."+m,function(){aX=!1
}).bind("click."+m,function(r){if(d(r.target).hasClass(aG[12])||d(r.target).hasClass("mCSB_draggerRail")){ab(j);
var w=d(this),i=w.find(".mCSB_dragger");
if(w.parent(".mCSB_scrollTools_horizontal").length>0){if(!g.overflowed[1]){return
}var p="x",u=r.pageX>i.offset().left?-1:1,q=Math.abs(h[0].offsetLeft)-0.9*u*k.width()
}else{if(!g.overflowed[0]){return
}var p="y",u=r.pageY>i.offset().top?-1:1,q=Math.abs(h[0].offsetTop)-0.9*u*k.height()
}ah(j,q.toString(),{dir:p,scrollEasing:"mcsEaseInOut"})
}})
},aB=function(){var h=d(this),m=h.data(aN),g=m.opt,k=aN+"_"+m.idx,f=d("#mCSB_"+m.idx+"_container"),j=f.parent();
f.bind("focusin."+k,function(){var l=d(b.activeElement),p=f.find(".mCustomScrollBox").length,i=0;
l.is(g.advanced.autoScrollOnFocus)&&(ab(h),clearTimeout(h[0]._focusTimeout),h[0]._focusTimer=p?(i+17)*p:0,h[0]._focusTimeout=setTimeout(function(){var q=[ae(l)[0],ae(l)[1]],o=[f[0].offsetTop,f[0].offsetLeft],u=[o[0]+q[0]>=0&&o[0]+q[0]<j.height()-l.outerHeight(!1),o[1]+q[1]>=0&&o[0]+q[1]<j.width()-l.outerWidth(!1)],r="yx"!==g.axis||u[0]||u[1]?"all":"none";
"x"===g.axis||u[0]||ah(h,q[0].toString(),{dir:"y",scrollEasing:"mcsEaseInOut",overwrite:r,dur:i}),"y"===g.axis||u[1]||ah(h,q[1].toString(),{dir:"x",scrollEasing:"mcsEaseInOut",overwrite:r,dur:i})
},h[0]._focusTimer))
})
},aq=function(){var h=d(this),f=h.data(aN),j=aN+"_"+f.idx,g=d("#mCSB_"+f.idx+"_container").parent();
g.bind("scroll."+j,function(){(0!==g.scrollTop()||0!==g.scrollLeft())&&d(".mCSB_"+f.idx+"_scrollbar").css("visibility","hidden")
})
},ac=function(){var j=d(this),g=j.data(aN),n=g.opt,h=g.sequential,m=aN+"_"+g.idx,f=".mCSB_"+g.idx+"_scrollbar",k=d(f+">a");
k.bind("mousedown."+m+" touchstart."+m+" pointerdown."+m+" MSPointerDown."+m+" mouseup."+m+" touchend."+m+" pointerup."+m+" MSPointerUp."+m+" mouseout."+m+" pointerout."+m+" MSPointerOut."+m+" click."+m,function(p){function o(q,l){h.scrollAmount=n.snapAmount||n.scrollButtons.scrollAmount,aJ(j,q,l)
}if(p.preventDefault(),aA(p)){var i=d(this).attr("class");
switch(h.type=n.scrollButtons.scrollType,p.type){case"mousedown":case"touchstart":case"pointerdown":case"MSPointerDown":if("stepped"===h.type){return
}aX=!0,g.tweenRunning=!1,o("on",i);
break;
case"mouseup":case"touchend":case"pointerup":case"MSPointerUp":case"mouseout":case"pointerout":case"MSPointerOut":if("stepped"===h.type){return
}aX=!1,h.dir&&o("off",i);
break;
case"click":if("stepped"!==h.type||g.tweenRunning){return
}o("on",i)
}}})
},au=function(){var p=d(this),g=p.data(aN),j=g.opt,f=g.sequential,h=aN+"_"+g.idx,q=d("#mCSB_"+g.idx),m=d("#mCSB_"+g.idx+"_container"),k=m.parent(),n="input,textarea,select,datalist,keygen,[contenteditable='true']";
q.attr("tabindex","0").bind("blur."+h+" keydown."+h+" keyup."+h,function(y){function o(z,l){f.type=j.keyboard.scrollType,f.scrollAmount=j.snapAmount||j.keyboard.scrollAmount,"stepped"===f.type&&g.tweenRunning||aJ(p,z,l)
}switch(y.type){case"blur":g.tweenRunning&&f.dir&&o("off",null);
break;
case"keydown":case"keyup":var u=y.keyCode?y.keyCode:y.which,w="on";
if("x"!==j.axis&&(38===u||40===u)||"y"!==j.axis&&(37===u||39===u)){if((38===u||40===u)&&!g.overflowed[0]||(37===u||39===u)&&!g.overflowed[1]){return
}"keyup"===y.type&&(w="off"),d(b.activeElement).is(n)||(y.preventDefault(),y.stopImmediatePropagation(),o(w,u))
}else{if(33===u||34===u){if((g.overflowed[0]||g.overflowed[1])&&(y.preventDefault(),y.stopImmediatePropagation()),"keyup"===y.type){ab(p);
var r=34===u?-1:1;
if("x"===j.axis||"yx"===j.axis&&g.overflowed[1]&&!g.overflowed[0]){var i="x",x=Math.abs(m[0].offsetLeft)-0.9*r*k.width()
}else{var i="y",x=Math.abs(m[0].offsetTop)-0.9*r*k.height()
}ah(p,x.toString(),{dir:i,scrollEasing:"mcsEaseInOut"})
}}else{if((35===u||36===u)&&!d(b.activeElement).is(n)&&((g.overflowed[0]||g.overflowed[1])&&(y.preventDefault(),y.stopImmediatePropagation()),"keyup"===y.type)){if("x"===j.axis||"yx"===j.axis&&g.overflowed[1]&&!g.overflowed[0]){var i="x",x=35===u?Math.abs(k.width()-m.outerWidth(!1)):0
}else{var i="y",x=35===u?Math.abs(k.height()-m.outerHeight(!1)):0
}ah(p,x.toString(),{dir:i,scrollEasing:"mcsEaseInOut"})
}}}}})
},aJ=function(z,y,j,p,g){function n(B){var D="stepped"!==u.type,h=g?g:B?D?w.scrollInertia/1.5:w.scrollInertia:1000/60,i=B?D?7.5:40:2.5,G=[Math.abs(q[0].offsetTop),Math.abs(q[0].offsetLeft)],F=[x.scrollRatio.y>10?10:x.scrollRatio.y,x.scrollRatio.x>10?10:x.scrollRatio.x],l="x"===u.dir[0]?G[1]+u.dir[1]*F[1]*i:G[0]+u.dir[1]*F[0]*i,f="x"===u.dir[0]?G[1]+u.dir[1]*parseInt(u.scrollAmount):G[0]+u.dir[1]*parseInt(u.scrollAmount),r="auto"!==u.scrollAmount?f:l,E=p?p:B?D?"mcsLinearOut":"mcsEaseInOut":"mcsLinear",C=B?!0:!1;
return B&&17>h&&(r="x"===u.dir[0]?G[1]:G[0]),ah(z,r.toString(),{dir:u.dir[0],scrollEasing:E,dur:h,onComplete:C}),B?void (u.dir=!1):(clearTimeout(u.step),void (u.step=setTimeout(function(){n()
},h)))
}function A(){clearTimeout(u.step),a(u,"step"),ab(z)
}var x=z.data(aN),w=x.opt,u=x.sequential,q=d("#mCSB_"+x.idx+"_container"),k="stepped"===u.type?!0:!1;
switch(y){case"on":if(u.dir=[j===aG[16]||j===aG[15]||39===j||37===j?"x":"y",j===aG[13]||j===aG[15]||38===j||37===j?-1:1],ab(z),aV(j)&&"stepped"===u.type){return
}n(k);
break;
case"off":A(),(k||x.tweenRunning&&u.dir)&&n(!0)
}},aR=function(g){var f=d(this).data(aN).opt,h=[];
return"function"==typeof g&&(g=g()),g instanceof Array?h=g.length>1?[g[0],g[1]]:"x"===f.axis?[null,g[0]]:[g[0],null]:(h[0]=g.y?g.y:g.x||"x"===f.axis?null:g,h[1]=g.x?g.x:g.y||"y"===f.axis?null:g),"function"==typeof h[0]&&(h[0]=h[0]()),"function"==typeof h[1]&&(h[1]=h[1]()),h
},e=function(B,z){if(null!=B&&"undefined"!=typeof B){var j=d(this),q=j.data(aN),f=q.opt,n=d("#mCSB_"+q.idx+"_container"),C=n.parent(),y=typeof B;
z||(z="x"===f.axis?"x":"y");
var x="x"===z?n.outerWidth(!1):n.outerHeight(!1),A="x"===z?n[0].offsetLeft:n[0].offsetTop,w="x"===z?"left":"top";
switch(y){case"function":return B();
case"object":var k=B.jquery?B:d(B);
if(!k.length){return
}return"x"===z?ae(k)[1]:ae(k)[0];
case"string":case"number":if(aV(B)){return Math.abs(B)
}if(-1!==B.indexOf("%")){return Math.abs(x*parseInt(B)/100)
}if(-1!==B.indexOf("-=")){return Math.abs(A-parseInt(B.split("-=")[1]))
}if(-1!==B.indexOf("+=")){var g=A+parseInt(B.split("+=")[1]);
return g>=0?0:Math.abs(g)
}if(-1!==B.indexOf("px")&&aV(B.split("px")[0])){return Math.abs(B.split("px")[0])
}if("top"===B||"left"===B){return 0
}if("bottom"===B){return Math.abs(C.height()-n.outerHeight(!1))
}if("right"===B){return Math.abs(C.width()-n.outerWidth(!1))
}if("first"===B||"last"===B){var k=n.find(":"+B);
return"x"===z?ae(k)[1]:ae(k)[0]
}return d(B).length?"x"===z?ae(d(B))[1]:ae(d(B))[0]:(n.css(w,B),void aW.update.call(null,j[0]))
}}},t=function(q){function J(){clearTimeout(E[0].autoUpdate),E[0].autoUpdate=setTimeout(function(){return G.advanced.updateOnSelectorChange&&(B=y(),B!==f)?(C(3),void (f=B)):(G.advanced.updateOnContentResize&&(z=[E.outerHeight(!1),E.outerWidth(!1),n.height(),n.width(),K()[0],K()[1]],(z[0]!==k[0]||z[1]!==k[1]||z[2]!==k[2]||z[3]!==k[3]||z[4]!==k[4]||z[5]!==k[5])&&(C(z[0]!==k[0]||z[1]!==k[1]),k=z)),G.advanced.updateOnImageLoad&&(F=A(),F!==I&&(E.find("img").each(function(){D(this)
}),I=F)),void ((G.advanced.updateOnSelectorChange||G.advanced.updateOnContentResize||G.advanced.updateOnImageLoad)&&J()))
},60)
}function A(){var g=0;
return G.advanced.updateOnImageLoad&&(g=E.find("img").length),g
}function D(h){function g(o,m){return function(){return m.apply(o,arguments)
}
}function i(){this.onload=null,d(h).addClass(aG[2]),C(2)
}if(d(h).hasClass(aG[2])){return void C()
}var l=new Image;
l.onload=g(l,i),l.src=h.src
}function y(){G.advanced.updateOnSelectorChange===!0&&(G.advanced.updateOnSelectorChange="*");
var h=0,g=E.find(G.advanced.updateOnSelectorChange);
return G.advanced.updateOnSelectorChange&&g.length>0&&g.each(function(){h+=d(this).height()+d(this).width()
}),h
}function C(g){clearTimeout(E[0].autoUpdate),aW.update.call(null,u[0],g)
}var u=d(this),H=u.data(aN),G=H.opt,E=d("#mCSB_"+H.idx+"_container");
if(q){return clearTimeout(E[0].autoUpdate),void a(E[0],"autoUpdate")
}var B,z,F,n=E.parent(),j=[d("#mCSB_"+H.idx+"_scrollbar_vertical"),d("#mCSB_"+H.idx+"_scrollbar_horizontal")],K=function(){return[j[0].is(":visible")?j[0].outerHeight(!0):0,j[1].is(":visible")?j[1].outerWidth(!0):0]
},f=y(),k=[E.outerHeight(!1),E.outerWidth(!1),n.height(),n.width(),K()[0],K()[1]],I=A();
J()
},ak=function(h,g,f){return Math.round(h/g)*g-f
},ab=function(g){var f=g.data(aN),h=d("#mCSB_"+f.idx+"_container,#mCSB_"+f.idx+"_container_wrapper,#mCSB_"+f.idx+"_dragger_vertical,#mCSB_"+f.idx+"_dragger_horizontal");
h.each(function(){an.call(this)
})
},ah=function(D,U,I){function L(f){return E&&Q.callbacks[f]&&"function"==typeof Q.callbacks[f]
}function G(){return[Q.callbacks.alwaysTriggerOffsets||V>=k[0]+R,Q.callbacks.alwaysTriggerOffsets||-F>=V]
}function K(){var h=[M[0].offsetTop,M[0].offsetLeft],f=[A[0].offsetTop,A[0].offsetLeft],l=[M.outerHeight(!1),M.outerWidth(!1)],g=[O.height(),O.width()];
D[0].mcs={content:M,top:h[0],left:h[1],draggerTop:f[0],draggerLeft:f[1],topPct:Math.round(100*Math.abs(h[0])/(Math.abs(l[0])-g[0])),leftPct:Math.round(100*Math.abs(h[1])/(Math.abs(l[1])-g[1])),direction:I.dir}
}var E=D.data(aN),Q=E.opt,P={trigger:"internal",dir:"y",scrollEasing:"mcsEaseOut",drag:!1,dur:Q.scrollInertia,overwrite:"all",callbacks:!0,onStart:!0,onUpdate:!0,onComplete:!0},I=d.extend(P,I),B=[I.dur,I.drag?0:I.dur],O=d("#mCSB_"+E.idx),M=d("#mCSB_"+E.idx+"_container"),J=M.parent(),H=Q.callbacks.onTotalScrollOffset?aR.call(D,Q.callbacks.onTotalScrollOffset):[0,0],N=Q.callbacks.onTotalScrollBackOffset?aR.call(D,Q.callbacks.onTotalScrollBackOffset):[0,0];
if(E.trigger=I.trigger,(0!==J.scrollTop()||0!==J.scrollLeft())&&(d(".mCSB_"+E.idx+"_scrollbar").css("visibility","visible"),J.scrollTop(0).scrollLeft(0)),"_resetY"!==U||E.contentReset.y||(L("onOverflowYNone")&&Q.callbacks.onOverflowYNone.call(D[0]),E.contentReset.y=1),"_resetX"!==U||E.contentReset.x||(L("onOverflowXNone")&&Q.callbacks.onOverflowXNone.call(D[0]),E.contentReset.x=1),"_resetY"!==U&&"_resetX"!==U){switch(!E.contentReset.y&&D[0].mcs||!E.overflowed[0]||(L("onOverflowY")&&Q.callbacks.onOverflowY.call(D[0]),E.contentReset.x=null),!E.contentReset.x&&D[0].mcs||!E.overflowed[1]||(L("onOverflowX")&&Q.callbacks.onOverflowX.call(D[0]),E.contentReset.x=null),Q.snapAmount&&(U=ak(U,Q.snapAmount,Q.snapOffset)),I.dir){case"x":var A=d("#mCSB_"+E.idx+"_dragger_horizontal"),q="left",V=M[0].offsetLeft,k=[O.width()-M.outerWidth(!1),A.parent().width()-A.width()],z=[U,0===U?0:U/E.scrollRatio.x],R=H[1],F=N[1],n=R>0?R/E.scrollRatio.x:0,j=F>0?F/E.scrollRatio.x:0;
break;
case"y":var A=d("#mCSB_"+E.idx+"_dragger_vertical"),q="top",V=M[0].offsetTop,k=[O.height()-M.outerHeight(!1),A.parent().height()-A.height()],z=[U,0===U?0:U/E.scrollRatio.y],R=H[0],F=N[0],n=R>0?R/E.scrollRatio.y:0,j=F>0?F/E.scrollRatio.y:0
}z[1]<0||0===z[0]&&0===z[1]?z=[0,0]:z[1]>=k[1]?z=[k[0],k[1]]:z[0]=-z[0],D[0].mcs||(K(),L("onInit")&&Q.callbacks.onInit.call(D[0])),clearTimeout(M[0].onCompleteTimeout),(E.tweenRunning||!(0===V&&z[0]>=0||V===k[0]&&z[0]<=k[0]))&&(ar(A[0],q,Math.round(z[1]),B[1],I.scrollEasing),ar(M[0],q,Math.round(z[0]),B[0],I.scrollEasing,I.overwrite,{onStart:function(){I.callbacks&&I.onStart&&!E.tweenRunning&&(L("onScrollStart")&&(K(),Q.callbacks.onScrollStart.call(D[0])),E.tweenRunning=!0,ay(A),E.cbOffsets=G())
},onUpdate:function(){I.callbacks&&I.onUpdate&&L("whileScrolling")&&(K(),Q.callbacks.whileScrolling.call(D[0]))
},onComplete:function(){if(I.callbacks&&I.onComplete){"yx"===Q.axis&&clearTimeout(M[0].onCompleteTimeout);
var f=M[0].idleTimer||0;
M[0].onCompleteTimeout=setTimeout(function(){L("onScroll")&&(K(),Q.callbacks.onScroll.call(D[0])),L("onTotalScroll")&&z[1]>=k[1]-n&&E.cbOffsets[0]&&(K(),Q.callbacks.onTotalScroll.call(D[0])),L("onTotalScrollBack")&&z[1]<=j&&E.cbOffsets[1]&&(K(),Q.callbacks.onTotalScrollBack.call(D[0])),E.tweenRunning=!1,M[0].idleTimer=0,ay(A,"hide")
},f)
}}}))
}},ar=function(N,R,F,G,J,D,I){function A(){Q.stop||(T||E.call(),T=ao()-k,P(),T>=Q.time&&(Q.time=T>Q.time?T+K-(T-Q.time):T+K-1,Q.time<T+1&&(Q.time=T+1)),Q.time<G?Q.id=H(A):y.call())
}function P(){G>0?(Q.currVal=M(Q.time,j,B,G,J),q[R]=Math.round(Q.currVal)+"px"):q[R]=F+"px",L.call()
}function O(){K=1000/60,Q.time=T+K,H=c.requestAnimationFrame?c.requestAnimationFrame:function(f){return P(),setTimeout(f,0.01)
},Q.id=H(A)
}function z(){null!=Q.id&&(c.requestAnimationFrame?c.cancelAnimationFrame(Q.id):clearTimeout(Q.id),Q.id=null)
}function M(m,h,f,p,u){switch(u){case"linear":case"mcsLinear":return f*m/p+h;
case"mcsLinearOut":return m/=p,m--,f*Math.sqrt(1-m*m)+h;
case"easeInOutSmooth":return m/=p/2,1>m?f/2*m*m+h:(m--,-f/2*(m*(m-2)-1)+h);
case"easeInOutStrong":return m/=p/2,1>m?f/2*Math.pow(2,10*(m-1))+h:(m--,f/2*(-Math.pow(2,-10*m)+2)+h);
case"easeInOut":case"mcsEaseInOut":return m/=p/2,1>m?f/2*m*m*m+h:(m-=2,f/2*(m*m*m+2)+h);
case"easeOutSmooth":return m/=p,m--,-f*(m*m*m*m-1)+h;
case"easeOutStrong":return f*(-Math.pow(2,-10*m/p)+1)+h;
case"easeOut":case"mcsEaseOut":default:var g=(m/=p)*m,l=g*m;
return h+f*(0.499999999999997*l*g+-2.5*g*g+5.5*l+-6.5*g+4*m)
}}N._mTween||(N._mTween={top:{},left:{}});
var K,H,I=I||{},E=I.onStart||function(){},L=I.onUpdate||function(){},y=I.onComplete||function(){},k=ao(),T=0,j=N.offsetTop,q=N.style,Q=N._mTween[R];
"left"===R&&(j=N.offsetLeft);
var B=F-j;
Q.stop=0,"none"!==D&&z(),O()
},ao=function(){return c.performance&&c.performance.now?c.performance.now():c.performance&&c.performance.webkitNow?c.performance.webkitNow():Date.now?Date.now():(new Date).getTime()
},an=function(){var g=this;
g._mTween||(g._mTween={top:{},left:{}});
for(var f=["top","left"],h=0;
h<f.length;
h++){var i=f[h];
g._mTween[i].id&&(c.requestAnimationFrame?c.cancelAnimationFrame(g._mTween[i].id):clearTimeout(g._mTween[i].id),g._mTween[i].id=null,g._mTween[i].stop=1)
}},a=function(h,g){try{delete h[g]
}catch(f){h[g]=null
}},aA=function(f){return !(f.which&&1!==f.which)
},aK=function(g){var f=g.originalEvent.pointerType;
return !(f&&"touch"!==f&&2!==f)
},aV=function(f){return !isNaN(parseFloat(f))&&isFinite(f)
},ae=function(g){var f=g.parents(".mCSB_container");
return[g.offset().top-f.offset().top,g.offset().left-f.offset().left]
};
d.fn[aM]=function(f){return aW[f]?aW[f].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof f&&f?void d.error("Method "+f+" does not exist"):aW.init.apply(this,arguments)
},d[aM]=function(f){return aW[f]?aW[f].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof f&&f?void d.error("Method "+f+" does not exist"):aW.init.apply(this,arguments)
},d[aM].defaults=aI,c[aM]=!0,d(c).load(function(){d(aS)[aM](),d.extend(d.expr[":"],{mcsInView:d.expr[":"].mcsInView||function(h){var f,j,k=d(h),g=k.parents(".mCSB_container");
if(g.length){return f=g.parent(),j=[g[0].offsetTop,g[0].offsetLeft],j[0]+ae(k)[0]>=0&&j[0]+ae(k)[0]<f.height()-k.outerHeight(!1)&&j[1]+ae(k)[1]>=0&&j[1]+ae(k)[1]<f.width()-k.outerWidth(!1)
}},mcsOverflow:d.expr[":"].mcsOverflow||function(g){var f=d(g).data(aN);
if(f){return f.overflowed[0]||f.overflowed[1]
}}})
})
})
}(jQuery,window,document);
(function(k,q,d){function w(a,e){this.bodyOverflowX;
this.callbacks={hide:[],show:[]};
this.checkInterval=null;
this.Content;
this.$el=k(a);
this.$elProxy;
this.elProxyPosition;
this.enabled=true;
this.options=k.extend({},h,e);
this.mouseIsOverProxy=false;
this.namespace="tooltipster-"+Math.round(Math.random()*100000);
this.Status="hidden";
this.timerHide=null;
this.timerShow=null;
this.$tooltip;
this.options.iconTheme=this.options.iconTheme.replace(".","");
this.options.theme=this.options.theme.replace(".","");
this._init()
}function c(a,f){var e=true;
k.each(a,function(n,l){if(typeof f[n]==="undefined"||a[n]!==f[n]){e=false;
return false
}});
return e
}function j(){return !m&&p
}function g(){var n=d.body||d.documentElement,f=n.style,l="transition";
if(typeof f[l]=="string"){return true
}v=["Moz","Webkit","Khtml","O","ms"],l=l.charAt(0).toUpperCase()+l.substr(1);
for(var a=0;
a<v.length;
a++){if(typeof f[v[a]+l]=="string"){return true
}}return false
}var b="tooltipster",h={animation:"fade",arrow:true,arrowColor:"",autoClose:true,content:null,contentAsHTML:false,contentCloning:true,debug:true,delay:200,minWidth:0,maxWidth:null,functionInit:function(f,a){},functionBefore:function(f,a){a()
},functionReady:function(f,a){},functionAfter:function(a){},hideOnClick:false,icon:"(?)",iconCloning:true,iconDesktop:false,iconTouch:false,iconTheme:"tooltipster-icon",interactive:false,interactiveTolerance:350,multiple:false,offsetX:0,offsetY:0,onlyOne:false,position:"top",positionTracker:false,positionTrackerCallback:function(a){if(this.option("trigger")=="hover"&&this.option("autoClose")){this.hide()
}},restoration:"current",speed:350,timer:0,theme:"tooltipster-default",touchDevices:true,trigger:"hover",updateAnimation:true};
w.prototype={_init:function(){var e=this;
if(d.querySelector){var f=null;
if(e.$el.data("tooltipster-initialTitle")===undefined){f=e.$el.attr("title");
if(f===undefined){f=null
}e.$el.data("tooltipster-initialTitle",f)
}if(e.options.content!==null){e._content_set(e.options.content)
}else{e._content_set(f)
}var a=e.options.functionInit.call(e.$el,e.$el,e.Content);
if(typeof a!=="undefined"){e._content_set(a)
}e.$el.removeAttr("title").addClass("tooltipstered");
if(!p&&e.options.iconDesktop||p&&e.options.iconTouch){if(typeof e.options.icon==="string"){e.$elProxy=k('<span class="'+e.options.iconTheme+'"></span>');
e.$elProxy.text(e.options.icon)
}else{if(e.options.iconCloning){e.$elProxy=e.options.icon.clone(true)
}else{e.$elProxy=e.options.icon
}}e.$elProxy.insertAfter(e.$el)
}else{e.$elProxy=e.$el
}if(e.options.trigger=="hover"){e.$elProxy.on("mouseenter."+e.namespace,function(){if(!j()||e.options.touchDevices){e.mouseIsOverProxy=true;
e._show()
}}).on("mouseleave."+e.namespace,function(){if(!j()||e.options.touchDevices){e.mouseIsOverProxy=false
}});
if(p&&e.options.touchDevices){e.$elProxy.on("touchstart."+e.namespace,function(){e._showNow()
})
}}else{if(e.options.trigger=="click"){e.$elProxy.on("click."+e.namespace,function(){if(!j()||e.options.touchDevices){e._show()
}})
}}}},_show:function(){var a=this;
if(a.Status!="shown"&&a.Status!="appearing"){if(a.options.delay){a.timerShow=setTimeout(function(){if(a.options.trigger=="click"||a.options.trigger=="hover"&&a.mouseIsOverProxy){a._showNow()
}},a.options.delay)
}else{a._showNow()
}}},_showNow:function(e){var a=this;
a.options.functionBefore.call(a.$el,a.$el,function(){if(a.enabled&&a.Content!==null){if(e){a.callbacks.show.push(e)
}a.callbacks.hide=[];
clearTimeout(a.timerShow);
a.timerShow=null;
clearTimeout(a.timerHide);
a.timerHide=null;
if(a.options.onlyOne){k(".tooltipstered").not(a.$el).each(function(o,B){var A=k(B),f=A.data("tooltipster-ns");
k.each(f,function(F,D){var G=A.data(D),C=G.status(),E=G.option("autoClose");
if(C!=="hidden"&&C!=="disappearing"&&E){G.hide()
}})
})
}var n=function(){a.Status="shown";
k.each(a.callbacks.show,function(i,f){f.call(a.$el)
});
a.callbacks.show=[]
};
if(a.Status!=="hidden"){var t=0;
if(a.Status==="disappearing"){a.Status="appearing";
if(g()){a.$tooltip.clearQueue().removeClass("tooltipster-dying").addClass("tooltipster-"+a.options.animation+"-show");
if(a.options.speed>0){a.$tooltip.delay(a.options.speed)
}a.$tooltip.queue(n)
}else{a.$tooltip.stop().fadeIn(n)
}}else{if(a.Status==="shown"){n()
}}}else{a.Status="appearing";
var t=a.options.speed;
a.bodyOverflowX=k("body").css("overflow-x");
k("body").css("overflow-x","hidden");
var y="tooltipster-"+a.options.animation,l="-webkit-transition-duration: "+a.options.speed+"ms; -webkit-animation-duration: "+a.options.speed+"ms; -moz-transition-duration: "+a.options.speed+"ms; -moz-animation-duration: "+a.options.speed+"ms; -o-transition-duration: "+a.options.speed+"ms; -o-animation-duration: "+a.options.speed+"ms; -ms-transition-duration: "+a.options.speed+"ms; -ms-animation-duration: "+a.options.speed+"ms; transition-duration: "+a.options.speed+"ms; animation-duration: "+a.options.speed+"ms;",u=a.options.minWidth?"min-width:"+Math.round(a.options.minWidth)+"px;":"",z=a.options.maxWidth?"max-width:"+Math.round(a.options.maxWidth)+"px;":"",r=a.options.interactive?"pointer-events: auto;":"";
a.$tooltip=k('<div class="tooltipster-base '+a.options.theme+'" style="'+u+" "+z+" "+r+" "+l+'"><div class="tooltipster-content"></div></div>');
if(g()){a.$tooltip.addClass(y)
}a._content_insert();
a.$tooltip.appendTo("body");
a.reposition();
a.options.functionReady.call(a.$el,a.$el,a.$tooltip);
if(g()){a.$tooltip.addClass(y+"-show");
if(a.options.speed>0){a.$tooltip.delay(a.options.speed)
}a.$tooltip.queue(n)
}else{a.$tooltip.css("display","none").fadeIn(a.options.speed,n)
}a._interval_set();
k(q).on("scroll."+a.namespace+" resize."+a.namespace,function(){a.reposition()
});
if(a.options.autoClose){k("body").off("."+a.namespace);
if(a.options.trigger=="hover"){if(p){setTimeout(function(){k("body").on("touchstart."+a.namespace,function(){a.hide()
})
},0)
}if(a.options.interactive){if(p){a.$tooltip.on("touchstart."+a.namespace,function(f){f.stopPropagation()
})
}var x=null;
a.$elProxy.add(a.$tooltip).on("mouseleave."+a.namespace+"-autoClose",function(){clearTimeout(x);
x=setTimeout(function(){a.hide()
},a.options.interactiveTolerance)
}).on("mouseenter."+a.namespace+"-autoClose",function(){clearTimeout(x)
})
}else{a.$elProxy.on("mouseleave."+a.namespace+"-autoClose",function(){a.hide()
})
}if(a.options.hideOnClick){a.$elProxy.on("click."+a.namespace+"-autoClose",function(){a.hide()
})
}}else{if(a.options.trigger=="click"){setTimeout(function(){k("body").on("click."+a.namespace+" touchstart."+a.namespace,function(){a.hide()
})
},0);
if(a.options.interactive){a.$tooltip.on("click."+a.namespace+" touchstart."+a.namespace,function(f){f.stopPropagation()
})
}}}}}if(a.options.timer>0){a.timerHide=setTimeout(function(){a.timerHide=null;
a.hide()
},a.options.timer+t)
}}})
},_interval_set:function(){var a=this;
a.checkInterval=setInterval(function(){if(k("body").find(a.$el).length===0||k("body").find(a.$elProxy).length===0||a.Status=="hidden"||k("body").find(a.$tooltip).length===0){if(a.Status=="shown"||a.Status=="appearing"){a.hide()
}a._interval_cancel()
}else{if(a.options.positionTracker){var f=a._repositionInfo(a.$elProxy),e=false;
if(c(f.dimension,a.elProxyPosition.dimension)){if(a.$elProxy.css("position")==="fixed"){if(c(f.position,a.elProxyPosition.position)){e=true
}}else{if(c(f.offset,a.elProxyPosition.offset)){e=true
}}}if(!e){a.reposition();
a.options.positionTrackerCallback.call(a,a.$el)
}}}},200)
},_interval_cancel:function(){clearInterval(this.checkInterval);
this.checkInterval=null
},_content_set:function(a){if(typeof a==="object"&&a!==null&&this.options.contentCloning){a=a.clone(true)
}this.Content=a
},_content_insert:function(){var f=this,a=this.$tooltip.find(".tooltipster-content");
if(typeof f.Content==="string"&&!f.options.contentAsHTML){a.text(f.Content)
}else{a.empty().append(f.Content)
}},_update:function(f){var a=this;
a._content_set(f);
if(a.Content!==null){if(a.Status!=="hidden"){a._content_insert();
a.reposition();
if(a.options.updateAnimation){if(g()){a.$tooltip.css({width:"","-webkit-transition":"all "+a.options.speed+"ms, width 0ms, height 0ms, left 0ms, top 0ms","-moz-transition":"all "+a.options.speed+"ms, width 0ms, height 0ms, left 0ms, top 0ms","-o-transition":"all "+a.options.speed+"ms, width 0ms, height 0ms, left 0ms, top 0ms","-ms-transition":"all "+a.options.speed+"ms, width 0ms, height 0ms, left 0ms, top 0ms",transition:"all "+a.options.speed+"ms, width 0ms, height 0ms, left 0ms, top 0ms"}).addClass("tooltipster-content-changing");
setTimeout(function(){if(a.Status!="hidden"){a.$tooltip.removeClass("tooltipster-content-changing");
setTimeout(function(){if(a.Status!=="hidden"){a.$tooltip.css({"-webkit-transition":a.options.speed+"ms","-moz-transition":a.options.speed+"ms","-o-transition":a.options.speed+"ms","-ms-transition":a.options.speed+"ms",transition:a.options.speed+"ms"})
}},a.options.speed)
}},a.options.speed)
}else{a.$tooltip.fadeTo(a.options.speed,0.5,function(){if(a.Status!="hidden"){a.$tooltip.fadeTo(a.options.speed,1)
}})
}}}}else{a.hide()
}},_repositionInfo:function(a){return{dimension:{height:a.outerHeight(false),width:a.outerWidth(false)},offset:a.offset(),position:{left:parseInt(a.css("left")),top:parseInt(a.css("top"))}}
},hide:function(l){var f=this;
if(l){f.callbacks.hide.push(l)
}f.callbacks.show=[];
clearTimeout(f.timerShow);
f.timerShow=null;
clearTimeout(f.timerHide);
f.timerHide=null;
var a=function(){k.each(f.callbacks.hide,function(n,i){i.call(f.$el)
});
f.callbacks.hide=[]
};
if(f.Status=="shown"||f.Status=="appearing"){f.Status="disappearing";
var e=function(){f.Status="hidden";
if(typeof f.Content=="object"&&f.Content!==null){f.Content.detach()
}f.$tooltip.remove();
f.$tooltip=null;
k(q).off("."+f.namespace);
k("body").off("."+f.namespace).css("overflow-x",f.bodyOverflowX);
k("body").off("."+f.namespace);
f.$elProxy.off("."+f.namespace+"-autoClose");
f.options.functionAfter.call(f.$el,f.$el);
a()
};
if(g()){f.$tooltip.clearQueue().removeClass("tooltipster-"+f.options.animation+"-show").addClass("tooltipster-dying");
if(f.options.speed>0){f.$tooltip.delay(f.options.speed)
}f.$tooltip.queue(e)
}else{f.$tooltip.stop().fadeOut(f.options.speed,e)
}}else{if(f.Status=="hidden"){a()
}}return f
},show:function(a){this._showNow(a);
return this
},update:function(a){return this.content(a)
},content:function(a){if(typeof a==="undefined"){return this.Content
}else{this._update(a);
return this
}},reposition:function(){var aC=this;
if(k("body").find(aC.$tooltip).length!==0){aC.$tooltip.css("width","");
aC.elProxyPosition=aC._repositionInfo(aC.$elProxy);
var ay=null,aH=k(q).width(),ax=aC.elProxyPosition,aB=aC.$tooltip.outerWidth(false),aw=aC.$tooltip.innerWidth()+1,aO=aC.$tooltip.outerHeight(false);
if(aC.$elProxy.is("area")){var aK=aC.$elProxy.attr("shape"),aE=aC.$elProxy.parent().attr("name"),aM=k('img[usemap="#'+aE+'"]'),aI=aM.offset().left,aA=aM.offset().top,aL=aC.$elProxy.attr("coords")!==undefined?aC.$elProxy.attr("coords").split(","):undefined;
if(aK=="circle"){var av=parseInt(aL[0]),aD=parseInt(aL[1]),aJ=parseInt(aL[2]);
ax.dimension.height=aJ*2;
ax.dimension.width=aJ*2;
ax.offset.top=aA+aD-aJ;
ax.offset.left=aI+av-aJ
}else{if(aK=="rect"){var av=parseInt(aL[0]),aD=parseInt(aL[1]),ar=parseInt(aL[2]),aN=parseInt(aL[3]);
ax.dimension.height=aN-aD;
ax.dimension.width=ar-av;
ax.offset.top=aA+aD;
ax.offset.left=aI+av
}else{if(aK=="poly"){var au=[],al=[],Z=0,at=0,Y=0,ad=0,an="even";
for(var aF=0;
aF<aL.length;
aF++){var af=parseInt(aL[aF]);
if(an=="even"){if(af>Y){Y=af;
if(aF===0){Z=Y
}}if(af<Z){Z=af
}an="odd"
}else{if(af>ad){ad=af;
if(aF==1){at=ad
}}if(af<at){at=af
}an="even"
}}ax.dimension.height=ad-at;
ax.dimension.width=Y-Z;
ax.offset.top=aA+at;
ax.offset.left=aI+Z
}else{ax.dimension.height=aM.outerHeight(false);
ax.dimension.width=aM.outerWidth(false);
ax.offset.top=aA;
ax.offset.left=aI
}}}}var ap=0,ac=0,ae=0,aP=parseInt(aC.options.offsetY),am=parseInt(aC.options.offsetX),ab=aC.options.position;
function aj(){var a=k(q).scrollLeft();
if(ap-a<0){ay=ap-a;
ap=a
}if(ap+aB-a>aH){ay=ap-(aH+a-aB);
ap=aH+a-aB
}}function ao(f,a){if(ax.offset.top-k(q).scrollTop()-aO-aP-12<0&&a.indexOf("top")>-1){ab=f
}if(ax.offset.top+ax.dimension.height+aO+12+aP>k(q).scrollTop()+k(q).height()&&a.indexOf("bottom")>-1){ab=f;
ae=ax.offset.top-aO-aP-12
}}if(ab=="top"){var aG=ax.offset.left+aB-(ax.offset.left+ax.dimension.width);
ap=ax.offset.left+am-aG/2;
ae=ax.offset.top-aO-aP-12;
aj();
ao("bottom","top")
}if(ab=="top-left"){ap=ax.offset.left+am;
ae=ax.offset.top-aO-aP-12;
aj();
ao("bottom-left","top-left")
}if(ab=="top-right"){ap=ax.offset.left+ax.dimension.width+am-aB;
ae=ax.offset.top-aO-aP-12;
aj();
ao("bottom-right","top-right")
}if(ab=="bottom"){var aG=ax.offset.left+aB-(ax.offset.left+ax.dimension.width);
ap=ax.offset.left-aG/2+am;
ae=ax.offset.top+ax.dimension.height+aP+12;
aj();
ao("top","bottom")
}if(ab=="bottom-left"){ap=ax.offset.left+am;
ae=ax.offset.top+ax.dimension.height+aP+12;
aj();
ao("top-left","bottom-left")
}if(ab=="bottom-right"){ap=ax.offset.left+ax.dimension.width+am-aB;
ae=ax.offset.top+ax.dimension.height+aP+12;
aj();
ao("top-right","bottom-right")
}if(ab=="left"){ap=ax.offset.left-am-aB-12;
ac=ax.offset.left+am+ax.dimension.width+12;
var ak=ax.offset.top+aO-(ax.offset.top+ax.dimension.height);
ae=ax.offset.top-ak/2-aP;
if(ap<0&&ac+aB>aH){var ai=parseFloat(aC.$tooltip.css("border-width"))*2,az=aB+ap-ai;
aC.$tooltip.css("width",az+"px");
aO=aC.$tooltip.outerHeight(false);
ap=ax.offset.left-am-az-12-ai;
ak=ax.offset.top+aO-(ax.offset.top+ax.dimension.height);
ae=ax.offset.top-ak/2-aP
}else{if(ap<0){ap=ax.offset.left+am+ax.dimension.width+12;
ay="left"
}}}if(ab=="right"){ap=ax.offset.left+am+ax.dimension.width+12;
ac=ax.offset.left-am-aB-12;
var ak=ax.offset.top+aO-(ax.offset.top+ax.dimension.height);
ae=ax.offset.top-ak/2-aP;
if(ap+aB>aH&&ac<0){var ai=parseFloat(aC.$tooltip.css("border-width"))*2,az=aH-ap-ai;
aC.$tooltip.css("width",az+"px");
aO=aC.$tooltip.outerHeight(false);
ak=ax.offset.top+aO-(ax.offset.top+ax.dimension.height);
ae=ax.offset.top-ak/2-aP
}else{if(ap+aB>aH){ap=ax.offset.left-am-aB-12;
ay="right"
}}}if(aC.options.arrow){var aa="tooltipster-arrow-"+ab;
if(aC.options.arrowColor.length<1){var Q=aC.$tooltip.css("background-color")
}else{var Q=aC.options.arrowColor
}if(!ay){ay=""
}else{if(ay=="left"){aa="tooltipster-arrow-right";
ay=""
}else{if(ay=="right"){aa="tooltipster-arrow-left";
ay=""
}else{ay="left:"+Math.round(ay)+"px;"
}}}if(ab=="top"||ab=="top-left"||ab=="top-right"){var aq=parseFloat(aC.$tooltip.css("border-bottom-width")),t=aC.$tooltip.css("border-bottom-color")
}else{if(ab=="bottom"||ab=="bottom-left"||ab=="bottom-right"){var aq=parseFloat(aC.$tooltip.css("border-top-width")),t=aC.$tooltip.css("border-top-color")
}else{if(ab=="left"){var aq=parseFloat(aC.$tooltip.css("border-right-width")),t=aC.$tooltip.css("border-right-color")
}else{if(ab=="right"){var aq=parseFloat(aC.$tooltip.css("border-left-width")),t=aC.$tooltip.css("border-left-color")
}else{var aq=parseFloat(aC.$tooltip.css("border-bottom-width")),t=aC.$tooltip.css("border-bottom-color")
}}}}if(aq>1){aq++
}var e="";
if(aq!==0){var G="",ah="border-color: "+t+";";
if(aa.indexOf("bottom")!==-1){G="margin-top: -"+Math.round(aq)+"px;"
}else{if(aa.indexOf("top")!==-1){G="margin-bottom: -"+Math.round(aq)+"px;"
}else{if(aa.indexOf("left")!==-1){G="margin-right: -"+Math.round(aq)+"px;"
}else{if(aa.indexOf("right")!==-1){G="margin-left: -"+Math.round(aq)+"px;"
}}}}e='<span class="tooltipster-arrow-border" style="'+G+" "+ah+';"></span>'
}aC.$tooltip.find(".tooltipster-arrow").remove();
var ag='<div class="'+aa+' tooltipster-arrow" style="'+ay+'">'+e+'<span style="border-color:'+Q+';"></span></div>';
aC.$tooltip.append(ag)
}aC.$tooltip.css({top:Math.round(ae)+"px",left:Math.round(ap)+"px"})
}return aC
},enable:function(){this.enabled=true;
return this
},disable:function(){this.hide();
this.enabled=false;
return this
},destroy:function(){var a=this;
a.hide();
if(a.$el[0]!==a.$elProxy[0]){a.$elProxy.remove()
}a.$el.removeData(a.namespace).off("."+a.namespace);
var f=a.$el.data("tooltipster-ns");
if(f.length===1){var e=null;
if(a.options.restoration==="previous"){e=a.$el.data("tooltipster-initialTitle")
}else{if(a.options.restoration==="current"){e=typeof a.Content==="string"?a.Content:k("<div></div>").append(a.Content).html()
}}if(e){a.$el.attr("title",e)
}a.$el.removeClass("tooltipstered").removeData("tooltipster-ns").removeData("tooltipster-initialTitle")
}else{f=k.grep(f,function(i,l){return i!==a.namespace
});
a.$el.data("tooltipster-ns",f)
}return a
},elementIcon:function(){return this.$el[0]!==this.$elProxy[0]?this.$elProxy[0]:undefined
},elementTooltip:function(){return this.$tooltip?this.$tooltip[0]:undefined
},option:function(f,a){if(typeof a=="undefined"){return this.options[f]
}else{this.options[f]=a;
return this
}},status:function(){return this.Status
}};
k.fn[b]=function(){var y=arguments;
if(this.length===0){if(typeof y[0]==="string"){var C=true;
switch(y[0]){case"setDefaults":k.extend(h,y[1]);
break;
default:C=false;
break
}if(C){return true
}else{return this
}}else{return this
}}else{if(typeof y[0]==="string"){var z="#*$~&";
this.each(function(){var l=k(this).data("tooltipster-ns"),a=l?k(this).data(l[0]):null;
if(a){if(typeof a[y[0]]==="function"){var f=a[y[0]](y[1],y[2])
}else{throw new Error('Unknown method .tooltipster("'+y[0]+'")')
}if(f!==a){z=f;
return false
}}else{throw new Error("You called Tooltipster's \""+y[0]+'" method on an uninitialized element')
}});
return z!=="#*$~&"?z:this
}else{var B=[],x=y[0]&&typeof y[0].multiple!=="undefined",i=x&&y[0].multiple||!x&&h.multiple,A=y[0]&&typeof y[0].debug!=="undefined",e=A&&y[0].debug||!A&&h.debug;
this.each(function(){var l=false,f=k(this).data("tooltipster-ns"),a=null;
if(!f){l=true
}else{if(i){l=true
}else{if(e){console.log('Tooltipster: one or more tooltips are already attached to this element: ignoring. Use the "multiple" option to attach more tooltips.')
}}}if(l){a=new w(this,y[0]);
if(!f){f=[]
}f.push(a.namespace);
k(this).data("tooltipster-ns",f);
k(this).data(a.namespace,a)
}B.push(a)
});
if(i){return B
}else{return this
}}}};
var p=!!("ontouchstart" in q);
var m=false;
k("body").one("mousemove",function(){m=true
})
})(jQuery,window,document);
WebFontConfig={custom:{families:["trajan-pro-3-regular","trajan-pro-3-bold","charlemagne","Source Sans Pro","Source Sans Pro Semibold","va-icon"],urls:["/etc/designs/vatican/library/clientlibs/themes/homepage_popes/styles/font.css"]}};
var wf=document.createElement("script");
wf.src="/etc/designs/vatican/library/clientlibs/themes/homepage_popes/js/webfont.js";
wf.type="text/javascript";
wf.async="true";
var s=document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(wf,s);
jQuery(document).ready(function(){selectData();
dropdownLanguage();
if(jQuery.fn.tooltipster){$(".tooltip").tooltipster({position:"top",arrowColor:"#7B5534",delay:50,speed:200})
}Popes.init();
search();
tabber();
swiper("#update-attivita");
swiper("#update-novita");
swiper("#update-video")
});
Popes={options:{searchItem:".pope-name h2",selectorItem:".pope-item",selector:"#pope-scrollbar",searchFilterItem:"#pope-filter",selectorClickFilter:"#century .dropdown li a",filterClassSuffix:"-century",filterLabelSelector:"#active-centrury-filter"},$popesScrollbar:null,scrollOptions:{axis:"x",advanced:{autoExpandHorizontalScroll:true},callbacks:{onScroll:function(){Popes.lazyload()
},onUpdate:function(){Popes.lazyload()
}}},update:function(){this.lazyload();
this.$popesScrollbar.mCustomScrollbar("update")
},init:function(){this.$popesScrollbar=jQuery(this.options.selector);
this.initScrollBar();
this.lazyload();
this.filterByName();
this.filterByClass()
},initScrollBar:function(){this.$popesScrollbar.mCustomScrollbar(this.scrollOptions)
},scrollTo:function(a){this.$popesScrollbar.mCustomScrollbar("scrollTo",a)
},scrollToStart:function(a){this.scrollTo(0)
},filterByName:function(){var a=this;
jQuery(a.options.searchFilterItem).instaFilta({targets:a.options.searchItem,sections:a.options.selectorItem,beginsWith:true,callback:function(b){a.scrollToStart();
a.update()
}})
},filterByClass:function(){var a=this;
jQuery(a.options.selectorClickFilter).click(function(d){d.preventDefault();
var f=jQuery(this).attr("rel");
var c=jQuery(this).text();
if(typeof f!="undefined"&&f!="*"){f+=a.options.filterClassSuffix;
var b="."+f;
jQuery(a.options.selectorItem).show();
jQuery(a.options.selectorItem).not(b).hide();
a.update()
}else{jQuery(a.options.selectorItem).show();
Popes.update()
}jQuery(a.options.filterLabelSelector).text(c)
})
},lazyload:function(){jQuery("img.lazy").lazyload()
}};
function selectData(){var b=new Date();
var a=b.getMonth()+1;
jQuery("li[data-month="+a+"]").addClass("current")
}function dropdownLanguage(){var b=new language(jQuery("#language"));
var a=new language(jQuery("#century"));
jQuery(document).click(function(){jQuery(".wrapper-dropdown").removeClass("active")
})
}function faceBox(a){$(a+"-overlay").delay(1000).fadeIn("fast");
$(a).delay(1000).fadeIn("slow");
$(a+" .close").click(function(){$(a+"-overlay").fadeOut("fast");
$(a).hide()
})
}function language(a){this.dropdown=a;
this.initEvents()
}language.prototype={initEvents:function(){var a=this;
a.dropdown.on("click",function(b){jQuery(this).toggleClass("active");
b.stopPropagation()
})
}};
function search(){var a=jQuery("#va-search"),d=a.find("input.va-search-input"),e=jQuery("html,body"),c=function(){a.data("open",true).addClass("va-search-open");
d.focus();
jQuery(".wrapper-dropdown").removeClass("active");
return false
},b=function(){a.data("open",false).removeClass("va-search-open")
};
d.on("click",function(f){f.stopPropagation();
a.data("open",true)
}).placeholder();
a.on("click",function(f){f.stopPropagation();
if(!a.data("open")){c();
e.off("click").on("click",function(g){b()
})
}else{if(d.val()===""){b();
return false
}}})
}function tabber(){jQuery(".update .tabs a").on("click",function(){jQuery(".update .tabs li.current").removeClass("current");
jQuery(this).parent().addClass("current");
jQuery(".update .panel.current").removeClass("current");
var b=jQuery(jQuery(this).attr("href"));
b.addClass("current");
var a=jQuery(this);
if(b.attr("id")=="update-foto"){if(typeof window.pageLang!="undefined"){photogalleryAjaxList(window.pageLang)
}}else{if(b.attr("id")=="update-video"){videoLiveAjax()
}}return false
})
}function jsonGalleryList(d){if(d){var b=0;
var a=d.list;
var c="en";
if(typeof window.pageLang!="undefined"&&window.pageLang==="it"){c="it"
}jQuery(".panel.type-foto").html("");
jQuery.each(a,function(e,g){if(b<2){jQuery(".panel.type-foto").append('<article><a href="'+g.link+'"><img width="80" height="80" src="'+g.firstImgMini+'"><h2>'+g.title+"</h2></a></article>");
b++
}else{var f=getGalleryTranslation();
jQuery(".panel.type-foto").append('<article><a href="https://www.vatican.va/content/photogallery/'+window.pageLang+'/papi/franciscus.html"><img width="80" height="80" src="/content/dam/vatican/homepage/image/gallery_franciscus.png"><h2>FRANCISCUS</h2></a></article>');
jQuery(".panel.type-foto").append('<article><a href="https://www.vatican.va/content/photogallery/'+window.pageLang+'.html"><img width="80" height="80" src="/content/dam/vatican/homepage/image/photogallery_home.png"><h2>'+f+'</h2></a></article><a href="https://photo.vaticanmedia.va/'+c+'/" target="_blank"><img class="vm-button-img" src="/etc/designs/vatican/library/images/buttons/button-vm-'+c+'.png" alt="Photo Vatican Media"></a>');
b++;
return false
}})
}}function videoLiveAjax(){if(jQuery(".panel.type-video #video-container iframe").length==0){jQuery.ajax({type:"GET",dataType:"jsonp",jsonpCallback:"jsonLiveTv",url:"https://www.comunicazione.va/it/servizi/live.properties.js",success:function(c,a,b){if(c){var d=c.prop.video;
jQuery(".panel.type-video #video-container").html('<iframe width="470" height="300" frameborder="0" allowfullscreen="" src="'+d+'"></iframe>')
}}})
}}function photogalleryAjaxList(a){if(jQuery(".panel.type-foto article").length==0){jQuery.ajax({type:"GET",dataType:"jsonp",jsonpCallback:"jsonGalleryList",url:"/content/vatican/"+a+".photogallery.js",error:function(b,d,c){},complete:function(b,c){jQuery(".panel div").animate({scrollTop:0},"slow")
}})
}}function swiper(a){jQuery(a+" .custom-swiper-container").cycle({fx:"fade",slides:"> .swiper-slide",pauseOnHover:true,speed:300,swipe:true,timeout:8000,pause:false,updateView:1,pager:a+" .swiper-pagination"})
}function twitterAjax(a){jQuery.ajax({type:"GET",dataType:"jsonp",jsonpCallback:"jsonTwitter",url:"/content/twitter/"+a+"/_jcr_content/innertop-1/twitterchannel.js",success:function(d,b,c){if(d){var e=d.data;
jQuery(".twitter div").html(e[0].html+' <a href="'+e[0].link+'" target="_blank">'+e[0].name+"</a>")
}},error:function(b,d,c){},complete:function(b,c){jQuery(".twitter div").marquee("twitterMarquee").on("selectstart",false).mouseover(function(){jQuery(this).trigger("stop")
}).mouseout(function(){jQuery(this).trigger("start")
}).mousemove(function(d){if(jQuery(this).data("drag")==true){this.scrollLeft=jQuery(this).data("scrollX")+(jQuery(this).data("x")-d.clientX)
}}).mousedown(function(d){jQuery(this).data("drag",true).data("x",d.clientX).data("scrollX",this.scrollLeft)
}).mouseup(function(){jQuery(this).data("drag",false)
})
}})
}function getGalleryTranslation(){var a="All Galleries";
if($(".panel.panel-scroll.type-foto#update-foto").length>0){a=$(".panel.panel-scroll.type-foto#update-foto").attr("translate")
}return a
}
/*! http://mths.be/placeholder v2.0.7 by @mathias */
(function(i,k,f){var b=Object.prototype.toString.call(i.operamini)=="[object OperaMini]";
var a="placeholder" in k.createElement("input")&&!b;
var g="placeholder" in k.createElement("textarea")&&!b;
var l=f.fn;
var e=f.valHooks;
var c=f.propHooks;
var n;
var m;
if(a&&g){m=l.placeholder=function(){return this
};
m.input=m.textarea=true
}else{m=l.placeholder=function(){var p=this;
p.filter((a?"textarea":":input")+"[placeholder]").not(".placeholder").bind({"focus.placeholder":d,"blur.placeholder":h}).data("placeholder-enabled",true).trigger("blur.placeholder");
return p
};
m.input=a;
m.textarea=g;
n={get:function(q){var p=f(q);
var r=p.data("placeholder-password");
if(r){return r[0].value
}return p.data("placeholder-enabled")&&p.hasClass("placeholder")?"":q.value
},set:function(q,t){var p=f(q);
var r=p.data("placeholder-password");
if(r){return r[0].value=t
}if(!p.data("placeholder-enabled")){return q.value=t
}if(t==""){q.value=t;
if(q!=o()){h.call(q)
}}else{if(p.hasClass("placeholder")){d.call(q,true,t)||(q.value=t)
}else{q.value=t
}}return p
}};
if(!a){e.input=n;
c.value=n
}if(!g){e.textarea=n;
c.value=n
}f(function(){f(k).delegate("form","submit.placeholder",function(){var p=f(".placeholder",this).each(d);
setTimeout(function(){p.each(h)
},10)
})
});
f(i).bind("beforeunload.placeholder",function(){f(".placeholder").each(function(){this.value=""
})
})
}function j(q){var p={};
var r=/^jQuery\d+$/;
f.each(q.attributes,function(u,t){if(t.specified&&!r.test(t.name)){p[t.name]=t.value
}});
return p
}function d(q,r){var p=this;
var t=f(p);
if(p.value==t.attr("placeholder")&&t.hasClass("placeholder")){if(t.data("placeholder-password")){t=t.hide().next().show().attr("id",t.removeAttr("id").data("placeholder-id"));
if(q===true){return t[0].value=r
}t.focus()
}else{p.value="";
t.removeClass("placeholder");
p==o()&&p.select()
}}}function h(){var u;
var p=this;
var t=f(p);
var r=this.id;
if(p.value==""){if(p.type=="password"){if(!t.data("placeholder-textinput")){try{u=t.clone().attr({type:"text"})
}catch(q){u=f("<input>").attr(f.extend(j(this),{type:"text"}))
}u.removeAttr("name").data({"placeholder-password":t,"placeholder-id":r}).bind("focus.placeholder",d);
t.data({"placeholder-textinput":u,"placeholder-id":r}).before(u)
}t=t.removeAttr("id").hide().prev().attr("id",r).show()
}t.addClass("placeholder");
t[0].value=t.attr("placeholder")
}else{t.removeClass("placeholder")
}}function o(){try{return k.activeElement
}catch(p){}}}(this,document,jQuery));
function css_browser_selector(g){var y=g.toLowerCase(),u=function(a){return y.indexOf(a)>-1
},t="gecko",o="webkit",c="safari",q="chrome",x="opera",w="mobile",m=0,z=window.devicePixelRatio?(window.devicePixelRatio+"").replace(".","_"):"1";
var r=[(!(/opera|webtv/.test(y))&&/msie\s(\d+)/.test(y)&&(m=RegExp.$1*1))?("ie ie"+m+((m==6||m==7)?" ie67 ie678 ie6789":(m==8)?" ie678 ie6789":(m==9)?" ie6789 ie9m":(m>9)?" ie9m":"")):(/trident\/\d+.*?;\s*rv:(\d+)\.(\d+)\)/.test(y)&&(m=[RegExp.$1,RegExp.$2]))?"ie ie"+m[0]+" ie"+m[0]+"_"+m[1]+" ie9m":(/firefox\/(\d+)\.(\d+)/.test(y)&&(re=RegExp))?t+" ff ff"+re.$1+" ff"+re.$1+"_"+re.$2:u("gecko/")?t:u(x)?x+(/version\/(\d+)/.test(y)?" "+x+RegExp.$1:(/opera(\s|\/)(\d+)/.test(y)?" "+x+RegExp.$2:"")):u("konqueror")?"konqueror":u("blackberry")?w+" blackberry":(u(q)||u("crios"))?o+" "+q:u("iron")?o+" iron":!u("cpu os")&&u("applewebkit/")?o+" "+c:u("mozilla/")?t:"",u("android")?w+" android":"",u("tablet")?"tablet":"",u("j2me")?w+" j2me":u("ipad; u; cpu os")?w+" chrome android tablet":u("ipad;u;cpu os")?w+" chromedef android tablet":u("iphone")?w+" ios iphone":u("ipod")?w+" ios ipod":u("ipad")?w+" ios ipad tablet":u("mac")?"mac":u("darwin")?"mac":u("webtv")?"webtv":u("win")?"win"+(u("windows nt 6.0")?" vista":""):u("freebsd")?"freebsd":(u("x11")||u("linux"))?"linux":"",(z!="1")?" retina ratio"+z:"","js portrait"].join(" ");
if(window.jQuery&&!window.jQuery.browser){window.jQuery.browser=m?{msie:1,version:m}:{}
}return r
}(function(i,d){var n=css_browser_selector(navigator.userAgent);
var k=i.documentElement;
k.className+=" "+n;
var h=n.replace(/^\s*|\s*$/g,"").split(/ +/);
d.CSSBS=1;
for(var l=0;
l<h.length;
l++){d["CSSBS_"+h[l]]=1
}var m=function(a){return i.documentElement[a]||i.body[a]
};
if(d.jQuery){(function(b){var j="portrait",f="landscape";
var g="smartnarrow",A="smartwide",t="tabletnarrow",a="tabletwide",y=g+" "+A+" "+t+" "+a+" pc";
var z=b(k);
var B=0,c=0;
function p(){if(B!=0){return
}try{var q=m("clientWidth"),r=m("clientHeight");
if(q>r){z.removeClass(j).addClass(f)
}else{z.removeClass(f).addClass(j)
}if(q==c){return
}c=q
}catch(o){}B=setTimeout(e,100)
}function e(){try{z.removeClass(y);
z.addClass((c<=360)?g:(c<=640)?A:(c<=768)?t:(c<=1024)?a:"pc")
}catch(o){}B=0
}if(d.CSSBS_ie){setInterval(p,1000)
}else{b(d).on("resize orientationchange",p).trigger("resize")
}})(d.jQuery)
}})(document,window);
/*!
* jQuery Cycle2; version: 2.1.3 build: 20140314
* http://jquery.malsup.com/cycle2/
* Copyright (c) 2014 M. Alsup; Dual licensed: MIT/GPL
*/
(function(c){function b(d){return(d||"").toLowerCase()
}var a="2.1.2";
c.fn.cycle=function(d){var e;
return 0!==this.length||c.isReady?this.each(function(){var m,h,j,k,g=c(this),i=c.fn.cycle.log;
if(!g.data("cycle.opts")){(g.data("cycle-log")===!1||d&&d.log===!1||h&&h.log===!1)&&(i=c.noop),i("--c2 init--"),m=g.data();
for(var f in m){m.hasOwnProperty(f)&&/^cycle[A-Z]+/.test(f)&&(k=m[f],j=f.match(/^cycle(.*)/)[1].replace(/^[A-Z]/,b),i(j+":",k,"("+typeof k+")"),m[j]=k)
}h=c.extend({},c.fn.cycle.defaults,m,d||{}),h.timeoutId=0,h.paused=h.paused||!1,h.container=g,h._maxZ=h.maxZ,h.API=c.extend({_container:g},c.fn.cycle.API),h.API.log=i,h.API.trigger=function(n,l){return h.container.trigger(n,l),h.API
},g.data("cycle.opts",h),g.data("cycle.API",h.API),h.API.trigger("cycle-bootstrap",[h,h.API]),h.API.addInitialSlides(),h.API.preInitSlideshow(),h.slides.length&&h.API.initSlideshow()
}}):(e={s:this.selector,c:this.context},c.fn.cycle.log("requeuing slideshow (dom not ready)"),c(function(){c(e.s,e.c).cycle(d)
}),this)
},c.fn.cycle.API={opts:function(){return this._container.data("cycle.opts")
},addInitialSlides:function(){var e=this.opts(),d=e.slides;
e.slideCount=0,e.slides=c(),d=d.jquery?d:e.container.find(d),e.random&&d.sort(function(){return Math.random()-0.5
}),e.API.add(d)
},preInitSlideshow:function(){var e=this.opts();
e.API.trigger("cycle-pre-initialize",[e]);
var d=c.fn.cycle.transitions[e.fx];
d&&c.isFunction(d.preInit)&&d.preInit(e),e._preInitialized=!0
},postInitSlideshow:function(){var e=this.opts();
e.API.trigger("cycle-post-initialize",[e]);
var d=c.fn.cycle.transitions[e.fx];
d&&c.isFunction(d.postInit)&&d.postInit(e)
},initSlideshow:function(){var e,d=this.opts(),f=d.container;
d.API.calcFirstSlide(),"static"==d.container.css("position")&&d.container.css("position","relative"),c(d.slides[d.currSlide]).css({opacity:1,display:"block",visibility:"visible"}),d.API.stackSlides(d.slides[d.currSlide],d.slides[d.nextSlide],!d.reverse),d.pauseOnHover&&(d.pauseOnHover!==!0&&(f=c(d.pauseOnHover)),f.hover(function(){d.API.pause(!0)
},function(){d.API.resume(!0)
})),d.timeout&&(e=d.API.getSlideOpts(d.currSlide),d.API.queueTransition(e,e.timeout+d.delay)),d._initialized=!0,d.API.updateView(!0),d.API.trigger("cycle-initialized",[d]),d.API.postInitSlideshow()
},pause:function(e){var d=this.opts(),g=d.API.getSlideOpts(),f=d.hoverPaused||d.paused;
e?d.hoverPaused=!0:d.paused=!0,f||(d.container.addClass("cycle-paused"),d.API.trigger("cycle-paused",[d]).log("cycle-paused"),g.timeout&&(clearTimeout(d.timeoutId),d.timeoutId=0,d._remainingTimeout-=c.now()-d._lastQueue,(0>d._remainingTimeout||isNaN(d._remainingTimeout))&&(d._remainingTimeout=void 0)))
},resume:function(g){var f=this.opts(),d=!f.hoverPaused&&!f.paused;
g?f.hoverPaused=!1:f.paused=!1,d||(f.container.removeClass("cycle-paused"),0===f.slides.filter(":animated").length&&f.API.queueTransition(f.API.getSlideOpts(),f._remainingTimeout),f.API.trigger("cycle-resumed",[f,f._remainingTimeout]).log("cycle-resumed"))
},add:function(e,d){var j,f=this.opts(),g=f.slideCount,h=!1;
"string"==c.type(e)&&(e=c.trim(e)),c(e).each(function(){var i,k=c(this);
d?f.container.prepend(k):f.container.append(k),f.slideCount++,i=f.API.buildSlideOpts(k),f.slides=d?c(k).add(f.slides):f.slides.add(k),f.API.initSlide(i,k,--f._maxZ),k.data("cycle.opts",i),f.API.trigger("cycle-slide-added",[f,i,k])
}),f.API.updateView(!0),h=f._preInitialized&&2>g&&f.slideCount>=1,h&&(f._initialized?f.timeout&&(j=f.slides.length,f.nextSlide=f.reverse?j-1:1,f.timeoutId||f.API.queueTransition(f)):f.API.initSlideshow())
},calcFirstSlide:function(){var f,d=this.opts();
f=parseInt(d.startingSlide||0,10),(f>=d.slides.length||0>f)&&(f=0),d.currSlide=f,d.reverse?(d.nextSlide=f-1,0>d.nextSlide&&(d.nextSlide=d.slides.length-1)):(d.nextSlide=f+1,d.nextSlide==d.slides.length&&(d.nextSlide=0))
},calcNextSlide:function(){var f,d=this.opts();
d.reverse?(f=0>d.nextSlide-1,d.nextSlide=f?d.slideCount-1:d.nextSlide-1,d.currSlide=f?0:d.nextSlide+1):(f=d.nextSlide+1==d.slides.length,d.nextSlide=f?0:d.nextSlide+1,d.currSlide=f?d.slides.length-1:d.nextSlide-1)
},calcTx:function(e,d){var g,f=e;
return d&&f.manualFx&&(g=c.fn.cycle.transitions[f.manualFx]),g||(g=c.fn.cycle.transitions[f.fx]),g||(g=c.fn.cycle.transitions.fade,f.API.log('Transition "'+f.fx+'" not found.  Using fade.')),g
},prepareTx:function(j,g){var f,p,h,k,m,d=this.opts();
return 2>d.slideCount?(d.timeoutId=0,void 0):(!j||d.busy&&!d.manualTrump||(d.API.stopTransition(),d.busy=!1,clearTimeout(d.timeoutId),d.timeoutId=0),d.busy||(0!==d.timeoutId||j)&&(p=d.slides[d.currSlide],h=d.slides[d.nextSlide],k=d.API.getSlideOpts(d.nextSlide),m=d.API.calcTx(k,j),d._tx=m,j&&void 0!==k.manualSpeed&&(k.speed=k.manualSpeed),d.nextSlide!=d.currSlide&&(j||!d.paused&&!d.hoverPaused&&d.timeout)?(d.API.trigger("cycle-before",[k,p,h,g]),m.before&&m.before(k,p,h,g),f=function(){d.busy=!1,d.container.data("cycle.opts")&&(m.after&&m.after(k,p,h,g),d.API.trigger("cycle-after",[k,p,h,g]),d.API.queueTransition(k),d.API.updateView(!0))
},d.busy=!0,m.transition?m.transition(k,p,h,g,f):d.API.doTransition(k,p,h,g,f),d.API.calcNextSlide(),d.API.updateView()):d.API.queueTransition(k)),void 0)
},doTransition:function(m,h,f,p,e){var j=m,g=c(h),d=c(f),k=function(){d.animate(j.animIn||{opacity:1},j.speed,j.easeIn||j.easing,e)
};
d.css(j.cssBefore||{}),g.animate(j.animOut||{},j.speed,j.easeOut||j.easing,function(){g.css(j.cssAfter||{}),j.sync||k()
}),j.sync&&k()
},queueTransition:function(e,d){var g=this.opts(),f=void 0!==d?d:e.timeout;
return 0===g.nextSlide&&0===--g.loop?(g.API.log("terminating; loop=0"),g.timeout=0,f?setTimeout(function(){g.API.trigger("cycle-finished",[g])
},f):g.API.trigger("cycle-finished",[g]),g.nextSlide=g.currSlide,void 0):void 0!==g.continueAuto&&(g.continueAuto===!1||c.isFunction(g.continueAuto)&&g.continueAuto()===!1)?(g.API.log("terminating automatic transitions"),g.timeout=0,g.timeoutId&&clearTimeout(g.timeoutId),void 0):(f&&(g._lastQueue=c.now(),void 0===d&&(g._remainingTimeout=e.timeout),g.paused||g.hoverPaused||(g.timeoutId=setTimeout(function(){g.API.prepareTx(!1,!g.reverse)
},f))),void 0)
},stopTransition:function(){var d=this.opts();
d.slides.filter(":animated").length&&(d.slides.stop(!1,!0),d.API.trigger("cycle-transition-stopped",[d])),d._tx&&d._tx.stopTransition&&d._tx.stopTransition(d)
},advanceSlide:function(f){var d=this.opts();
return clearTimeout(d.timeoutId),d.timeoutId=0,d.nextSlide=d.currSlide+f,0>d.nextSlide?d.nextSlide=d.slides.length-1:d.nextSlide>=d.slides.length&&(d.nextSlide=0),d.API.prepareTx(!0,f>=0),!1
},buildSlideOpts:function(e){var k,f,h=this.opts(),j=e.data()||{};
for(var d in j){j.hasOwnProperty(d)&&/^cycle[A-Z]+/.test(d)&&(k=j[d],f=d.match(/^cycle(.*)/)[1].replace(/^[A-Z]/,b),h.API.log("["+(h.slideCount-1)+"]",f+":",k,"("+typeof k+")"),j[f]=k)
}j=c.extend({},c.fn.cycle.defaults,h,j),j.slideNum=h.slideCount;
try{delete j.API,delete j.slideCount,delete j.currSlide,delete j.nextSlide,delete j.slides
}catch(g){}return j
},getSlideOpts:function(e){var d=this.opts();
void 0===e&&(e=d.currSlide);
var g=d.slides[e],f=c(g).data("cycle.opts");
return c.extend({},d,f)
},initSlide:function(e,d,g){var f=this.opts();
d.css(e.slideCss||{}),g>0&&d.css("zIndex",g),isNaN(e.speed)&&(e.speed=c.fx.speeds[e.speed]||c.fx.speeds._default),e.sync||(e.speed=e.speed/2),d.addClass(f.slideClass)
},updateView:function(h,f){var d=this.opts();
if(d._initialized){var j=d.API.getSlideOpts(),g=d.slides[d.currSlide];
!h&&f!==!0&&(d.API.trigger("cycle-update-view-before",[d,j,g]),0>d.updateView)||(d.slideActiveClass&&d.slides.removeClass(d.slideActiveClass).eq(d.currSlide).addClass(d.slideActiveClass),h&&d.hideNonActive&&d.slides.filter(":not(."+d.slideActiveClass+")").css("visibility","hidden"),0===d.updateView&&setTimeout(function(){d.API.trigger("cycle-update-view",[d,j,g,h])
},j.speed/(d.sync?2:1)),0!==d.updateView&&d.API.trigger("cycle-update-view",[d,j,g,h]),h&&d.API.trigger("cycle-update-view-after",[d,j,g]))
}},getComponent:function(e){var d=this.opts(),f=d[e];
return"string"==typeof f?/^\s*[\>|\+|~]/.test(f)?d.container.find(f):c(f):f.jquery?f:c(f)
},stackSlides:function(f,e,k){var g=this.opts();
f||(f=g.slides[g.currSlide],e=g.slides[g.nextSlide],k=!g.reverse),c(f).css("zIndex",g.maxZ);
var h,j=g.maxZ-2,d=g.slideCount;
if(k){for(h=g.currSlide+1;
d>h;
h++){c(g.slides[h]).css("zIndex",j--)
}for(h=0;
g.currSlide>h;
h++){c(g.slides[h]).css("zIndex",j--)
}}else{for(h=g.currSlide-1;
h>=0;
h--){c(g.slides[h]).css("zIndex",j--)
}for(h=d-1;
h>g.currSlide;
h--){c(g.slides[h]).css("zIndex",j--)
}}c(e).css("zIndex",g.maxZ-1)
},getSlideIndex:function(d){return this.opts().slides.index(d)
}},c.fn.cycle.log=function(){window.console&&console.log&&console.log("[cycle2] "+Array.prototype.join.call(arguments," "))
},c.fn.cycle.version=function(){return"Cycle2: "+a
},c.fn.cycle.transitions={custom:{},none:{before:function(g,f,d,h){g.API.stackSlides(d,f,h),g.cssBefore={opacity:1,visibility:"visible",display:"block"}
}},fade:{before:function(e,d,h,f){var g=e.API.getSlideOpts(e.nextSlide).slideCss||{};
e.API.stackSlides(d,h,f),e.cssBefore=c.extend(g,{opacity:0,visibility:"visible",display:"block"}),e.animIn={opacity:1},e.animOut={opacity:0}
}},fadeout:{before:function(e,d,h,f){var g=e.API.getSlideOpts(e.nextSlide).slideCss||{};
e.API.stackSlides(d,h,f),e.cssBefore=c.extend(g,{opacity:1,visibility:"visible",display:"block"}),e.animOut={opacity:0}
}},scrollHorz:{before:function(h,f,d,j){h.API.stackSlides(f,d,j);
var g=h.container.css("overflow","hidden").width();
h.cssBefore={left:j?g:-g,top:0,opacity:1,visibility:"visible",display:"block"},h.cssAfter={zIndex:h._maxZ-2,left:0},h.animIn={left:0},h.animOut={left:j?-g:g}
}}},c.fn.cycle.defaults={allowWrap:!0,autoSelector:".cycle-slideshow[data-cycle-auto-init!=false]",delay:0,easing:null,fx:"fade",hideNonActive:!0,loop:0,manualFx:void 0,manualSpeed:void 0,manualTrump:!0,maxZ:100,pauseOnHover:!1,reverse:!1,slideActiveClass:"cycle-slide-active",slideClass:"cycle-slide",slideCss:{position:"absolute",top:0,left:0},slides:"> img",speed:500,startingSlide:0,sync:!0,timeout:4000,updateView:0},c(document).ready(function(){c(c.fn.cycle.defaults.autoSelector).cycle()
})
})(jQuery),
/*! Cycle2 autoheight plugin; Copyright (c) M.Alsup, 2012; version: 20130913 */
function(d){function b(g,k){var h,i,j,e=k.autoHeight;
if("container"==e){i=d(k.slides[k.currSlide]).outerHeight(),k.container.height(i)
}else{if(k._autoHeightRatio){k.container.height(k.container.width()/k._autoHeightRatio)
}else{if("calc"===e||"number"==d.type(e)&&e>=0){if(j="calc"===e?a(g,k):e>=k.slides.length?0:e,j==k._sentinelIndex){return
}k._sentinelIndex=j,k._sentinel&&k._sentinel.remove(),h=d(k.slides[j].cloneNode(!0)),h.removeAttr("id name rel").find("[id],[name],[rel]").removeAttr("id name rel"),h.css({position:"static",visibility:"hidden",display:"block"}).prependTo(k.container).addClass("cycle-sentinel cycle-slide").removeClass("cycle-slide-active"),h.find("*").css("visibility","hidden"),k._sentinel=h
}}}}function a(g,e){var j=0,h=-1;
return e.slides.each(function(l){var k=d(this).height();
k>h&&(h=k,j=l)
}),j
}function f(g,e,k,h){var j=d(h).outerHeight();
e.container.animate({height:j},e.autoHeightSpeed,e.autoHeightEasing)
}function c(e,g){g._autoHeightOnResize&&(d(window).off("resize orientationchange",g._autoHeightOnResize),g._autoHeightOnResize=null),g.container.off("cycle-slide-added cycle-slide-removed",b),g.container.off("cycle-destroyed",c),g.container.off("cycle-before",f),g._sentinel&&(g._sentinel.remove(),g._sentinel=null)
}d.extend(d.fn.cycle.defaults,{autoHeight:0,autoHeightSpeed:250,autoHeightEasing:null}),d(document).on("cycle-initialized",function(h,m){function n(){b(h,m)
}var g,j=m.autoHeight,e=d.type(j),k=null;
("string"===e||"number"===e)&&(m.container.on("cycle-slide-added cycle-slide-removed",b),m.container.on("cycle-destroyed",c),"container"==j?m.container.on("cycle-before",f):"string"===e&&/\d+\:\d+/.test(j)&&(g=j.match(/(\d+)\:(\d+)/),g=g[1]/g[2],m._autoHeightRatio=g),"number"!==e&&(m._autoHeightOnResize=function(){clearTimeout(k),k=setTimeout(n,50)
},d(window).on("resize orientationchange",m._autoHeightOnResize)),setTimeout(n,30))
})
}(jQuery),
/*! caption plugin for Cycle2;  version: 20130306 */
function(a){a.extend(a.fn.cycle.defaults,{caption:"> .cycle-caption",captionTemplate:"{{slideNum}} / {{slideCount}}",overlay:"> .cycle-overlay",overlayTemplate:"<div>{{title}}</div><div>{{desc}}</div>",captionModule:"caption"}),a(document).on("cycle-update-view",function(c,b,e,d){"caption"===b.captionModule&&a.each(["caption","overlay"],function(){var g=this,f=e[g+"Template"],h=b.API.getComponent(g);
h.length&&f?(h.html(b.API.tmpl(f,e,b,d)),h.show()):h.hide()
})
}),a(document).on("cycle-destroyed",function(c,b){var d;
a.each(["caption","overlay"],function(){var g=this,f=b[g+"Template"];
b[g]&&f&&(d=b.API.getComponent("caption"),d.empty())
})
})
}(jQuery),
/*! command plugin for Cycle2;  version: 20130707 */
function(b){var a=b.fn.cycle;
b.fn.cycle=function(d){var h,e,f,g=b.makeArray(arguments);
return"number"==b.type(d)?this.cycle("goto",d):"string"==b.type(d)?this.each(function(){var c;
return h=d,f=b(this).data("cycle.opts"),void 0===f?(a.log('slideshow must be initialized before sending commands; "'+h+'" ignored'),void 0):(h="goto"==h?"jump":h,e=f.API[h],b.isFunction(e)?(c=b.makeArray(g),c.shift(),e.apply(f.API,c)):(a.log("unknown command: ",h),void 0))
}):a.apply(this,arguments)
},b.extend(b.fn.cycle,a),b.extend(a.API,{next:function(){var d=this.opts();
if(!d.busy||d.manualTrump){var c=d.reverse?-1:1;
d.allowWrap===!1&&d.currSlide+c>=d.slideCount||(d.API.advanceSlide(c),d.API.trigger("cycle-next",[d]).log("cycle-next"))
}},prev:function(){var d=this.opts();
if(!d.busy||d.manualTrump){var c=d.reverse?1:-1;
d.allowWrap===!1&&0>d.currSlide+c||(d.API.advanceSlide(c),d.API.trigger("cycle-prev",[d]).log("cycle-prev"))
}},destroy:function(){this.stop();
var d=this.opts(),c=b.isFunction(b._data)?b._data:b.noop;
clearTimeout(d.timeoutId),d.timeoutId=0,d.API.stop(),d.API.trigger("cycle-destroyed",[d]).log("cycle-destroyed"),d.container.removeData(),c(d.container[0],"parsedAttrs",!1),d.retainStylesOnDestroy||(d.container.removeAttr("style"),d.slides.removeAttr("style"),d.slides.removeClass(d.slideActiveClass)),d.slides.each(function(){b(this).removeData(),c(this,"parsedAttrs",!1)
})
},jump:function(f){var d,c=this.opts();
if(!c.busy||c.manualTrump){var g=parseInt(f,10);
if(isNaN(g)||0>g||g>=c.slides.length){return c.API.log("goto: invalid slide index: "+g),void 0
}if(g==c.currSlide){return c.API.log("goto: skipping, already on slide",g),void 0
}c.nextSlide=g,clearTimeout(c.timeoutId),c.timeoutId=0,c.API.log("goto: ",g," (zero-index)"),d=c.currSlide<c.nextSlide,c.API.prepareTx(!0,d)
}},stop:function(){var d=this.opts(),c=d.container;
clearTimeout(d.timeoutId),d.timeoutId=0,d.API.stopTransition(),d.pauseOnHover&&(d.pauseOnHover!==!0&&(c=b(d.pauseOnHover)),c.off("mouseenter mouseleave")),d.API.trigger("cycle-stopped",[d]).log("cycle-stopped")
},reinit:function(){var c=this.opts();
c.API.destroy(),c.container.cycle()
},remove:function(f){for(var e,k,g=this.opts(),h=[],j=1,d=0;
g.slides.length>d;
d++){e=g.slides[d],d==f?k=e:(h.push(e),b(e).data("cycle.opts").slideNum=j,j++)
}k&&(g.slides=b(h),g.slideCount--,b(k).remove(),f==g.currSlide?g.API.advanceSlide(1):g.currSlide>f?g.currSlide--:g.currSlide++,g.API.trigger("cycle-slide-removed",[g,f,k]).log("cycle-slide-removed"),g.API.updateView())
}}),b(document).on("click.cycle","[data-cycle-cmd]",function(d){d.preventDefault();
var c=b(this),f=c.data("cycle-cmd"),e=c.data("cycle-context")||".cycle-slideshow";
b(e).cycle(f,c.data("cycle-arg"))
})
}(jQuery),
/*! hash plugin for Cycle2;  version: 20130905 */
function(b){function a(d,c){var e;
return d._hashFence?(d._hashFence=!1,void 0):(e=window.location.hash.substring(1),d.slides.each(function(f){if(b(this).data("cycle-hash")==e){if(c===!0){d.startingSlide=f
}else{var g=f>d.currSlide;
d.nextSlide=f,d.API.prepareTx(!0,g)
}return !1
}}),void 0)
}b(document).on("cycle-pre-initialize",function(c,d){a(d,!0),d._onHashChange=function(){a(d,!1)
},b(window).on("hashchange",d._onHashChange)
}),b(document).on("cycle-update-view",function(f,d,c){c.hash&&"#"+c.hash!=window.location.hash&&(d._hashFence=!0,window.location.hash=c.hash)
}),b(document).on("cycle-destroyed",function(d,c){c._onHashChange&&b(window).off("hashchange",c._onHashChange)
})
}(jQuery),
/*! loader plugin for Cycle2;  version: 20131121 */
function(a){a.extend(a.fn.cycle.defaults,{loader:!1}),a(document).on("cycle-bootstrap",function(c,b){function e(h,m){function j(l){var n;
"wait"==b.loader?(g.push(l),0===f&&(g.sort(k),d.apply(b.API,[g,m]),b.container.removeClass("cycle-loading"))):(n=a(b.slides[b.currSlide]),d.apply(b.API,[l,m]),n.show(),b.container.removeClass("cycle-loading"))
}function k(n,l){return n.data("index")-l.data("index")
}var g=[];
if("string"==a.type(h)){h=a.trim(h)
}else{if("array"===a.type(h)){for(var i=0;
h.length>i;
i++){h[i]=a(h[i])[0]
}}}h=a(h);
var f=h.length;
f&&(h.css("visibility","hidden").appendTo("body").each(function(n){function q(){0===--o&&(--f,j(p))
}var o=0,p=a(this),l=p.is("img")?p:p.find("img");
return p.data("index",n),l=l.filter(":not(.cycle-loader-ignore)").filter(':not([src=""])'),l.length?(o=l.length,l.each(function(){this.complete?q():a(this).load(function(){q()
}).on("error",function(){0===--o&&(b.API.log("slide skipped; img not loaded:",this.src),0===--f&&"wait"==b.loader&&d.apply(b.API,[g,m]))
})
}),void 0):(--f,g.push(p),void 0)
}),f&&b.container.addClass("cycle-loading"))
}var d;
b.loader&&(d=b.API.add,b.API.add=e)
})
}(jQuery),
/*! pager plugin for Cycle2;  version: 20140324 */
function(c){function b(e,d,h){var f,g=e.API.getComponent("pager");
g.each(function(){var i=c(this);
if(d.pagerTemplate){var j=e.API.tmpl(d.pagerTemplate,d,e,h[0]);
f=c(j).appendTo(i)
}else{f=i.children().eq(e.slideCount-1)
}f.on(e.pagerEvent,function(k){e.pagerEventBubble||k.preventDefault(),e.API.page(i,k.currentTarget)
})
})
}function a(h,f){var d=this.opts();
if(!d.busy||d.manualTrump){var k=h.children().index(f),g=k,j=g>d.currSlide;
d.currSlide!=g&&(d.nextSlide=g,d.API.prepareTx(!0,j),d.API.trigger("cycle-pager-activated",[d,h,f]))
}}c.extend(c.fn.cycle.defaults,{pager:"> .cycle-pager",pagerActiveClass:"cycle-pager-active",pagerEvent:"click.cycle",pagerEventBubble:void 0,pagerTemplate:"<span>&bull;</span>"}),c(document).on("cycle-bootstrap",function(f,d,g){g.buildPagerLink=b
}),c(document).on("cycle-slide-added",function(g,d,h,f){d.pager&&(d.API.buildPagerLink(d,h,f),d.API.page=a)
}),c(document).on("cycle-slide-removed",function(e,d,g){if(d.pager){var f=d.API.getComponent("pager");
f.each(function(){var h=c(this);
c(h.children()[g]).remove()
})
}}),c(document).on("cycle-update-view",function(e,d){var f;
d.pager&&(f=d.API.getComponent("pager"),f.each(function(){c(this).children().removeClass(d.pagerActiveClass).eq(d.currSlide).addClass(d.pagerActiveClass)
}))
}),c(document).on("cycle-destroyed",function(g,f){var d=f.API.getComponent("pager");
d&&(d.children().off(f.pagerEvent),f.pagerTemplate&&d.empty())
})
}(jQuery),
/*! prevnext plugin for Cycle2;  version: 20130709 */
function(a){a.extend(a.fn.cycle.defaults,{next:"> .cycle-next",nextEvent:"click.cycle",disabledClass:"disabled",prev:"> .cycle-prev",prevEvent:"click.cycle",swipe:!1}),a(document).on("cycle-initialized",function(d,c){if(c.API.getComponent("next").on(c.nextEvent,function(g){g.preventDefault(),c.API.next()
}),c.API.getComponent("prev").on(c.prevEvent,function(g){g.preventDefault(),c.API.prev()
}),c.swipe){var b=c.swipeVert?"swipeUp.cycle":"swipeLeft.cycle swipeleft.cycle",f=c.swipeVert?"swipeDown.cycle":"swipeRight.cycle swiperight.cycle";
c.container.on(b,function(){c.API.next()
}),c.container.on(f,function(){c.API.prev()
})
}}),a(document).on("cycle-update-view",function(g,d){if(!d.allowWrap){var b=d.disabledClass,k=d.API.getComponent("next"),f=d.API.getComponent("prev"),h=d._prevBoundry||0,j=void 0!==d._nextBoundry?d._nextBoundry:d.slideCount-1;
d.currSlide==j?k.addClass(b).prop("disabled",!0):k.removeClass(b).prop("disabled",!1),d.currSlide===h?f.addClass(b).prop("disabled",!0):f.removeClass(b).prop("disabled",!1)
}}),a(document).on("cycle-destroyed",function(c,b){b.API.getComponent("prev").off(b.nextEvent),b.API.getComponent("next").off(b.prevEvent),b.container.off("swipeleft.cycle swiperight.cycle swipeLeft.cycle swipeRight.cycle swipeUp.cycle swipeDown.cycle")
})
}(jQuery),
/*! progressive loader plugin for Cycle2;  version: 20130315 */
function(a){a.extend(a.fn.cycle.defaults,{progressive:!1}),a(document).on("cycle-pre-initialize",function(p,h){if(h.progressive){var f,q,e=h.API,k=e.next,g=e.prev,b=e.prepareTx,m=a.type(h.progressive);
if("array"==m){f=h.progressive
}else{if(a.isFunction(h.progressive)){f=h.progressive(h)
}else{if("string"==m){if(q=a(h.progressive),f=a.trim(q.html()),!f){return
}if(/^(\[)/.test(f)){try{f=a.parseJSON(f)
}catch(j){return e.log("error parsing progressive slides",j),void 0
}}else{f=f.split(RegExp(q.data("cycle-split")||"\n")),f[f.length-1]||f.pop()
}}}}b&&(e.prepareTx=function(i,c){var d,l;
return i||0===f.length?(b.apply(h.API,[i,c]),void 0):(c&&h.currSlide==h.slideCount-1?(l=f[0],f=f.slice(1),h.container.one("cycle-slide-added",function(o,n){setTimeout(function(){n.API.advanceSlide(1)
},50)
}),h.API.add(l)):c||0!==h.currSlide?b.apply(h.API,[i,c]):(d=f.length-1,l=f[d],f=f.slice(0,d),h.container.one("cycle-slide-added",function(o,n){setTimeout(function(){n.currSlide=1,n.API.advanceSlide(-1)
},50)
}),h.API.add(l,!0)),void 0)
}),k&&(e.next=function(){var d=this.opts();
if(f.length&&d.currSlide==d.slideCount-1){var c=f[0];
f=f.slice(1),d.container.one("cycle-slide-added",function(l,i){k.apply(i.API),i.container.removeClass("cycle-loading")
}),d.container.addClass("cycle-loading"),d.API.add(c)
}else{k.apply(d.API)
}}),g&&(e.prev=function(){var l=this.opts();
if(f.length&&0===l.currSlide){var d=f.length-1,c=f[d];
f=f.slice(0,d),l.container.one("cycle-slide-added",function(n,i){i.currSlide=1,i.API.advanceSlide(-1),i.container.removeClass("cycle-loading")
}),l.container.addClass("cycle-loading"),l.API.add(c,!0)
}else{g.apply(l.API)
}})
}})
}(jQuery),
/*! tmpl plugin for Cycle2;  version: 20121227 */
function(a){a.extend(a.fn.cycle.defaults,{tmplRegex:"{{((.)?.*?)}}"}),a.extend(a.fn.cycle.API,{tmpl:function(c,b){var e=RegExp(b.tmplRegex||a.fn.cycle.defaults.tmplRegex,"g"),d=a.makeArray(arguments);
return d.shift(),c.replace(e,function(h,g){var p,k,m,f,j=g.split(".");
for(p=0;
d.length>p;
p++){if(m=d[p]){if(j.length>1){for(f=m,k=0;
j.length>k;
k++){m=f,f=f[j[k]]||g
}}else{f=m[g]
}if(a.isFunction(f)){return f.apply(m,d)
}if(void 0!==f&&null!==f&&f!=g){return f
}}}return g
})
}})
}(jQuery);
(function(a){a.event.special.swipe=a.event.special.swipe||{scrollSupressionThreshold:10,durationThreshold:1000,horizontalDistanceThreshold:30,verticalDistanceThreshold:75,setup:function(){var b=a(this);
b.bind("touchstart",function(c){function g(j){if(e){var h=j.originalEvent.touches?j.originalEvent.touches[0]:j;
d={time:(new Date).getTime(),coords:[h.pageX,h.pageY]},Math.abs(e.coords[0]-d.coords[0])>a.event.special.swipe.scrollSupressionThreshold&&j.preventDefault()
}}var d,f=c.originalEvent.touches?c.originalEvent.touches[0]:c,e={time:(new Date).getTime(),coords:[f.pageX,f.pageY],origin:a(c.target)};
b.bind("touchmove",g).one("touchend",function(){b.unbind("touchmove",g),e&&d&&d.time-e.time<a.event.special.swipe.durationThreshold&&Math.abs(e.coords[0]-d.coords[0])>a.event.special.swipe.horizontalDistanceThreshold&&Math.abs(e.coords[1]-d.coords[1])<a.event.special.swipe.verticalDistanceThreshold&&e.origin.trigger("swipe").trigger(e.coords[0]>d.coords[0]?"swipeleft":"swiperight"),e=d=void 0
})
})
}},a.event.special.swipeleft=a.event.special.swipeleft||{setup:function(){a(this).bind("swipe",a.noop)
}},a.event.special.swiperight=a.event.special.swiperight||a.event.special.swipeleft
})(jQuery);
if(navigator.userAgent.match(/(iPad|iPod|iPhone);.*CPU.*OS 6_\d/i)){(function(j){function l(i,y,w){function e(){if(x){x.apply(j,arguments);
if(!f){delete y[q];
x=null
}}}var q,x=w[0],f=i===g;
w[0]=e;
q=i.apply(j,w);
y[q]={args:w,created:Date.now(),cb:x,id:q};
return q
}function k(B,q,e,C,i){function y(){if(A.cb){A.cb.apply(j,arguments);
if(!z){delete e[C];
A.cb=null
}}}var A=e[C];
if(!A){return
}var z=B===g;
q(A.id);
if(!z){var x=A.args[1];
var w=Date.now()-A.created;
if(w<0){w=0
}x-=w;
if(x<0){x=0
}A.args[1]=x
}A.args[0]=y;
A.created=Date.now();
A.id=B.apply(j,A.args)
}var m={};
var d={};
var b=j.setTimeout;
var g=j.setInterval;
var p=j.clearTimeout;
var c=j.clearInterval;
if(!j.addEventListener){return false
}j.setTimeout=function(){return l(b,m,arguments)
};
j.setInterval=function(){return l(g,d,arguments)
};
j.clearTimeout=function(a){var f=m[a];
if(f){delete m[a];
p(f.id)
}};
j.clearInterval=function(f){var a=d[f];
if(a){delete d[f];
c(a.id)
}};
var h=j;
while(h.location!=h.parent.location){h=h.parent
}h.addEventListener("scroll",function(){var a;
for(a in m){k(b,p,m,a)
}for(a in d){k(g,c,d,a)
}})
})(window)
}(function(a){a.fn.marquee=function(b){var e=[],d=this.length;
function c(m,k,l){var j=l.behavior,h=l.width,g=l.dir;
var i=0;
if(j=="alternate"){i=m==1?k[l.widthAxis]-(h*2):h
}else{if(j=="slide"){if(m==-1){i=g==-1?k[l.widthAxis]:h
}else{i=g==-1?k[l.widthAxis]-(h*2):0
}}else{i=m==-1?k[l.widthAxis]:0
}}return i
}function f(){var h=e.length,j=null,m=null,l={},k=[],g=false;
while(h--){j=e[h];
m=a(j);
l=m.data("marqueeState");
if(m.data("paused")!==true){j[l.axis]+=(l.scrollamount*l.dir);
g=l.dir==-1?j[l.axis]<=c(l.dir*-1,j,l):j[l.axis]>=c(l.dir*-1,j,l);
if((l.behavior=="scroll"&&l.last==j[l.axis])||(l.behavior=="alternate"&&g&&l.last!=-1)||(l.behavior=="slide"&&g&&l.last!=-1)){if(l.behavior=="alternate"){l.dir*=-1
}l.last=-1;
m.trigger("stop");
l.loops--;
if(l.loops===0){if(l.behavior!="slide"){j[l.axis]=c(l.dir,j,l)
}else{j[l.axis]=c(l.dir*-1,j,l)
}m.trigger("end")
}else{k.push(j);
m.trigger("start");
j[l.axis]=c(l.dir,j,l)
}}else{k.push(j)
}l.last=j[l.axis];
m.data("marqueeState",l)
}else{k.push(j)
}}e=k;
if(e.length){setTimeout(f,25)
}}this.each(function(j){var n=a(this),g=n.attr("width")||n.width(),o=n.attr("height")||n.height(),p=n.after("<div "+(b?'class="'+b+'" ':"")+'style="display: block-inline; width: '+g+"px; height: "+o+'px; overflow: hidden;"><div style="float: left; white-space: nowrap;">'+n.html()+"</div></div>").next(),m=p.get(0),k=0,l=(n.attr("direction")||"left").toLowerCase(),h={dir:/down|right/.test(l)?-1:1,axis:/left|right/.test(l)?"scrollLeft":"scrollTop",widthAxis:/left|right/.test(l)?"scrollWidth":"scrollHeight",last:-1,loops:n.attr("loop")||-1,scrollamount:n.attr("scrollamount")||this.scrollAmount||2,behavior:(n.attr("behavior")||"scroll").toLowerCase(),width:/left|right/.test(l)?g:o};
if(n.attr("loop")==-1&&h.behavior=="slide"){h.loops=1
}n.remove();
if(/left|right/.test(l)){p.find("> div").css("padding","0 "+g+"px")
}else{p.find("> div").css("padding",o+"px 0")
}p.bind("stop",function(){p.data("paused",true)
}).bind("pause",function(){p.data("paused",true)
}).bind("start",function(){p.data("paused",false)
}).bind("unpause",function(){p.data("paused",false)
}).data("marqueeState",h);
e.push(m);
m[h.axis]=c(h.dir,m,h);
p.trigger("start");
if(j+1==d){f()
}});
return a(e)
}
}(jQuery));