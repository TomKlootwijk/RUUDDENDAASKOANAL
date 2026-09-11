$(document).ready(function(){VA2_Utils.fixedMenu();
if($("#va-popup").length>0){VA2Popup.initPopup()
}});
VA2_Utils={fixedMenu:function(){var d=60;
if($(".opening.banner").length>0){d=$(".opening.banner").outerHeight()
}var a=$("header.va-header.container");
var b=0;
var c;
$(window).on("scroll",function(){var e=$(this).scrollTop();
var f=$(window).width();
if(e>d){a.addClass("header-scrolled")
}else{a.removeClass("header-scrolled")
}a.stop(true,true).fadeIn(0);
if(f<768){clearTimeout(c);
if(e>b){c=setTimeout(function(){a.stop(true,true).fadeOut(300)
},300)
}else{if(e<b){a.stop(true,true).fadeIn(300)
}}b=e
}})
}};
VA2Popup={initPopup:function(){var a=VA2_Cookie.getCookie("vatican_close_popup_alert");
if(a==""){$("#va-popup").fadeIn("slow");
$("#va-popup").removeClass("hide-popup")
}$("#va-popup .btn-close").click(function(b){b.preventDefault;
VA2_Cookie.setCookie("vatican_close_popup_alert",true,30);
$("#va-popup").fadeOut("slow");
$("#va-popup").addClass("hide-popup")
})
}};
VA2_Cookie={getCookie:function(d){var b=d+"=";
var a=document.cookie.split(";");
for(var e=0;
e<a.length;
e++){var f=a[e];
while(f.charAt(0)==" "){f=f.substring(1)
}if(f.indexOf(b)==0){return f.substring(b.length,f.length)
}}return""
},setCookie:function(b,f,c){var e=new Date();
e.setTime(e.getTime()+(c*24*60*60*1000));
var a="expires="+e.toUTCString();
document.cookie=b+"="+f+";"+a+";path=/"
},};