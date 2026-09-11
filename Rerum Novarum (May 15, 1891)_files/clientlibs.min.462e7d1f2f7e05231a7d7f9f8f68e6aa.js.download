/*! jQuery UI - v1.12.1 - 2016-09-14
* http://jqueryui.com
* Includes: widget.js, position.js, data.js, disable-selection.js, effect.js, effects/effect-blind.js, effects/effect-bounce.js, effects/effect-clip.js, effects/effect-drop.js, effects/effect-explode.js, effects/effect-fade.js, effects/effect-fold.js, effects/effect-highlight.js, effects/effect-puff.js, effects/effect-pulsate.js, effects/effect-scale.js, effects/effect-shake.js, effects/effect-size.js, effects/effect-slide.js, effects/effect-transfer.js, focusable.js, form-reset-mixin.js, jquery-1-7.js, keycode.js, labels.js, scroll-parent.js, tabbable.js, unique-id.js, widgets/accordion.js, widgets/autocomplete.js, widgets/button.js, widgets/checkboxradio.js, widgets/controlgroup.js, widgets/datepicker.js, widgets/dialog.js, widgets/draggable.js, widgets/droppable.js, widgets/menu.js, widgets/mouse.js, widgets/progressbar.js, widgets/resizable.js, widgets/selectable.js, widgets/selectmenu.js, widgets/slider.js, widgets/sortable.js, widgets/spinner.js, widgets/tabs.js, widgets/tooltip.js
* Copyright jQuery Foundation and other contributors; Licensed MIT */
(function(a){if(typeof define==="function"&&define.amd){define(["jquery"],a)
}else{a(jQuery)
}}(function(ak){ak.ui=ak.ui||{};
var y=ak.ui.version="1.12.1";
/*!
 * jQuery UI Widget 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var I=0;
var al=Array.prototype.slice;
ak.cleanData=(function(av){return function(aw){var ay,az,ax;
for(ax=0;
(az=aw[ax])!=null;
ax++){try{ay=ak._data(az,"events");
if(ay&&ay.remove){ak(az).triggerHandler("remove")
}}catch(aA){}}av(aw)
}
})(ak.cleanData);
ak.widget=function(av,aw,aD){var aB,ay,aC;
var ax={};
var aA=av.split(".")[0];
av=av.split(".")[1];
var az=aA+"-"+av;
if(!aD){aD=aw;
aw=ak.Widget
}if(ak.isArray(aD)){aD=ak.extend.apply(null,[{}].concat(aD))
}ak.expr[":"][az.toLowerCase()]=function(aE){return !!ak.data(aE,az)
};
ak[aA]=ak[aA]||{};
aB=ak[aA][av];
ay=ak[aA][av]=function(aE,aF){if(!this._createWidget){return new ay(aE,aF)
}if(arguments.length){this._createWidget(aE,aF)
}};
ak.extend(ay,aB,{version:aD.version,_proto:ak.extend({},aD),_childConstructors:[]});
aC=new aw();
aC.options=ak.widget.extend({},aC.options);
ak.each(aD,function(aF,aE){if(!ak.isFunction(aE)){ax[aF]=aE;
return
}ax[aF]=(function(){function aG(){return aw.prototype[aF].apply(this,arguments)
}function aH(aI){return aw.prototype[aF].apply(this,aI)
}return function(){var aK=this._super;
var aI=this._superApply;
var aJ;
this._super=aG;
this._superApply=aH;
aJ=aE.apply(this,arguments);
this._super=aK;
this._superApply=aI;
return aJ
}
})()
});
ay.prototype=ak.widget.extend(aC,{widgetEventPrefix:aB?(aC.widgetEventPrefix||av):av},ax,{constructor:ay,namespace:aA,widgetName:av,widgetFullName:az});
if(aB){ak.each(aB._childConstructors,function(aF,aG){var aE=aG.prototype;
ak.widget(aE.namespace+"."+aE.widgetName,ay,aG._proto)
});
delete aB._childConstructors
}else{aw._childConstructors.push(ay)
}ak.widget.bridge(av,ay);
return ay
};
ak.widget.extend=function(aA){var aw=al.call(arguments,1);
var az=0;
var av=aw.length;
var ax;
var ay;
for(;
az<av;
az++){for(ax in aw[az]){ay=aw[az][ax];
if(aw[az].hasOwnProperty(ax)&&ay!==undefined){if(ak.isPlainObject(ay)){aA[ax]=ak.isPlainObject(aA[ax])?ak.widget.extend({},aA[ax],ay):ak.widget.extend({},ay)
}else{aA[ax]=ay
}}}}return aA
};
ak.widget.bridge=function(aw,av){var ax=av.prototype.widgetFullName||aw;
ak.fn[aw]=function(aA){var ay=typeof aA==="string";
var az=al.call(arguments,1);
var aB=this;
if(ay){if(!this.length&&aA==="instance"){aB=undefined
}else{this.each(function(){var aD;
var aC=ak.data(this,ax);
if(aA==="instance"){aB=aC;
return false
}if(!aC){return ak.error("cannot call methods on "+aw+" prior to initialization; attempted to call method '"+aA+"'")
}if(!ak.isFunction(aC[aA])||aA.charAt(0)==="_"){return ak.error("no such method '"+aA+"' for "+aw+" widget instance")
}aD=aC[aA].apply(aC,az);
if(aD!==aC&&aD!==undefined){aB=aD&&aD.jquery?aB.pushStack(aD.get()):aD;
return false
}})
}}else{if(az.length){aA=ak.widget.extend.apply(null,[aA].concat(az))
}this.each(function(){var aC=ak.data(this,ax);
if(aC){aC.option(aA||{});
if(aC._init){aC._init()
}}else{ak.data(this,ax,new av(aA,this))
}})
}return aB
}
};
ak.Widget=function(){};
ak.Widget._childConstructors=[];
ak.Widget.prototype={widgetName:"widget",widgetEventPrefix:"",defaultElement:"<div>",options:{classes:{},disabled:false,create:null},_createWidget:function(av,aw){aw=ak(aw||this.defaultElement||this)[0];
this.element=ak(aw);
this.uuid=I++;
this.eventNamespace="."+this.widgetName+this.uuid;
this.bindings=ak();
this.hoverable=ak();
this.focusable=ak();
this.classesElementLookup={};
if(aw!==this){ak.data(aw,this.widgetFullName,this);
this._on(true,this.element,{remove:function(ax){if(ax.target===aw){this.destroy()
}}});
this.document=ak(aw.style?aw.ownerDocument:aw.document||aw);
this.window=ak(this.document[0].defaultView||this.document[0].parentWindow)
}this.options=ak.widget.extend({},this.options,this._getCreateOptions(),av);
this._create();
if(this.options.disabled){this._setOptionDisabled(this.options.disabled)
}this._trigger("create",null,this._getCreateEventData());
this._init()
},_getCreateOptions:function(){return{}
},_getCreateEventData:ak.noop,_create:ak.noop,_init:ak.noop,destroy:function(){var av=this;
this._destroy();
ak.each(this.classesElementLookup,function(aw,ax){av._removeClass(ax,aw)
});
this.element.off(this.eventNamespace).removeData(this.widgetFullName);
this.widget().off(this.eventNamespace).removeAttr("aria-disabled");
this.bindings.off(this.eventNamespace)
},_destroy:ak.noop,widget:function(){return this.element
},option:function(ay,az){var av=ay;
var aA;
var ax;
var aw;
if(arguments.length===0){return ak.widget.extend({},this.options)
}if(typeof ay==="string"){av={};
aA=ay.split(".");
ay=aA.shift();
if(aA.length){ax=av[ay]=ak.widget.extend({},this.options[ay]);
for(aw=0;
aw<aA.length-1;
aw++){ax[aA[aw]]=ax[aA[aw]]||{};
ax=ax[aA[aw]]
}ay=aA.pop();
if(arguments.length===1){return ax[ay]===undefined?null:ax[ay]
}ax[ay]=az
}else{if(arguments.length===1){return this.options[ay]===undefined?null:this.options[ay]
}av[ay]=az
}}this._setOptions(av);
return this
},_setOptions:function(av){var aw;
for(aw in av){this._setOption(aw,av[aw])
}return this
},_setOption:function(av,aw){if(av==="classes"){this._setOptionClasses(aw)
}this.options[av]=aw;
if(av==="disabled"){this._setOptionDisabled(aw)
}return this
},_setOptionClasses:function(ay){var av,ax,aw;
for(av in ay){aw=this.classesElementLookup[av];
if(ay[av]===this.options.classes[av]||!aw||!aw.length){continue
}ax=ak(aw.get());
this._removeClass(aw,av);
ax.addClass(this._classes({element:ax,keys:av,classes:ay,add:true}))
}},_setOptionDisabled:function(av){this._toggleClass(this.widget(),this.widgetFullName+"-disabled",null,!!av);
if(av){this._removeClass(this.hoverable,null,"ui-state-hover");
this._removeClass(this.focusable,null,"ui-state-focus")
}},enable:function(){return this._setOptions({disabled:false})
},disable:function(){return this._setOptions({disabled:true})
},_classes:function(av){var aw=[];
var ax=this;
av=ak.extend({element:this.element,classes:this.options.classes||{}},av);
function ay(aA,aC){var aB,az;
for(az=0;
az<aA.length;
az++){aB=ax.classesElementLookup[aA[az]]||ak();
if(av.add){aB=ak(ak.unique(aB.get().concat(av.element.get())))
}else{aB=ak(aB.not(av.element).get())
}ax.classesElementLookup[aA[az]]=aB;
aw.push(aA[az]);
if(aC&&av.classes[aA[az]]){aw.push(av.classes[aA[az]])
}}}this._on(av.element,{remove:"_untrackClassesElement"});
if(av.keys){ay(av.keys.match(/\S+/g)||[],true)
}if(av.extra){ay(av.extra.match(/\S+/g)||[])
}return aw.join(" ")
},_untrackClassesElement:function(aw){var av=this;
ak.each(av.classesElementLookup,function(ax,ay){if(ak.inArray(aw.target,ay)!==-1){av.classesElementLookup[ax]=ak(ay.not(aw.target).get())
}})
},_removeClass:function(aw,ax,av){return this._toggleClass(aw,ax,av,false)
},_addClass:function(aw,ax,av){return this._toggleClass(aw,ax,av,true)
},_toggleClass:function(ay,az,av,aA){aA=(typeof aA==="boolean")?aA:av;
var aw=(typeof ay==="string"||ay===null),ax={extra:aw?az:av,keys:aw?ay:az,element:aw?this.element:ay,add:aA};
ax.element.toggleClass(this._classes(ax),aA);
return this
},_on:function(ay,ax,aw){var az;
var av=this;
if(typeof ay!=="boolean"){aw=ax;
ax=ay;
ay=false
}if(!aw){aw=ax;
ax=this.element;
az=this.widget()
}else{ax=az=ak(ax);
this.bindings=this.bindings.add(ax)
}ak.each(aw,function(aF,aE){function aC(){if(!ay&&(av.options.disabled===true||ak(this).hasClass("ui-state-disabled"))){return
}return(typeof aE==="string"?av[aE]:aE).apply(av,arguments)
}if(typeof aE!=="string"){aC.guid=aE.guid=aE.guid||aC.guid||ak.guid++
}var aD=aF.match(/^([\w:-]*)\s*(.*)$/);
var aB=aD[1]+av.eventNamespace;
var aA=aD[2];
if(aA){az.on(aB,aA,aC)
}else{ax.on(aB,aC)
}})
},_off:function(aw,av){av=(av||"").split(" ").join(this.eventNamespace+" ")+this.eventNamespace;
aw.off(av).off(av);
this.bindings=ak(this.bindings.not(aw).get());
this.focusable=ak(this.focusable.not(aw).get());
this.hoverable=ak(this.hoverable.not(aw).get())
},_delay:function(ay,ax){function aw(){return(typeof ay==="string"?av[ay]:ay).apply(av,arguments)
}var av=this;
return setTimeout(aw,ax||0)
},_hoverable:function(av){this.hoverable=this.hoverable.add(av);
this._on(av,{mouseenter:function(aw){this._addClass(ak(aw.currentTarget),null,"ui-state-hover")
},mouseleave:function(aw){this._removeClass(ak(aw.currentTarget),null,"ui-state-hover")
}})
},_focusable:function(av){this.focusable=this.focusable.add(av);
this._on(av,{focusin:function(aw){this._addClass(ak(aw.currentTarget),null,"ui-state-focus")
},focusout:function(aw){this._removeClass(ak(aw.currentTarget),null,"ui-state-focus")
}})
},_trigger:function(av,aw,ax){var aA,az;
var ay=this.options[av];
ax=ax||{};
aw=ak.Event(aw);
aw.type=(av===this.widgetEventPrefix?av:this.widgetEventPrefix+av).toLowerCase();
aw.target=this.element[0];
az=aw.originalEvent;
if(az){for(aA in az){if(!(aA in aw)){aw[aA]=az[aA]
}}}this.element.trigger(aw,ax);
return !(ak.isFunction(ay)&&ay.apply(this.element[0],[aw].concat(ax))===false||aw.isDefaultPrevented())
}};
ak.each({show:"fadeIn",hide:"fadeOut"},function(aw,av){ak.Widget.prototype["_"+aw]=function(az,ay,aB){if(typeof ay==="string"){ay={effect:ay}
}var aA;
var ax=!ay?aw:ay===true||typeof ay==="number"?av:ay.effect||av;
ay=ay||{};
if(typeof ay==="number"){ay={duration:ay}
}aA=!ak.isEmptyObject(ay);
ay.complete=aB;
if(ay.delay){az.delay(ay.delay)
}if(aA&&ak.effects&&ak.effects.effect[ax]){az[aw](ay)
}else{if(ax!==aw&&az[ax]){az[ax](ay.duration,ay.easing,aB)
}else{az.queue(function(aC){ak(this)[aw]();
if(aB){aB.call(az[0])
}aC()
})
}}}
});
var l=ak.widget;
/*!
 * jQuery UI Position 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 *
 * http://api.jqueryui.com/position/
 */
(function(){var aC,aD=Math.max,aG=Math.abs,ax=/left|center|right/,aA=/top|center|bottom/,av=/[\+\-]\d+(\.[\d]+)?%?/,aE=/^\w+/,aw=/%$/,az=ak.fn.position;
function aF(aJ,aI,aH){return[parseFloat(aJ[0])*(aw.test(aJ[0])?aI/100:1),parseFloat(aJ[1])*(aw.test(aJ[1])?aH/100:1)]
}function aB(aH,aI){return parseInt(ak.css(aH,aI),10)||0
}function ay(aI){var aH=aI[0];
if(aH.nodeType===9){return{width:aI.width(),height:aI.height(),offset:{top:0,left:0}}
}if(ak.isWindow(aH)){return{width:aI.width(),height:aI.height(),offset:{top:aI.scrollTop(),left:aI.scrollLeft()}}
}if(aH.preventDefault){return{width:0,height:0,offset:{top:aH.pageY,left:aH.pageX}}
}return{width:aI.outerWidth(),height:aI.outerHeight(),offset:aI.offset()}
}ak.position={scrollbarWidth:function(){if(aC!==undefined){return aC
}var aI,aH,aK=ak("<div style='display:block;position:absolute;width:50px;height:50px;overflow:hidden;'><div style='height:100px;width:auto;'></div></div>"),aJ=aK.children()[0];
ak("body").append(aK);
aI=aJ.offsetWidth;
aK.css("overflow","scroll");
aH=aJ.offsetWidth;
if(aI===aH){aH=aK[0].clientWidth
}aK.remove();
return(aC=aI-aH)
},getScrollInfo:function(aL){var aK=aL.isWindow||aL.isDocument?"":aL.element.css("overflow-x"),aJ=aL.isWindow||aL.isDocument?"":aL.element.css("overflow-y"),aI=aK==="scroll"||(aK==="auto"&&aL.width<aL.element[0].scrollWidth),aH=aJ==="scroll"||(aJ==="auto"&&aL.height<aL.element[0].scrollHeight);
return{width:aH?ak.position.scrollbarWidth():0,height:aI?ak.position.scrollbarWidth():0}
},getWithinInfo:function(aJ){var aK=ak(aJ||window),aH=ak.isWindow(aK[0]),aL=!!aK[0]&&aK[0].nodeType===9,aI=!aH&&!aL;
return{element:aK,isWindow:aH,isDocument:aL,offset:aI?ak(aJ).offset():{left:0,top:0},scrollLeft:aK.scrollLeft(),scrollTop:aK.scrollTop(),width:aK.outerWidth(),height:aK.outerHeight()}
}};
ak.fn.position=function(aR){if(!aR||!aR.of){return az.apply(this,arguments)
}aR=ak.extend({},aR);
var aS,aO,aM,aQ,aL,aH,aN=ak(aR.of),aK=ak.position.getWithinInfo(aR.within),aI=ak.position.getScrollInfo(aK),aP=(aR.collision||"flip").split(" "),aJ={};
aH=ay(aN);
if(aN[0].preventDefault){aR.at="left top"
}aO=aH.width;
aM=aH.height;
aQ=aH.offset;
aL=ak.extend({},aQ);
ak.each(["my","at"],function(){var aV=(aR[this]||"").split(" "),aU,aT;
if(aV.length===1){aV=ax.test(aV[0])?aV.concat(["center"]):aA.test(aV[0])?["center"].concat(aV):["center","center"]
}aV[0]=ax.test(aV[0])?aV[0]:"center";
aV[1]=aA.test(aV[1])?aV[1]:"center";
aU=av.exec(aV[0]);
aT=av.exec(aV[1]);
aJ[this]=[aU?aU[0]:0,aT?aT[0]:0];
aR[this]=[aE.exec(aV[0])[0],aE.exec(aV[1])[0]]
});
if(aP.length===1){aP[1]=aP[0]
}if(aR.at[0]==="right"){aL.left+=aO
}else{if(aR.at[0]==="center"){aL.left+=aO/2
}}if(aR.at[1]==="bottom"){aL.top+=aM
}else{if(aR.at[1]==="center"){aL.top+=aM/2
}}aS=aF(aJ.at,aO,aM);
aL.left+=aS[0];
aL.top+=aS[1];
return this.each(function(){var aU,a3,aW=ak(this),aY=aW.outerWidth(),aV=aW.outerHeight(),aX=aB(this,"marginLeft"),aT=aB(this,"marginTop"),a2=aY+aX+aB(this,"marginRight")+aI.width,a1=aV+aT+aB(this,"marginBottom")+aI.height,aZ=ak.extend({},aL),a0=aF(aJ.my,aW.outerWidth(),aW.outerHeight());
if(aR.my[0]==="right"){aZ.left-=aY
}else{if(aR.my[0]==="center"){aZ.left-=aY/2
}}if(aR.my[1]==="bottom"){aZ.top-=aV
}else{if(aR.my[1]==="center"){aZ.top-=aV/2
}}aZ.left+=a0[0];
aZ.top+=a0[1];
aU={marginLeft:aX,marginTop:aT};
ak.each(["left","top"],function(a5,a4){if(ak.ui.position[aP[a5]]){ak.ui.position[aP[a5]][a4](aZ,{targetWidth:aO,targetHeight:aM,elemWidth:aY,elemHeight:aV,collisionPosition:aU,collisionWidth:a2,collisionHeight:a1,offset:[aS[0]+a0[0],aS[1]+a0[1]],my:aR.my,at:aR.at,within:aK,elem:aW})
}});
if(aR.using){a3=function(a7){var a9=aQ.left-aZ.left,a6=a9+aO-aY,a8=aQ.top-aZ.top,a5=a8+aM-aV,a4={target:{element:aN,left:aQ.left,top:aQ.top,width:aO,height:aM},element:{element:aW,left:aZ.left,top:aZ.top,width:aY,height:aV},horizontal:a6<0?"left":a9>0?"right":"center",vertical:a5<0?"top":a8>0?"bottom":"middle"};
if(aO<aY&&aG(a9+a6)<aO){a4.horizontal="center"
}if(aM<aV&&aG(a8+a5)<aM){a4.vertical="middle"
}if(aD(aG(a9),aG(a6))>aD(aG(a8),aG(a5))){a4.important="horizontal"
}else{a4.important="vertical"
}aR.using.call(this,a7,a4)
}
}aW.offset(ak.extend(aZ,{using:a3}))
})
};
ak.ui.position={fit:{left:function(aL,aK){var aJ=aK.within,aN=aJ.isWindow?aJ.scrollLeft:aJ.offset.left,aP=aJ.width,aM=aL.left-aK.collisionPosition.marginLeft,aO=aN-aM,aI=aM+aK.collisionWidth-aP-aN,aH;
if(aK.collisionWidth>aP){if(aO>0&&aI<=0){aH=aL.left+aO+aK.collisionWidth-aP-aN;
aL.left+=aO-aH
}else{if(aI>0&&aO<=0){aL.left=aN
}else{if(aO>aI){aL.left=aN+aP-aK.collisionWidth
}else{aL.left=aN
}}}}else{if(aO>0){aL.left+=aO
}else{if(aI>0){aL.left-=aI
}else{aL.left=aD(aL.left-aM,aL.left)
}}}},top:function(aK,aJ){var aI=aJ.within,aO=aI.isWindow?aI.scrollTop:aI.offset.top,aP=aJ.within.height,aM=aK.top-aJ.collisionPosition.marginTop,aN=aO-aM,aL=aM+aJ.collisionHeight-aP-aO,aH;
if(aJ.collisionHeight>aP){if(aN>0&&aL<=0){aH=aK.top+aN+aJ.collisionHeight-aP-aO;
aK.top+=aN-aH
}else{if(aL>0&&aN<=0){aK.top=aO
}else{if(aN>aL){aK.top=aO+aP-aJ.collisionHeight
}else{aK.top=aO
}}}}else{if(aN>0){aK.top+=aN
}else{if(aL>0){aK.top-=aL
}else{aK.top=aD(aK.top-aM,aK.top)
}}}}},flip:{left:function(aN,aM){var aL=aM.within,aR=aL.offset.left+aL.scrollLeft,aU=aL.width,aJ=aL.isWindow?aL.scrollLeft:aL.offset.left,aO=aN.left-aM.collisionPosition.marginLeft,aS=aO-aJ,aI=aO+aM.collisionWidth-aU-aJ,aQ=aM.my[0]==="left"?-aM.elemWidth:aM.my[0]==="right"?aM.elemWidth:0,aT=aM.at[0]==="left"?aM.targetWidth:aM.at[0]==="right"?-aM.targetWidth:0,aK=-2*aM.offset[0],aH,aP;
if(aS<0){aH=aN.left+aQ+aT+aK+aM.collisionWidth-aU-aR;
if(aH<0||aH<aG(aS)){aN.left+=aQ+aT+aK
}}else{if(aI>0){aP=aN.left-aM.collisionPosition.marginLeft+aQ+aT+aK-aJ;
if(aP>0||aG(aP)<aI){aN.left+=aQ+aT+aK
}}}},top:function(aM,aL){var aK=aL.within,aT=aK.offset.top+aK.scrollTop,aU=aK.height,aH=aK.isWindow?aK.scrollTop:aK.offset.top,aO=aM.top-aL.collisionPosition.marginTop,aQ=aO-aH,aN=aO+aL.collisionHeight-aU-aH,aR=aL.my[1]==="top",aP=aR?-aL.elemHeight:aL.my[1]==="bottom"?aL.elemHeight:0,aV=aL.at[1]==="top"?aL.targetHeight:aL.at[1]==="bottom"?-aL.targetHeight:0,aJ=-2*aL.offset[1],aS,aI;
if(aQ<0){aI=aM.top+aP+aV+aJ+aL.collisionHeight-aU-aT;
if(aI<0||aI<aG(aQ)){aM.top+=aP+aV+aJ
}}else{if(aN>0){aS=aM.top-aL.collisionPosition.marginTop+aP+aV+aJ-aH;
if(aS>0||aG(aS)<aN){aM.top+=aP+aV+aJ
}}}}},flipfit:{left:function(){ak.ui.position.flip.left.apply(this,arguments);
ak.ui.position.fit.left.apply(this,arguments)
},top:function(){ak.ui.position.flip.top.apply(this,arguments);
ak.ui.position.fit.top.apply(this,arguments)
}}}
})();
var ah=ak.ui.position;
/*!
 * jQuery UI :data 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var q=ak.extend(ak.expr[":"],{data:ak.expr.createPseudo?ak.expr.createPseudo(function(av){return function(aw){return !!ak.data(aw,av)
}
}):function(ax,aw,av){return !!ak.data(ax,av[3])
}});
/*!
 * jQuery UI Disable Selection 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var m=ak.fn.extend({disableSelection:(function(){var av="onselectstart" in document.createElement("div")?"selectstart":"mousedown";
return function(){return this.on(av+".ui-disableSelection",function(aw){aw.preventDefault()
})
}
})(),enableSelection:function(){return this.off(".ui-disableSelection")
}});
/*!
 * jQuery UI Effects 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var t="ui-effects-",ad="ui-effects-style",ap="ui-effects-animated",b=ak;
ak.effects={effect:{}};
/*!
 * jQuery Color Animations v2.1.2
 * https://github.com/jquery/jquery-color
 *
 * Copyright 2014 jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 *
 * Date: Wed Jan 16 08:47:09 2013 -0600
 */
(function(aJ,ay){var aF="backgroundColor borderBottomColor borderLeftColor borderRightColor borderTopColor color columnRuleColor outlineColor textDecorationColor textEmphasisColor",aC=/^([\-+])=\s*(\d+\.?\d*)/,aB=[{re:/rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(?:,\s*(\d?(?:\.\d+)?)\s*)?\)/,parse:function(aK){return[aK[1],aK[2],aK[3],aK[4]]
}},{re:/rgba?\(\s*(\d+(?:\.\d+)?)\%\s*,\s*(\d+(?:\.\d+)?)\%\s*,\s*(\d+(?:\.\d+)?)\%\s*(?:,\s*(\d?(?:\.\d+)?)\s*)?\)/,parse:function(aK){return[aK[1]*2.55,aK[2]*2.55,aK[3]*2.55,aK[4]]
}},{re:/#([a-f0-9]{2})([a-f0-9]{2})([a-f0-9]{2})/,parse:function(aK){return[parseInt(aK[1],16),parseInt(aK[2],16),parseInt(aK[3],16)]
}},{re:/#([a-f0-9])([a-f0-9])([a-f0-9])/,parse:function(aK){return[parseInt(aK[1]+aK[1],16),parseInt(aK[2]+aK[2],16),parseInt(aK[3]+aK[3],16)]
}},{re:/hsla?\(\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\%\s*,\s*(\d+(?:\.\d+)?)\%\s*(?:,\s*(\d?(?:\.\d+)?)\s*)?\)/,space:"hsla",parse:function(aK){return[aK[1],aK[2]/100,aK[3]/100,aK[4]]
}}],az=aJ.Color=function(aL,aM,aK,aN){return new aJ.Color.fn.parse(aL,aM,aK,aN)
},aE={rgba:{props:{red:{idx:0,type:"byte"},green:{idx:1,type:"byte"},blue:{idx:2,type:"byte"}}},hsla:{props:{hue:{idx:0,type:"degrees"},saturation:{idx:1,type:"percent"},lightness:{idx:2,type:"percent"}}}},aI={"byte":{floor:true,max:255},percent:{max:1},degrees:{mod:360,floor:true}},aH=az.support={},aw=aJ("<p>")[0],av,aG=aJ.each;
aw.style.cssText="background-color:rgba(1,1,1,.5)";
aH.rgba=aw.style.backgroundColor.indexOf("rgba")>-1;
aG(aE,function(aK,aL){aL.cache="_"+aK;
aL.props.alpha={idx:3,type:"percent",def:1}
});
function aD(aL,aN,aM){var aK=aI[aN.type]||{};
if(aL==null){return(aM||!aN.def)?null:aN.def
}aL=aK.floor?~~aL:parseFloat(aL);
if(isNaN(aL)){return aN.def
}if(aK.mod){return(aL+aK.mod)%aK.mod
}return 0>aL?0:aK.max<aL?aK.max:aL
}function aA(aK){var aM=az(),aL=aM._rgba=[];
aK=aK.toLowerCase();
aG(aB,function(aR,aS){var aP,aQ=aS.re.exec(aK),aO=aQ&&aS.parse(aQ),aN=aS.space||"rgba";
if(aO){aP=aM[aN](aO);
aM[aE[aN].cache]=aP[aE[aN].cache];
aL=aM._rgba=aP._rgba;
return false
}});
if(aL.length){if(aL.join()==="0,0,0,0"){aJ.extend(aL,av.transparent)
}return aM
}return av[aK]
}az.fn=aJ.extend(az.prototype,{parse:function(aQ,aO,aK,aP){if(aQ===ay){this._rgba=[null,null,null,null];
return this
}if(aQ.jquery||aQ.nodeType){aQ=aJ(aQ).css(aO);
aO=ay
}var aN=this,aM=aJ.type(aQ),aL=this._rgba=[];
if(aO!==ay){aQ=[aQ,aO,aK,aP];
aM="array"
}if(aM==="string"){return this.parse(aA(aQ)||av._default)
}if(aM==="array"){aG(aE.rgba.props,function(aR,aS){aL[aS.idx]=aD(aQ[aS.idx],aS)
});
return this
}if(aM==="object"){if(aQ instanceof az){aG(aE,function(aR,aS){if(aQ[aS.cache]){aN[aS.cache]=aQ[aS.cache].slice()
}})
}else{aG(aE,function(aS,aT){var aR=aT.cache;
aG(aT.props,function(aU,aV){if(!aN[aR]&&aT.to){if(aU==="alpha"||aQ[aU]==null){return
}aN[aR]=aT.to(aN._rgba)
}aN[aR][aV.idx]=aD(aQ[aU],aV,true)
});
if(aN[aR]&&aJ.inArray(null,aN[aR].slice(0,3))<0){aN[aR][3]=1;
if(aT.from){aN._rgba=aT.from(aN[aR])
}}})
}return this
}},is:function(aM){var aK=az(aM),aN=true,aL=this;
aG(aE,function(aO,aQ){var aR,aP=aK[aQ.cache];
if(aP){aR=aL[aQ.cache]||aQ.to&&aQ.to(aL._rgba)||[];
aG(aQ.props,function(aS,aT){if(aP[aT.idx]!=null){aN=(aP[aT.idx]===aR[aT.idx]);
return aN
}})
}return aN
});
return aN
},_space:function(){var aK=[],aL=this;
aG(aE,function(aM,aN){if(aL[aN.cache]){aK.push(aM)
}});
return aK.pop()
},transition:function(aL,aR){var aM=az(aL),aN=aM._space(),aO=aE[aN],aP=this.alpha()===0?az("transparent"):this,aQ=aP[aO.cache]||aO.to(aP._rgba),aK=aQ.slice();
aM=aM[aO.cache];
aG(aO.props,function(aV,aX){var aU=aX.idx,aT=aQ[aU],aS=aM[aU],aW=aI[aX.type]||{};
if(aS===null){return
}if(aT===null){aK[aU]=aS
}else{if(aW.mod){if(aS-aT>aW.mod/2){aT+=aW.mod
}else{if(aT-aS>aW.mod/2){aT-=aW.mod
}}}aK[aU]=aD((aS-aT)*aR+aT,aX)
}});
return this[aN](aK)
},blend:function(aN){if(this._rgba[3]===1){return this
}var aM=this._rgba.slice(),aL=aM.pop(),aK=az(aN)._rgba;
return az(aJ.map(aM,function(aO,aP){return(1-aL)*aK[aP]+aL*aO
}))
},toRgbaString:function(){var aL="rgba(",aK=aJ.map(this._rgba,function(aM,aN){return aM==null?(aN>2?1:0):aM
});
if(aK[3]===1){aK.pop();
aL="rgb("
}return aL+aK.join()+")"
},toHslaString:function(){var aL="hsla(",aK=aJ.map(this.hsla(),function(aM,aN){if(aM==null){aM=aN>2?1:0
}if(aN&&aN<3){aM=Math.round(aM*100)+"%"
}return aM
});
if(aK[3]===1){aK.pop();
aL="hsl("
}return aL+aK.join()+")"
},toHexString:function(aK){var aL=this._rgba.slice(),aM=aL.pop();
if(aK){aL.push(~~(aM*255))
}return"#"+aJ.map(aL,function(aN){aN=(aN||0).toString(16);
return aN.length===1?"0"+aN:aN
}).join("")
},toString:function(){return this._rgba[3]===0?"transparent":this.toRgbaString()
}});
az.fn.parse.prototype=az.fn;
function ax(aM,aL,aK){aK=(aK+1)%1;
if(aK*6<1){return aM+(aL-aM)*aK*6
}if(aK*2<1){return aL
}if(aK*3<2){return aM+(aL-aM)*((2/3)-aK)*6
}return aM
}aE.hsla.to=function(aM){if(aM[0]==null||aM[1]==null||aM[2]==null){return[null,null,null,aM[3]]
}var aK=aM[0]/255,aP=aM[1]/255,aQ=aM[2]/255,aS=aM[3],aR=Math.max(aK,aP,aQ),aN=Math.min(aK,aP,aQ),aT=aR-aN,aU=aR+aN,aL=aU*0.5,aO,aV;
if(aN===aR){aO=0
}else{if(aK===aR){aO=(60*(aP-aQ)/aT)+360
}else{if(aP===aR){aO=(60*(aQ-aK)/aT)+120
}else{aO=(60*(aK-aP)/aT)+240
}}}if(aT===0){aV=0
}else{if(aL<=0.5){aV=aT/aU
}else{aV=aT/(2-aU)
}}return[Math.round(aO)%360,aV,aL,aS==null?1:aS]
};
aE.hsla.from=function(aO){if(aO[0]==null||aO[1]==null||aO[2]==null){return[null,null,null,aO[3]]
}var aN=aO[0]/360,aM=aO[1],aL=aO[2],aK=aO[3],aP=aL<=0.5?aL*(1+aM):aL+aM-aL*aM,aQ=2*aL-aP;
return[Math.round(ax(aQ,aP,aN+(1/3))*255),Math.round(ax(aQ,aP,aN)*255),Math.round(ax(aQ,aP,aN-(1/3))*255),aK]
};
aG(aE,function(aL,aN){var aM=aN.props,aK=aN.cache,aP=aN.to,aO=aN.from;
az.fn[aL]=function(aU){if(aP&&!this[aK]){this[aK]=aP(this._rgba)
}if(aU===ay){return this[aK].slice()
}var aR,aT=aJ.type(aU),aQ=(aT==="array"||aT==="object")?aU:arguments,aS=this[aK].slice();
aG(aM,function(aV,aX){var aW=aQ[aT==="object"?aV:aX.idx];
if(aW==null){aW=aS[aX.idx]
}aS[aX.idx]=aD(aW,aX)
});
if(aO){aR=az(aO(aS));
aR[aK]=aS;
return aR
}else{return az(aS)
}};
aG(aM,function(aQ,aR){if(az.fn[aQ]){return
}az.fn[aQ]=function(aV){var aX=aJ.type(aV),aU=(aQ==="alpha"?(this._hsla?"hsla":"rgba"):aL),aT=this[aU](),aW=aT[aR.idx],aS;
if(aX==="undefined"){return aW
}if(aX==="function"){aV=aV.call(this,aW);
aX=aJ.type(aV)
}if(aV==null&&aR.empty){return this
}if(aX==="string"){aS=aC.exec(aV);
if(aS){aV=aW+parseFloat(aS[2])*(aS[1]==="+"?1:-1)
}}aT[aR.idx]=aV;
return this[aU](aT)
}
})
});
az.hook=function(aL){var aK=aL.split(" ");
aG(aK,function(aM,aN){aJ.cssHooks[aN]={set:function(aR,aS){var aP,aQ,aO="";
if(aS!=="transparent"&&(aJ.type(aS)!=="string"||(aP=aA(aS)))){aS=az(aP||aS);
if(!aH.rgba&&aS._rgba[3]!==1){aQ=aN==="backgroundColor"?aR.parentNode:aR;
while((aO===""||aO==="transparent")&&aQ&&aQ.style){try{aO=aJ.css(aQ,"backgroundColor");
aQ=aQ.parentNode
}catch(aT){}}aS=aS.blend(aO&&aO!=="transparent"?aO:"_default")
}aS=aS.toRgbaString()
}try{aR.style[aN]=aS
}catch(aT){}}};
aJ.fx.step[aN]=function(aO){if(!aO.colorInit){aO.start=az(aO.elem,aN);
aO.end=az(aO.end);
aO.colorInit=true
}aJ.cssHooks[aN].set(aO.elem,aO.start.transition(aO.end,aO.pos))
}
})
};
az.hook(aF);
aJ.cssHooks.borderColor={expand:function(aL){var aK={};
aG(["Top","Right","Bottom","Left"],function(aN,aM){aK["border"+aM+"Color"]=aL
});
return aK
}};
av=aJ.Color.names={aqua:"#00ffff",black:"#000000",blue:"#0000ff",fuchsia:"#ff00ff",gray:"#808080",green:"#008000",lime:"#00ff00",maroon:"#800000",navy:"#000080",olive:"#808000",purple:"#800080",red:"#ff0000",silver:"#c0c0c0",teal:"#008080",white:"#ffffff",yellow:"#ffff00",transparent:[null,null,null,0],_default:"#ffffff"}
})(b);
(function(){var aw=["add","remove","toggle"],ax={border:1,borderBottom:1,borderColor:1,borderLeft:1,borderRight:1,borderTop:1,borderWidth:1,margin:1,padding:1};
ak.each(["borderLeftStyle","borderRightStyle","borderBottomStyle","borderTopStyle"],function(az,aA){ak.fx.step[aA]=function(aB){if(aB.end!=="none"&&!aB.setAttr||aB.pos===1&&!aB.setAttr){b.style(aB.elem,aA,aB.end);
aB.setAttr=true
}}
});
function ay(aD){var aA,az,aB=aD.ownerDocument.defaultView?aD.ownerDocument.defaultView.getComputedStyle(aD,null):aD.currentStyle,aC={};
if(aB&&aB.length&&aB[0]&&aB[aB[0]]){az=aB.length;
while(az--){aA=aB[az];
if(typeof aB[aA]==="string"){aC[ak.camelCase(aA)]=aB[aA]
}}}else{for(aA in aB){if(typeof aB[aA]==="string"){aC[aA]=aB[aA]
}}}return aC
}function av(az,aB){var aD={},aA,aC;
for(aA in aB){aC=aB[aA];
if(az[aA]!==aC){if(!ax[aA]){if(ak.fx.step[aA]||!isNaN(parseFloat(aC))){aD[aA]=aC
}}}}return aD
}if(!ak.fn.addBack){ak.fn.addBack=function(az){return this.add(az==null?this.prevObject:this.prevObject.filter(az))
}
}ak.effects.animateClass=function(az,aA,aD,aC){var aB=ak.speed(aA,aD,aC);
return this.queue(function(){var aG=ak(this),aE=aG.attr("class")||"",aF,aH=aB.children?aG.find("*").addBack():aG;
aH=aH.map(function(){var aI=ak(this);
return{el:aI,start:ay(this)}
});
aF=function(){ak.each(aw,function(aI,aJ){if(az[aJ]){aG[aJ+"Class"](az[aJ])
}})
};
aF();
aH=aH.map(function(){this.end=ay(this.el[0]);
this.diff=av(this.start,this.end);
return this
});
aG.attr("class",aE);
aH=aH.map(function(){var aK=this,aI=ak.Deferred(),aJ=ak.extend({},aB,{queue:false,complete:function(){aI.resolve(aK)
}});
this.el.animate(this.diff,aJ);
return aI.promise()
});
ak.when.apply(ak,aH.get()).done(function(){aF();
ak.each(arguments,function(){var aI=this.el;
ak.each(this.diff,function(aJ){aI.css(aJ,"")
})
});
aB.complete.call(aG[0])
})
})
};
ak.fn.extend({addClass:(function(az){return function(aB,aA,aD,aC){return aA?ak.effects.animateClass.call(this,{add:aB},aA,aD,aC):az.apply(this,arguments)
}
})(ak.fn.addClass),removeClass:(function(az){return function(aB,aA,aD,aC){return arguments.length>1?ak.effects.animateClass.call(this,{remove:aB},aA,aD,aC):az.apply(this,arguments)
}
})(ak.fn.removeClass),toggleClass:(function(az){return function(aC,aB,aA,aE,aD){if(typeof aB==="boolean"||aB===undefined){if(!aA){return az.apply(this,arguments)
}else{return ak.effects.animateClass.call(this,(aB?{add:aC}:{remove:aC}),aA,aE,aD)
}}else{return ak.effects.animateClass.call(this,{toggle:aC},aB,aA,aE)
}}
})(ak.fn.toggleClass),switchClass:function(az,aB,aA,aD,aC){return ak.effects.animateClass.call(this,{add:aB,remove:az},aA,aD,aC)
}})
})();
(function(){if(ak.expr&&ak.expr.filters&&ak.expr.filters.animated){ak.expr.filters.animated=(function(ay){return function(az){return !!ak(az).data(ap)||ay(az)
}
})(ak.expr.filters.animated)
}if(ak.uiBackCompat!==false){ak.extend(ak.effects,{save:function(az,aB){var ay=0,aA=aB.length;
for(;
ay<aA;
ay++){if(aB[ay]!==null){az.data(t+aB[ay],az[0].style[aB[ay]])
}}},restore:function(az,aC){var aB,ay=0,aA=aC.length;
for(;
ay<aA;
ay++){if(aC[ay]!==null){aB=az.data(t+aC[ay]);
az.css(aC[ay],aB)
}}},setMode:function(ay,az){if(az==="toggle"){az=ay.is(":hidden")?"show":"hide"
}return az
},createWrapper:function(az){if(az.parent().is(".ui-effects-wrapper")){return az.parent()
}var aA={width:az.outerWidth(true),height:az.outerHeight(true),"float":az.css("float")},aD=ak("<div></div>").addClass("ui-effects-wrapper").css({fontSize:"100%",background:"transparent",border:"none",margin:0,padding:0}),ay={width:az.width(),height:az.height()},aC=document.activeElement;
try{aC.id
}catch(aB){aC=document.body
}az.wrap(aD);
if(az[0]===aC||ak.contains(az[0],aC)){ak(aC).trigger("focus")
}aD=az.parent();
if(az.css("position")==="static"){aD.css({position:"relative"});
az.css({position:"relative"})
}else{ak.extend(aA,{position:az.css("position"),zIndex:az.css("z-index")});
ak.each(["top","left","bottom","right"],function(aE,aF){aA[aF]=az.css(aF);
if(isNaN(parseInt(aA[aF],10))){aA[aF]="auto"
}});
az.css({position:"relative",top:0,left:0,right:"auto",bottom:"auto"})
}az.css(ay);
return aD.css(aA).show()
},removeWrapper:function(ay){var az=document.activeElement;
if(ay.parent().is(".ui-effects-wrapper")){ay.parent().replaceWith(ay);
if(ay[0]===az||ak.contains(ay[0],az)){ak(az).trigger("focus")
}}return ay
}})
}ak.extend(ak.effects,{version:"1.12.1",define:function(ay,aA,az){if(!az){az=aA;
aA="effect"
}ak.effects.effect[ay]=az;
ak.effects.effect[ay].mode=aA;
return az
},scaledDimensions:function(az,aA,aB){if(aA===0){return{height:0,width:0,outerHeight:0,outerWidth:0}
}var ay=aB!=="horizontal"?((aA||100)/100):1,aC=aB!=="vertical"?((aA||100)/100):1;
return{height:az.height()*aC,width:az.width()*ay,outerHeight:az.outerHeight()*aC,outerWidth:az.outerWidth()*ay}
},clipToBox:function(ay){return{width:ay.clip.right-ay.clip.left,height:ay.clip.bottom-ay.clip.top,left:ay.clip.left,top:ay.clip.top}
},unshift:function(az,aB,aA){var ay=az.queue();
if(aB>1){ay.splice.apply(ay,[1,0].concat(ay.splice(aB,aA)))
}az.dequeue()
},saveStyle:function(ay){ay.data(ad,ay[0].style.cssText)
},restoreStyle:function(ay){ay[0].style.cssText=ay.data(ad)||"";
ay.removeData(ad)
},mode:function(ay,aA){var az=ay.is(":hidden");
if(aA==="toggle"){aA=az?"show":"hide"
}if(az?aA==="hide":aA==="show"){aA="none"
}return aA
},getBaseline:function(az,aA){var aB,ay;
switch(az[0]){case"top":aB=0;
break;
case"middle":aB=0.5;
break;
case"bottom":aB=1;
break;
default:aB=az[0]/aA.height
}switch(az[1]){case"left":ay=0;
break;
case"center":ay=0.5;
break;
case"right":ay=1;
break;
default:ay=az[1]/aA.width
}return{x:ay,y:aB}
},createPlaceholder:function(az){var aB,aA=az.css("position"),ay=az.position();
az.css({marginTop:az.css("marginTop"),marginBottom:az.css("marginBottom"),marginLeft:az.css("marginLeft"),marginRight:az.css("marginRight")}).outerWidth(az.outerWidth()).outerHeight(az.outerHeight());
if(/^(static|relative)/.test(aA)){aA="absolute";
aB=ak("<"+az[0].nodeName+">").insertAfter(az).css({display:/^(inline|ruby)/.test(az.css("display"))?"inline-block":"block",visibility:"hidden",marginTop:az.css("marginTop"),marginBottom:az.css("marginBottom"),marginLeft:az.css("marginLeft"),marginRight:az.css("marginRight"),"float":az.css("float")}).outerWidth(az.outerWidth()).outerHeight(az.outerHeight()).addClass("ui-effects-placeholder");
az.data(t+"placeholder",aB)
}az.css({position:aA,left:ay.left,top:ay.top});
return aB
},removePlaceholder:function(ay){var aA=t+"placeholder",az=ay.data(aA);
if(az){az.remove();
ay.removeData(aA)
}},cleanUp:function(ay){ak.effects.restoreStyle(ay);
ak.effects.removePlaceholder(ay)
},setTransition:function(az,aB,ay,aA){aA=aA||{};
ak.each(aB,function(aD,aC){var aE=az.cssUnit(aC);
if(aE[0]>0){aA[aC]=aE[0]*ay+aE[1]
}});
return aA
}});
function aw(az,ay,aA,aB){if(ak.isPlainObject(az)){ay=az;
az=az.effect
}az={effect:az};
if(ay==null){ay={}
}if(ak.isFunction(ay)){aB=ay;
aA=null;
ay={}
}if(typeof ay==="number"||ak.fx.speeds[ay]){aB=aA;
aA=ay;
ay={}
}if(ak.isFunction(aA)){aB=aA;
aA=null
}if(ay){ak.extend(az,ay)
}aA=aA||ay.duration;
az.duration=ak.fx.off?0:typeof aA==="number"?aA:aA in ak.fx.speeds?ak.fx.speeds[aA]:ak.fx.speeds._default;
az.complete=aB||ay.complete;
return az
}function ax(ay){if(!ay||typeof ay==="number"||ak.fx.speeds[ay]){return true
}if(typeof ay==="string"&&!ak.effects.effect[ay]){return true
}if(ak.isFunction(ay)){return true
}if(typeof ay==="object"&&!ay.effect){return true
}return false
}ak.fn.extend({effect:function(){var aG=aw.apply(this,arguments),aF=ak.effects.effect[aG.effect],aC=aF.mode,aE=aG.queue,aB=aE||"fx",ay=aG.complete,aD=aG.mode,az=[],aH=function(aK){var aJ=ak(this),aI=ak.effects.mode(aJ,aD)||aC;
aJ.data(ap,true);
az.push(aI);
if(aC&&(aI==="show"||(aI===aC&&aI==="hide"))){aJ.show()
}if(!aC||aI!=="none"){ak.effects.saveStyle(aJ)
}if(ak.isFunction(aK)){aK()
}};
if(ak.fx.off||!aF){if(aD){return this[aD](aG.duration,ay)
}else{return this.each(function(){if(ay){ay.call(this)
}})
}}function aA(aK){var aL=ak(this);
function aJ(){aL.removeData(ap);
ak.effects.cleanUp(aL);
if(aG.mode==="hide"){aL.hide()
}aI()
}function aI(){if(ak.isFunction(ay)){ay.call(aL[0])
}if(ak.isFunction(aK)){aK()
}}aG.mode=az.shift();
if(ak.uiBackCompat!==false&&!aC){if(aL.is(":hidden")?aD==="hide":aD==="show"){aL[aD]();
aI()
}else{aF.call(aL[0],aG,aI)
}}else{if(aG.mode==="none"){aL[aD]();
aI()
}else{aF.call(aL[0],aG,aJ)
}}}return aE===false?this.each(aH).each(aA):this.queue(aB,aH).queue(aB,aA)
},show:(function(ay){return function(aA){if(ax(aA)){return ay.apply(this,arguments)
}else{var az=aw.apply(this,arguments);
az.mode="show";
return this.effect.call(this,az)
}}
})(ak.fn.show),hide:(function(ay){return function(aA){if(ax(aA)){return ay.apply(this,arguments)
}else{var az=aw.apply(this,arguments);
az.mode="hide";
return this.effect.call(this,az)
}}
})(ak.fn.hide),toggle:(function(ay){return function(aA){if(ax(aA)||typeof aA==="boolean"){return ay.apply(this,arguments)
}else{var az=aw.apply(this,arguments);
az.mode="toggle";
return this.effect.call(this,az)
}}
})(ak.fn.toggle),cssUnit:function(ay){var az=this.css(ay),aA=[];
ak.each(["em","px","%","pt"],function(aB,aC){if(az.indexOf(aC)>0){aA=[parseFloat(az),aC]
}});
return aA
},cssClip:function(ay){if(ay){return this.css("clip","rect("+ay.top+"px "+ay.right+"px "+ay.bottom+"px "+ay.left+"px)")
}return av(this.css("clip"),this)
},transfer:function(aJ,aB){var aD=ak(this),aF=ak(aJ.to),aI=aF.css("position")==="fixed",aE=ak("body"),aG=aI?aE.scrollTop():0,aH=aI?aE.scrollLeft():0,ay=aF.offset(),aA={top:ay.top-aG,left:ay.left-aH,height:aF.innerHeight(),width:aF.innerWidth()},aC=aD.offset(),az=ak("<div class='ui-effects-transfer'></div>").appendTo("body").addClass(aJ.className).css({top:aC.top-aG,left:aC.left-aH,height:aD.innerHeight(),width:aD.innerWidth(),position:aI?"fixed":"absolute"}).animate(aA,aJ.duration,aJ.easing,function(){az.remove();
if(ak.isFunction(aB)){aB()
}})
}});
function av(aD,aA){var aC=aA.outerWidth(),aB=aA.outerHeight(),az=/^rect\((-?\d*\.?\d*px|-?\d+%|auto),?\s*(-?\d*\.?\d*px|-?\d+%|auto),?\s*(-?\d*\.?\d*px|-?\d+%|auto),?\s*(-?\d*\.?\d*px|-?\d+%|auto)\)$/,ay=az.exec(aD)||["",0,aC,aB,0];
return{top:parseFloat(ay[1])||0,right:ay[2]==="auto"?aC:parseFloat(ay[2]),bottom:ay[3]==="auto"?aB:parseFloat(ay[3]),left:parseFloat(ay[4])||0}
}ak.fx.step.clip=function(ay){if(!ay.clipInit){ay.start=ak(ay.elem).cssClip();
if(typeof ay.end==="string"){ay.end=av(ay.end,ay.elem)
}ay.clipInit=true
}ak(ay.elem).cssClip({top:ay.pos*(ay.end.top-ay.start.top)+ay.start.top,right:ay.pos*(ay.end.right-ay.start.right)+ay.start.right,bottom:ay.pos*(ay.end.bottom-ay.start.bottom)+ay.start.bottom,left:ay.pos*(ay.end.left-ay.start.left)+ay.start.left})
}
})();
(function(){var av={};
ak.each(["Quad","Cubic","Quart","Quint","Expo"],function(ax,aw){av[aw]=function(ay){return Math.pow(ay,ax+2)
}
});
ak.extend(av,{Sine:function(aw){return 1-Math.cos(aw*Math.PI/2)
},Circ:function(aw){return 1-Math.sqrt(1-aw*aw)
},Elastic:function(aw){return aw===0||aw===1?aw:-Math.pow(2,8*(aw-1))*Math.sin(((aw-1)*80-7.5)*Math.PI/15)
},Back:function(aw){return aw*aw*(3*aw-2)
},Bounce:function(ay){var aw,ax=4;
while(ay<((aw=Math.pow(2,--ax))-1)/11){}return 1/Math.pow(4,3-ax)-7.5625*Math.pow((aw*3-2)/22-ay,2)
}});
ak.each(av,function(ax,aw){ak.easing["easeIn"+ax]=aw;
ak.easing["easeOut"+ax]=function(ay){return 1-aw(1-ay)
};
ak.easing["easeInOut"+ax]=function(ay){return ay<0.5?aw(ay*2)/2:1-aw(ay*-2+2)/2
}
})
})();
var H=ak.effects;
/*!
 * jQuery UI Effects Blind 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var E=ak.effects.define("blind","hide",function(ax,av){var aA={up:["bottom","top"],vertical:["bottom","top"],down:["top","bottom"],left:["right","left"],horizontal:["right","left"],right:["left","right"]},ay=ak(this),az=ax.direction||"up",aC=ay.cssClip(),aw={clip:ak.extend({},aC)},aB=ak.effects.createPlaceholder(ay);
aw.clip[aA[az][0]]=aw.clip[aA[az][1]];
if(ax.mode==="show"){ay.cssClip(aw.clip);
if(aB){aB.css(ak.effects.clipToBox(aw))
}aw.clip=aC
}if(aB){aB.animate(ak.effects.clipToBox(aw),ax.duration,ax.easing)
}ay.animate(aw,{queue:false,duration:ax.duration,easing:ax.easing,complete:av})
});
/*!
 * jQuery UI Effects Bounce 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var z=ak.effects.define("bounce",function(aw,aD){var az,aH,aK,av=ak(this),aC=aw.mode,aB=aC==="hide",aL=aC==="show",aM=aw.direction||"up",ax=aw.distance,aA=aw.times||5,aN=aA*2+(aL||aB?1:0),aJ=aw.duration/aN,aF=aw.easing,ay=(aM==="up"||aM==="down")?"top":"left",aE=(aM==="up"||aM==="left"),aI=0,aG=av.queue().length;
ak.effects.createPlaceholder(av);
aK=av.css(ay);
if(!ax){ax=av[ay==="top"?"outerHeight":"outerWidth"]()/3
}if(aL){aH={opacity:1};
aH[ay]=aK;
av.css("opacity",0).css(ay,aE?-ax*2:ax*2).animate(aH,aJ,aF)
}if(aB){ax=ax/Math.pow(2,aA-1)
}aH={};
aH[ay]=aK;
for(;
aI<aA;
aI++){az={};
az[ay]=(aE?"-=":"+=")+ax;
av.animate(az,aJ,aF).animate(aH,aJ,aF);
ax=aB?ax*2:ax/2
}if(aB){az={opacity:0};
az[ay]=(aE?"-=":"+=")+ax;
av.animate(az,aJ,aF)
}av.queue(aD);
ak.effects.unshift(av,aG,aN+1)
});
/*!
 * jQuery UI Effects Clip 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var ae=ak.effects.define("clip","hide",function(aD,az){var aw,ax={},aA=ak(this),aC=aD.direction||"vertical",aB=aC==="both",av=aB||aC==="horizontal",ay=aB||aC==="vertical";
aw=aA.cssClip();
ax.clip={top:ay?(aw.bottom-aw.top)/2:aw.top,right:av?(aw.right-aw.left)/2:aw.right,bottom:ay?(aw.bottom-aw.top)/2:aw.bottom,left:av?(aw.right-aw.left)/2:aw.left};
ak.effects.createPlaceholder(aA);
if(aD.mode==="show"){aA.cssClip(ax.clip);
ax.clip=aw
}aA.animate(ax,{queue:false,duration:aD.duration,easing:aD.easing,complete:az})
});
/*!
 * jQuery UI Effects Drop 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var V=ak.effects.define("drop","hide",function(aF,ay){var av,az=ak(this),aB=aF.mode,aD=aB==="show",aC=aF.direction||"left",aw=(aC==="up"||aC==="down")?"top":"left",aE=(aC==="up"||aC==="left")?"-=":"+=",aA=(aE==="+=")?"-=":"+=",ax={opacity:0};
ak.effects.createPlaceholder(az);
av=aF.distance||az[aw==="top"?"outerHeight":"outerWidth"](true)/2;
ax[aw]=aE+av;
if(aD){az.css(ax);
ax[aw]=aA+av;
ax.opacity=1
}az.animate(ax,{queue:false,duration:aF.duration,easing:aF.easing,complete:ay})
});
/*!
 * jQuery UI Effects Explode 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var at=ak.effects.define("explode","hide",function(aw,aI){var aL,aK,ay,aG,aF,aD,aC=aw.pieces?Math.round(Math.sqrt(aw.pieces)):3,ax=aC,av=ak(this),aE=aw.mode,aM=aE==="show",aA=av.show().css("visibility","hidden").offset(),aJ=Math.ceil(av.outerWidth()/ax),aH=Math.ceil(av.outerHeight()/aC),aB=[];
function aN(){aB.push(this);
if(aB.length===aC*ax){az()
}}for(aL=0;
aL<aC;
aL++){aG=aA.top+aL*aH;
aD=aL-(aC-1)/2;
for(aK=0;
aK<ax;
aK++){ay=aA.left+aK*aJ;
aF=aK-(ax-1)/2;
av.clone().appendTo("body").wrap("<div></div>").css({position:"absolute",visibility:"visible",left:-aK*aJ,top:-aL*aH}).parent().addClass("ui-effects-explode").css({position:"absolute",overflow:"hidden",width:aJ,height:aH,left:ay+(aM?aF*aJ:0),top:aG+(aM?aD*aH:0),opacity:aM?0:1}).animate({left:ay+(aM?0:aF*aJ),top:aG+(aM?0:aD*aH),opacity:aM?1:0},aw.duration||500,aw.easing,aN)
}}function az(){av.css({visibility:"visible"});
ak(aB).remove();
aI()
}});
/*!
 * jQuery UI Effects Fade 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var au=ak.effects.define("fade","toggle",function(ax,aw){var av=ax.mode==="show";
ak(this).css("opacity",av?0:1).animate({opacity:av?1:0},{queue:false,duration:ax.duration,easing:ax.easing,complete:aw})
});
/*!
 * jQuery UI Effects Fold 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var u=ak.effects.define("fold","hide",function(aL,aA){var aB=ak(this),aC=aL.mode,aI=aC==="show",aD=aC==="hide",aK=aL.size||15,aE=/([0-9]+)%/.exec(aK),aJ=!!aL.horizFirst,ay=aJ?["right","bottom"]:["bottom","right"],az=aL.duration/2,aH=ak.effects.createPlaceholder(aB),aw=aB.cssClip(),aG={clip:ak.extend({},aw)},aF={clip:ak.extend({},aw)},av=[aw[ay[0]],aw[ay[1]]],ax=aB.queue().length;
if(aE){aK=parseInt(aE[1],10)/100*av[aD?0:1]
}aG.clip[ay[0]]=aK;
aF.clip[ay[0]]=aK;
aF.clip[ay[1]]=0;
if(aI){aB.cssClip(aF.clip);
if(aH){aH.css(ak.effects.clipToBox(aF))
}aF.clip=aw
}aB.queue(function(aM){if(aH){aH.animate(ak.effects.clipToBox(aG),az,aL.easing).animate(ak.effects.clipToBox(aF),az,aL.easing)
}aM()
}).animate(aG,az,aL.easing).animate(aF,az,aL.easing).queue(aA);
ak.effects.unshift(aB,ax,4)
});
/*!
 * jQuery UI Effects Highlight 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var J=ak.effects.define("highlight","show",function(aw,av){var ax=ak(this),ay={backgroundColor:ax.css("backgroundColor")};
if(aw.mode==="hide"){ay.opacity=0
}ak.effects.saveStyle(ax);
ax.css({backgroundImage:"none",backgroundColor:aw.color||"#ffff99"}).animate(ay,{queue:false,duration:aw.duration,easing:aw.easing,complete:av})
});
/*!
 * jQuery UI Effects Size 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var S=ak.effects.define("size",function(ay,aE){var aC,aD,aI,av=ak(this),aA=["fontSize"],aJ=["borderTopWidth","borderBottomWidth","paddingTop","paddingBottom"],ax=["borderLeftWidth","borderRightWidth","paddingLeft","paddingRight"],aB=ay.mode,aH=aB!=="effect",aM=ay.scale||"both",aK=ay.origin||["middle","center"],aL=av.css("position"),az=av.position(),aF=ak.effects.scaledDimensions(av),aG=ay.from||aF,aw=ay.to||ak.effects.scaledDimensions(av,0);
ak.effects.createPlaceholder(av);
if(aB==="show"){aI=aG;
aG=aw;
aw=aI
}aD={from:{y:aG.height/aF.height,x:aG.width/aF.width},to:{y:aw.height/aF.height,x:aw.width/aF.width}};
if(aM==="box"||aM==="both"){if(aD.from.y!==aD.to.y){aG=ak.effects.setTransition(av,aJ,aD.from.y,aG);
aw=ak.effects.setTransition(av,aJ,aD.to.y,aw)
}if(aD.from.x!==aD.to.x){aG=ak.effects.setTransition(av,ax,aD.from.x,aG);
aw=ak.effects.setTransition(av,ax,aD.to.x,aw)
}}if(aM==="content"||aM==="both"){if(aD.from.y!==aD.to.y){aG=ak.effects.setTransition(av,aA,aD.from.y,aG);
aw=ak.effects.setTransition(av,aA,aD.to.y,aw)
}}if(aK){aC=ak.effects.getBaseline(aK,aF);
aG.top=(aF.outerHeight-aG.outerHeight)*aC.y+az.top;
aG.left=(aF.outerWidth-aG.outerWidth)*aC.x+az.left;
aw.top=(aF.outerHeight-aw.outerHeight)*aC.y+az.top;
aw.left=(aF.outerWidth-aw.outerWidth)*aC.x+az.left
}av.css(aG);
if(aM==="content"||aM==="both"){aJ=aJ.concat(["marginTop","marginBottom"]).concat(aA);
ax=ax.concat(["marginLeft","marginRight"]);
av.find("*[width]").each(function(){var aQ=ak(this),aN=ak.effects.scaledDimensions(aQ),aP={height:aN.height*aD.from.y,width:aN.width*aD.from.x,outerHeight:aN.outerHeight*aD.from.y,outerWidth:aN.outerWidth*aD.from.x},aO={height:aN.height*aD.to.y,width:aN.width*aD.to.x,outerHeight:aN.height*aD.to.y,outerWidth:aN.width*aD.to.x};
if(aD.from.y!==aD.to.y){aP=ak.effects.setTransition(aQ,aJ,aD.from.y,aP);
aO=ak.effects.setTransition(aQ,aJ,aD.to.y,aO)
}if(aD.from.x!==aD.to.x){aP=ak.effects.setTransition(aQ,ax,aD.from.x,aP);
aO=ak.effects.setTransition(aQ,ax,aD.to.x,aO)
}if(aH){ak.effects.saveStyle(aQ)
}aQ.css(aP);
aQ.animate(aO,ay.duration,ay.easing,function(){if(aH){ak.effects.restoreStyle(aQ)
}})
})
}av.animate(aw,{queue:false,duration:ay.duration,easing:ay.easing,complete:function(){var aN=av.offset();
if(aw.opacity===0){av.css("opacity",aG.opacity)
}if(!aH){av.css("position",aL==="static"?"relative":aL).offset(aN);
ak.effects.saveStyle(av)
}aE()
}})
});
/*!
 * jQuery UI Effects Scale 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var O=ak.effects.define("scale",function(aw,av){var ax=ak(this),aA=aw.mode,ay=parseInt(aw.percent,10)||(parseInt(aw.percent,10)===0?0:(aA!=="effect"?0:100)),az=ak.extend(true,{from:ak.effects.scaledDimensions(ax),to:ak.effects.scaledDimensions(ax,ay,aw.direction||"both"),origin:aw.origin||["middle","center"]},aw);
if(aw.fade){az.from.opacity=1;
az.to.opacity=0
}ak.effects.effect.size.call(this,az,av)
});
/*!
 * jQuery UI Effects Puff 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var A=ak.effects.define("puff","hide",function(aw,av){var ax=ak.extend(true,{},aw,{fade:true,percent:parseInt(aw.percent,10)||150});
ak.effects.effect.scale.call(this,ax,av)
});
/*!
 * jQuery UI Effects Pulsate 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var x=ak.effects.define("pulsate","show",function(aG,ax){var az=ak(this),aA=aG.mode,aE=aA==="show",aB=aA==="hide",aF=aE||aB,aC=((aG.times||5)*2)+(aF?1:0),aw=aG.duration/aC,aD=0,ay=1,av=az.queue().length;
if(aE||!az.is(":visible")){az.css("opacity",0).show();
aD=1
}for(;
ay<aC;
ay++){az.animate({opacity:aD},aw,aG.easing);
aD=1-aD
}az.animate({opacity:aD},aw,aG.easing);
az.queue(ax);
ak.effects.unshift(az,av,aC+1)
});
/*!
 * jQuery UI Effects Shake 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var aj=ak.effects.define("shake",function(aJ,aC){var aD=1,aE=ak(this),aG=aJ.direction||"left",av=aJ.distance||20,aw=aJ.times||3,aH=aw*2+1,aA=Math.round(aJ.duration/aH),az=(aG==="up"||aG==="down")?"top":"left",ax=(aG==="up"||aG==="left"),aB={},aI={},aF={},ay=aE.queue().length;
ak.effects.createPlaceholder(aE);
aB[az]=(ax?"-=":"+=")+av;
aI[az]=(ax?"+=":"-=")+av*2;
aF[az]=(ax?"-=":"+=")+av*2;
aE.animate(aB,aA,aJ.easing);
for(;
aD<aw;
aD++){aE.animate(aI,aA,aJ.easing).animate(aF,aA,aJ.easing)
}aE.animate(aI,aA,aJ.easing).animate(aB,aA/2,aJ.easing).queue(aC);
ak.effects.unshift(aE,ay,aH+1)
});
/*!
 * jQuery UI Effects Slide 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var ai=ak.effects.define("slide","show",function(aG,aC){var az,aw,aD=ak(this),ax={up:["bottom","top"],down:["top","bottom"],left:["right","left"],right:["left","right"]},aE=aG.mode,aF=aG.direction||"left",aA=(aF==="up"||aF==="down")?"top":"left",ay=(aF==="up"||aF==="left"),av=aG.distance||aD[aA==="top"?"outerHeight":"outerWidth"](true),aB={};
ak.effects.createPlaceholder(aD);
az=aD.cssClip();
aw=aD.position()[aA];
aB[aA]=(ay?-1:1)*av+aw;
aB.clip=aD.cssClip();
aB.clip[ax[aF][1]]=aB.clip[ax[aF][0]];
if(aE==="show"){aD.cssClip(aB.clip);
aD.css(aA,aB[aA]);
aB.clip=az;
aB[aA]=aw
}aD.animate(aB,{queue:false,duration:aG.duration,easing:aG.easing,complete:aC})
});
/*!
 * jQuery UI Effects Transfer 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var H;
if(ak.uiBackCompat!==false){H=ak.effects.define("transfer",function(aw,av){ak(this).transfer(aw,av)
})
}var M=H;
/*!
 * jQuery UI Focusable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.ui.focusable=function(ay,aw){var aB,az,ax,aA,av,aC=ay.nodeName.toLowerCase();
if("area"===aC){aB=ay.parentNode;
az=aB.name;
if(!ay.href||!az||aB.nodeName.toLowerCase()!=="map"){return false
}ax=ak("img[usemap='#"+az+"']");
return ax.length>0&&ax.is(":visible")
}if(/^(input|select|textarea|button|object)$/.test(aC)){aA=!ay.disabled;
if(aA){av=ak(ay).closest("fieldset")[0];
if(av){aA=!av.disabled
}}}else{if("a"===aC){aA=ay.href||aw
}else{aA=aw
}}return aA&&ak(ay).is(":visible")&&o(ak(ay))
};
function o(aw){var av=aw.css("visibility");
while(av==="inherit"){aw=aw.parent();
av=aw.css("visibility")
}return av!=="hidden"
}ak.extend(ak.expr[":"],{focusable:function(av){return ak.ui.focusable(av,ak.attr(av,"tabindex")!=null)
}});
var ar=ak.ui.focusable;
var i=ak.fn.form=function(){return typeof this[0].form==="string"?this.closest("form"):ak(this[0].form)
};
/*!
 * jQuery UI Form Reset Mixin 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var N=ak.ui.formResetMixin={_formResetHandler:function(){var av=ak(this);
setTimeout(function(){var aw=av.data("ui-form-reset-instances");
ak.each(aw,function(){this.refresh()
})
})
},_bindFormResetHandler:function(){this.form=this.element.form();
if(!this.form.length){return
}var av=this.form.data("ui-form-reset-instances")||[];
if(!av.length){this.form.on("reset.ui-form-reset",this._formResetHandler)
}av.push(this);
this.form.data("ui-form-reset-instances",av)
},_unbindFormResetHandler:function(){if(!this.form.length){return
}var av=this.form.data("ui-form-reset-instances");
av.splice(ak.inArray(this,av),1);
if(av.length){this.form.data("ui-form-reset-instances",av)
}else{this.form.removeData("ui-form-reset-instances").off("reset.ui-form-reset")
}}};
/*!
 * jQuery UI Support for jQuery core 1.7.x 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 *
 */
if(ak.fn.jquery.substring(0,3)==="1.7"){ak.each(["Width","Height"],function(ax,av){var aw=av==="Width"?["Left","Right"]:["Top","Bottom"],ay=av.toLowerCase(),aA={innerWidth:ak.fn.innerWidth,innerHeight:ak.fn.innerHeight,outerWidth:ak.fn.outerWidth,outerHeight:ak.fn.outerHeight};
function az(aD,aC,aB,aE){ak.each(aw,function(){aC-=parseFloat(ak.css(aD,"padding"+this))||0;
if(aB){aC-=parseFloat(ak.css(aD,"border"+this+"Width"))||0
}if(aE){aC-=parseFloat(ak.css(aD,"margin"+this))||0
}});
return aC
}ak.fn["inner"+av]=function(aB){if(aB===undefined){return aA["inner"+av].call(this)
}return this.each(function(){ak(this).css(ay,az(this,aB)+"px")
})
};
ak.fn["outer"+av]=function(aB,aC){if(typeof aB!=="number"){return aA["outer"+av].call(this,aB)
}return this.each(function(){ak(this).css(ay,az(this,aB,true,aC)+"px")
})
}
});
ak.fn.addBack=function(av){return this.add(av==null?this.prevObject:this.prevObject.filter(av))
}
}
/*!
 * jQuery UI Keycode 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var n=ak.ui.keyCode={BACKSPACE:8,COMMA:188,DELETE:46,DOWN:40,END:35,ENTER:13,ESCAPE:27,HOME:36,LEFT:37,PAGE_DOWN:34,PAGE_UP:33,PERIOD:190,RIGHT:39,SPACE:32,TAB:9,UP:38};
var h=ak.ui.escapeSelector=(function(){var av=/([!"#$%&'()*+,./:;<=>?@[\]^`{|}~])/g;
return function(aw){return aw.replace(av,"\\$1")
}
})();
/*!
 * jQuery UI Labels 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var am=ak.fn.labels=function(){var aw,av,az,ay,ax;
if(this[0].labels&&this[0].labels.length){return this.pushStack(this[0].labels)
}ay=this.eq(0).parents("label");
az=this.attr("id");
if(az){aw=this.eq(0).parents().last();
ax=aw.add(aw.length?aw.siblings():this.siblings());
av="label[for='"+ak.ui.escapeSelector(az)+"']";
ay=ay.add(ax.find(av).addBack(av))
}return this.pushStack(ay)
};
/*!
 * jQuery UI Scroll Parent 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var Z=ak.fn.scrollParent=function(ax){var aw=this.css("position"),av=aw==="absolute",ay=ax?/(auto|scroll|hidden)/:/(auto|scroll)/,az=this.parents().filter(function(){var aA=ak(this);
if(av&&aA.css("position")==="static"){return false
}return ay.test(aA.css("overflow")+aA.css("overflow-y")+aA.css("overflow-x"))
}).eq(0);
return aw==="fixed"||!az.length?ak(this[0].ownerDocument||document):az
};
/*!
 * jQuery UI Tabbable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var f=ak.extend(ak.expr[":"],{tabbable:function(ax){var aw=ak.attr(ax,"tabindex"),av=aw!=null;
return(!av||aw>=0)&&ak.ui.focusable(ax,av)
}});
/*!
 * jQuery UI Unique ID 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var aa=ak.fn.extend({uniqueId:(function(){var av=0;
return function(){return this.each(function(){if(!this.id){this.id="ui-id-"+(++av)
}})
}
})(),removeUniqueId:function(){return this.each(function(){if(/^ui-id-\d+$/.test(this.id)){ak(this).removeAttr("id")
}})
}});
/*!
 * jQuery UI Accordion 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var d=ak.widget("ui.accordion",{version:"1.12.1",options:{active:0,animate:{},classes:{"ui-accordion-header":"ui-corner-top","ui-accordion-header-collapsed":"ui-corner-all","ui-accordion-content":"ui-corner-bottom"},collapsible:false,event:"click",header:"> li > :first-child, > :not(li):even",heightStyle:"auto",icons:{activeHeader:"ui-icon-triangle-1-s",header:"ui-icon-triangle-1-e"},activate:null,beforeActivate:null},hideProps:{borderTopWidth:"hide",borderBottomWidth:"hide",paddingTop:"hide",paddingBottom:"hide",height:"hide"},showProps:{borderTopWidth:"show",borderBottomWidth:"show",paddingTop:"show",paddingBottom:"show",height:"show"},_create:function(){var av=this.options;
this.prevShow=this.prevHide=ak();
this._addClass("ui-accordion","ui-widget ui-helper-reset");
this.element.attr("role","tablist");
if(!av.collapsible&&(av.active===false||av.active==null)){av.active=0
}this._processPanels();
if(av.active<0){av.active+=this.headers.length
}this._refresh()
},_getCreateEventData:function(){return{header:this.active,panel:!this.active.length?ak():this.active.next()}
},_createIcons:function(){var ax,aw,av=this.options.icons;
if(av){ax=ak("<span>");
this._addClass(ax,"ui-accordion-header-icon","ui-icon "+av.header);
ax.prependTo(this.headers);
aw=this.active.children(".ui-accordion-header-icon");
this._removeClass(aw,av.header)._addClass(aw,null,av.activeHeader)._addClass(this.headers,"ui-accordion-icons")
}},_destroyIcons:function(){this._removeClass(this.headers,"ui-accordion-icons");
this.headers.children(".ui-accordion-header-icon").remove()
},_destroy:function(){var av;
this.element.removeAttr("role");
this.headers.removeAttr("role aria-expanded aria-selected aria-controls tabIndex").removeUniqueId();
this._destroyIcons();
av=this.headers.next().css("display","").removeAttr("role aria-hidden aria-labelledby").removeUniqueId();
if(this.options.heightStyle!=="content"){av.css("height","")
}},_setOption:function(av,aw){if(av==="active"){this._activate(aw);
return
}if(av==="event"){if(this.options.event){this._off(this.headers,this.options.event)
}this._setupEvents(aw)
}this._super(av,aw);
if(av==="collapsible"&&!aw&&this.options.active===false){this._activate(0)
}if(av==="icons"){this._destroyIcons();
if(aw){this._createIcons()
}}},_setOptionDisabled:function(av){this._super(av);
this.element.attr("aria-disabled",av);
this._toggleClass(null,"ui-state-disabled",!!av);
this._toggleClass(this.headers.add(this.headers.next()),null,"ui-state-disabled",!!av)
},_keydown:function(ay){if(ay.altKey||ay.ctrlKey){return
}var az=ak.ui.keyCode,ax=this.headers.length,av=this.headers.index(ay.target),aw=false;
switch(ay.keyCode){case az.RIGHT:case az.DOWN:aw=this.headers[(av+1)%ax];
break;
case az.LEFT:case az.UP:aw=this.headers[(av-1+ax)%ax];
break;
case az.SPACE:case az.ENTER:this._eventHandler(ay);
break;
case az.HOME:aw=this.headers[0];
break;
case az.END:aw=this.headers[ax-1];
break
}if(aw){ak(ay.target).attr("tabIndex",-1);
ak(aw).attr("tabIndex",0);
ak(aw).trigger("focus");
ay.preventDefault()
}},_panelKeyDown:function(av){if(av.keyCode===ak.ui.keyCode.UP&&av.ctrlKey){ak(av.currentTarget).prev().trigger("focus")
}},refresh:function(){var av=this.options;
this._processPanels();
if((av.active===false&&av.collapsible===true)||!this.headers.length){av.active=false;
this.active=ak()
}else{if(av.active===false){this._activate(0)
}else{if(this.active.length&&!ak.contains(this.element[0],this.active[0])){if(this.headers.length===this.headers.find(".ui-state-disabled").length){av.active=false;
this.active=ak()
}else{this._activate(Math.max(0,av.active-1))
}}else{av.active=this.headers.index(this.active)
}}}this._destroyIcons();
this._refresh()
},_processPanels:function(){var aw=this.headers,av=this.panels;
this.headers=this.element.find(this.options.header);
this._addClass(this.headers,"ui-accordion-header ui-accordion-header-collapsed","ui-state-default");
this.panels=this.headers.next().filter(":not(.ui-accordion-content-active)").hide();
this._addClass(this.panels,"ui-accordion-content","ui-helper-reset ui-widget-content");
if(av){this._off(aw.not(this.headers));
this._off(av.not(this.panels))
}},_refresh:function(){var ay,aw=this.options,av=aw.heightStyle,ax=this.element.parent();
this.active=this._findActive(aw.active);
this._addClass(this.active,"ui-accordion-header-active","ui-state-active")._removeClass(this.active,"ui-accordion-header-collapsed");
this._addClass(this.active.next(),"ui-accordion-content-active");
this.active.next().show();
this.headers.attr("role","tab").each(function(){var aC=ak(this),aB=aC.uniqueId().attr("id"),az=aC.next(),aA=az.uniqueId().attr("id");
aC.attr("aria-controls",aA);
az.attr("aria-labelledby",aB)
}).next().attr("role","tabpanel");
this.headers.not(this.active).attr({"aria-selected":"false","aria-expanded":"false",tabIndex:-1}).next().attr({"aria-hidden":"true"}).hide();
if(!this.active.length){this.headers.eq(0).attr("tabIndex",0)
}else{this.active.attr({"aria-selected":"true","aria-expanded":"true",tabIndex:0}).next().attr({"aria-hidden":"false"})
}this._createIcons();
this._setupEvents(aw.event);
if(av==="fill"){ay=ax.height();
this.element.siblings(":visible").each(function(){var aA=ak(this),az=aA.css("position");
if(az==="absolute"||az==="fixed"){return
}ay-=aA.outerHeight(true)
});
this.headers.each(function(){ay-=ak(this).outerHeight(true)
});
this.headers.next().each(function(){ak(this).height(Math.max(0,ay-ak(this).innerHeight()+ak(this).height()))
}).css("overflow","auto")
}else{if(av==="auto"){ay=0;
this.headers.next().each(function(){var az=ak(this).is(":visible");
if(!az){ak(this).show()
}ay=Math.max(ay,ak(this).css("height","").height());
if(!az){ak(this).hide()
}}).height(ay)
}}},_activate:function(av){var aw=this._findActive(av)[0];
if(aw===this.active[0]){return
}aw=aw||this.active[0];
this._eventHandler({target:aw,currentTarget:aw,preventDefault:ak.noop})
},_findActive:function(av){return typeof av==="number"?this.headers.eq(av):ak()
},_setupEvents:function(aw){var av={keydown:"_keydown"};
if(aw){ak.each(aw.split(" "),function(ay,ax){av[ax]="_eventHandler"
})
}this._off(this.headers.add(this.headers.next()));
this._on(this.headers,av);
this._on(this.headers.next(),{keydown:"_panelKeyDown"});
this._hoverable(this.headers);
this._focusable(this.headers)
},_eventHandler:function(aw){var ax,ay,aF=this.options,aA=this.active,aB=ak(aw.currentTarget),aD=aB[0]===aA[0],az=aD&&aF.collapsible,av=az?ak():aB.next(),aC=aA.next(),aE={oldHeader:aA,oldPanel:aC,newHeader:az?ak():aB,newPanel:av};
aw.preventDefault();
if((aD&&!aF.collapsible)||(this._trigger("beforeActivate",aw,aE)===false)){return
}aF.active=az?false:this.headers.index(aB);
this.active=aD?ak():aB;
this._toggle(aE);
this._removeClass(aA,"ui-accordion-header-active","ui-state-active");
if(aF.icons){ax=aA.children(".ui-accordion-header-icon");
this._removeClass(ax,null,aF.icons.activeHeader)._addClass(ax,null,aF.icons.header)
}if(!aD){this._removeClass(aB,"ui-accordion-header-collapsed")._addClass(aB,"ui-accordion-header-active","ui-state-active");
if(aF.icons){ay=aB.children(".ui-accordion-header-icon");
this._removeClass(ay,null,aF.icons.header)._addClass(ay,null,aF.icons.activeHeader)
}this._addClass(aB.next(),"ui-accordion-content-active")
}},_toggle:function(ax){var av=ax.newPanel,aw=this.prevShow.length?this.prevShow:ax.oldPanel;
this.prevShow.add(this.prevHide).stop(true,true);
this.prevShow=av;
this.prevHide=aw;
if(this.options.animate){this._animate(av,aw,ax)
}else{aw.hide();
av.show();
this._toggleComplete(ax)
}aw.attr({"aria-hidden":"true"});
aw.prev().attr({"aria-selected":"false","aria-expanded":"false"});
if(av.length&&aw.length){aw.prev().attr({tabIndex:-1,"aria-expanded":"false"})
}else{if(av.length){this.headers.filter(function(){return parseInt(ak(this).attr("tabIndex"),10)===0
}).attr("tabIndex",-1)
}}av.attr("aria-hidden","false").prev().attr({"aria-selected":"true","aria-expanded":"true",tabIndex:0})
},_animate:function(av,aE,aA){var aD,aC,az,aB=this,aF=0,ay=av.css("box-sizing"),aG=av.length&&(!aE.length||(av.index()<aE.index())),ax=this.options.animate||{},aH=aG&&ax.down||ax,aw=function(){aB._toggleComplete(aA)
};
if(typeof aH==="number"){az=aH
}if(typeof aH==="string"){aC=aH
}aC=aC||aH.easing||ax.easing;
az=az||aH.duration||ax.duration;
if(!aE.length){return av.animate(this.showProps,az,aC,aw)
}if(!av.length){return aE.animate(this.hideProps,az,aC,aw)
}aD=av.show().outerHeight();
aE.animate(this.hideProps,{duration:az,easing:aC,step:function(aI,aJ){aJ.now=Math.round(aI)
}});
av.hide().animate(this.showProps,{duration:az,easing:aC,complete:aw,step:function(aI,aJ){aJ.now=Math.round(aI);
if(aJ.prop!=="height"){if(ay==="content-box"){aF+=aJ.now
}}else{if(aB.options.heightStyle!=="content"){aJ.now=Math.round(aD-aE.outerHeight()-aF);
aF=0
}}}})
},_toggleComplete:function(ax){var av=ax.oldPanel,aw=av.prev();
this._removeClass(av,"ui-accordion-content-active");
this._removeClass(aw,"ui-accordion-header-active")._addClass(aw,"ui-accordion-header-collapsed");
if(av.length){av.parent()[0].className=av.parent()[0].className
}this._trigger("activate",null,ax)
}});
var j=ak.ui.safeActiveElement=function(av){var ax;
try{ax=av.activeElement
}catch(aw){ax=av.body
}if(!ax){ax=av.body
}if(!ax.nodeName){ax=av.body
}return ax
};
/*!
 * jQuery UI Menu 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var p=ak.widget("ui.menu",{version:"1.12.1",defaultElement:"<ul>",delay:300,options:{icons:{submenu:"ui-icon-caret-1-e"},items:"> *",menus:"ul",position:{my:"left top",at:"right top"},role:"menu",blur:null,focus:null,select:null},_create:function(){this.activeMenu=this.element;
this.mouseHandled=false;
this.element.uniqueId().attr({role:this.options.role,tabIndex:0});
this._addClass("ui-menu","ui-widget ui-widget-content");
this._on({"mousedown .ui-menu-item":function(av){av.preventDefault()
},"click .ui-menu-item":function(av){var ax=ak(av.target);
var aw=ak(ak.ui.safeActiveElement(this.document[0]));
if(!this.mouseHandled&&ax.not(".ui-state-disabled").length){this.select(av);
if(!av.isPropagationStopped()){this.mouseHandled=true
}if(ax.has(".ui-menu").length){this.expand(av)
}else{if(!this.element.is(":focus")&&aw.closest(".ui-menu").length){this.element.trigger("focus",[true]);
if(this.active&&this.active.parents(".ui-menu").length===1){clearTimeout(this.timer)
}}}}},"mouseenter .ui-menu-item":function(av){if(this.previousFilter){return
}var aw=ak(av.target).closest(".ui-menu-item"),ax=ak(av.currentTarget);
if(aw[0]!==ax[0]){return
}this._removeClass(ax.siblings().children(".ui-state-active"),null,"ui-state-active");
this.focus(av,ax)
},mouseleave:"collapseAll","mouseleave .ui-menu":"collapseAll",focus:function(ax,av){var aw=this.active||this.element.find(this.options.items).eq(0);
if(!av){this.focus(ax,aw)
}},blur:function(av){this._delay(function(){var aw=!ak.contains(this.element[0],ak.ui.safeActiveElement(this.document[0]));
if(aw){this.collapseAll(av)
}})
},keydown:"_keydown"});
this.refresh();
this._on(this.document,{click:function(av){if(this._closeOnDocumentClick(av)){this.collapseAll(av)
}this.mouseHandled=false
}})
},_destroy:function(){var aw=this.element.find(".ui-menu-item").removeAttr("role aria-disabled"),av=aw.children(".ui-menu-item-wrapper").removeUniqueId().removeAttr("tabIndex role aria-haspopup");
this.element.removeAttr("aria-activedescendant").find(".ui-menu").addBack().removeAttr("role aria-labelledby aria-expanded aria-hidden aria-disabled tabIndex").removeUniqueId().show();
av.children().each(function(){var ax=ak(this);
if(ax.data("ui-menu-submenu-caret")){ax.remove()
}})
},_keydown:function(az){var aw,ay,aA,ax,av=true;
switch(az.keyCode){case ak.ui.keyCode.PAGE_UP:this.previousPage(az);
break;
case ak.ui.keyCode.PAGE_DOWN:this.nextPage(az);
break;
case ak.ui.keyCode.HOME:this._move("first","first",az);
break;
case ak.ui.keyCode.END:this._move("last","last",az);
break;
case ak.ui.keyCode.UP:this.previous(az);
break;
case ak.ui.keyCode.DOWN:this.next(az);
break;
case ak.ui.keyCode.LEFT:this.collapse(az);
break;
case ak.ui.keyCode.RIGHT:if(this.active&&!this.active.is(".ui-state-disabled")){this.expand(az)
}break;
case ak.ui.keyCode.ENTER:case ak.ui.keyCode.SPACE:this._activate(az);
break;
case ak.ui.keyCode.ESCAPE:this.collapse(az);
break;
default:av=false;
ay=this.previousFilter||"";
ax=false;
aA=az.keyCode>=96&&az.keyCode<=105?(az.keyCode-96).toString():String.fromCharCode(az.keyCode);
clearTimeout(this.filterTimer);
if(aA===ay){ax=true
}else{aA=ay+aA
}aw=this._filterMenuItems(aA);
aw=ax&&aw.index(this.active.next())!==-1?this.active.nextAll(".ui-menu-item"):aw;
if(!aw.length){aA=String.fromCharCode(az.keyCode);
aw=this._filterMenuItems(aA)
}if(aw.length){this.focus(az,aw);
this.previousFilter=aA;
this.filterTimer=this._delay(function(){delete this.previousFilter
},1000)
}else{delete this.previousFilter
}}if(av){az.preventDefault()
}},_activate:function(av){if(this.active&&!this.active.is(".ui-state-disabled")){if(this.active.children("[aria-haspopup='true']").length){this.expand(av)
}else{this.select(av)
}}},refresh:function(){var aC,ax,aA,ay,av,aB=this,az=this.options.icons.submenu,aw=this.element.find(this.options.menus);
this._toggleClass("ui-menu-icons",null,!!this.element.find(".ui-icon").length);
aA=aw.filter(":not(.ui-menu)").hide().attr({role:this.options.role,"aria-hidden":"true","aria-expanded":"false"}).each(function(){var aF=ak(this),aD=aF.prev(),aE=ak("<span>").data("ui-menu-submenu-caret",true);
aB._addClass(aE,"ui-menu-icon","ui-icon "+az);
aD.attr("aria-haspopup","true").prepend(aE);
aF.attr("aria-labelledby",aD.attr("id"))
});
this._addClass(aA,"ui-menu","ui-widget ui-widget-content ui-front");
aC=aw.add(this.element);
ax=aC.find(this.options.items);
ax.not(".ui-menu-item").each(function(){var aD=ak(this);
if(aB._isDivider(aD)){aB._addClass(aD,"ui-menu-divider","ui-widget-content")
}});
ay=ax.not(".ui-menu-item, .ui-menu-divider");
av=ay.children().not(".ui-menu").uniqueId().attr({tabIndex:-1,role:this._itemRole()});
this._addClass(ay,"ui-menu-item")._addClass(av,"ui-menu-item-wrapper");
ax.filter(".ui-state-disabled").attr("aria-disabled","true");
if(this.active&&!ak.contains(this.element[0],this.active[0])){this.blur()
}},_itemRole:function(){return{menu:"menuitem",listbox:"option"}[this.options.role]
},_setOption:function(aw,ax){if(aw==="icons"){var av=this.element.find(".ui-menu-icon");
this._removeClass(av,null,this.options.icons.submenu)._addClass(av,null,ax.submenu)
}this._super(aw,ax)
},_setOptionDisabled:function(av){this._super(av);
this.element.attr("aria-disabled",String(av));
this._toggleClass(null,"ui-state-disabled",!!av)
},focus:function(ax,aw){var az,ay,av;
this.blur(ax,ax&&ax.type==="focus");
this._scrollIntoView(aw);
this.active=aw.first();
ay=this.active.children(".ui-menu-item-wrapper");
this._addClass(ay,null,"ui-state-active");
if(this.options.role){this.element.attr("aria-activedescendant",ay.attr("id"))
}av=this.active.parent().closest(".ui-menu-item").children(".ui-menu-item-wrapper");
this._addClass(av,null,"ui-state-active");
if(ax&&ax.type==="keydown"){this._close()
}else{this.timer=this._delay(function(){this._close()
},this.delay)
}az=aw.children(".ui-menu");
if(az.length&&ax&&(/^mouse/.test(ax.type))){this._startOpening(az)
}this.activeMenu=aw.parent();
this._trigger("focus",ax,{item:aw})
},_scrollIntoView:function(ay){var aB,ax,az,av,aw,aA;
if(this._hasScroll()){aB=parseFloat(ak.css(this.activeMenu[0],"borderTopWidth"))||0;
ax=parseFloat(ak.css(this.activeMenu[0],"paddingTop"))||0;
az=ay.offset().top-this.activeMenu.offset().top-aB-ax;
av=this.activeMenu.scrollTop();
aw=this.activeMenu.height();
aA=ay.outerHeight();
if(az<0){this.activeMenu.scrollTop(av+az)
}else{if(az+aA>aw){this.activeMenu.scrollTop(av+az-aw+aA)
}}}},blur:function(aw,av){if(!av){clearTimeout(this.timer)
}if(!this.active){return
}this._removeClass(this.active.children(".ui-menu-item-wrapper"),null,"ui-state-active");
this._trigger("blur",aw,{item:this.active});
this.active=null
},_startOpening:function(av){clearTimeout(this.timer);
if(av.attr("aria-hidden")!=="true"){return
}this.timer=this._delay(function(){this._close();
this._open(av)
},this.delay)
},_open:function(aw){var av=ak.extend({of:this.active},this.options.position);
clearTimeout(this.timer);
this.element.find(".ui-menu").not(aw.parents(".ui-menu")).hide().attr("aria-hidden","true");
aw.show().removeAttr("aria-hidden").attr("aria-expanded","true").position(av)
},collapseAll:function(aw,av){clearTimeout(this.timer);
this.timer=this._delay(function(){var ax=av?this.element:ak(aw&&aw.target).closest(this.element.find(".ui-menu"));
if(!ax.length){ax=this.element
}this._close(ax);
this.blur(aw);
this._removeClass(ax.find(".ui-state-active"),null,"ui-state-active");
this.activeMenu=ax
},this.delay)
},_close:function(av){if(!av){av=this.active?this.active.parent():this.element
}av.find(".ui-menu").hide().attr("aria-hidden","true").attr("aria-expanded","false")
},_closeOnDocumentClick:function(av){return !ak(av.target).closest(".ui-menu").length
},_isDivider:function(av){return !/[^\-\u2014\u2013\s]/.test(av.text())
},collapse:function(aw){var av=this.active&&this.active.parent().closest(".ui-menu-item",this.element);
if(av&&av.length){this._close();
this.focus(aw,av)
}},expand:function(aw){var av=this.active&&this.active.children(".ui-menu ").find(this.options.items).first();
if(av&&av.length){this._open(av.parent());
this._delay(function(){this.focus(aw,av)
})
}},next:function(av){this._move("next","first",av)
},previous:function(av){this._move("prev","last",av)
},isFirstItem:function(){return this.active&&!this.active.prevAll(".ui-menu-item").length
},isLastItem:function(){return this.active&&!this.active.nextAll(".ui-menu-item").length
},_move:function(ay,aw,ax){var av;
if(this.active){if(ay==="first"||ay==="last"){av=this.active[ay==="first"?"prevAll":"nextAll"](".ui-menu-item").eq(-1)
}else{av=this.active[ay+"All"](".ui-menu-item").eq(0)
}}if(!av||!av.length||!this.active){av=this.activeMenu.find(this.options.items)[aw]()
}this.focus(ax,av)
},nextPage:function(ax){var aw,ay,av;
if(!this.active){this.next(ax);
return
}if(this.isLastItem()){return
}if(this._hasScroll()){ay=this.active.offset().top;
av=this.element.height();
this.active.nextAll(".ui-menu-item").each(function(){aw=ak(this);
return aw.offset().top-ay-av<0
});
this.focus(ax,aw)
}else{this.focus(ax,this.activeMenu.find(this.options.items)[!this.active?"first":"last"]())
}},previousPage:function(ax){var aw,ay,av;
if(!this.active){this.next(ax);
return
}if(this.isFirstItem()){return
}if(this._hasScroll()){ay=this.active.offset().top;
av=this.element.height();
this.active.prevAll(".ui-menu-item").each(function(){aw=ak(this);
return aw.offset().top-ay+av>0
});
this.focus(ax,aw)
}else{this.focus(ax,this.activeMenu.find(this.options.items).first())
}},_hasScroll:function(){return this.element.outerHeight()<this.element.prop("scrollHeight")
},select:function(av){this.active=this.active||ak(av.target).closest(".ui-menu-item");
var aw={item:this.active};
if(!this.active.has(".ui-menu").length){this.collapseAll(av,true)
}this._trigger("select",av,aw)
},_filterMenuItems:function(ax){var av=ax.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g,"\\$&"),aw=new RegExp("^"+av,"i");
return this.activeMenu.find(this.options.items).filter(".ui-menu-item").filter(function(){return aw.test(ak.trim(ak(this).children(".ui-menu-item-wrapper").text()))
})
}});
/*!
 * jQuery UI Autocomplete 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.autocomplete",{version:"1.12.1",defaultElement:"<input>",options:{appendTo:null,autoFocus:false,delay:300,minLength:1,position:{my:"left top",at:"left bottom",collision:"none"},source:null,change:null,close:null,focus:null,open:null,response:null,search:null,select:null},requestIndex:0,pending:0,_create:function(){var ax,av,ay,aA=this.element[0].nodeName.toLowerCase(),az=aA==="textarea",aw=aA==="input";
this.isMultiLine=az||!aw&&this._isContentEditable(this.element);
this.valueMethod=this.element[az||aw?"val":"text"];
this.isNewMenu=true;
this._addClass("ui-autocomplete-input");
this.element.attr("autocomplete","off");
this._on(this.element,{keydown:function(aB){if(this.element.prop("readOnly")){ax=true;
ay=true;
av=true;
return
}ax=false;
ay=false;
av=false;
var aC=ak.ui.keyCode;
switch(aB.keyCode){case aC.PAGE_UP:ax=true;
this._move("previousPage",aB);
break;
case aC.PAGE_DOWN:ax=true;
this._move("nextPage",aB);
break;
case aC.UP:ax=true;
this._keyEvent("previous",aB);
break;
case aC.DOWN:ax=true;
this._keyEvent("next",aB);
break;
case aC.ENTER:if(this.menu.active){ax=true;
aB.preventDefault();
this.menu.select(aB)
}break;
case aC.TAB:if(this.menu.active){this.menu.select(aB)
}break;
case aC.ESCAPE:if(this.menu.element.is(":visible")){if(!this.isMultiLine){this._value(this.term)
}this.close(aB);
aB.preventDefault()
}break;
default:av=true;
this._searchTimeout(aB);
break
}},keypress:function(aB){if(ax){ax=false;
if(!this.isMultiLine||this.menu.element.is(":visible")){aB.preventDefault()
}return
}if(av){return
}var aC=ak.ui.keyCode;
switch(aB.keyCode){case aC.PAGE_UP:this._move("previousPage",aB);
break;
case aC.PAGE_DOWN:this._move("nextPage",aB);
break;
case aC.UP:this._keyEvent("previous",aB);
break;
case aC.DOWN:this._keyEvent("next",aB);
break
}},input:function(aB){if(ay){ay=false;
aB.preventDefault();
return
}this._searchTimeout(aB)
},focus:function(){this.selectedItem=null;
this.previous=this._value()
},blur:function(aB){if(this.cancelBlur){delete this.cancelBlur;
return
}clearTimeout(this.searching);
this.close(aB);
this._change(aB)
}});
this._initSource();
this.menu=ak("<ul>").appendTo(this._appendTo()).menu({role:null}).hide().menu("instance");
this._addClass(this.menu.element,"ui-autocomplete","ui-front");
this._on(this.menu.element,{mousedown:function(aB){aB.preventDefault();
this.cancelBlur=true;
this._delay(function(){delete this.cancelBlur;
if(this.element[0]!==ak.ui.safeActiveElement(this.document[0])){this.element.trigger("focus")
}})
},menufocus:function(aD,aE){var aB,aC;
if(this.isNewMenu){this.isNewMenu=false;
if(aD.originalEvent&&/^mouse/.test(aD.originalEvent.type)){this.menu.blur();
this.document.one("mousemove",function(){ak(aD.target).trigger(aD.originalEvent)
});
return
}}aC=aE.item.data("ui-autocomplete-item");
if(false!==this._trigger("focus",aD,{item:aC})){if(aD.originalEvent&&/^key/.test(aD.originalEvent.type)){this._value(aC.value)
}}aB=aE.item.attr("aria-label")||aC.value;
if(aB&&ak.trim(aB).length){this.liveRegion.children().hide();
ak("<div>").text(aB).appendTo(this.liveRegion)
}},menuselect:function(aD,aE){var aC=aE.item.data("ui-autocomplete-item"),aB=this.previous;
if(this.element[0]!==ak.ui.safeActiveElement(this.document[0])){this.element.trigger("focus");
this.previous=aB;
this._delay(function(){this.previous=aB;
this.selectedItem=aC
})
}if(false!==this._trigger("select",aD,{item:aC})){this._value(aC.value)
}this.term=this._value();
this.close(aD);
this.selectedItem=aC
}});
this.liveRegion=ak("<div>",{role:"status","aria-live":"assertive","aria-relevant":"additions"}).appendTo(this.document[0].body);
this._addClass(this.liveRegion,null,"ui-helper-hidden-accessible");
this._on(this.window,{beforeunload:function(){this.element.removeAttr("autocomplete")
}})
},_destroy:function(){clearTimeout(this.searching);
this.element.removeAttr("autocomplete");
this.menu.element.remove();
this.liveRegion.remove()
},_setOption:function(av,aw){this._super(av,aw);
if(av==="source"){this._initSource()
}if(av==="appendTo"){this.menu.element.appendTo(this._appendTo())
}if(av==="disabled"&&aw&&this.xhr){this.xhr.abort()
}},_isEventTargetInWidget:function(av){var aw=this.menu.element[0];
return av.target===this.element[0]||av.target===aw||ak.contains(aw,av.target)
},_closeOnClickOutside:function(av){if(!this._isEventTargetInWidget(av)){this.close()
}},_appendTo:function(){var av=this.options.appendTo;
if(av){av=av.jquery||av.nodeType?ak(av):this.document.find(av).eq(0)
}if(!av||!av[0]){av=this.element.closest(".ui-front, dialog")
}if(!av.length){av=this.document[0].body
}return av
},_initSource:function(){var ax,av,aw=this;
if(ak.isArray(this.options.source)){ax=this.options.source;
this.source=function(az,ay){ay(ak.ui.autocomplete.filter(ax,az.term))
}
}else{if(typeof this.options.source==="string"){av=this.options.source;
this.source=function(az,ay){if(aw.xhr){aw.xhr.abort()
}aw.xhr=ak.ajax({url:av,data:az,dataType:"json",success:function(aA){ay(aA)
},error:function(){ay([])
}})
}
}else{this.source=this.options.source
}}},_searchTimeout:function(av){clearTimeout(this.searching);
this.searching=this._delay(function(){var ax=this.term===this._value(),aw=this.menu.element.is(":visible"),ay=av.altKey||av.ctrlKey||av.metaKey||av.shiftKey;
if(!ax||(ax&&!aw&&!ay)){this.selectedItem=null;
this.search(null,av)
}},this.options.delay)
},search:function(aw,av){aw=aw!=null?aw:this._value();
this.term=this._value();
if(aw.length<this.options.minLength){return this.close(av)
}if(this._trigger("search",av)===false){return
}return this._search(aw)
},_search:function(av){this.pending++;
this._addClass("ui-autocomplete-loading");
this.cancelSearch=false;
this.source({term:av},this._response())
},_response:function(){var av=++this.requestIndex;
return ak.proxy(function(aw){if(av===this.requestIndex){this.__response(aw)
}this.pending--;
if(!this.pending){this._removeClass("ui-autocomplete-loading")
}},this)
},__response:function(av){if(av){av=this._normalize(av)
}this._trigger("response",null,{content:av});
if(!this.options.disabled&&av&&av.length&&!this.cancelSearch){this._suggest(av);
this._trigger("open")
}else{this._close()
}},close:function(av){this.cancelSearch=true;
this._close(av)
},_close:function(av){this._off(this.document,"mousedown");
if(this.menu.element.is(":visible")){this.menu.element.hide();
this.menu.blur();
this.isNewMenu=true;
this._trigger("close",av)
}},_change:function(av){if(this.previous!==this._value()){this._trigger("change",av,{item:this.selectedItem})
}},_normalize:function(av){if(av.length&&av[0].label&&av[0].value){return av
}return ak.map(av,function(aw){if(typeof aw==="string"){return{label:aw,value:aw}
}return ak.extend({},aw,{label:aw.label||aw.value,value:aw.value||aw.label})
})
},_suggest:function(av){var aw=this.menu.element.empty();
this._renderMenu(aw,av);
this.isNewMenu=true;
this.menu.refresh();
aw.show();
this._resizeMenu();
aw.position(ak.extend({of:this.element},this.options.position));
if(this.options.autoFocus){this.menu.next()
}this._on(this.document,{mousedown:"_closeOnClickOutside"})
},_resizeMenu:function(){var av=this.menu.element;
av.outerWidth(Math.max(av.width("").outerWidth()+1,this.element.outerWidth()))
},_renderMenu:function(aw,av){var ax=this;
ak.each(av,function(ay,az){ax._renderItemData(aw,az)
})
},_renderItemData:function(av,aw){return this._renderItem(av,aw).data("ui-autocomplete-item",aw)
},_renderItem:function(av,aw){return ak("<li>").append(ak("<div>").text(aw.label)).appendTo(av)
},_move:function(aw,av){if(!this.menu.element.is(":visible")){this.search(null,av);
return
}if(this.menu.isFirstItem()&&/^previous/.test(aw)||this.menu.isLastItem()&&/^next/.test(aw)){if(!this.isMultiLine){this._value(this.term)
}this.menu.blur();
return
}this.menu[aw](av)
},widget:function(){return this.menu.element
},_value:function(){return this.valueMethod.apply(this.element,arguments)
},_keyEvent:function(aw,av){if(!this.isMultiLine||this.menu.element.is(":visible")){this._move(aw,av);
av.preventDefault()
}},_isContentEditable:function(aw){if(!aw.length){return false
}var av=aw.prop("contentEditable");
if(av==="inherit"){return this._isContentEditable(aw.parent())
}return av==="true"
}});
ak.extend(ak.ui.autocomplete,{escapeRegex:function(av){return av.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g,"\\$&")
},filter:function(ax,av){var aw=new RegExp(ak.ui.autocomplete.escapeRegex(av),"i");
return ak.grep(ax,function(ay){return aw.test(ay.label||ay.value||ay)
})
}});
ak.widget("ui.autocomplete",ak.ui.autocomplete,{options:{messages:{noResults:"No search results.",results:function(av){return av+(av>1?" results are":" result is")+" available, use up and down arrow keys to navigate."
}}},__response:function(aw){var av;
this._superApply(arguments);
if(this.options.disabled||this.cancelSearch){return
}if(aw&&aw.length){av=this.options.messages.results(aw.length)
}else{av=this.options.messages.noResults
}this.liveRegion.children().hide();
ak("<div>").text(av).appendTo(this.liveRegion)
}});
var an=ak.ui.autocomplete;
/*!
 * jQuery UI Controlgroup 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var g=/ui-corner-([a-z]){2,6}/g;
var v=ak.widget("ui.controlgroup",{version:"1.12.1",defaultElement:"<div>",options:{direction:"horizontal",disabled:null,onlyVisible:true,items:{button:"input[type=button], input[type=submit], input[type=reset], button, a",controlgroupLabel:".ui-controlgroup-label",checkboxradio:"input[type='checkbox'], input[type='radio']",selectmenu:"select",spinner:".ui-spinner-input"}},_create:function(){this._enhance()
},_enhance:function(){this.element.attr("role","toolbar");
this.refresh()
},_destroy:function(){this._callChildMethod("destroy");
this.childWidgets.removeData("ui-controlgroup-data");
this.element.removeAttr("role");
if(this.options.items.controlgroupLabel){this.element.find(this.options.items.controlgroupLabel).find(".ui-controlgroup-label-contents").contents().unwrap()
}},_initWidgets:function(){var aw=this,av=[];
ak.each(this.options.items,function(az,ax){var aA;
var ay={};
if(!ax){return
}if(az==="controlgroupLabel"){aA=aw.element.find(ax);
aA.each(function(){var aB=ak(this);
if(aB.children(".ui-controlgroup-label-contents").length){return
}aB.contents().wrapAll("<span class='ui-controlgroup-label-contents'></span>")
});
aw._addClass(aA,null,"ui-widget ui-widget-content ui-state-default");
av=av.concat(aA.get());
return
}if(!ak.fn[az]){return
}if(aw["_"+az+"Options"]){ay=aw["_"+az+"Options"]("middle")
}else{ay={classes:{}}
}aw.element.find(ax).each(function(){var aC=ak(this);
var aB=aC[az]("instance");
var aD=ak.widget.extend({},ay);
if(az==="button"&&aC.parent(".ui-spinner").length){return
}if(!aB){aB=aC[az]()[az]("instance")
}if(aB){aD.classes=aw._resolveClassesValues(aD.classes,aB)
}aC[az](aD);
var aE=aC[az]("widget");
ak.data(aE[0],"ui-controlgroup-data",aB?aB:aC[az]("instance"));
av.push(aE[0])
})
});
this.childWidgets=ak(ak.unique(av));
this._addClass(this.childWidgets,"ui-controlgroup-item")
},_callChildMethod:function(av){this.childWidgets.each(function(){var aw=ak(this),ax=aw.data("ui-controlgroup-data");
if(ax&&ax[av]){ax[av]()
}})
},_updateCornerClass:function(ax,aw){var av="ui-corner-top ui-corner-bottom ui-corner-left ui-corner-right ui-corner-all";
var ay=this._buildSimpleOptions(aw,"label").classes.label;
this._removeClass(ax,null,av);
this._addClass(ax,null,ay)
},_buildSimpleOptions:function(aw,ax){var ay=this.options.direction==="vertical";
var av={classes:{}};
av.classes[ax]={middle:"",first:"ui-corner-"+(ay?"top":"left"),last:"ui-corner-"+(ay?"bottom":"right"),only:"ui-corner-all"}[aw];
return av
},_spinnerOptions:function(av){var aw=this._buildSimpleOptions(av,"ui-spinner");
aw.classes["ui-spinner-up"]="";
aw.classes["ui-spinner-down"]="";
return aw
},_buttonOptions:function(av){return this._buildSimpleOptions(av,"ui-button")
},_checkboxradioOptions:function(av){return this._buildSimpleOptions(av,"ui-checkboxradio-label")
},_selectmenuOptions:function(av){var aw=this.options.direction==="vertical";
return{width:aw?"auto":false,classes:{middle:{"ui-selectmenu-button-open":"","ui-selectmenu-button-closed":""},first:{"ui-selectmenu-button-open":"ui-corner-"+(aw?"top":"tl"),"ui-selectmenu-button-closed":"ui-corner-"+(aw?"top":"left")},last:{"ui-selectmenu-button-open":aw?"":"ui-corner-tr","ui-selectmenu-button-closed":"ui-corner-"+(aw?"bottom":"right")},only:{"ui-selectmenu-button-open":"ui-corner-top","ui-selectmenu-button-closed":"ui-corner-all"}}[av]}
},_resolveClassesValues:function(ax,aw){var av={};
ak.each(ax,function(ay){var az=aw.options.classes[ay]||"";
az=ak.trim(az.replace(g,""));
av[ay]=(az+" "+ax[ay]).replace(/\s+/g," ")
});
return av
},_setOption:function(av,aw){if(av==="direction"){this._removeClass("ui-controlgroup-"+this.options.direction)
}this._super(av,aw);
if(av==="disabled"){this._callChildMethod(aw?"disable":"enable");
return
}this.refresh()
},refresh:function(){var av,aw=this;
this._addClass("ui-controlgroup ui-controlgroup-"+this.options.direction);
if(this.options.direction==="horizontal"){this._addClass(null,"ui-helper-clearfix")
}this._initWidgets();
av=this.childWidgets;
if(this.options.onlyVisible){av=av.filter(":visible")
}if(av.length){ak.each(["first","last"],function(az,aA){var ax=av[aA]().data("ui-controlgroup-data");
if(ax&&aw["_"+ax.widgetName+"Options"]){var ay=aw["_"+ax.widgetName+"Options"](av.length===1?"only":aA);
ay.classes=aw._resolveClassesValues(ay.classes,ax);
ax.element[ax.widgetName](ay)
}else{aw._updateCornerClass(av[aA](),aA)
}});
this._callChildMethod("refresh")
}}});
/*!
 * jQuery UI Checkboxradio 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.checkboxradio",[ak.ui.formResetMixin,{version:"1.12.1",options:{disabled:null,label:null,icon:true,classes:{"ui-checkboxradio-label":"ui-corner-all","ui-checkboxradio-icon":"ui-corner-all"}},_getCreateOptions:function(){var aw,ay;
var ax=this;
var av=this._super()||{};
this._readType();
ay=this.element.labels();
this.label=ak(ay[ay.length-1]);
if(!this.label.length){ak.error("No label found for checkboxradio widget")
}this.originalLabel="";
this.label.contents().not(this.element[0]).each(function(){ax.originalLabel+=this.nodeType===3?ak(this).text():this.outerHTML
});
if(this.originalLabel){av.label=this.originalLabel
}aw=this.element[0].disabled;
if(aw!=null){av.disabled=aw
}return av
},_create:function(){var av=this.element[0].checked;
this._bindFormResetHandler();
if(this.options.disabled==null){this.options.disabled=this.element[0].disabled
}this._setOption("disabled",this.options.disabled);
this._addClass("ui-checkboxradio","ui-helper-hidden-accessible");
this._addClass(this.label,"ui-checkboxradio-label","ui-button ui-widget");
if(this.type==="radio"){this._addClass(this.label,"ui-checkboxradio-radio-label")
}if(this.options.label&&this.options.label!==this.originalLabel){this._updateLabel()
}else{if(this.originalLabel){this.options.label=this.originalLabel
}}this._enhance();
if(av){this._addClass(this.label,"ui-checkboxradio-checked","ui-state-active");
if(this.icon){this._addClass(this.icon,null,"ui-state-hover")
}}this._on({change:"_toggleClasses",focus:function(){this._addClass(this.label,null,"ui-state-focus ui-visual-focus")
},blur:function(){this._removeClass(this.label,null,"ui-state-focus ui-visual-focus")
}})
},_readType:function(){var av=this.element[0].nodeName.toLowerCase();
this.type=this.element[0].type;
if(av!=="input"||!/radio|checkbox/.test(this.type)){ak.error("Can't create checkboxradio on element.nodeName="+av+" and element.type="+this.type)
}},_enhance:function(){this._updateIcon(this.element[0].checked)
},widget:function(){return this.label
},_getRadioGroup:function(){var ax;
var av=this.element[0].name;
var aw="input[name='"+ak.ui.escapeSelector(av)+"']";
if(!av){return ak([])
}if(this.form.length){ax=ak(this.form[0].elements).filter(aw)
}else{ax=ak(aw).filter(function(){return ak(this).form().length===0
})
}return ax.not(this.element)
},_toggleClasses:function(){var av=this.element[0].checked;
this._toggleClass(this.label,"ui-checkboxradio-checked","ui-state-active",av);
if(this.options.icon&&this.type==="checkbox"){this._toggleClass(this.icon,null,"ui-icon-check ui-state-checked",av)._toggleClass(this.icon,null,"ui-icon-blank",!av)
}if(this.type==="radio"){this._getRadioGroup().each(function(){var aw=ak(this).checkboxradio("instance");
if(aw){aw._removeClass(aw.label,"ui-checkboxradio-checked","ui-state-active")
}})
}},_destroy:function(){this._unbindFormResetHandler();
if(this.icon){this.icon.remove();
this.iconSpace.remove()
}},_setOption:function(av,aw){if(av==="label"&&!aw){return
}this._super(av,aw);
if(av==="disabled"){this._toggleClass(this.label,null,"ui-state-disabled",aw);
this.element[0].disabled=aw;
return
}this.refresh()
},_updateIcon:function(aw){var av="ui-icon ui-icon-background ";
if(this.options.icon){if(!this.icon){this.icon=ak("<span>");
this.iconSpace=ak("<span> </span>");
this._addClass(this.iconSpace,"ui-checkboxradio-icon-space")
}if(this.type==="checkbox"){av+=aw?"ui-icon-check ui-state-checked":"ui-icon-blank";
this._removeClass(this.icon,null,aw?"ui-icon-blank":"ui-icon-check")
}else{av+="ui-icon-blank"
}this._addClass(this.icon,"ui-checkboxradio-icon",av);
if(!aw){this._removeClass(this.icon,null,"ui-icon-check ui-state-checked")
}this.icon.prependTo(this.label).after(this.iconSpace)
}else{if(this.icon!==undefined){this.icon.remove();
this.iconSpace.remove();
delete this.icon
}}},_updateLabel:function(){var av=this.label.contents().not(this.element[0]);
if(this.icon){av=av.not(this.icon[0])
}if(this.iconSpace){av=av.not(this.iconSpace[0])
}av.remove();
this.label.append(this.options.label)
},refresh:function(){var aw=this.element[0].checked,av=this.element[0].disabled;
this._updateIcon(aw);
this._toggleClass(this.label,"ui-checkboxradio-checked","ui-state-active",aw);
if(this.options.label!==null){this._updateLabel()
}if(av!==this.options.disabled){this._setOptions({disabled:av})
}}}]);
var ao=ak.ui.checkboxradio;
/*!
 * jQuery UI Button 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.button",{version:"1.12.1",defaultElement:"<button>",options:{classes:{"ui-button":"ui-corner-all"},disabled:null,icon:null,iconPosition:"beginning",label:null,showLabel:true},_getCreateOptions:function(){var aw,av=this._super()||{};
this.isInput=this.element.is("input");
aw=this.element[0].disabled;
if(aw!=null){av.disabled=aw
}this.originalLabel=this.isInput?this.element.val():this.element.html();
if(this.originalLabel){av.label=this.originalLabel
}return av
},_create:function(){if(!this.option.showLabel&!this.options.icon){this.options.showLabel=true
}if(this.options.disabled==null){this.options.disabled=this.element[0].disabled||false
}this.hasTitle=!!this.element.attr("title");
if(this.options.label&&this.options.label!==this.originalLabel){if(this.isInput){this.element.val(this.options.label)
}else{this.element.html(this.options.label)
}}this._addClass("ui-button","ui-widget");
this._setOption("disabled",this.options.disabled);
this._enhance();
if(this.element.is("a")){this._on({keyup:function(av){if(av.keyCode===ak.ui.keyCode.SPACE){av.preventDefault();
if(this.element[0].click){this.element[0].click()
}else{this.element.trigger("click")
}}}})
}},_enhance:function(){if(!this.element.is("button")){this.element.attr("role","button")
}if(this.options.icon){this._updateIcon("icon",this.options.icon);
this._updateTooltip()
}},_updateTooltip:function(){this.title=this.element.attr("title");
if(!this.options.showLabel&&!this.title){this.element.attr("title",this.options.label)
}},_updateIcon:function(ax,az){var aw=ax!=="iconPosition",av=aw?this.options.iconPosition:az,ay=av==="top"||av==="bottom";
if(!this.icon){this.icon=ak("<span>");
this._addClass(this.icon,"ui-button-icon","ui-icon");
if(!this.options.showLabel){this._addClass("ui-button-icon-only")
}}else{if(aw){this._removeClass(this.icon,null,this.options.icon)
}}if(aw){this._addClass(this.icon,null,az)
}this._attachIcon(av);
if(ay){this._addClass(this.icon,null,"ui-widget-icon-block");
if(this.iconSpace){this.iconSpace.remove()
}}else{if(!this.iconSpace){this.iconSpace=ak("<span> </span>");
this._addClass(this.iconSpace,"ui-button-icon-space")
}this._removeClass(this.icon,null,"ui-wiget-icon-block");
this._attachIconSpace(av)
}},_destroy:function(){this.element.removeAttr("role");
if(this.icon){this.icon.remove()
}if(this.iconSpace){this.iconSpace.remove()
}if(!this.hasTitle){this.element.removeAttr("title")
}},_attachIconSpace:function(av){this.icon[/^(?:end|bottom)/.test(av)?"before":"after"](this.iconSpace)
},_attachIcon:function(av){this.element[/^(?:end|bottom)/.test(av)?"append":"prepend"](this.icon)
},_setOptions:function(aw){var ax=aw.showLabel===undefined?this.options.showLabel:aw.showLabel,av=aw.icon===undefined?this.options.icon:aw.icon;
if(!ax&&!av){aw.showLabel=true
}this._super(aw)
},_setOption:function(av,aw){if(av==="icon"){if(aw){this._updateIcon(av,aw)
}else{if(this.icon){this.icon.remove();
if(this.iconSpace){this.iconSpace.remove()
}}}}if(av==="iconPosition"){this._updateIcon(av,aw)
}if(av==="showLabel"){this._toggleClass("ui-button-icon-only",null,!aw);
this._updateTooltip()
}if(av==="label"){if(this.isInput){this.element.val(aw)
}else{this.element.html(aw);
if(this.icon){this._attachIcon(this.options.iconPosition);
this._attachIconSpace(this.options.iconPosition)
}}}this._super(av,aw);
if(av==="disabled"){this._toggleClass(null,"ui-state-disabled",aw);
this.element[0].disabled=aw;
if(aw){this.element.blur()
}}},refresh:function(){var av=this.element.is("input, button")?this.element[0].disabled:this.element.hasClass("ui-button-disabled");
if(av!==this.options.disabled){this._setOptions({disabled:av})
}this._updateTooltip()
}});
if(ak.uiBackCompat!==false){ak.widget("ui.button",ak.ui.button,{options:{text:true,icons:{primary:null,secondary:null}},_create:function(){if(this.options.showLabel&&!this.options.text){this.options.showLabel=this.options.text
}if(!this.options.showLabel&&this.options.text){this.options.text=this.options.showLabel
}if(!this.options.icon&&(this.options.icons.primary||this.options.icons.secondary)){if(this.options.icons.primary){this.options.icon=this.options.icons.primary
}else{this.options.icon=this.options.icons.secondary;
this.options.iconPosition="end"
}}else{if(this.options.icon){this.options.icons.primary=this.options.icon
}}this._super()
},_setOption:function(av,aw){if(av==="text"){this._super("showLabel",aw);
return
}if(av==="showLabel"){this.options.text=aw
}if(av==="icon"){this.options.icons.primary=aw
}if(av==="icons"){if(aw.primary){this._super("icon",aw.primary);
this._super("iconPosition","beginning")
}else{if(aw.secondary){this._super("icon",aw.secondary);
this._super("iconPosition","end")
}}}this._superApply(arguments)
}});
ak.fn.button=(function(av){return function(){if(!this.length||(this.length&&this[0].tagName!=="INPUT")||(this.length&&this[0].tagName==="INPUT"&&(this.attr("type")!=="checkbox"&&this.attr("type")!=="radio"))){return av.apply(this,arguments)
}if(!ak.ui.checkboxradio){ak.error("Checkboxradio widget missing")
}if(arguments.length===0){return this.checkboxradio({icon:false})
}return this.checkboxradio.apply(this,arguments)
}
})(ak.fn.button);
ak.fn.buttonset=function(){if(!ak.ui.controlgroup){ak.error("Controlgroup widget missing")
}if(arguments[0]==="option"&&arguments[1]==="items"&&arguments[2]){return this.controlgroup.apply(this,[arguments[0],"items.button",arguments[2]])
}if(arguments[0]==="option"&&arguments[1]==="items"){return this.controlgroup.apply(this,[arguments[0],"items.button"])
}if(typeof arguments[0]==="object"&&arguments[0].items){arguments[0].items={button:arguments[0].items}
}return this.controlgroup.apply(this,arguments)
}
}var C=ak.ui.button;
/*!
 * jQuery UI Datepicker 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.extend(ak.ui,{datepicker:{version:"1.12.1"}});
var aq;
function af(aw){var av,ax;
while(aw.length&&aw[0]!==document){av=aw.css("position");
if(av==="absolute"||av==="relative"||av==="fixed"){ax=parseInt(aw.css("zIndex"),10);
if(!isNaN(ax)&&ax!==0){return ax
}}aw=aw.parent()
}return 0
}function P(){this._curInst=null;
this._keyEvent=false;
this._disabledInputs=[];
this._datepickerShowing=false;
this._inDialog=false;
this._mainDivId="ui-datepicker-div";
this._inlineClass="ui-datepicker-inline";
this._appendClass="ui-datepicker-append";
this._triggerClass="ui-datepicker-trigger";
this._dialogClass="ui-datepicker-dialog";
this._disableClass="ui-datepicker-disabled";
this._unselectableClass="ui-datepicker-unselectable";
this._currentClass="ui-datepicker-current-day";
this._dayOverClass="ui-datepicker-days-cell-over";
this.regional=[];
this.regional[""]={closeText:"Done",prevText:"Prev",nextText:"Next",currentText:"Today",monthNames:["January","February","March","April","May","June","July","August","September","October","November","December"],monthNamesShort:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],dayNames:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],dayNamesShort:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],dayNamesMin:["Su","Mo","Tu","We","Th","Fr","Sa"],weekHeader:"Wk",dateFormat:"mm/dd/yy",firstDay:0,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
this._defaults={showOn:"focus",showAnim:"fadeIn",showOptions:{},defaultDate:null,appendText:"",buttonText:"...",buttonImage:"",buttonImageOnly:false,hideIfNoPrevNext:false,navigationAsDateFormat:false,gotoCurrent:false,changeMonth:false,changeYear:false,yearRange:"c-10:c+10",showOtherMonths:false,selectOtherMonths:false,showWeek:false,calculateWeek:this.iso8601Week,shortYearCutoff:"+10",minDate:null,maxDate:null,duration:"fast",beforeShowDay:null,beforeShow:null,onSelect:null,onChangeMonthYear:null,onClose:null,numberOfMonths:1,showCurrentAtPos:0,stepMonths:1,stepBigMonths:12,altField:"",altFormat:"",constrainInput:true,showButtonPanel:false,autoSize:false,disabled:false};
ak.extend(this._defaults,this.regional[""]);
this.regional.en=ak.extend(true,{},this.regional[""]);
this.regional["en-US"]=ak.extend(true,{},this.regional.en);
this.dpDiv=X(ak("<div id='"+this._mainDivId+"' class='ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all'></div>"))
}ak.extend(P.prototype,{markerClassName:"hasDatepicker",maxRows:4,_widgetDatepicker:function(){return this.dpDiv
},setDefaults:function(av){F(this._defaults,av||{});
return this
},_attachDatepicker:function(ay,av){var az,ax,aw;
az=ay.nodeName.toLowerCase();
ax=(az==="div"||az==="span");
if(!ay.id){this.uuid+=1;
ay.id="dp"+this.uuid
}aw=this._newInst(ak(ay),ax);
aw.settings=ak.extend({},av||{});
if(az==="input"){this._connectDatepicker(ay,aw)
}else{if(ax){this._inlineDatepicker(ay,aw)
}}},_newInst:function(aw,av){var ax=aw[0].id.replace(/([^A-Za-z0-9_\-])/g,"\\\\$1");
return{id:ax,input:aw,selectedDay:0,selectedMonth:0,selectedYear:0,drawMonth:0,drawYear:0,inline:av,dpDiv:(!av?this.dpDiv:X(ak("<div class='"+this._inlineClass+" ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all'></div>")))}
},_connectDatepicker:function(ax,aw){var av=ak(ax);
aw.append=ak([]);
aw.trigger=ak([]);
if(av.hasClass(this.markerClassName)){return
}this._attachments(av,aw);
av.addClass(this.markerClassName).on("keydown",this._doKeyDown).on("keypress",this._doKeyPress).on("keyup",this._doKeyUp);
this._autoSize(aw);
ak.data(ax,"datepicker",aw);
if(aw.settings.disabled){this._disableDatepicker(ax)
}},_attachments:function(ax,aA){var aw,az,av,aB=this._get(aA,"appendText"),ay=this._get(aA,"isRTL");
if(aA.append){aA.append.remove()
}if(aB){aA.append=ak("<span class='"+this._appendClass+"'>"+aB+"</span>");
ax[ay?"before":"after"](aA.append)
}ax.off("focus",this._showDatepicker);
if(aA.trigger){aA.trigger.remove()
}aw=this._get(aA,"showOn");
if(aw==="focus"||aw==="both"){ax.on("focus",this._showDatepicker)
}if(aw==="button"||aw==="both"){az=this._get(aA,"buttonText");
av=this._get(aA,"buttonImage");
aA.trigger=ak(this._get(aA,"buttonImageOnly")?ak("<img/>").addClass(this._triggerClass).attr({src:av,alt:az,title:az}):ak("<button type='button'></button>").addClass(this._triggerClass).html(!av?az:ak("<img/>").attr({src:av,alt:az,title:az})));
ax[ay?"before":"after"](aA.trigger);
aA.trigger.on("click",function(){if(ak.datepicker._datepickerShowing&&ak.datepicker._lastInput===ax[0]){ak.datepicker._hideDatepicker()
}else{if(ak.datepicker._datepickerShowing&&ak.datepicker._lastInput!==ax[0]){ak.datepicker._hideDatepicker();
ak.datepicker._showDatepicker(ax[0])
}else{ak.datepicker._showDatepicker(ax[0])
}}return false
})
}},_autoSize:function(aB){if(this._get(aB,"autoSize")&&!aB.inline){var ay,aw,ax,aA,az=new Date(2009,12-1,20),av=this._get(aB,"dateFormat");
if(av.match(/[DM]/)){ay=function(aC){aw=0;
ax=0;
for(aA=0;
aA<aC.length;
aA++){if(aC[aA].length>aw){aw=aC[aA].length;
ax=aA
}}return ax
};
az.setMonth(ay(this._get(aB,(av.match(/MM/)?"monthNames":"monthNamesShort"))));
az.setDate(ay(this._get(aB,(av.match(/DD/)?"dayNames":"dayNamesShort")))+20-az.getDay())
}aB.input.attr("size",this._formatDate(aB,az).length)
}},_inlineDatepicker:function(aw,av){var ax=ak(aw);
if(ax.hasClass(this.markerClassName)){return
}ax.addClass(this.markerClassName).append(av.dpDiv);
ak.data(aw,"datepicker",av);
this._setDate(av,this._getDefaultDate(av),true);
this._updateDatepicker(av);
this._updateAlternate(av);
if(av.settings.disabled){this._disableDatepicker(aw)
}av.dpDiv.css("display","block")
},_dialogDatepicker:function(aC,aw,aA,ax,aB){var av,aF,az,aE,aD,ay=this._dialogInst;
if(!ay){this.uuid+=1;
av="dp"+this.uuid;
this._dialogInput=ak("<input type='text' id='"+av+"' style='position: absolute; top: -100px; width: 0px;'/>");
this._dialogInput.on("keydown",this._doKeyDown);
ak("body").append(this._dialogInput);
ay=this._dialogInst=this._newInst(this._dialogInput,false);
ay.settings={};
ak.data(this._dialogInput[0],"datepicker",ay)
}F(ay.settings,ax||{});
aw=(aw&&aw.constructor===Date?this._formatDate(ay,aw):aw);
this._dialogInput.val(aw);
this._pos=(aB?(aB.length?aB:[aB.pageX,aB.pageY]):null);
if(!this._pos){aF=document.documentElement.clientWidth;
az=document.documentElement.clientHeight;
aE=document.documentElement.scrollLeft||document.body.scrollLeft;
aD=document.documentElement.scrollTop||document.body.scrollTop;
this._pos=[(aF/2)-100+aE,(az/2)-150+aD]
}this._dialogInput.css("left",(this._pos[0]+20)+"px").css("top",this._pos[1]+"px");
ay.settings.onSelect=aA;
this._inDialog=true;
this.dpDiv.addClass(this._dialogClass);
this._showDatepicker(this._dialogInput[0]);
if(ak.blockUI){ak.blockUI(this.dpDiv)
}ak.data(this._dialogInput[0],"datepicker",ay);
return this
},_destroyDatepicker:function(ax){var ay,av=ak(ax),aw=ak.data(ax,"datepicker");
if(!av.hasClass(this.markerClassName)){return
}ay=ax.nodeName.toLowerCase();
ak.removeData(ax,"datepicker");
if(ay==="input"){aw.append.remove();
aw.trigger.remove();
av.removeClass(this.markerClassName).off("focus",this._showDatepicker).off("keydown",this._doKeyDown).off("keypress",this._doKeyPress).off("keyup",this._doKeyUp)
}else{if(ay==="div"||ay==="span"){av.removeClass(this.markerClassName).empty()
}}if(aq===aw){aq=null
}},_enableDatepicker:function(ay){var az,ax,av=ak(ay),aw=ak.data(ay,"datepicker");
if(!av.hasClass(this.markerClassName)){return
}az=ay.nodeName.toLowerCase();
if(az==="input"){ay.disabled=false;
aw.trigger.filter("button").each(function(){this.disabled=false
}).end().filter("img").css({opacity:"1.0",cursor:""})
}else{if(az==="div"||az==="span"){ax=av.children("."+this._inlineClass);
ax.children().removeClass("ui-state-disabled");
ax.find("select.ui-datepicker-month, select.ui-datepicker-year").prop("disabled",false)
}}this._disabledInputs=ak.map(this._disabledInputs,function(aA){return(aA===ay?null:aA)
})
},_disableDatepicker:function(ay){var az,ax,av=ak(ay),aw=ak.data(ay,"datepicker");
if(!av.hasClass(this.markerClassName)){return
}az=ay.nodeName.toLowerCase();
if(az==="input"){ay.disabled=true;
aw.trigger.filter("button").each(function(){this.disabled=true
}).end().filter("img").css({opacity:"0.5",cursor:"default"})
}else{if(az==="div"||az==="span"){ax=av.children("."+this._inlineClass);
ax.children().addClass("ui-state-disabled");
ax.find("select.ui-datepicker-month, select.ui-datepicker-year").prop("disabled",true)
}}this._disabledInputs=ak.map(this._disabledInputs,function(aA){return(aA===ay?null:aA)
});
this._disabledInputs[this._disabledInputs.length]=ay
},_isDisabledDatepicker:function(aw){if(!aw){return false
}for(var av=0;
av<this._disabledInputs.length;
av++){if(this._disabledInputs[av]===aw){return true
}}return false
},_getInst:function(aw){try{return ak.data(aw,"datepicker")
}catch(av){throw"Missing instance data for this datepicker"
}},_optionDatepicker:function(aB,aw,aA){var ax,av,az,aC,ay=this._getInst(aB);
if(arguments.length===2&&typeof aw==="string"){return(aw==="defaults"?ak.extend({},ak.datepicker._defaults):(ay?(aw==="all"?ak.extend({},ay.settings):this._get(ay,aw)):null))
}ax=aw||{};
if(typeof aw==="string"){ax={};
ax[aw]=aA
}if(ay){if(this._curInst===ay){this._hideDatepicker()
}av=this._getDateDatepicker(aB,true);
az=this._getMinMaxDate(ay,"min");
aC=this._getMinMaxDate(ay,"max");
F(ay.settings,ax);
if(az!==null&&ax.dateFormat!==undefined&&ax.minDate===undefined){ay.settings.minDate=this._formatDate(ay,az)
}if(aC!==null&&ax.dateFormat!==undefined&&ax.maxDate===undefined){ay.settings.maxDate=this._formatDate(ay,aC)
}if("disabled" in ax){if(ax.disabled){this._disableDatepicker(aB)
}else{this._enableDatepicker(aB)
}}this._attachments(ak(aB),ay);
this._autoSize(ay);
this._setDate(ay,av);
this._updateAlternate(ay);
this._updateDatepicker(ay)
}},_changeDatepicker:function(ax,av,aw){this._optionDatepicker(ax,av,aw)
},_refreshDatepicker:function(aw){var av=this._getInst(aw);
if(av){this._updateDatepicker(av)
}},_setDateDatepicker:function(ax,av){var aw=this._getInst(ax);
if(aw){this._setDate(aw,av);
this._updateDatepicker(aw);
this._updateAlternate(aw)
}},_getDateDatepicker:function(ax,av){var aw=this._getInst(ax);
if(aw&&!aw.inline){this._setDateFromField(aw,av)
}return(aw?this._getDate(aw):null)
},_doKeyDown:function(ay){var aw,av,aA,az=ak.datepicker._getInst(ay.target),aB=true,ax=az.dpDiv.is(".ui-datepicker-rtl");
az._keyEvent=true;
if(ak.datepicker._datepickerShowing){switch(ay.keyCode){case 9:ak.datepicker._hideDatepicker();
aB=false;
break;
case 13:aA=ak("td."+ak.datepicker._dayOverClass+":not(."+ak.datepicker._currentClass+")",az.dpDiv);
if(aA[0]){ak.datepicker._selectDay(ay.target,az.selectedMonth,az.selectedYear,aA[0])
}aw=ak.datepicker._get(az,"onSelect");
if(aw){av=ak.datepicker._formatDate(az);
aw.apply((az.input?az.input[0]:null),[av,az])
}else{ak.datepicker._hideDatepicker()
}return false;
case 27:ak.datepicker._hideDatepicker();
break;
case 33:ak.datepicker._adjustDate(ay.target,(ay.ctrlKey?-ak.datepicker._get(az,"stepBigMonths"):-ak.datepicker._get(az,"stepMonths")),"M");
break;
case 34:ak.datepicker._adjustDate(ay.target,(ay.ctrlKey?+ak.datepicker._get(az,"stepBigMonths"):+ak.datepicker._get(az,"stepMonths")),"M");
break;
case 35:if(ay.ctrlKey||ay.metaKey){ak.datepicker._clearDate(ay.target)
}aB=ay.ctrlKey||ay.metaKey;
break;
case 36:if(ay.ctrlKey||ay.metaKey){ak.datepicker._gotoToday(ay.target)
}aB=ay.ctrlKey||ay.metaKey;
break;
case 37:if(ay.ctrlKey||ay.metaKey){ak.datepicker._adjustDate(ay.target,(ax?+1:-1),"D")
}aB=ay.ctrlKey||ay.metaKey;
if(ay.originalEvent.altKey){ak.datepicker._adjustDate(ay.target,(ay.ctrlKey?-ak.datepicker._get(az,"stepBigMonths"):-ak.datepicker._get(az,"stepMonths")),"M")
}break;
case 38:if(ay.ctrlKey||ay.metaKey){ak.datepicker._adjustDate(ay.target,-7,"D")
}aB=ay.ctrlKey||ay.metaKey;
break;
case 39:if(ay.ctrlKey||ay.metaKey){ak.datepicker._adjustDate(ay.target,(ax?-1:+1),"D")
}aB=ay.ctrlKey||ay.metaKey;
if(ay.originalEvent.altKey){ak.datepicker._adjustDate(ay.target,(ay.ctrlKey?+ak.datepicker._get(az,"stepBigMonths"):+ak.datepicker._get(az,"stepMonths")),"M")
}break;
case 40:if(ay.ctrlKey||ay.metaKey){ak.datepicker._adjustDate(ay.target,+7,"D")
}aB=ay.ctrlKey||ay.metaKey;
break;
default:aB=false
}}else{if(ay.keyCode===36&&ay.ctrlKey){ak.datepicker._showDatepicker(this)
}else{aB=false
}}if(aB){ay.preventDefault();
ay.stopPropagation()
}},_doKeyPress:function(ax){var aw,av,ay=ak.datepicker._getInst(ax.target);
if(ak.datepicker._get(ay,"constrainInput")){aw=ak.datepicker._possibleChars(ak.datepicker._get(ay,"dateFormat"));
av=String.fromCharCode(ax.charCode==null?ax.keyCode:ax.charCode);
return ax.ctrlKey||ax.metaKey||(av<" "||!aw||aw.indexOf(av)>-1)
}},_doKeyUp:function(ax){var av,ay=ak.datepicker._getInst(ax.target);
if(ay.input.val()!==ay.lastVal){try{av=ak.datepicker.parseDate(ak.datepicker._get(ay,"dateFormat"),(ay.input?ay.input.val():null),ak.datepicker._getFormatConfig(ay));
if(av){ak.datepicker._setDateFromField(ay);
ak.datepicker._updateAlternate(ay);
ak.datepicker._updateDatepicker(ay)
}}catch(aw){}}return true
},_showDatepicker:function(aw){aw=aw.target||aw;
if(aw.nodeName.toLowerCase()!=="input"){aw=ak("input",aw.parentNode)[0]
}if(ak.datepicker._isDisabledDatepicker(aw)||ak.datepicker._lastInput===aw){return
}var ay,aC,ax,aA,aB,av,az;
ay=ak.datepicker._getInst(aw);
if(ak.datepicker._curInst&&ak.datepicker._curInst!==ay){ak.datepicker._curInst.dpDiv.stop(true,true);
if(ay&&ak.datepicker._datepickerShowing){ak.datepicker._hideDatepicker(ak.datepicker._curInst.input[0])
}}aC=ak.datepicker._get(ay,"beforeShow");
ax=aC?aC.apply(aw,[aw,ay]):{};
if(ax===false){return
}F(ay.settings,ax);
ay.lastVal=null;
ak.datepicker._lastInput=aw;
ak.datepicker._setDateFromField(ay);
if(ak.datepicker._inDialog){aw.value=""
}if(!ak.datepicker._pos){ak.datepicker._pos=ak.datepicker._findPos(aw);
ak.datepicker._pos[1]+=aw.offsetHeight
}aA=false;
ak(aw).parents().each(function(){aA|=ak(this).css("position")==="fixed";
return !aA
});
aB={left:ak.datepicker._pos[0],top:ak.datepicker._pos[1]};
ak.datepicker._pos=null;
ay.dpDiv.empty();
ay.dpDiv.css({position:"absolute",display:"block",top:"-1000px"});
ak.datepicker._updateDatepicker(ay);
aB=ak.datepicker._checkOffset(ay,aB,aA);
ay.dpDiv.css({position:(ak.datepicker._inDialog&&ak.blockUI?"static":(aA?"fixed":"absolute")),display:"none",left:aB.left+"px",top:aB.top+"px"});
if(!ay.inline){av=ak.datepicker._get(ay,"showAnim");
az=ak.datepicker._get(ay,"duration");
ay.dpDiv.css("z-index",af(ak(aw))+1);
ak.datepicker._datepickerShowing=true;
if(ak.effects&&ak.effects.effect[av]){ay.dpDiv.show(av,ak.datepicker._get(ay,"showOptions"),az)
}else{ay.dpDiv[av||"show"](av?az:null)
}if(ak.datepicker._shouldFocusInput(ay)){ay.input.trigger("focus")
}ak.datepicker._curInst=ay
}},_updateDatepicker:function(ay){this.maxRows=4;
aq=ay;
ay.dpDiv.empty().append(this._generateHTML(ay));
this._attachHandlers(ay);
var aA,av=this._getNumberOfMonths(ay),az=av[1],ax=17,aw=ay.dpDiv.find("."+this._dayOverClass+" a");
if(aw.length>0){K.apply(aw.get(0))
}ay.dpDiv.removeClass("ui-datepicker-multi-2 ui-datepicker-multi-3 ui-datepicker-multi-4").width("");
if(az>1){ay.dpDiv.addClass("ui-datepicker-multi-"+az).css("width",(ax*az)+"em")
}ay.dpDiv[(av[0]!==1||av[1]!==1?"add":"remove")+"Class"]("ui-datepicker-multi");
ay.dpDiv[(this._get(ay,"isRTL")?"add":"remove")+"Class"]("ui-datepicker-rtl");
if(ay===ak.datepicker._curInst&&ak.datepicker._datepickerShowing&&ak.datepicker._shouldFocusInput(ay)){ay.input.trigger("focus")
}if(ay.yearshtml){aA=ay.yearshtml;
setTimeout(function(){if(aA===ay.yearshtml&&ay.yearshtml){ay.dpDiv.find("select.ui-datepicker-year:first").replaceWith(ay.yearshtml)
}aA=ay.yearshtml=null
},0)
}},_shouldFocusInput:function(av){return av.input&&av.input.is(":visible")&&!av.input.is(":disabled")&&!av.input.is(":focus")
},_checkOffset:function(aA,ay,ax){var az=aA.dpDiv.outerWidth(),aD=aA.dpDiv.outerHeight(),aC=aA.input?aA.input.outerWidth():0,av=aA.input?aA.input.outerHeight():0,aB=document.documentElement.clientWidth+(ax?0:ak(document).scrollLeft()),aw=document.documentElement.clientHeight+(ax?0:ak(document).scrollTop());
ay.left-=(this._get(aA,"isRTL")?(az-aC):0);
ay.left-=(ax&&ay.left===aA.input.offset().left)?ak(document).scrollLeft():0;
ay.top-=(ax&&ay.top===(aA.input.offset().top+av))?ak(document).scrollTop():0;
ay.left-=Math.min(ay.left,(ay.left+az>aB&&aB>az)?Math.abs(ay.left+az-aB):0);
ay.top-=Math.min(ay.top,(ay.top+aD>aw&&aw>aD)?Math.abs(aD+av):0);
return ay
},_findPos:function(ay){var av,ax=this._getInst(ay),aw=this._get(ax,"isRTL");
while(ay&&(ay.type==="hidden"||ay.nodeType!==1||ak.expr.filters.hidden(ay))){ay=ay[aw?"previousSibling":"nextSibling"]
}av=ak(ay).offset();
return[av.left,av.top]
},_hideDatepicker:function(ax){var aw,aA,az,av,ay=this._curInst;
if(!ay||(ax&&ay!==ak.data(ax,"datepicker"))){return
}if(this._datepickerShowing){aw=this._get(ay,"showAnim");
aA=this._get(ay,"duration");
az=function(){ak.datepicker._tidyDialog(ay)
};
if(ak.effects&&(ak.effects.effect[aw]||ak.effects[aw])){ay.dpDiv.hide(aw,ak.datepicker._get(ay,"showOptions"),aA,az)
}else{ay.dpDiv[(aw==="slideDown"?"slideUp":(aw==="fadeIn"?"fadeOut":"hide"))]((aw?aA:null),az)
}if(!aw){az()
}this._datepickerShowing=false;
av=this._get(ay,"onClose");
if(av){av.apply((ay.input?ay.input[0]:null),[(ay.input?ay.input.val():""),ay])
}this._lastInput=null;
if(this._inDialog){this._dialogInput.css({position:"absolute",left:"0",top:"-100px"});
if(ak.blockUI){ak.unblockUI();
ak("body").append(this.dpDiv)
}}this._inDialog=false
}},_tidyDialog:function(av){av.dpDiv.removeClass(this._dialogClass).off(".ui-datepicker-calendar")
},_checkExternalClick:function(aw){if(!ak.datepicker._curInst){return
}var av=ak(aw.target),ax=ak.datepicker._getInst(av[0]);
if(((av[0].id!==ak.datepicker._mainDivId&&av.parents("#"+ak.datepicker._mainDivId).length===0&&!av.hasClass(ak.datepicker.markerClassName)&&!av.closest("."+ak.datepicker._triggerClass).length&&ak.datepicker._datepickerShowing&&!(ak.datepicker._inDialog&&ak.blockUI)))||(av.hasClass(ak.datepicker.markerClassName)&&ak.datepicker._curInst!==ax)){ak.datepicker._hideDatepicker()
}},_adjustDate:function(az,ay,ax){var aw=ak(az),av=this._getInst(aw[0]);
if(this._isDisabledDatepicker(aw[0])){return
}this._adjustInstDate(av,ay+(ax==="M"?this._get(av,"showCurrentAtPos"):0),ax);
this._updateDatepicker(av)
},_gotoToday:function(ay){var av,ax=ak(ay),aw=this._getInst(ax[0]);
if(this._get(aw,"gotoCurrent")&&aw.currentDay){aw.selectedDay=aw.currentDay;
aw.drawMonth=aw.selectedMonth=aw.currentMonth;
aw.drawYear=aw.selectedYear=aw.currentYear
}else{av=new Date();
aw.selectedDay=av.getDate();
aw.drawMonth=aw.selectedMonth=av.getMonth();
aw.drawYear=aw.selectedYear=av.getFullYear()
}this._notifyChange(aw);
this._adjustDate(ax)
},_selectMonthYear:function(az,av,ay){var ax=ak(az),aw=this._getInst(ax[0]);
aw["selected"+(ay==="M"?"Month":"Year")]=aw["draw"+(ay==="M"?"Month":"Year")]=parseInt(av.options[av.selectedIndex].value,10);
this._notifyChange(aw);
this._adjustDate(ax)
},_selectDay:function(aA,ay,av,az){var aw,ax=ak(aA);
if(ak(az).hasClass(this._unselectableClass)||this._isDisabledDatepicker(ax[0])){return
}aw=this._getInst(ax[0]);
aw.selectedDay=aw.currentDay=ak("a",az).html();
aw.selectedMonth=aw.currentMonth=ay;
aw.selectedYear=aw.currentYear=av;
this._selectDate(aA,this._formatDate(aw,aw.currentDay,aw.currentMonth,aw.currentYear))
},_clearDate:function(aw){var av=ak(aw);
this._selectDate(av,"")
},_selectDate:function(az,av){var aw,ay=ak(az),ax=this._getInst(ay[0]);
av=(av!=null?av:this._formatDate(ax));
if(ax.input){ax.input.val(av)
}this._updateAlternate(ax);
aw=this._get(ax,"onSelect");
if(aw){aw.apply((ax.input?ax.input[0]:null),[av,ax])
}else{if(ax.input){ax.input.trigger("change")
}}if(ax.inline){this._updateDatepicker(ax)
}else{this._hideDatepicker();
this._lastInput=ax.input[0];
if(typeof(ax.input[0])!=="object"){ax.input.trigger("focus")
}this._lastInput=null
}},_updateAlternate:function(az){var ay,ax,av,aw=this._get(az,"altField");
if(aw){ay=this._get(az,"altFormat")||this._get(az,"dateFormat");
ax=this._getDate(az);
av=this.formatDate(ay,ax,this._getFormatConfig(az));
ak(aw).val(av)
}},noWeekends:function(aw){var av=aw.getDay();
return[(av>0&&av<6),""]
},iso8601Week:function(av){var aw,ax=new Date(av.getTime());
ax.setDate(ax.getDate()+4-(ax.getDay()||7));
aw=ax.getTime();
ax.setMonth(0);
ax.setDate(1);
return Math.floor(Math.round((aw-ax)/86400000)/7)+1
},parseDate:function(aL,aG,aN){if(aL==null||aG==null){throw"Invalid arguments"
}aG=(typeof aG==="object"?aG.toString():aG+"");
if(aG===""){return null
}var ay,aI,aw,aM=0,aB=(aN?aN.shortYearCutoff:null)||this._defaults.shortYearCutoff,ax=(typeof aB!=="string"?aB:new Date().getFullYear()%100+parseInt(aB,10)),aE=(aN?aN.dayNamesShort:null)||this._defaults.dayNamesShort,aP=(aN?aN.dayNames:null)||this._defaults.dayNames,av=(aN?aN.monthNamesShort:null)||this._defaults.monthNamesShort,az=(aN?aN.monthNames:null)||this._defaults.monthNames,aA=-1,aQ=-1,aK=-1,aD=-1,aJ=false,aO,aF=function(aS){var aT=(ay+1<aL.length&&aL.charAt(ay+1)===aS);
if(aT){ay++
}return aT
},aR=function(aU){var aS=aF(aU),aV=(aU==="@"?14:(aU==="!"?20:(aU==="y"&&aS?4:(aU==="o"?3:2)))),aX=(aU==="y"?aV:1),aW=new RegExp("^\\d{"+aX+","+aV+"}"),aT=aG.substring(aM).match(aW);
if(!aT){throw"Missing number at position "+aM
}aM+=aT[0].length;
return parseInt(aT[0],10)
},aC=function(aT,aU,aW){var aS=-1,aV=ak.map(aF(aT)?aW:aU,function(aY,aX){return[[aX,aY]]
}).sort(function(aY,aX){return -(aY[1].length-aX[1].length)
});
ak.each(aV,function(aY,aZ){var aX=aZ[1];
if(aG.substr(aM,aX.length).toLowerCase()===aX.toLowerCase()){aS=aZ[0];
aM+=aX.length;
return false
}});
if(aS!==-1){return aS+1
}else{throw"Unknown name at position "+aM
}},aH=function(){if(aG.charAt(aM)!==aL.charAt(ay)){throw"Unexpected literal at position "+aM
}aM++
};
for(ay=0;
ay<aL.length;
ay++){if(aJ){if(aL.charAt(ay)==="'"&&!aF("'")){aJ=false
}else{aH()
}}else{switch(aL.charAt(ay)){case"d":aK=aR("d");
break;
case"D":aC("D",aE,aP);
break;
case"o":aD=aR("o");
break;
case"m":aQ=aR("m");
break;
case"M":aQ=aC("M",av,az);
break;
case"y":aA=aR("y");
break;
case"@":aO=new Date(aR("@"));
aA=aO.getFullYear();
aQ=aO.getMonth()+1;
aK=aO.getDate();
break;
case"!":aO=new Date((aR("!")-this._ticksTo1970)/10000);
aA=aO.getFullYear();
aQ=aO.getMonth()+1;
aK=aO.getDate();
break;
case"'":if(aF("'")){aH()
}else{aJ=true
}break;
default:aH()
}}}if(aM<aG.length){aw=aG.substr(aM);
if(!/^\s+/.test(aw)){throw"Extra/unparsed characters found in date: "+aw
}}if(aA===-1){aA=new Date().getFullYear()
}else{if(aA<100){aA+=new Date().getFullYear()-new Date().getFullYear()%100+(aA<=ax?0:-100)
}}if(aD>-1){aQ=1;
aK=aD;
do{aI=this._getDaysInMonth(aA,aQ-1);
if(aK<=aI){break
}aQ++;
aK-=aI
}while(true)
}aO=this._daylightSavingAdjust(new Date(aA,aQ-1,aK));
if(aO.getFullYear()!==aA||aO.getMonth()+1!==aQ||aO.getDate()!==aK){throw"Invalid date"
}return aO
},ATOM:"yy-mm-dd",COOKIE:"D, dd M yy",ISO_8601:"yy-mm-dd",RFC_822:"D, d M y",RFC_850:"DD, dd-M-y",RFC_1036:"D, d M y",RFC_1123:"D, d M yy",RFC_2822:"D, d M yy",RSS:"D, d M y",TICKS:"!",TIMESTAMP:"@",W3C:"yy-mm-dd",_ticksTo1970:(((1970-1)*365+Math.floor(1970/4)-Math.floor(1970/100)+Math.floor(1970/400))*24*60*60*10000000),formatDate:function(aE,ay,az){if(!ay){return""
}var aG,aH=(az?az.dayNamesShort:null)||this._defaults.dayNamesShort,aw=(az?az.dayNames:null)||this._defaults.dayNames,aC=(az?az.monthNamesShort:null)||this._defaults.monthNamesShort,aA=(az?az.monthNames:null)||this._defaults.monthNames,aF=function(aI){var aJ=(aG+1<aE.length&&aE.charAt(aG+1)===aI);
if(aJ){aG++
}return aJ
},av=function(aK,aL,aI){var aJ=""+aL;
if(aF(aK)){while(aJ.length<aI){aJ="0"+aJ
}}return aJ
},aB=function(aI,aK,aJ,aL){return(aF(aI)?aL[aK]:aJ[aK])
},ax="",aD=false;
if(ay){for(aG=0;
aG<aE.length;
aG++){if(aD){if(aE.charAt(aG)==="'"&&!aF("'")){aD=false
}else{ax+=aE.charAt(aG)
}}else{switch(aE.charAt(aG)){case"d":ax+=av("d",ay.getDate(),2);
break;
case"D":ax+=aB("D",ay.getDay(),aH,aw);
break;
case"o":ax+=av("o",Math.round((new Date(ay.getFullYear(),ay.getMonth(),ay.getDate()).getTime()-new Date(ay.getFullYear(),0,0).getTime())/86400000),3);
break;
case"m":ax+=av("m",ay.getMonth()+1,2);
break;
case"M":ax+=aB("M",ay.getMonth(),aC,aA);
break;
case"y":ax+=(aF("y")?ay.getFullYear():(ay.getFullYear()%100<10?"0":"")+ay.getFullYear()%100);
break;
case"@":ax+=ay.getTime();
break;
case"!":ax+=ay.getTime()*10000+this._ticksTo1970;
break;
case"'":if(aF("'")){ax+="'"
}else{aD=true
}break;
default:ax+=aE.charAt(aG)
}}}}return ax
},_possibleChars:function(az){var ay,ax="",aw=false,av=function(aA){var aB=(ay+1<az.length&&az.charAt(ay+1)===aA);
if(aB){ay++
}return aB
};
for(ay=0;
ay<az.length;
ay++){if(aw){if(az.charAt(ay)==="'"&&!av("'")){aw=false
}else{ax+=az.charAt(ay)
}}else{switch(az.charAt(ay)){case"d":case"m":case"y":case"@":ax+="0123456789";
break;
case"D":case"M":return null;
case"'":if(av("'")){ax+="'"
}else{aw=true
}break;
default:ax+=az.charAt(ay)
}}}return ax
},_get:function(aw,av){return aw.settings[av]!==undefined?aw.settings[av]:this._defaults[av]
},_setDateFromField:function(aA,ax){if(aA.input.val()===aA.lastVal){return
}var av=this._get(aA,"dateFormat"),aC=aA.lastVal=aA.input?aA.input.val():null,aB=this._getDefaultDate(aA),aw=aB,ay=this._getFormatConfig(aA);
try{aw=this.parseDate(av,aC,ay)||aB
}catch(az){aC=(ax?"":aC)
}aA.selectedDay=aw.getDate();
aA.drawMonth=aA.selectedMonth=aw.getMonth();
aA.drawYear=aA.selectedYear=aw.getFullYear();
aA.currentDay=(aC?aw.getDate():0);
aA.currentMonth=(aC?aw.getMonth():0);
aA.currentYear=(aC?aw.getFullYear():0);
this._adjustInstDate(aA)
},_getDefaultDate:function(av){return this._restrictMinMax(av,this._determineDate(av,this._get(av,"defaultDate"),new Date()))
},_determineDate:function(az,aw,aA){var ay=function(aC){var aB=new Date();
aB.setDate(aB.getDate()+aC);
return aB
},ax=function(aI){try{return ak.datepicker.parseDate(ak.datepicker._get(az,"dateFormat"),aI,ak.datepicker._getFormatConfig(az))
}catch(aH){}var aC=(aI.toLowerCase().match(/^c/)?ak.datepicker._getDate(az):null)||new Date(),aD=aC.getFullYear(),aG=aC.getMonth(),aB=aC.getDate(),aF=/([+\-]?[0-9]+)\s*(d|D|w|W|m|M|y|Y)?/g,aE=aF.exec(aI);
while(aE){switch(aE[2]||"d"){case"d":case"D":aB+=parseInt(aE[1],10);
break;
case"w":case"W":aB+=parseInt(aE[1],10)*7;
break;
case"m":case"M":aG+=parseInt(aE[1],10);
aB=Math.min(aB,ak.datepicker._getDaysInMonth(aD,aG));
break;
case"y":case"Y":aD+=parseInt(aE[1],10);
aB=Math.min(aB,ak.datepicker._getDaysInMonth(aD,aG));
break
}aE=aF.exec(aI)
}return new Date(aD,aG,aB)
},av=(aw==null||aw===""?aA:(typeof aw==="string"?ax(aw):(typeof aw==="number"?(isNaN(aw)?aA:ay(aw)):new Date(aw.getTime()))));
av=(av&&av.toString()==="Invalid Date"?aA:av);
if(av){av.setHours(0);
av.setMinutes(0);
av.setSeconds(0);
av.setMilliseconds(0)
}return this._daylightSavingAdjust(av)
},_daylightSavingAdjust:function(av){if(!av){return null
}av.setHours(av.getHours()>12?av.getHours()+2:0);
return av
},_setDate:function(aB,ay,aA){var av=!ay,ax=aB.selectedMonth,az=aB.selectedYear,aw=this._restrictMinMax(aB,this._determineDate(aB,ay,new Date()));
aB.selectedDay=aB.currentDay=aw.getDate();
aB.drawMonth=aB.selectedMonth=aB.currentMonth=aw.getMonth();
aB.drawYear=aB.selectedYear=aB.currentYear=aw.getFullYear();
if((ax!==aB.selectedMonth||az!==aB.selectedYear)&&!aA){this._notifyChange(aB)
}this._adjustInstDate(aB);
if(aB.input){aB.input.val(av?"":this._formatDate(aB))
}},_getDate:function(aw){var av=(!aw.currentYear||(aw.input&&aw.input.val()==="")?null:this._daylightSavingAdjust(new Date(aw.currentYear,aw.currentMonth,aw.currentDay)));
return av
},_attachHandlers:function(aw){var av=this._get(aw,"stepMonths"),ax="#"+aw.id.replace(/\\\\/g,"\\");
aw.dpDiv.find("[data-handler]").map(function(){var ay={prev:function(){ak.datepicker._adjustDate(ax,-av,"M")
},next:function(){ak.datepicker._adjustDate(ax,+av,"M")
},hide:function(){ak.datepicker._hideDatepicker()
},today:function(){ak.datepicker._gotoToday(ax)
},selectDay:function(){ak.datepicker._selectDay(ax,+this.getAttribute("data-month"),+this.getAttribute("data-year"),this);
return false
},selectMonth:function(){ak.datepicker._selectMonthYear(ax,this,"M");
return false
},selectYear:function(){ak.datepicker._selectMonthYear(ax,this,"Y");
return false
}};
ak(this).on(this.getAttribute("data-event"),ay[this.getAttribute("data-handler")])
})
},_generateHTML:function(bb){var aO,aN,a6,aY,az,bf,a9,a2,bi,aW,bm,aG,aI,aH,aw,be,aE,aR,bh,a4,bn,aQ,aV,aF,aA,a7,a0,a3,a1,aD,aT,aJ,ba,bd,ay,bg,bk,aZ,aK,bc=new Date(),aP=this._daylightSavingAdjust(new Date(bc.getFullYear(),bc.getMonth(),bc.getDate())),bj=this._get(bb,"isRTL"),bl=this._get(bb,"showButtonPanel"),a5=this._get(bb,"hideIfNoPrevNext"),aU=this._get(bb,"navigationAsDateFormat"),aL=this._getNumberOfMonths(bb),aC=this._get(bb,"showCurrentAtPos"),aX=this._get(bb,"stepMonths"),aS=(aL[0]!==1||aL[1]!==1),ax=this._daylightSavingAdjust((!bb.currentDay?new Date(9999,9,9):new Date(bb.currentYear,bb.currentMonth,bb.currentDay))),aB=this._getMinMaxDate(bb,"min"),aM=this._getMinMaxDate(bb,"max"),av=bb.drawMonth-aC,a8=bb.drawYear;
if(av<0){av+=12;
a8--
}if(aM){aO=this._daylightSavingAdjust(new Date(aM.getFullYear(),aM.getMonth()-(aL[0]*aL[1])+1,aM.getDate()));
aO=(aB&&aO<aB?aB:aO);
while(this._daylightSavingAdjust(new Date(a8,av,1))>aO){av--;
if(av<0){av=11;
a8--
}}}bb.drawMonth=av;
bb.drawYear=a8;
aN=this._get(bb,"prevText");
aN=(!aU?aN:this.formatDate(aN,this._daylightSavingAdjust(new Date(a8,av-aX,1)),this._getFormatConfig(bb)));
a6=(this._canAdjustMonth(bb,-1,a8,av)?"<a class='ui-datepicker-prev ui-corner-all' data-handler='prev' data-event='click' title='"+aN+"'><span class='ui-icon ui-icon-circle-triangle-"+(bj?"e":"w")+"'>"+aN+"</span></a>":(a5?"":"<a class='ui-datepicker-prev ui-corner-all ui-state-disabled' title='"+aN+"'><span class='ui-icon ui-icon-circle-triangle-"+(bj?"e":"w")+"'>"+aN+"</span></a>"));
aY=this._get(bb,"nextText");
aY=(!aU?aY:this.formatDate(aY,this._daylightSavingAdjust(new Date(a8,av+aX,1)),this._getFormatConfig(bb)));
az=(this._canAdjustMonth(bb,+1,a8,av)?"<a class='ui-datepicker-next ui-corner-all' data-handler='next' data-event='click' title='"+aY+"'><span class='ui-icon ui-icon-circle-triangle-"+(bj?"w":"e")+"'>"+aY+"</span></a>":(a5?"":"<a class='ui-datepicker-next ui-corner-all ui-state-disabled' title='"+aY+"'><span class='ui-icon ui-icon-circle-triangle-"+(bj?"w":"e")+"'>"+aY+"</span></a>"));
bf=this._get(bb,"currentText");
a9=(this._get(bb,"gotoCurrent")&&bb.currentDay?ax:aP);
bf=(!aU?bf:this.formatDate(bf,a9,this._getFormatConfig(bb)));
a2=(!bb.inline?"<button type='button' class='ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all' data-handler='hide' data-event='click'>"+this._get(bb,"closeText")+"</button>":"");
bi=(bl)?"<div class='ui-datepicker-buttonpane ui-widget-content'>"+(bj?a2:"")+(this._isInRange(bb,a9)?"<button type='button' class='ui-datepicker-current ui-state-default ui-priority-secondary ui-corner-all' data-handler='today' data-event='click'>"+bf+"</button>":"")+(bj?"":a2)+"</div>":"";
aW=parseInt(this._get(bb,"firstDay"),10);
aW=(isNaN(aW)?0:aW);
bm=this._get(bb,"showWeek");
aG=this._get(bb,"dayNames");
aI=this._get(bb,"dayNamesMin");
aH=this._get(bb,"monthNames");
aw=this._get(bb,"monthNamesShort");
be=this._get(bb,"beforeShowDay");
aE=this._get(bb,"showOtherMonths");
aR=this._get(bb,"selectOtherMonths");
bh=this._getDefaultDate(bb);
a4="";
for(aQ=0;
aQ<aL[0];
aQ++){aV="";
this.maxRows=4;
for(aF=0;
aF<aL[1];
aF++){aA=this._daylightSavingAdjust(new Date(a8,av,bb.selectedDay));
a7=" ui-corner-all";
a0="";
if(aS){a0+="<div class='ui-datepicker-group";
if(aL[1]>1){switch(aF){case 0:a0+=" ui-datepicker-group-first";
a7=" ui-corner-"+(bj?"right":"left");
break;
case aL[1]-1:a0+=" ui-datepicker-group-last";
a7=" ui-corner-"+(bj?"left":"right");
break;
default:a0+=" ui-datepicker-group-middle";
a7="";
break
}}a0+="'>"
}a0+="<div class='ui-datepicker-header ui-widget-header ui-helper-clearfix"+a7+"'>"+(/all|left/.test(a7)&&aQ===0?(bj?az:a6):"")+(/all|right/.test(a7)&&aQ===0?(bj?a6:az):"")+this._generateMonthYearHeader(bb,av,a8,aB,aM,aQ>0||aF>0,aH,aw)+"</div><table class='ui-datepicker-calendar'><thead><tr>";
a3=(bm?"<th class='ui-datepicker-week-col'>"+this._get(bb,"weekHeader")+"</th>":"");
for(bn=0;
bn<7;
bn++){a1=(bn+aW)%7;
a3+="<th scope='col'"+((bn+aW+6)%7>=5?" class='ui-datepicker-week-end'":"")+"><span title='"+aG[a1]+"'>"+aI[a1]+"</span></th>"
}a0+=a3+"</tr></thead><tbody>";
aD=this._getDaysInMonth(a8,av);
if(a8===bb.selectedYear&&av===bb.selectedMonth){bb.selectedDay=Math.min(bb.selectedDay,aD)
}aT=(this._getFirstDayOfMonth(a8,av)-aW+7)%7;
aJ=Math.ceil((aT+aD)/7);
ba=(aS?this.maxRows>aJ?this.maxRows:aJ:aJ);
this.maxRows=ba;
bd=this._daylightSavingAdjust(new Date(a8,av,1-aT));
for(ay=0;
ay<ba;
ay++){a0+="<tr>";
bg=(!bm?"":"<td class='ui-datepicker-week-col'>"+this._get(bb,"calculateWeek")(bd)+"</td>");
for(bn=0;
bn<7;
bn++){bk=(be?be.apply((bb.input?bb.input[0]:null),[bd]):[true,""]);
aZ=(bd.getMonth()!==av);
aK=(aZ&&!aR)||!bk[0]||(aB&&bd<aB)||(aM&&bd>aM);
bg+="<td class='"+((bn+aW+6)%7>=5?" ui-datepicker-week-end":"")+(aZ?" ui-datepicker-other-month":"")+((bd.getTime()===aA.getTime()&&av===bb.selectedMonth&&bb._keyEvent)||(bh.getTime()===bd.getTime()&&bh.getTime()===aA.getTime())?" "+this._dayOverClass:"")+(aK?" "+this._unselectableClass+" ui-state-disabled":"")+(aZ&&!aE?"":" "+bk[1]+(bd.getTime()===ax.getTime()?" "+this._currentClass:"")+(bd.getTime()===aP.getTime()?" ui-datepicker-today":""))+"'"+((!aZ||aE)&&bk[2]?" title='"+bk[2].replace(/'/g,"&#39;")+"'":"")+(aK?"":" data-handler='selectDay' data-event='click' data-month='"+bd.getMonth()+"' data-year='"+bd.getFullYear()+"'")+">"+(aZ&&!aE?"&#xa0;":(aK?"<span class='ui-state-default'>"+bd.getDate()+"</span>":"<a class='ui-state-default"+(bd.getTime()===aP.getTime()?" ui-state-highlight":"")+(bd.getTime()===ax.getTime()?" ui-state-active":"")+(aZ?" ui-priority-secondary":"")+"' href='#'>"+bd.getDate()+"</a>"))+"</td>";
bd.setDate(bd.getDate()+1);
bd=this._daylightSavingAdjust(bd)
}a0+=bg+"</tr>"
}av++;
if(av>11){av=0;
a8++
}a0+="</tbody></table>"+(aS?"</div>"+((aL[0]>0&&aF===aL[1]-1)?"<div class='ui-datepicker-row-break'></div>":""):"");
aV+=a0
}a4+=aV
}a4+=bi;
bb._keyEvent=false;
return a4
},_generateMonthYearHeader:function(az,ax,aH,aB,aF,aI,aD,av){var aM,aw,aN,aK,aA,aJ,aG,aC,ay=this._get(az,"changeMonth"),aO=this._get(az,"changeYear"),aP=this._get(az,"showMonthAfterYear"),aE="<div class='ui-datepicker-title'>",aL="";
if(aI||!ay){aL+="<span class='ui-datepicker-month'>"+aD[ax]+"</span>"
}else{aM=(aB&&aB.getFullYear()===aH);
aw=(aF&&aF.getFullYear()===aH);
aL+="<select class='ui-datepicker-month' data-handler='selectMonth' data-event='change'>";
for(aN=0;
aN<12;
aN++){if((!aM||aN>=aB.getMonth())&&(!aw||aN<=aF.getMonth())){aL+="<option value='"+aN+"'"+(aN===ax?" selected='selected'":"")+">"+av[aN]+"</option>"
}}aL+="</select>"
}if(!aP){aE+=aL+(aI||!(ay&&aO)?"&#xa0;":"")
}if(!az.yearshtml){az.yearshtml="";
if(aI||!aO){aE+="<span class='ui-datepicker-year'>"+aH+"</span>"
}else{aK=this._get(az,"yearRange").split(":");
aA=new Date().getFullYear();
aJ=function(aR){var aQ=(aR.match(/c[+\-].*/)?aH+parseInt(aR.substring(1),10):(aR.match(/[+\-].*/)?aA+parseInt(aR,10):parseInt(aR,10)));
return(isNaN(aQ)?aA:aQ)
};
aG=aJ(aK[0]);
aC=Math.max(aG,aJ(aK[1]||""));
aG=(aB?Math.max(aG,aB.getFullYear()):aG);
aC=(aF?Math.min(aC,aF.getFullYear()):aC);
az.yearshtml+="<select class='ui-datepicker-year' data-handler='selectYear' data-event='change'>";
for(;
aG<=aC;
aG++){az.yearshtml+="<option value='"+aG+"'"+(aG===aH?" selected='selected'":"")+">"+aG+"</option>"
}az.yearshtml+="</select>";
aE+=az.yearshtml;
az.yearshtml=null
}}aE+=this._get(az,"yearSuffix");
if(aP){aE+=(aI||!(ay&&aO)?"&#xa0;":"")+aL
}aE+="</div>";
return aE
},_adjustInstDate:function(ay,aB,aA){var ax=ay.selectedYear+(aA==="Y"?aB:0),az=ay.selectedMonth+(aA==="M"?aB:0),av=Math.min(ay.selectedDay,this._getDaysInMonth(ax,az))+(aA==="D"?aB:0),aw=this._restrictMinMax(ay,this._daylightSavingAdjust(new Date(ax,az,av)));
ay.selectedDay=aw.getDate();
ay.drawMonth=ay.selectedMonth=aw.getMonth();
ay.drawYear=ay.selectedYear=aw.getFullYear();
if(aA==="M"||aA==="Y"){this._notifyChange(ay)
}},_restrictMinMax:function(ay,aw){var ax=this._getMinMaxDate(ay,"min"),az=this._getMinMaxDate(ay,"max"),av=(ax&&aw<ax?ax:aw);
return(az&&av>az?az:av)
},_notifyChange:function(aw){var av=this._get(aw,"onChangeMonthYear");
if(av){av.apply((aw.input?aw.input[0]:null),[aw.selectedYear,aw.selectedMonth+1,aw])
}},_getNumberOfMonths:function(aw){var av=this._get(aw,"numberOfMonths");
return(av==null?[1,1]:(typeof av==="number"?[1,av]:av))
},_getMinMaxDate:function(aw,av){return this._determineDate(aw,this._get(aw,av+"Date"),null)
},_getDaysInMonth:function(av,aw){return 32-this._daylightSavingAdjust(new Date(av,aw,32)).getDate()
},_getFirstDayOfMonth:function(av,aw){return new Date(av,aw,1).getDay()
},_canAdjustMonth:function(ay,aA,ax,az){var av=this._getNumberOfMonths(ay),aw=this._daylightSavingAdjust(new Date(ax,az+(aA<0?aA:av[0]*av[1]),1));
if(aA<0){aw.setDate(this._getDaysInMonth(aw.getFullYear(),aw.getMonth()))
}return this._isInRange(ay,aw)
},_isInRange:function(az,ax){var aw,aC,ay=this._getMinMaxDate(az,"min"),av=this._getMinMaxDate(az,"max"),aD=null,aA=null,aB=this._get(az,"yearRange");
if(aB){aw=aB.split(":");
aC=new Date().getFullYear();
aD=parseInt(aw[0],10);
aA=parseInt(aw[1],10);
if(aw[0].match(/[+\-].*/)){aD+=aC
}if(aw[1].match(/[+\-].*/)){aA+=aC
}}return((!ay||ax.getTime()>=ay.getTime())&&(!av||ax.getTime()<=av.getTime())&&(!aD||ax.getFullYear()>=aD)&&(!aA||ax.getFullYear()<=aA))
},_getFormatConfig:function(av){var aw=this._get(av,"shortYearCutoff");
aw=(typeof aw!=="string"?aw:new Date().getFullYear()%100+parseInt(aw,10));
return{shortYearCutoff:aw,dayNamesShort:this._get(av,"dayNamesShort"),dayNames:this._get(av,"dayNames"),monthNamesShort:this._get(av,"monthNamesShort"),monthNames:this._get(av,"monthNames")}
},_formatDate:function(ay,av,az,ax){if(!av){ay.currentDay=ay.selectedDay;
ay.currentMonth=ay.selectedMonth;
ay.currentYear=ay.selectedYear
}var aw=(av?(typeof av==="object"?av:this._daylightSavingAdjust(new Date(ax,az,av))):this._daylightSavingAdjust(new Date(ay.currentYear,ay.currentMonth,ay.currentDay)));
return this.formatDate(this._get(ay,"dateFormat"),aw,this._getFormatConfig(ay))
}});
function X(aw){var av="button, .ui-datepicker-prev, .ui-datepicker-next, .ui-datepicker-calendar td a";
return aw.on("mouseout",av,function(){ak(this).removeClass("ui-state-hover");
if(this.className.indexOf("ui-datepicker-prev")!==-1){ak(this).removeClass("ui-datepicker-prev-hover")
}if(this.className.indexOf("ui-datepicker-next")!==-1){ak(this).removeClass("ui-datepicker-next-hover")
}}).on("mouseover",av,K)
}function K(){if(!ak.datepicker._isDisabledDatepicker(aq.inline?aq.dpDiv.parent()[0]:aq.input[0])){ak(this).parents(".ui-datepicker-calendar").find("a").removeClass("ui-state-hover");
ak(this).addClass("ui-state-hover");
if(this.className.indexOf("ui-datepicker-prev")!==-1){ak(this).addClass("ui-datepicker-prev-hover")
}if(this.className.indexOf("ui-datepicker-next")!==-1){ak(this).addClass("ui-datepicker-next-hover")
}}}function F(ax,aw){ak.extend(ax,aw);
for(var av in aw){if(aw[av]==null){ax[av]=aw[av]
}}return ax
}ak.fn.datepicker=function(aw){if(!this.length){return this
}if(!ak.datepicker.initialized){ak(document).on("mousedown",ak.datepicker._checkExternalClick);
ak.datepicker.initialized=true
}if(ak("#"+ak.datepicker._mainDivId).length===0){ak("body").append(ak.datepicker.dpDiv)
}var av=Array.prototype.slice.call(arguments,1);
if(typeof aw==="string"&&(aw==="isDisabled"||aw==="getDate"||aw==="widget")){return ak.datepicker["_"+aw+"Datepicker"].apply(ak.datepicker,[this[0]].concat(av))
}if(aw==="option"&&arguments.length===2&&typeof arguments[1]==="string"){return ak.datepicker["_"+aw+"Datepicker"].apply(ak.datepicker,[this[0]].concat(av))
}return this.each(function(){typeof aw==="string"?ak.datepicker["_"+aw+"Datepicker"].apply(ak.datepicker,[this].concat(av)):ak.datepicker._attachDatepicker(this,aw)
})
};
ak.datepicker=new P();
ak.datepicker.initialized=false;
ak.datepicker.uuid=new Date().getTime();
ak.datepicker.version="1.12.1";
var k=ak.datepicker;
var L=ak.ui.ie=!!/msie [\w.]+/.exec(navigator.userAgent.toLowerCase());
/*!
 * jQuery UI Mouse 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var ab=false;
ak(document).on("mouseup",function(){ab=false
});
var a=ak.widget("ui.mouse",{version:"1.12.1",options:{cancel:"input, textarea, button, select, option",distance:1,delay:0},_mouseInit:function(){var av=this;
this.element.on("mousedown."+this.widgetName,function(aw){return av._mouseDown(aw)
}).on("click."+this.widgetName,function(aw){if(true===ak.data(aw.target,av.widgetName+".preventClickEvent")){ak.removeData(aw.target,av.widgetName+".preventClickEvent");
aw.stopImmediatePropagation();
return false
}});
this.started=false
},_mouseDestroy:function(){this.element.off("."+this.widgetName);
if(this._mouseMoveDelegate){this.document.off("mousemove."+this.widgetName,this._mouseMoveDelegate).off("mouseup."+this.widgetName,this._mouseUpDelegate)
}},_mouseDown:function(ax){if(ab){return
}this._mouseMoved=false;
(this._mouseStarted&&this._mouseUp(ax));
this._mouseDownEvent=ax;
var aw=this,ay=(ax.which===1),av=(typeof this.options.cancel==="string"&&ax.target.nodeName?ak(ax.target).closest(this.options.cancel).length:false);
if(!ay||av||!this._mouseCapture(ax)){return true
}this.mouseDelayMet=!this.options.delay;
if(!this.mouseDelayMet){this._mouseDelayTimer=setTimeout(function(){aw.mouseDelayMet=true
},this.options.delay)
}if(this._mouseDistanceMet(ax)&&this._mouseDelayMet(ax)){this._mouseStarted=(this._mouseStart(ax)!==false);
if(!this._mouseStarted){ax.preventDefault();
return true
}}if(true===ak.data(ax.target,this.widgetName+".preventClickEvent")){ak.removeData(ax.target,this.widgetName+".preventClickEvent")
}this._mouseMoveDelegate=function(az){return aw._mouseMove(az)
};
this._mouseUpDelegate=function(az){return aw._mouseUp(az)
};
this.document.on("mousemove."+this.widgetName,this._mouseMoveDelegate).on("mouseup."+this.widgetName,this._mouseUpDelegate);
ax.preventDefault();
ab=true;
return true
},_mouseMove:function(av){if(this._mouseMoved){if(ak.ui.ie&&(!document.documentMode||document.documentMode<9)&&!av.button){return this._mouseUp(av)
}else{if(!av.which){if(av.originalEvent.altKey||av.originalEvent.ctrlKey||av.originalEvent.metaKey||av.originalEvent.shiftKey){this.ignoreMissingWhich=true
}else{if(!this.ignoreMissingWhich){return this._mouseUp(av)
}}}}}if(av.which||av.button){this._mouseMoved=true
}if(this._mouseStarted){this._mouseDrag(av);
return av.preventDefault()
}if(this._mouseDistanceMet(av)&&this._mouseDelayMet(av)){this._mouseStarted=(this._mouseStart(this._mouseDownEvent,av)!==false);
(this._mouseStarted?this._mouseDrag(av):this._mouseUp(av))
}return !this._mouseStarted
},_mouseUp:function(av){this.document.off("mousemove."+this.widgetName,this._mouseMoveDelegate).off("mouseup."+this.widgetName,this._mouseUpDelegate);
if(this._mouseStarted){this._mouseStarted=false;
if(av.target===this._mouseDownEvent.target){ak.data(av.target,this.widgetName+".preventClickEvent",true)
}this._mouseStop(av)
}if(this._mouseDelayTimer){clearTimeout(this._mouseDelayTimer);
delete this._mouseDelayTimer
}this.ignoreMissingWhich=false;
ab=false;
av.preventDefault()
},_mouseDistanceMet:function(av){return(Math.max(Math.abs(this._mouseDownEvent.pageX-av.pageX),Math.abs(this._mouseDownEvent.pageY-av.pageY))>=this.options.distance)
},_mouseDelayMet:function(){return this.mouseDelayMet
},_mouseStart:function(){},_mouseDrag:function(){},_mouseStop:function(){},_mouseCapture:function(){return true
}});
var G=ak.ui.plugin={add:function(aw,ax,az){var av,ay=ak.ui[aw].prototype;
for(av in az){ay.plugins[av]=ay.plugins[av]||[];
ay.plugins[av].push([ax,az[av]])
}},call:function(av,ay,ax,aw){var az,aA=av.plugins[ay];
if(!aA){return
}if(!aw&&(!av.element[0].parentNode||av.element[0].parentNode.nodeType===11)){return
}for(az=0;
az<aA.length;
az++){if(av.options[aA[az][0]]){aA[az][1].apply(av.element,ax)
}}}};
var c=ak.ui.safeBlur=function(av){if(av&&av.nodeName.toLowerCase()!=="body"){ak(av).trigger("blur")
}};
/*!
 * jQuery UI Draggable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.draggable",ak.ui.mouse,{version:"1.12.1",widgetEventPrefix:"drag",options:{addClasses:true,appendTo:"parent",axis:false,connectToSortable:false,containment:false,cursor:"auto",cursorAt:false,grid:false,handle:false,helper:"original",iframeFix:false,opacity:false,refreshPositions:false,revert:false,revertDuration:500,scope:"default",scroll:true,scrollSensitivity:20,scrollSpeed:20,snap:false,snapMode:"both",snapTolerance:20,stack:false,zIndex:false,drag:null,start:null,stop:null},_create:function(){if(this.options.helper==="original"){this._setPositionRelative()
}if(this.options.addClasses){this._addClass("ui-draggable")
}this._setHandleClassName();
this._mouseInit()
},_setOption:function(av,aw){this._super(av,aw);
if(av==="handle"){this._removeHandleClassName();
this._setHandleClassName()
}},_destroy:function(){if((this.helper||this.element).is(".ui-draggable-dragging")){this.destroyOnClear=true;
return
}this._removeHandleClassName();
this._mouseDestroy()
},_mouseCapture:function(av){var aw=this.options;
if(this.helper||aw.disabled||ak(av.target).closest(".ui-resizable-handle").length>0){return false
}this.handle=this._getHandle(av);
if(!this.handle){return false
}this._blurActiveElement(av);
this._blockFrames(aw.iframeFix===true?"iframe":aw.iframeFix);
return true
},_blockFrames:function(av){this.iframeBlocks=this.document.find(av).map(function(){var aw=ak(this);
return ak("<div>").css("position","absolute").appendTo(aw.parent()).outerWidth(aw.outerWidth()).outerHeight(aw.outerHeight()).offset(aw.offset())[0]
})
},_unblockFrames:function(){if(this.iframeBlocks){this.iframeBlocks.remove();
delete this.iframeBlocks
}},_blurActiveElement:function(aw){var av=ak.ui.safeActiveElement(this.document[0]),ax=ak(aw.target);
if(ax.closest(av).length){return
}ak.ui.safeBlur(av)
},_mouseStart:function(av){var aw=this.options;
this.helper=this._createHelper(av);
this._addClass(this.helper,"ui-draggable-dragging");
this._cacheHelperProportions();
if(ak.ui.ddmanager){ak.ui.ddmanager.current=this
}this._cacheMargins();
this.cssPosition=this.helper.css("position");
this.scrollParent=this.helper.scrollParent(true);
this.offsetParent=this.helper.offsetParent();
this.hasFixedAncestor=this.helper.parents().filter(function(){return ak(this).css("position")==="fixed"
}).length>0;
this.positionAbs=this.element.offset();
this._refreshOffsets(av);
this.originalPosition=this.position=this._generatePosition(av,false);
this.originalPageX=av.pageX;
this.originalPageY=av.pageY;
(aw.cursorAt&&this._adjustOffsetFromHelper(aw.cursorAt));
this._setContainment();
if(this._trigger("start",av)===false){this._clear();
return false
}this._cacheHelperProportions();
if(ak.ui.ddmanager&&!aw.dropBehaviour){ak.ui.ddmanager.prepareOffsets(this,av)
}this._mouseDrag(av,true);
if(ak.ui.ddmanager){ak.ui.ddmanager.dragStart(this,av)
}return true
},_refreshOffsets:function(av){this.offset={top:this.positionAbs.top-this.margins.top,left:this.positionAbs.left-this.margins.left,scroll:false,parent:this._getParentOffset(),relative:this._getRelativeOffset()};
this.offset.click={left:av.pageX-this.offset.left,top:av.pageY-this.offset.top}
},_mouseDrag:function(av,ax){if(this.hasFixedAncestor){this.offset.parent=this._getParentOffset()
}this.position=this._generatePosition(av,true);
this.positionAbs=this._convertPositionTo("absolute");
if(!ax){var aw=this._uiHash();
if(this._trigger("drag",av,aw)===false){this._mouseUp(new ak.Event("mouseup",av));
return false
}this.position=aw.position
}this.helper[0].style.left=this.position.left+"px";
this.helper[0].style.top=this.position.top+"px";
if(ak.ui.ddmanager){ak.ui.ddmanager.drag(this,av)
}return false
},_mouseStop:function(aw){var av=this,ax=false;
if(ak.ui.ddmanager&&!this.options.dropBehaviour){ax=ak.ui.ddmanager.drop(this,aw)
}if(this.dropped){ax=this.dropped;
this.dropped=false
}if((this.options.revert==="invalid"&&!ax)||(this.options.revert==="valid"&&ax)||this.options.revert===true||(ak.isFunction(this.options.revert)&&this.options.revert.call(this.element,ax))){ak(this.helper).animate(this.originalPosition,parseInt(this.options.revertDuration,10),function(){if(av._trigger("stop",aw)!==false){av._clear()
}})
}else{if(this._trigger("stop",aw)!==false){this._clear()
}}return false
},_mouseUp:function(av){this._unblockFrames();
if(ak.ui.ddmanager){ak.ui.ddmanager.dragStop(this,av)
}if(this.handleElement.is(av.target)){this.element.trigger("focus")
}return ak.ui.mouse.prototype._mouseUp.call(this,av)
},cancel:function(){if(this.helper.is(".ui-draggable-dragging")){this._mouseUp(new ak.Event("mouseup",{target:this.element[0]}))
}else{this._clear()
}return this
},_getHandle:function(av){return this.options.handle?!!ak(av.target).closest(this.element.find(this.options.handle)).length:true
},_setHandleClassName:function(){this.handleElement=this.options.handle?this.element.find(this.options.handle):this.element;
this._addClass(this.handleElement,"ui-draggable-handle")
},_removeHandleClassName:function(){this._removeClass(this.handleElement,"ui-draggable-handle")
},_createHelper:function(aw){var ay=this.options,ax=ak.isFunction(ay.helper),av=ax?ak(ay.helper.apply(this.element[0],[aw])):(ay.helper==="clone"?this.element.clone().removeAttr("id"):this.element);
if(!av.parents("body").length){av.appendTo((ay.appendTo==="parent"?this.element[0].parentNode:ay.appendTo))
}if(ax&&av[0]===this.element[0]){this._setPositionRelative()
}if(av[0]!==this.element[0]&&!(/(fixed|absolute)/).test(av.css("position"))){av.css("position","absolute")
}return av
},_setPositionRelative:function(){if(!(/^(?:r|a|f)/).test(this.element.css("position"))){this.element[0].style.position="relative"
}},_adjustOffsetFromHelper:function(av){if(typeof av==="string"){av=av.split(" ")
}if(ak.isArray(av)){av={left:+av[0],top:+av[1]||0}
}if("left" in av){this.offset.click.left=av.left+this.margins.left
}if("right" in av){this.offset.click.left=this.helperProportions.width-av.right+this.margins.left
}if("top" in av){this.offset.click.top=av.top+this.margins.top
}if("bottom" in av){this.offset.click.top=this.helperProportions.height-av.bottom+this.margins.top
}},_isRootNode:function(av){return(/(html|body)/i).test(av.tagName)||av===this.document[0]
},_getParentOffset:function(){var aw=this.offsetParent.offset(),av=this.document[0];
if(this.cssPosition==="absolute"&&this.scrollParent[0]!==av&&ak.contains(this.scrollParent[0],this.offsetParent[0])){aw.left+=this.scrollParent.scrollLeft();
aw.top+=this.scrollParent.scrollTop()
}if(this._isRootNode(this.offsetParent[0])){aw={top:0,left:0}
}return{top:aw.top+(parseInt(this.offsetParent.css("borderTopWidth"),10)||0),left:aw.left+(parseInt(this.offsetParent.css("borderLeftWidth"),10)||0)}
},_getRelativeOffset:function(){if(this.cssPosition!=="relative"){return{top:0,left:0}
}var av=this.element.position(),aw=this._isRootNode(this.scrollParent[0]);
return{top:av.top-(parseInt(this.helper.css("top"),10)||0)+(!aw?this.scrollParent.scrollTop():0),left:av.left-(parseInt(this.helper.css("left"),10)||0)+(!aw?this.scrollParent.scrollLeft():0)}
},_cacheMargins:function(){this.margins={left:(parseInt(this.element.css("marginLeft"),10)||0),top:(parseInt(this.element.css("marginTop"),10)||0),right:(parseInt(this.element.css("marginRight"),10)||0),bottom:(parseInt(this.element.css("marginBottom"),10)||0)}
},_cacheHelperProportions:function(){this.helperProportions={width:this.helper.outerWidth(),height:this.helper.outerHeight()}
},_setContainment:function(){var aw,az,ax,ay=this.options,av=this.document[0];
this.relativeContainer=null;
if(!ay.containment){this.containment=null;
return
}if(ay.containment==="window"){this.containment=[ak(window).scrollLeft()-this.offset.relative.left-this.offset.parent.left,ak(window).scrollTop()-this.offset.relative.top-this.offset.parent.top,ak(window).scrollLeft()+ak(window).width()-this.helperProportions.width-this.margins.left,ak(window).scrollTop()+(ak(window).height()||av.body.parentNode.scrollHeight)-this.helperProportions.height-this.margins.top];
return
}if(ay.containment==="document"){this.containment=[0,0,ak(av).width()-this.helperProportions.width-this.margins.left,(ak(av).height()||av.body.parentNode.scrollHeight)-this.helperProportions.height-this.margins.top];
return
}if(ay.containment.constructor===Array){this.containment=ay.containment;
return
}if(ay.containment==="parent"){ay.containment=this.helper[0].parentNode
}az=ak(ay.containment);
ax=az[0];
if(!ax){return
}aw=/(scroll|auto)/.test(az.css("overflow"));
this.containment=[(parseInt(az.css("borderLeftWidth"),10)||0)+(parseInt(az.css("paddingLeft"),10)||0),(parseInt(az.css("borderTopWidth"),10)||0)+(parseInt(az.css("paddingTop"),10)||0),(aw?Math.max(ax.scrollWidth,ax.offsetWidth):ax.offsetWidth)-(parseInt(az.css("borderRightWidth"),10)||0)-(parseInt(az.css("paddingRight"),10)||0)-this.helperProportions.width-this.margins.left-this.margins.right,(aw?Math.max(ax.scrollHeight,ax.offsetHeight):ax.offsetHeight)-(parseInt(az.css("borderBottomWidth"),10)||0)-(parseInt(az.css("paddingBottom"),10)||0)-this.helperProportions.height-this.margins.top-this.margins.bottom];
this.relativeContainer=az
},_convertPositionTo:function(aw,ay){if(!ay){ay=this.position
}var av=aw==="absolute"?1:-1,ax=this._isRootNode(this.scrollParent[0]);
return{top:(ay.top+this.offset.relative.top*av+this.offset.parent.top*av-((this.cssPosition==="fixed"?-this.offset.scroll.top:(ax?0:this.offset.scroll.top))*av)),left:(ay.left+this.offset.relative.left*av+this.offset.parent.left*av-((this.cssPosition==="fixed"?-this.offset.scroll.left:(ax?0:this.offset.scroll.left))*av))}
},_generatePosition:function(aw,aC){var av,aD,aE,ay,ax=this.options,aB=this._isRootNode(this.scrollParent[0]),aA=aw.pageX,az=aw.pageY;
if(!aB||!this.offset.scroll){this.offset.scroll={top:this.scrollParent.scrollTop(),left:this.scrollParent.scrollLeft()}
}if(aC){if(this.containment){if(this.relativeContainer){aD=this.relativeContainer.offset();
av=[this.containment[0]+aD.left,this.containment[1]+aD.top,this.containment[2]+aD.left,this.containment[3]+aD.top]
}else{av=this.containment
}if(aw.pageX-this.offset.click.left<av[0]){aA=av[0]+this.offset.click.left
}if(aw.pageY-this.offset.click.top<av[1]){az=av[1]+this.offset.click.top
}if(aw.pageX-this.offset.click.left>av[2]){aA=av[2]+this.offset.click.left
}if(aw.pageY-this.offset.click.top>av[3]){az=av[3]+this.offset.click.top
}}if(ax.grid){aE=ax.grid[1]?this.originalPageY+Math.round((az-this.originalPageY)/ax.grid[1])*ax.grid[1]:this.originalPageY;
az=av?((aE-this.offset.click.top>=av[1]||aE-this.offset.click.top>av[3])?aE:((aE-this.offset.click.top>=av[1])?aE-ax.grid[1]:aE+ax.grid[1])):aE;
ay=ax.grid[0]?this.originalPageX+Math.round((aA-this.originalPageX)/ax.grid[0])*ax.grid[0]:this.originalPageX;
aA=av?((ay-this.offset.click.left>=av[0]||ay-this.offset.click.left>av[2])?ay:((ay-this.offset.click.left>=av[0])?ay-ax.grid[0]:ay+ax.grid[0])):ay
}if(ax.axis==="y"){aA=this.originalPageX
}if(ax.axis==="x"){az=this.originalPageY
}}return{top:(az-this.offset.click.top-this.offset.relative.top-this.offset.parent.top+(this.cssPosition==="fixed"?-this.offset.scroll.top:(aB?0:this.offset.scroll.top))),left:(aA-this.offset.click.left-this.offset.relative.left-this.offset.parent.left+(this.cssPosition==="fixed"?-this.offset.scroll.left:(aB?0:this.offset.scroll.left)))}
},_clear:function(){this._removeClass(this.helper,"ui-draggable-dragging");
if(this.helper[0]!==this.element[0]&&!this.cancelHelperRemoval){this.helper.remove()
}this.helper=null;
this.cancelHelperRemoval=false;
if(this.destroyOnClear){this.destroy()
}},_trigger:function(av,aw,ax){ax=ax||this._uiHash();
ak.ui.plugin.call(this,av,[aw,ax,this],true);
if(/^(drag|start|stop)/.test(av)){this.positionAbs=this._convertPositionTo("absolute");
ax.offset=this.positionAbs
}return ak.Widget.prototype._trigger.call(this,av,aw,ax)
},plugins:{},_uiHash:function(){return{helper:this.helper,position:this.position,originalPosition:this.originalPosition,offset:this.positionAbs}
}});
ak.ui.plugin.add("draggable","connectToSortable",{start:function(ax,ay,av){var aw=ak.extend({},ay,{item:av.element});
av.sortables=[];
ak(av.options.connectToSortable).each(function(){var az=ak(this).sortable("instance");
if(az&&!az.options.disabled){av.sortables.push(az);
az.refreshPositions();
az._trigger("activate",ax,aw)
}})
},stop:function(ax,ay,av){var aw=ak.extend({},ay,{item:av.element});
av.cancelHelperRemoval=false;
ak.each(av.sortables,function(){var az=this;
if(az.isOver){az.isOver=0;
av.cancelHelperRemoval=true;
az.cancelHelperRemoval=false;
az._storedCSS={position:az.placeholder.css("position"),top:az.placeholder.css("top"),left:az.placeholder.css("left")};
az._mouseStop(ax);
az.options.helper=az.options._helper
}else{az.cancelHelperRemoval=true;
az._trigger("deactivate",ax,aw)
}})
},drag:function(aw,ax,av){ak.each(av.sortables,function(){var ay=false,az=this;
az.positionAbs=av.positionAbs;
az.helperProportions=av.helperProportions;
az.offset.click=av.offset.click;
if(az._intersectsWith(az.containerCache)){ay=true;
ak.each(av.sortables,function(){this.positionAbs=av.positionAbs;
this.helperProportions=av.helperProportions;
this.offset.click=av.offset.click;
if(this!==az&&this._intersectsWith(this.containerCache)&&ak.contains(az.element[0],this.element[0])){ay=false
}return ay
})
}if(ay){if(!az.isOver){az.isOver=1;
av._parent=ax.helper.parent();
az.currentItem=ax.helper.appendTo(az.element).data("ui-sortable-item",true);
az.options._helper=az.options.helper;
az.options.helper=function(){return ax.helper[0]
};
aw.target=az.currentItem[0];
az._mouseCapture(aw,true);
az._mouseStart(aw,true,true);
az.offset.click.top=av.offset.click.top;
az.offset.click.left=av.offset.click.left;
az.offset.parent.left-=av.offset.parent.left-az.offset.parent.left;
az.offset.parent.top-=av.offset.parent.top-az.offset.parent.top;
av._trigger("toSortable",aw);
av.dropped=az.element;
ak.each(av.sortables,function(){this.refreshPositions()
});
av.currentItem=av.element;
az.fromOutside=av
}if(az.currentItem){az._mouseDrag(aw);
ax.position=az.position
}}else{if(az.isOver){az.isOver=0;
az.cancelHelperRemoval=true;
az.options._revert=az.options.revert;
az.options.revert=false;
az._trigger("out",aw,az._uiHash(az));
az._mouseStop(aw,true);
az.options.revert=az.options._revert;
az.options.helper=az.options._helper;
if(az.placeholder){az.placeholder.remove()
}ax.helper.appendTo(av._parent);
av._refreshOffsets(aw);
ax.position=av._generatePosition(aw,true);
av._trigger("fromSortable",aw);
av.dropped=false;
ak.each(av.sortables,function(){this.refreshPositions()
})
}}})
}});
ak.ui.plugin.add("draggable","cursor",{start:function(ax,ay,av){var aw=ak("body"),az=av.options;
if(aw.css("cursor")){az._cursor=aw.css("cursor")
}aw.css("cursor",az.cursor)
},stop:function(aw,ax,av){var ay=av.options;
if(ay._cursor){ak("body").css("cursor",ay._cursor)
}}});
ak.ui.plugin.add("draggable","opacity",{start:function(ax,ay,av){var aw=ak(ay.helper),az=av.options;
if(aw.css("opacity")){az._opacity=aw.css("opacity")
}aw.css("opacity",az.opacity)
},stop:function(aw,ax,av){var ay=av.options;
if(ay._opacity){ak(ax.helper).css("opacity",ay._opacity)
}}});
ak.ui.plugin.add("draggable","scroll",{start:function(aw,ax,av){if(!av.scrollParentNotHidden){av.scrollParentNotHidden=av.helper.scrollParent(false)
}if(av.scrollParentNotHidden[0]!==av.document[0]&&av.scrollParentNotHidden[0].tagName!=="HTML"){av.overflowOffset=av.scrollParentNotHidden.offset()
}},drag:function(ay,az,ax){var aA=ax.options,aw=false,aB=ax.scrollParentNotHidden[0],av=ax.document[0];
if(aB!==av&&aB.tagName!=="HTML"){if(!aA.axis||aA.axis!=="x"){if((ax.overflowOffset.top+aB.offsetHeight)-ay.pageY<aA.scrollSensitivity){aB.scrollTop=aw=aB.scrollTop+aA.scrollSpeed
}else{if(ay.pageY-ax.overflowOffset.top<aA.scrollSensitivity){aB.scrollTop=aw=aB.scrollTop-aA.scrollSpeed
}}}if(!aA.axis||aA.axis!=="y"){if((ax.overflowOffset.left+aB.offsetWidth)-ay.pageX<aA.scrollSensitivity){aB.scrollLeft=aw=aB.scrollLeft+aA.scrollSpeed
}else{if(ay.pageX-ax.overflowOffset.left<aA.scrollSensitivity){aB.scrollLeft=aw=aB.scrollLeft-aA.scrollSpeed
}}}}else{if(!aA.axis||aA.axis!=="x"){if(ay.pageY-ak(av).scrollTop()<aA.scrollSensitivity){aw=ak(av).scrollTop(ak(av).scrollTop()-aA.scrollSpeed)
}else{if(ak(window).height()-(ay.pageY-ak(av).scrollTop())<aA.scrollSensitivity){aw=ak(av).scrollTop(ak(av).scrollTop()+aA.scrollSpeed)
}}}if(!aA.axis||aA.axis!=="y"){if(ay.pageX-ak(av).scrollLeft()<aA.scrollSensitivity){aw=ak(av).scrollLeft(ak(av).scrollLeft()-aA.scrollSpeed)
}else{if(ak(window).width()-(ay.pageX-ak(av).scrollLeft())<aA.scrollSensitivity){aw=ak(av).scrollLeft(ak(av).scrollLeft()+aA.scrollSpeed)
}}}}if(aw!==false&&ak.ui.ddmanager&&!aA.dropBehaviour){ak.ui.ddmanager.prepareOffsets(ax,ay)
}}});
ak.ui.plugin.add("draggable","snap",{start:function(aw,ax,av){var ay=av.options;
av.snapElements=[];
ak(ay.snap.constructor!==String?(ay.snap.items||":data(ui-draggable)"):ay.snap).each(function(){var aA=ak(this),az=aA.offset();
if(this!==av.element[0]){av.snapElements.push({item:this,width:aA.outerWidth(),height:aA.outerHeight(),top:az.top,left:az.left})
}})
},drag:function(aH,aE,ay){var av,aM,aA,aB,aG,aD,aC,aN,aI,az,aF=ay.options,aL=aF.snapTolerance,aK=aE.offset.left,aJ=aK+ay.helperProportions.width,ax=aE.offset.top,aw=ax+ay.helperProportions.height;
for(aI=ay.snapElements.length-1;
aI>=0;
aI--){aG=ay.snapElements[aI].left-ay.margins.left;
aD=aG+ay.snapElements[aI].width;
aC=ay.snapElements[aI].top-ay.margins.top;
aN=aC+ay.snapElements[aI].height;
if(aJ<aG-aL||aK>aD+aL||aw<aC-aL||ax>aN+aL||!ak.contains(ay.snapElements[aI].item.ownerDocument,ay.snapElements[aI].item)){if(ay.snapElements[aI].snapping){(ay.options.snap.release&&ay.options.snap.release.call(ay.element,aH,ak.extend(ay._uiHash(),{snapItem:ay.snapElements[aI].item})))
}ay.snapElements[aI].snapping=false;
continue
}if(aF.snapMode!=="inner"){av=Math.abs(aC-aw)<=aL;
aM=Math.abs(aN-ax)<=aL;
aA=Math.abs(aG-aJ)<=aL;
aB=Math.abs(aD-aK)<=aL;
if(av){aE.position.top=ay._convertPositionTo("relative",{top:aC-ay.helperProportions.height,left:0}).top
}if(aM){aE.position.top=ay._convertPositionTo("relative",{top:aN,left:0}).top
}if(aA){aE.position.left=ay._convertPositionTo("relative",{top:0,left:aG-ay.helperProportions.width}).left
}if(aB){aE.position.left=ay._convertPositionTo("relative",{top:0,left:aD}).left
}}az=(av||aM||aA||aB);
if(aF.snapMode!=="outer"){av=Math.abs(aC-ax)<=aL;
aM=Math.abs(aN-aw)<=aL;
aA=Math.abs(aG-aK)<=aL;
aB=Math.abs(aD-aJ)<=aL;
if(av){aE.position.top=ay._convertPositionTo("relative",{top:aC,left:0}).top
}if(aM){aE.position.top=ay._convertPositionTo("relative",{top:aN-ay.helperProportions.height,left:0}).top
}if(aA){aE.position.left=ay._convertPositionTo("relative",{top:0,left:aG}).left
}if(aB){aE.position.left=ay._convertPositionTo("relative",{top:0,left:aD-ay.helperProportions.width}).left
}}if(!ay.snapElements[aI].snapping&&(av||aM||aA||aB||az)){(ay.options.snap.snap&&ay.options.snap.snap.call(ay.element,aH,ak.extend(ay._uiHash(),{snapItem:ay.snapElements[aI].item})))
}ay.snapElements[aI].snapping=(av||aM||aA||aB||az)
}}});
ak.ui.plugin.add("draggable","stack",{start:function(ax,ay,av){var aw,aA=av.options,az=ak.makeArray(ak(aA.stack)).sort(function(aC,aB){return(parseInt(ak(aC).css("zIndex"),10)||0)-(parseInt(ak(aB).css("zIndex"),10)||0)
});
if(!az.length){return
}aw=parseInt(ak(az[0]).css("zIndex"),10)||0;
ak(az).each(function(aB){ak(this).css("zIndex",aw+aB)
});
this.css("zIndex",(aw+az.length))
}});
ak.ui.plugin.add("draggable","zIndex",{start:function(ax,ay,av){var aw=ak(ay.helper),az=av.options;
if(aw.css("zIndex")){az._zIndex=aw.css("zIndex")
}aw.css("zIndex",az.zIndex)
},stop:function(aw,ax,av){var ay=av.options;
if(ay._zIndex){ak(ax.helper).css("zIndex",ay._zIndex)
}}});
var w=ak.ui.draggable;
/*!
 * jQuery UI Resizable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.resizable",ak.ui.mouse,{version:"1.12.1",widgetEventPrefix:"resize",options:{alsoResize:false,animate:false,animateDuration:"slow",animateEasing:"swing",aspectRatio:false,autoHide:false,classes:{"ui-resizable-se":"ui-icon ui-icon-gripsmall-diagonal-se"},containment:false,ghost:false,grid:false,handles:"e,s,se",helper:false,maxHeight:null,maxWidth:null,minHeight:10,minWidth:10,zIndex:90,resize:null,start:null,stop:null},_num:function(av){return parseFloat(av)||0
},_isNumber:function(av){return !isNaN(parseFloat(av))
},_hasScroll:function(ay,aw){if(ak(ay).css("overflow")==="hidden"){return false
}var av=(aw&&aw==="left")?"scrollLeft":"scrollTop",ax=false;
if(ay[av]>0){return true
}ay[av]=1;
ax=(ay[av]>0);
ay[av]=0;
return ax
},_create:function(){var aw,ax=this.options,av=this;
this._addClass("ui-resizable");
ak.extend(this,{_aspectRatio:!!(ax.aspectRatio),aspectRatio:ax.aspectRatio,originalElement:this.element,_proportionallyResizeElements:[],_helper:ax.helper||ax.ghost||ax.animate?ax.helper||"ui-resizable-helper":null});
if(this.element[0].nodeName.match(/^(canvas|textarea|input|select|button|img)$/i)){this.element.wrap(ak("<div class='ui-wrapper' style='overflow: hidden;'></div>").css({position:this.element.css("position"),width:this.element.outerWidth(),height:this.element.outerHeight(),top:this.element.css("top"),left:this.element.css("left")}));
this.element=this.element.parent().data("ui-resizable",this.element.resizable("instance"));
this.elementIsWrapper=true;
aw={marginTop:this.originalElement.css("marginTop"),marginRight:this.originalElement.css("marginRight"),marginBottom:this.originalElement.css("marginBottom"),marginLeft:this.originalElement.css("marginLeft")};
this.element.css(aw);
this.originalElement.css("margin",0);
this.originalResizeStyle=this.originalElement.css("resize");
this.originalElement.css("resize","none");
this._proportionallyResizeElements.push(this.originalElement.css({position:"static",zoom:1,display:"block"}));
this.originalElement.css(aw);
this._proportionallyResize()
}this._setupHandles();
if(ax.autoHide){ak(this.element).on("mouseenter",function(){if(ax.disabled){return
}av._removeClass("ui-resizable-autohide");
av._handles.show()
}).on("mouseleave",function(){if(ax.disabled){return
}if(!av.resizing){av._addClass("ui-resizable-autohide");
av._handles.hide()
}})
}this._mouseInit()
},_destroy:function(){this._mouseDestroy();
var aw,av=function(ax){ak(ax).removeData("resizable").removeData("ui-resizable").off(".resizable").find(".ui-resizable-handle").remove()
};
if(this.elementIsWrapper){av(this.element);
aw=this.element;
this.originalElement.css({position:aw.css("position"),width:aw.outerWidth(),height:aw.outerHeight(),top:aw.css("top"),left:aw.css("left")}).insertAfter(aw);
aw.remove()
}this.originalElement.css("resize",this.originalResizeStyle);
av(this.originalElement);
return this
},_setOption:function(av,aw){this._super(av,aw);
switch(av){case"handles":this._removeHandles();
this._setupHandles();
break;
default:break
}},_setupHandles:function(){var aA=this.options,az,aw,aB,av,ax,ay=this;
this.handles=aA.handles||(!ak(".ui-resizable-handle",this.element).length?"e,s,se":{n:".ui-resizable-n",e:".ui-resizable-e",s:".ui-resizable-s",w:".ui-resizable-w",se:".ui-resizable-se",sw:".ui-resizable-sw",ne:".ui-resizable-ne",nw:".ui-resizable-nw"});
this._handles=ak();
if(this.handles.constructor===String){if(this.handles==="all"){this.handles="n,e,s,w,se,sw,ne,nw"
}aB=this.handles.split(",");
this.handles={};
for(aw=0;
aw<aB.length;
aw++){az=ak.trim(aB[aw]);
av="ui-resizable-"+az;
ax=ak("<div>");
this._addClass(ax,"ui-resizable-handle "+av);
ax.css({zIndex:aA.zIndex});
this.handles[az]=".ui-resizable-"+az;
this.element.append(ax)
}}this._renderAxis=function(aG){var aD,aE,aC,aF;
aG=aG||this.element;
for(aD in this.handles){if(this.handles[aD].constructor===String){this.handles[aD]=this.element.children(this.handles[aD]).first().show()
}else{if(this.handles[aD].jquery||this.handles[aD].nodeType){this.handles[aD]=ak(this.handles[aD]);
this._on(this.handles[aD],{mousedown:ay._mouseDown})
}}if(this.elementIsWrapper&&this.originalElement[0].nodeName.match(/^(textarea|input|select|button)$/i)){aE=ak(this.handles[aD],this.element);
aF=/sw|ne|nw|se|n|s/.test(aD)?aE.outerHeight():aE.outerWidth();
aC=["padding",/ne|nw|n/.test(aD)?"Top":/se|sw|s/.test(aD)?"Bottom":/^e$/.test(aD)?"Right":"Left"].join("");
aG.css(aC,aF);
this._proportionallyResize()
}this._handles=this._handles.add(this.handles[aD])
}};
this._renderAxis(this.element);
this._handles=this._handles.add(this.element.find(".ui-resizable-handle"));
this._handles.disableSelection();
this._handles.on("mouseover",function(){if(!ay.resizing){if(this.className){ax=this.className.match(/ui-resizable-(se|sw|ne|nw|n|e|s|w)/i)
}ay.axis=ax&&ax[1]?ax[1]:"se"
}});
if(aA.autoHide){this._handles.hide();
this._addClass("ui-resizable-autohide")
}},_removeHandles:function(){this._handles.remove()
},_mouseCapture:function(ax){var aw,ay,av=false;
for(aw in this.handles){ay=ak(this.handles[aw])[0];
if(ay===ax.target||ak.contains(ay,ax.target)){av=true
}}return !this.options.disabled&&av
},_mouseStart:function(aw){var aA,ax,az,ay=this.options,av=this.element;
this.resizing=true;
this._renderProxy();
aA=this._num(this.helper.css("left"));
ax=this._num(this.helper.css("top"));
if(ay.containment){aA+=ak(ay.containment).scrollLeft()||0;
ax+=ak(ay.containment).scrollTop()||0
}this.offset=this.helper.offset();
this.position={left:aA,top:ax};
this.size=this._helper?{width:this.helper.width(),height:this.helper.height()}:{width:av.width(),height:av.height()};
this.originalSize=this._helper?{width:av.outerWidth(),height:av.outerHeight()}:{width:av.width(),height:av.height()};
this.sizeDiff={width:av.outerWidth()-av.width(),height:av.outerHeight()-av.height()};
this.originalPosition={left:aA,top:ax};
this.originalMousePosition={left:aw.pageX,top:aw.pageY};
this.aspectRatio=(typeof ay.aspectRatio==="number")?ay.aspectRatio:((this.originalSize.width/this.originalSize.height)||1);
az=ak(".ui-resizable-"+this.axis).css("cursor");
ak("body").css("cursor",az==="auto"?this.axis+"-resize":az);
this._addClass("ui-resizable-resizing");
this._propagate("start",aw);
return true
},_mouseDrag:function(aA){var aB,az,aC=this.originalMousePosition,aw=this.axis,ax=(aA.pageX-aC.left)||0,av=(aA.pageY-aC.top)||0,ay=this._change[aw];
this._updatePrevProperties();
if(!ay){return false
}aB=ay.apply(this,[aA,ax,av]);
this._updateVirtualBoundaries(aA.shiftKey);
if(this._aspectRatio||aA.shiftKey){aB=this._updateRatio(aB,aA)
}aB=this._respectSize(aB,aA);
this._updateCache(aB);
this._propagate("resize",aA);
az=this._applyChanges();
if(!this._helper&&this._proportionallyResizeElements.length){this._proportionallyResize()
}if(!ak.isEmptyObject(az)){this._updatePrevProperties();
this._trigger("resize",aA,this.ui());
this._applyChanges()
}return false
},_mouseStop:function(ay){this.resizing=false;
var ax,av,aw,aB,aE,aA,aD,az=this.options,aC=this;
if(this._helper){ax=this._proportionallyResizeElements;
av=ax.length&&(/textarea/i).test(ax[0].nodeName);
aw=av&&this._hasScroll(ax[0],"left")?0:aC.sizeDiff.height;
aB=av?0:aC.sizeDiff.width;
aE={width:(aC.helper.width()-aB),height:(aC.helper.height()-aw)};
aA=(parseFloat(aC.element.css("left"))+(aC.position.left-aC.originalPosition.left))||null;
aD=(parseFloat(aC.element.css("top"))+(aC.position.top-aC.originalPosition.top))||null;
if(!az.animate){this.element.css(ak.extend(aE,{top:aD,left:aA}))
}aC.helper.height(aC.size.height);
aC.helper.width(aC.size.width);
if(this._helper&&!az.animate){this._proportionallyResize()
}}ak("body").css("cursor","auto");
this._removeClass("ui-resizable-resizing");
this._propagate("stop",ay);
if(this._helper){this.helper.remove()
}return false
},_updatePrevProperties:function(){this.prevPosition={top:this.position.top,left:this.position.left};
this.prevSize={width:this.size.width,height:this.size.height}
},_applyChanges:function(){var av={};
if(this.position.top!==this.prevPosition.top){av.top=this.position.top+"px"
}if(this.position.left!==this.prevPosition.left){av.left=this.position.left+"px"
}if(this.size.width!==this.prevSize.width){av.width=this.size.width+"px"
}if(this.size.height!==this.prevSize.height){av.height=this.size.height+"px"
}this.helper.css(av);
return av
},_updateVirtualBoundaries:function(ax){var az,ay,aw,aB,av,aA=this.options;
av={minWidth:this._isNumber(aA.minWidth)?aA.minWidth:0,maxWidth:this._isNumber(aA.maxWidth)?aA.maxWidth:Infinity,minHeight:this._isNumber(aA.minHeight)?aA.minHeight:0,maxHeight:this._isNumber(aA.maxHeight)?aA.maxHeight:Infinity};
if(this._aspectRatio||ax){az=av.minHeight*this.aspectRatio;
aw=av.minWidth/this.aspectRatio;
ay=av.maxHeight*this.aspectRatio;
aB=av.maxWidth/this.aspectRatio;
if(az>av.minWidth){av.minWidth=az
}if(aw>av.minHeight){av.minHeight=aw
}if(ay<av.maxWidth){av.maxWidth=ay
}if(aB<av.maxHeight){av.maxHeight=aB
}}this._vBoundaries=av
},_updateCache:function(av){this.offset=this.helper.offset();
if(this._isNumber(av.left)){this.position.left=av.left
}if(this._isNumber(av.top)){this.position.top=av.top
}if(this._isNumber(av.height)){this.size.height=av.height
}if(this._isNumber(av.width)){this.size.width=av.width
}},_updateRatio:function(ax){var ay=this.position,aw=this.size,av=this.axis;
if(this._isNumber(ax.height)){ax.width=(ax.height*this.aspectRatio)
}else{if(this._isNumber(ax.width)){ax.height=(ax.width/this.aspectRatio)
}}if(av==="sw"){ax.left=ay.left+(aw.width-ax.width);
ax.top=null
}if(av==="nw"){ax.top=ay.top+(aw.height-ax.height);
ax.left=ay.left+(aw.width-ax.width)
}return ax
},_respectSize:function(aA){var ax=this._vBoundaries,aD=this.axis,aF=this._isNumber(aA.width)&&ax.maxWidth&&(ax.maxWidth<aA.width),aB=this._isNumber(aA.height)&&ax.maxHeight&&(ax.maxHeight<aA.height),ay=this._isNumber(aA.width)&&ax.minWidth&&(ax.minWidth>aA.width),aE=this._isNumber(aA.height)&&ax.minHeight&&(ax.minHeight>aA.height),aw=this.originalPosition.left+this.originalSize.width,aC=this.originalPosition.top+this.originalSize.height,az=/sw|nw|w/.test(aD),av=/nw|ne|n/.test(aD);
if(ay){aA.width=ax.minWidth
}if(aE){aA.height=ax.minHeight
}if(aF){aA.width=ax.maxWidth
}if(aB){aA.height=ax.maxHeight
}if(ay&&az){aA.left=aw-ax.minWidth
}if(aF&&az){aA.left=aw-ax.maxWidth
}if(aE&&av){aA.top=aC-ax.minHeight
}if(aB&&av){aA.top=aC-ax.maxHeight
}if(!aA.width&&!aA.height&&!aA.left&&aA.top){aA.top=null
}else{if(!aA.width&&!aA.height&&!aA.top&&aA.left){aA.left=null
}}return aA
},_getPaddingPlusBorderDimensions:function(ax){var aw=0,ay=[],az=[ax.css("borderTopWidth"),ax.css("borderRightWidth"),ax.css("borderBottomWidth"),ax.css("borderLeftWidth")],av=[ax.css("paddingTop"),ax.css("paddingRight"),ax.css("paddingBottom"),ax.css("paddingLeft")];
for(;
aw<4;
aw++){ay[aw]=(parseFloat(az[aw])||0);
ay[aw]+=(parseFloat(av[aw])||0)
}return{height:ay[0]+ay[2],width:ay[1]+ay[3]}
},_proportionallyResize:function(){if(!this._proportionallyResizeElements.length){return
}var ax,aw=0,av=this.helper||this.element;
for(;
aw<this._proportionallyResizeElements.length;
aw++){ax=this._proportionallyResizeElements[aw];
if(!this.outerDimensions){this.outerDimensions=this._getPaddingPlusBorderDimensions(ax)
}ax.css({height:(av.height()-this.outerDimensions.height)||0,width:(av.width()-this.outerDimensions.width)||0})
}},_renderProxy:function(){var av=this.element,aw=this.options;
this.elementOffset=av.offset();
if(this._helper){this.helper=this.helper||ak("<div style='overflow:hidden;'></div>");
this._addClass(this.helper,this._helper);
this.helper.css({width:this.element.outerWidth(),height:this.element.outerHeight(),position:"absolute",left:this.elementOffset.left+"px",top:this.elementOffset.top+"px",zIndex:++aw.zIndex});
this.helper.appendTo("body").disableSelection()
}else{this.helper=this.element
}},_change:{e:function(aw,av){return{width:this.originalSize.width+av}
},w:function(ax,av){var aw=this.originalSize,ay=this.originalPosition;
return{left:ay.left+av,width:aw.width-av}
},n:function(ay,aw,av){var ax=this.originalSize,az=this.originalPosition;
return{top:az.top+av,height:ax.height-av}
},s:function(ax,aw,av){return{height:this.originalSize.height+av}
},se:function(ax,aw,av){return ak.extend(this._change.s.apply(this,arguments),this._change.e.apply(this,[ax,aw,av]))
},sw:function(ax,aw,av){return ak.extend(this._change.s.apply(this,arguments),this._change.w.apply(this,[ax,aw,av]))
},ne:function(ax,aw,av){return ak.extend(this._change.n.apply(this,arguments),this._change.e.apply(this,[ax,aw,av]))
},nw:function(ax,aw,av){return ak.extend(this._change.n.apply(this,arguments),this._change.w.apply(this,[ax,aw,av]))
}},_propagate:function(aw,av){ak.ui.plugin.call(this,aw,[av,this.ui()]);
(aw!=="resize"&&this._trigger(aw,av,this.ui()))
},plugins:{},ui:function(){return{originalElement:this.originalElement,element:this.element,helper:this.helper,position:this.position,size:this.size,originalSize:this.originalSize,originalPosition:this.originalPosition}
}});
ak.ui.plugin.add("resizable","animate",{stop:function(ay){var aD=ak(this).resizable("instance"),aA=aD.options,ax=aD._proportionallyResizeElements,av=ax.length&&(/textarea/i).test(ax[0].nodeName),aw=av&&aD._hasScroll(ax[0],"left")?0:aD.sizeDiff.height,aC=av?0:aD.sizeDiff.width,az={width:(aD.size.width-aC),height:(aD.size.height-aw)},aB=(parseFloat(aD.element.css("left"))+(aD.position.left-aD.originalPosition.left))||null,aE=(parseFloat(aD.element.css("top"))+(aD.position.top-aD.originalPosition.top))||null;
aD.element.animate(ak.extend(az,aE&&aB?{top:aE,left:aB}:{}),{duration:aA.animateDuration,easing:aA.animateEasing,step:function(){var aF={width:parseFloat(aD.element.css("width")),height:parseFloat(aD.element.css("height")),top:parseFloat(aD.element.css("top")),left:parseFloat(aD.element.css("left"))};
if(ax&&ax.length){ak(ax[0]).css({width:aF.width,height:aF.height})
}aD._updateCache(aF);
aD._propagate("resize",ay)
}})
}});
ak.ui.plugin.add("resizable","containment",{start:function(){var aD,ax,aF,av,aC,ay,aG,aE=ak(this).resizable("instance"),aB=aE.options,aA=aE.element,aw=aB.containment,az=(aw instanceof ak)?aw.get(0):(/parent/.test(aw))?aA.parent().get(0):aw;
if(!az){return
}aE.containerElement=ak(az);
if(/document/.test(aw)||aw===document){aE.containerOffset={left:0,top:0};
aE.containerPosition={left:0,top:0};
aE.parentData={element:ak(document),left:0,top:0,width:ak(document).width(),height:ak(document).height()||document.body.parentNode.scrollHeight}
}else{aD=ak(az);
ax=[];
ak(["Top","Right","Left","Bottom"]).each(function(aI,aH){ax[aI]=aE._num(aD.css("padding"+aH))
});
aE.containerOffset=aD.offset();
aE.containerPosition=aD.position();
aE.containerSize={height:(aD.innerHeight()-ax[3]),width:(aD.innerWidth()-ax[1])};
aF=aE.containerOffset;
av=aE.containerSize.height;
aC=aE.containerSize.width;
ay=(aE._hasScroll(az,"left")?az.scrollWidth:aC);
aG=(aE._hasScroll(az)?az.scrollHeight:av);
aE.parentData={element:az,left:aF.left,top:aF.top,width:ay,height:aG}
}},resize:function(aw){var aC,aH,aB,az,aD=ak(this).resizable("instance"),ay=aD.options,aF=aD.containerOffset,aE=aD.position,aG=aD._aspectRatio||aw.shiftKey,av={top:0,left:0},ax=aD.containerElement,aA=true;
if(ax[0]!==document&&(/static/).test(ax.css("position"))){av=aF
}if(aE.left<(aD._helper?aF.left:0)){aD.size.width=aD.size.width+(aD._helper?(aD.position.left-aF.left):(aD.position.left-av.left));
if(aG){aD.size.height=aD.size.width/aD.aspectRatio;
aA=false
}aD.position.left=ay.helper?aF.left:0
}if(aE.top<(aD._helper?aF.top:0)){aD.size.height=aD.size.height+(aD._helper?(aD.position.top-aF.top):aD.position.top);
if(aG){aD.size.width=aD.size.height*aD.aspectRatio;
aA=false
}aD.position.top=aD._helper?aF.top:0
}aB=aD.containerElement.get(0)===aD.element.parent().get(0);
az=/relative|absolute/.test(aD.containerElement.css("position"));
if(aB&&az){aD.offset.left=aD.parentData.left+aD.position.left;
aD.offset.top=aD.parentData.top+aD.position.top
}else{aD.offset.left=aD.element.offset().left;
aD.offset.top=aD.element.offset().top
}aC=Math.abs(aD.sizeDiff.width+(aD._helper?aD.offset.left-av.left:(aD.offset.left-aF.left)));
aH=Math.abs(aD.sizeDiff.height+(aD._helper?aD.offset.top-av.top:(aD.offset.top-aF.top)));
if(aC+aD.size.width>=aD.parentData.width){aD.size.width=aD.parentData.width-aC;
if(aG){aD.size.height=aD.size.width/aD.aspectRatio;
aA=false
}}if(aH+aD.size.height>=aD.parentData.height){aD.size.height=aD.parentData.height-aH;
if(aG){aD.size.width=aD.size.height*aD.aspectRatio;
aA=false
}}if(!aA){aD.position.left=aD.prevPosition.left;
aD.position.top=aD.prevPosition.top;
aD.size.width=aD.prevSize.width;
aD.size.height=aD.prevSize.height
}},stop:function(){var aA=ak(this).resizable("instance"),aw=aA.options,aB=aA.containerOffset,av=aA.containerPosition,ax=aA.containerElement,ay=ak(aA.helper),aD=ay.offset(),aC=ay.outerWidth()-aA.sizeDiff.width,az=ay.outerHeight()-aA.sizeDiff.height;
if(aA._helper&&!aw.animate&&(/relative/).test(ax.css("position"))){ak(this).css({left:aD.left-av.left-aB.left,width:aC,height:az})
}if(aA._helper&&!aw.animate&&(/static/).test(ax.css("position"))){ak(this).css({left:aD.left-av.left-aB.left,width:aC,height:az})
}}});
ak.ui.plugin.add("resizable","alsoResize",{start:function(){var av=ak(this).resizable("instance"),aw=av.options;
ak(aw.alsoResize).each(function(){var ax=ak(this);
ax.data("ui-resizable-alsoresize",{width:parseFloat(ax.width()),height:parseFloat(ax.height()),left:parseFloat(ax.css("left")),top:parseFloat(ax.css("top"))})
})
},resize:function(aw,ay){var av=ak(this).resizable("instance"),az=av.options,ax=av.originalSize,aB=av.originalPosition,aA={height:(av.size.height-ax.height)||0,width:(av.size.width-ax.width)||0,top:(av.position.top-aB.top)||0,left:(av.position.left-aB.left)||0};
ak(az.alsoResize).each(function(){var aE=ak(this),aF=ak(this).data("ui-resizable-alsoresize"),aD={},aC=aE.parents(ay.originalElement[0]).length?["width","height"]:["width","height","top","left"];
ak.each(aC,function(aG,aI){var aH=(aF[aI]||0)+(aA[aI]||0);
if(aH&&aH>=0){aD[aI]=aH||null
}});
aE.css(aD)
})
},stop:function(){ak(this).removeData("ui-resizable-alsoresize")
}});
ak.ui.plugin.add("resizable","ghost",{start:function(){var aw=ak(this).resizable("instance"),av=aw.size;
aw.ghost=aw.originalElement.clone();
aw.ghost.css({opacity:0.25,display:"block",position:"relative",height:av.height,width:av.width,margin:0,left:0,top:0});
aw._addClass(aw.ghost,"ui-resizable-ghost");
if(ak.uiBackCompat!==false&&typeof aw.options.ghost==="string"){aw.ghost.addClass(this.options.ghost)
}aw.ghost.appendTo(aw.helper)
},resize:function(){var av=ak(this).resizable("instance");
if(av.ghost){av.ghost.css({position:"relative",height:av.size.height,width:av.size.width})
}},stop:function(){var av=ak(this).resizable("instance");
if(av.ghost&&av.helper){av.helper.get(0).removeChild(av.ghost.get(0))
}}});
ak.ui.plugin.add("resizable","grid",{resize:function(){var ay,aD=ak(this).resizable("instance"),aH=aD.options,aB=aD.size,aC=aD.originalSize,aE=aD.originalPosition,aM=aD.axis,av=typeof aH.grid==="number"?[aH.grid,aH.grid]:aH.grid,aK=(av[0]||1),aJ=(av[1]||1),aA=Math.round((aB.width-aC.width)/aK)*aK,az=Math.round((aB.height-aC.height)/aJ)*aJ,aF=aC.width+aA,aI=aC.height+az,ax=aH.maxWidth&&(aH.maxWidth<aF),aG=aH.maxHeight&&(aH.maxHeight<aI),aL=aH.minWidth&&(aH.minWidth>aF),aw=aH.minHeight&&(aH.minHeight>aI);
aH.grid=av;
if(aL){aF+=aK
}if(aw){aI+=aJ
}if(ax){aF-=aK
}if(aG){aI-=aJ
}if(/^(se|s|e)$/.test(aM)){aD.size.width=aF;
aD.size.height=aI
}else{if(/^(ne)$/.test(aM)){aD.size.width=aF;
aD.size.height=aI;
aD.position.top=aE.top-az
}else{if(/^(sw)$/.test(aM)){aD.size.width=aF;
aD.size.height=aI;
aD.position.left=aE.left-aA
}else{if(aI-aJ<=0||aF-aK<=0){ay=aD._getPaddingPlusBorderDimensions(this)
}if(aI-aJ>0){aD.size.height=aI;
aD.position.top=aE.top-az
}else{aI=aJ-ay.height;
aD.size.height=aI;
aD.position.top=aE.top+aC.height-aI
}if(aF-aK>0){aD.size.width=aF;
aD.position.left=aE.left-aA
}else{aF=aK-ay.width;
aD.size.width=aF;
aD.position.left=aE.left+aC.width-aF
}}}}}});
var B=ak.ui.resizable;
/*!
 * jQuery UI Dialog 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.dialog",{version:"1.12.1",options:{appendTo:"body",autoOpen:true,buttons:[],classes:{"ui-dialog":"ui-corner-all","ui-dialog-titlebar":"ui-corner-all"},closeOnEscape:true,closeText:"Close",draggable:true,hide:null,height:"auto",maxHeight:null,maxWidth:null,minHeight:150,minWidth:150,modal:false,position:{my:"center",at:"center",of:window,collision:"fit",using:function(aw){var av=ak(this).css(aw).offset().top;
if(av<0){ak(this).css("top",aw.top-av)
}}},resizable:true,show:null,title:null,width:300,beforeClose:null,close:null,drag:null,dragStart:null,dragStop:null,focus:null,open:null,resize:null,resizeStart:null,resizeStop:null},sizeRelatedOptions:{buttons:true,height:true,maxHeight:true,maxWidth:true,minHeight:true,minWidth:true,width:true},resizableRelatedOptions:{maxHeight:true,maxWidth:true,minHeight:true,minWidth:true},_create:function(){this.originalCss={display:this.element[0].style.display,width:this.element[0].style.width,minHeight:this.element[0].style.minHeight,maxHeight:this.element[0].style.maxHeight,height:this.element[0].style.height};
this.originalPosition={parent:this.element.parent(),index:this.element.parent().children().index(this.element)};
this.originalTitle=this.element.attr("title");
if(this.options.title==null&&this.originalTitle!=null){this.options.title=this.originalTitle
}if(this.options.disabled){this.options.disabled=false
}this._createWrapper();
this.element.show().removeAttr("title").appendTo(this.uiDialog);
this._addClass("ui-dialog-content","ui-widget-content");
this._createTitlebar();
this._createButtonPane();
if(this.options.draggable&&ak.fn.draggable){this._makeDraggable()
}if(this.options.resizable&&ak.fn.resizable){this._makeResizable()
}this._isOpen=false;
this._trackFocus()
},_init:function(){if(this.options.autoOpen){this.open()
}},_appendTo:function(){var av=this.options.appendTo;
if(av&&(av.jquery||av.nodeType)){return ak(av)
}return this.document.find(av||"body").eq(0)
},_destroy:function(){var aw,av=this.originalPosition;
this._untrackInstance();
this._destroyOverlay();
this.element.removeUniqueId().css(this.originalCss).detach();
this.uiDialog.remove();
if(this.originalTitle){this.element.attr("title",this.originalTitle)
}aw=av.parent.children().eq(av.index);
if(aw.length&&aw[0]!==this.element[0]){aw.before(this.element)
}else{av.parent.append(this.element)
}},widget:function(){return this.uiDialog
},disable:ak.noop,enable:ak.noop,close:function(aw){var av=this;
if(!this._isOpen||this._trigger("beforeClose",aw)===false){return
}this._isOpen=false;
this._focusedElement=null;
this._destroyOverlay();
this._untrackInstance();
if(!this.opener.filter(":focusable").trigger("focus").length){ak.ui.safeBlur(ak.ui.safeActiveElement(this.document[0]))
}this._hide(this.uiDialog,this.options.hide,function(){av._trigger("close",aw)
})
},isOpen:function(){return this._isOpen
},moveToTop:function(){this._moveToTop()
},_moveToTop:function(az,av){var ay=false,ax=this.uiDialog.siblings(".ui-front:visible").map(function(){return +ak(this).css("z-index")
}).get(),aw=Math.max.apply(null,ax);
if(aw>=+this.uiDialog.css("z-index")){this.uiDialog.css("z-index",aw+1);
ay=true
}if(ay&&!av){this._trigger("focus",az)
}return ay
},open:function(){var av=this;
if(this._isOpen){if(this._moveToTop()){this._focusTabbable()
}return
}this._isOpen=true;
this.opener=ak(ak.ui.safeActiveElement(this.document[0]));
this._size();
this._position();
this._createOverlay();
this._moveToTop(null,true);
if(this.overlay){this.overlay.css("z-index",this.uiDialog.css("z-index")-1)
}this._show(this.uiDialog,this.options.show,function(){av._focusTabbable();
av._trigger("focus")
});
this._makeFocusTarget();
this._trigger("open")
},_focusTabbable:function(){var av=this._focusedElement;
if(!av){av=this.element.find("[autofocus]")
}if(!av.length){av=this.element.find(":tabbable")
}if(!av.length){av=this.uiDialogButtonPane.find(":tabbable")
}if(!av.length){av=this.uiDialogTitlebarClose.filter(":tabbable")
}if(!av.length){av=this.uiDialog
}av.eq(0).trigger("focus")
},_keepFocus:function(av){function aw(){var ay=ak.ui.safeActiveElement(this.document[0]),ax=this.uiDialog[0]===ay||ak.contains(this.uiDialog[0],ay);
if(!ax){this._focusTabbable()
}}av.preventDefault();
aw.call(this);
this._delay(aw)
},_createWrapper:function(){this.uiDialog=ak("<div>").hide().attr({tabIndex:-1,role:"dialog"}).appendTo(this._appendTo());
this._addClass(this.uiDialog,"ui-dialog","ui-widget ui-widget-content ui-front");
this._on(this.uiDialog,{keydown:function(ax){if(this.options.closeOnEscape&&!ax.isDefaultPrevented()&&ax.keyCode&&ax.keyCode===ak.ui.keyCode.ESCAPE){ax.preventDefault();
this.close(ax);
return
}if(ax.keyCode!==ak.ui.keyCode.TAB||ax.isDefaultPrevented()){return
}var aw=this.uiDialog.find(":tabbable"),ay=aw.filter(":first"),av=aw.filter(":last");
if((ax.target===av[0]||ax.target===this.uiDialog[0])&&!ax.shiftKey){this._delay(function(){ay.trigger("focus")
});
ax.preventDefault()
}else{if((ax.target===ay[0]||ax.target===this.uiDialog[0])&&ax.shiftKey){this._delay(function(){av.trigger("focus")
});
ax.preventDefault()
}}},mousedown:function(av){if(this._moveToTop(av)){this._focusTabbable()
}}});
if(!this.element.find("[aria-describedby]").length){this.uiDialog.attr({"aria-describedby":this.element.uniqueId().attr("id")})
}},_createTitlebar:function(){var av;
this.uiDialogTitlebar=ak("<div>");
this._addClass(this.uiDialogTitlebar,"ui-dialog-titlebar","ui-widget-header ui-helper-clearfix");
this._on(this.uiDialogTitlebar,{mousedown:function(aw){if(!ak(aw.target).closest(".ui-dialog-titlebar-close")){this.uiDialog.trigger("focus")
}}});
this.uiDialogTitlebarClose=ak("<button type='button'></button>").button({label:ak("<a>").text(this.options.closeText).html(),icon:"ui-icon-closethick",showLabel:false}).appendTo(this.uiDialogTitlebar);
this._addClass(this.uiDialogTitlebarClose,"ui-dialog-titlebar-close");
this._on(this.uiDialogTitlebarClose,{click:function(aw){aw.preventDefault();
this.close(aw)
}});
av=ak("<span>").uniqueId().prependTo(this.uiDialogTitlebar);
this._addClass(av,"ui-dialog-title");
this._title(av);
this.uiDialogTitlebar.prependTo(this.uiDialog);
this.uiDialog.attr({"aria-labelledby":av.attr("id")})
},_title:function(av){if(this.options.title){av.text(this.options.title)
}else{av.html("&#160;")
}},_createButtonPane:function(){this.uiDialogButtonPane=ak("<div>");
this._addClass(this.uiDialogButtonPane,"ui-dialog-buttonpane","ui-widget-content ui-helper-clearfix");
this.uiButtonSet=ak("<div>").appendTo(this.uiDialogButtonPane);
this._addClass(this.uiButtonSet,"ui-dialog-buttonset");
this._createButtons()
},_createButtons:function(){var aw=this,av=this.options.buttons;
this.uiDialogButtonPane.remove();
this.uiButtonSet.empty();
if(ak.isEmptyObject(av)||(ak.isArray(av)&&!av.length)){this._removeClass(this.uiDialog,"ui-dialog-buttons");
return
}ak.each(av,function(ax,ay){var az,aA;
ay=ak.isFunction(ay)?{click:ay,text:ax}:ay;
ay=ak.extend({type:"button"},ay);
az=ay.click;
aA={icon:ay.icon,iconPosition:ay.iconPosition,showLabel:ay.showLabel,icons:ay.icons,text:ay.text};
delete ay.click;
delete ay.icon;
delete ay.iconPosition;
delete ay.showLabel;
delete ay.icons;
if(typeof ay.text==="boolean"){delete ay.text
}ak("<button></button>",ay).button(aA).appendTo(aw.uiButtonSet).on("click",function(){az.apply(aw.element[0],arguments)
})
});
this._addClass(this.uiDialog,"ui-dialog-buttons");
this.uiDialogButtonPane.appendTo(this.uiDialog)
},_makeDraggable:function(){var ax=this,aw=this.options;
function av(ay){return{position:ay.position,offset:ay.offset}
}this.uiDialog.draggable({cancel:".ui-dialog-content, .ui-dialog-titlebar-close",handle:".ui-dialog-titlebar",containment:"document",start:function(ay,az){ax._addClass(ak(this),"ui-dialog-dragging");
ax._blockFrames();
ax._trigger("dragStart",ay,av(az))
},drag:function(ay,az){ax._trigger("drag",ay,av(az))
},stop:function(ay,az){var aB=az.offset.left-ax.document.scrollLeft(),aA=az.offset.top-ax.document.scrollTop();
aw.position={my:"left top",at:"left"+(aB>=0?"+":"")+aB+" top"+(aA>=0?"+":"")+aA,of:ax.window};
ax._removeClass(ak(this),"ui-dialog-dragging");
ax._unblockFrames();
ax._trigger("dragStop",ay,av(az))
}})
},_makeResizable:function(){var aA=this,ay=this.options,az=ay.resizable,av=this.uiDialog.css("position"),ax=typeof az==="string"?az:"n,e,s,w,se,sw,ne,nw";
function aw(aB){return{originalPosition:aB.originalPosition,originalSize:aB.originalSize,position:aB.position,size:aB.size}
}this.uiDialog.resizable({cancel:".ui-dialog-content",containment:"document",alsoResize:this.element,maxWidth:ay.maxWidth,maxHeight:ay.maxHeight,minWidth:ay.minWidth,minHeight:this._minHeight(),handles:ax,start:function(aB,aC){aA._addClass(ak(this),"ui-dialog-resizing");
aA._blockFrames();
aA._trigger("resizeStart",aB,aw(aC))
},resize:function(aB,aC){aA._trigger("resize",aB,aw(aC))
},stop:function(aB,aC){var aF=aA.uiDialog.offset(),aE=aF.left-aA.document.scrollLeft(),aD=aF.top-aA.document.scrollTop();
ay.height=aA.uiDialog.height();
ay.width=aA.uiDialog.width();
ay.position={my:"left top",at:"left"+(aE>=0?"+":"")+aE+" top"+(aD>=0?"+":"")+aD,of:aA.window};
aA._removeClass(ak(this),"ui-dialog-resizing");
aA._unblockFrames();
aA._trigger("resizeStop",aB,aw(aC))
}}).css("position",av)
},_trackFocus:function(){this._on(this.widget(),{focusin:function(av){this._makeFocusTarget();
this._focusedElement=ak(av.target)
}})
},_makeFocusTarget:function(){this._untrackInstance();
this._trackingInstances().unshift(this)
},_untrackInstance:function(){var aw=this._trackingInstances(),av=ak.inArray(this,aw);
if(av!==-1){aw.splice(av,1)
}},_trackingInstances:function(){var av=this.document.data("ui-dialog-instances");
if(!av){av=[];
this.document.data("ui-dialog-instances",av)
}return av
},_minHeight:function(){var av=this.options;
return av.height==="auto"?av.minHeight:Math.min(av.minHeight,av.height)
},_position:function(){var av=this.uiDialog.is(":visible");
if(!av){this.uiDialog.show()
}this.uiDialog.position(this.options.position);
if(!av){this.uiDialog.hide()
}},_setOptions:function(ax){var ay=this,aw=false,av={};
ak.each(ax,function(az,aA){ay._setOption(az,aA);
if(az in ay.sizeRelatedOptions){aw=true
}if(az in ay.resizableRelatedOptions){av[az]=aA
}});
if(aw){this._size();
this._position()
}if(this.uiDialog.is(":data(ui-resizable)")){this.uiDialog.resizable("option",av)
}},_setOption:function(ax,ay){var aw,az,av=this.uiDialog;
if(ax==="disabled"){return
}this._super(ax,ay);
if(ax==="appendTo"){this.uiDialog.appendTo(this._appendTo())
}if(ax==="buttons"){this._createButtons()
}if(ax==="closeText"){this.uiDialogTitlebarClose.button({label:ak("<a>").text(""+this.options.closeText).html()})
}if(ax==="draggable"){aw=av.is(":data(ui-draggable)");
if(aw&&!ay){av.draggable("destroy")
}if(!aw&&ay){this._makeDraggable()
}}if(ax==="position"){this._position()
}if(ax==="resizable"){az=av.is(":data(ui-resizable)");
if(az&&!ay){av.resizable("destroy")
}if(az&&typeof ay==="string"){av.resizable("option","handles",ay)
}if(!az&&ay!==false){this._makeResizable()
}}if(ax==="title"){this._title(this.uiDialogTitlebar.find(".ui-dialog-title"))
}},_size:function(){var av,ax,ay,aw=this.options;
this.element.show().css({width:"auto",minHeight:0,maxHeight:"none",height:0});
if(aw.minWidth>aw.width){aw.width=aw.minWidth
}av=this.uiDialog.css({height:"auto",width:aw.width}).outerHeight();
ax=Math.max(0,aw.minHeight-av);
ay=typeof aw.maxHeight==="number"?Math.max(0,aw.maxHeight-av):"none";
if(aw.height==="auto"){this.element.css({minHeight:ax,maxHeight:ay,height:"auto"})
}else{this.element.height(Math.max(0,aw.height-av))
}if(this.uiDialog.is(":data(ui-resizable)")){this.uiDialog.resizable("option","minHeight",this._minHeight())
}},_blockFrames:function(){this.iframeBlocks=this.document.find("iframe").map(function(){var av=ak(this);
return ak("<div>").css({position:"absolute",width:av.outerWidth(),height:av.outerHeight()}).appendTo(av.parent()).offset(av.offset())[0]
})
},_unblockFrames:function(){if(this.iframeBlocks){this.iframeBlocks.remove();
delete this.iframeBlocks
}},_allowInteraction:function(av){if(ak(av.target).closest(".ui-dialog").length){return true
}return !!ak(av.target).closest(".ui-datepicker").length
},_createOverlay:function(){if(!this.options.modal){return
}var av=true;
this._delay(function(){av=false
});
if(!this.document.data("ui-dialog-overlays")){this._on(this.document,{focusin:function(aw){if(av){return
}if(!this._allowInteraction(aw)){aw.preventDefault();
this._trackingInstances()[0]._focusTabbable()
}}})
}this.overlay=ak("<div>").appendTo(this._appendTo());
this._addClass(this.overlay,null,"ui-widget-overlay ui-front");
this._on(this.overlay,{mousedown:"_keepFocus"});
this.document.data("ui-dialog-overlays",(this.document.data("ui-dialog-overlays")||0)+1)
},_destroyOverlay:function(){if(!this.options.modal){return
}if(this.overlay){var av=this.document.data("ui-dialog-overlays")-1;
if(!av){this._off(this.document,"focusin");
this.document.removeData("ui-dialog-overlays")
}else{this.document.data("ui-dialog-overlays",av)
}this.overlay.remove();
this.overlay=null
}}});
if(ak.uiBackCompat!==false){ak.widget("ui.dialog",ak.ui.dialog,{options:{dialogClass:""},_createWrapper:function(){this._super();
this.uiDialog.addClass(this.options.dialogClass)
},_setOption:function(av,aw){if(av==="dialogClass"){this.uiDialog.removeClass(this.options.dialogClass).addClass(aw)
}this._superApply(arguments)
}})
}var ac=ak.ui.dialog;
/*!
 * jQuery UI Droppable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.droppable",{version:"1.12.1",widgetEventPrefix:"drop",options:{accept:"*",addClasses:true,greedy:false,scope:"default",tolerance:"intersect",activate:null,deactivate:null,drop:null,out:null,over:null},_create:function(){var aw,ax=this.options,av=ax.accept;
this.isover=false;
this.isout=true;
this.accept=ak.isFunction(av)?av:function(ay){return ay.is(av)
};
this.proportions=function(){if(arguments.length){aw=arguments[0]
}else{return aw?aw:aw={width:this.element[0].offsetWidth,height:this.element[0].offsetHeight}
}};
this._addToManager(ax.scope);
ax.addClasses&&this._addClass("ui-droppable")
},_addToManager:function(av){ak.ui.ddmanager.droppables[av]=ak.ui.ddmanager.droppables[av]||[];
ak.ui.ddmanager.droppables[av].push(this)
},_splice:function(av){var aw=0;
for(;
aw<av.length;
aw++){if(av[aw]===this){av.splice(aw,1)
}}},_destroy:function(){var av=ak.ui.ddmanager.droppables[this.options.scope];
this._splice(av)
},_setOption:function(aw,ax){if(aw==="accept"){this.accept=ak.isFunction(ax)?ax:function(ay){return ay.is(ax)
}
}else{if(aw==="scope"){var av=ak.ui.ddmanager.droppables[this.options.scope];
this._splice(av);
this._addToManager(ax)
}}this._super(aw,ax)
},_activate:function(aw){var av=ak.ui.ddmanager.current;
this._addActiveClass();
if(av){this._trigger("activate",aw,this.ui(av))
}},_deactivate:function(aw){var av=ak.ui.ddmanager.current;
this._removeActiveClass();
if(av){this._trigger("deactivate",aw,this.ui(av))
}},_over:function(aw){var av=ak.ui.ddmanager.current;
if(!av||(av.currentItem||av.element)[0]===this.element[0]){return
}if(this.accept.call(this.element[0],(av.currentItem||av.element))){this._addHoverClass();
this._trigger("over",aw,this.ui(av))
}},_out:function(aw){var av=ak.ui.ddmanager.current;
if(!av||(av.currentItem||av.element)[0]===this.element[0]){return
}if(this.accept.call(this.element[0],(av.currentItem||av.element))){this._removeHoverClass();
this._trigger("out",aw,this.ui(av))
}},_drop:function(aw,ax){var av=ax||ak.ui.ddmanager.current,ay=false;
if(!av||(av.currentItem||av.element)[0]===this.element[0]){return false
}this.element.find(":data(ui-droppable)").not(".ui-draggable-dragging").each(function(){var az=ak(this).droppable("instance");
if(az.options.greedy&&!az.options.disabled&&az.options.scope===av.options.scope&&az.accept.call(az.element[0],(av.currentItem||av.element))&&s(av,ak.extend(az,{offset:az.element.offset()}),az.options.tolerance,aw)){ay=true;
return false
}});
if(ay){return false
}if(this.accept.call(this.element[0],(av.currentItem||av.element))){this._removeActiveClass();
this._removeHoverClass();
this._trigger("drop",aw,this.ui(av));
return this.element
}return false
},ui:function(av){return{draggable:(av.currentItem||av.element),helper:av.helper,position:av.position,offset:av.positionAbs}
},_addHoverClass:function(){this._addClass("ui-droppable-hover")
},_removeHoverClass:function(){this._removeClass("ui-droppable-hover")
},_addActiveClass:function(){this._addClass("ui-droppable-active")
},_removeActiveClass:function(){this._removeClass("ui-droppable-active")
}});
var s=ak.ui.intersect=(function(){function av(ax,aw,ay){return(ax>=aw)&&(ax<(aw+ay))
}return function(aH,aB,aF,ax){if(!aB.offset){return false
}var az=(aH.positionAbs||aH.position.absolute).left+aH.margins.left,aE=(aH.positionAbs||aH.position.absolute).top+aH.margins.top,ay=az+aH.helperProportions.width,aD=aE+aH.helperProportions.height,aA=aB.offset.left,aG=aB.offset.top,aw=aA+aB.proportions().width,aC=aG+aB.proportions().height;
switch(aF){case"fit":return(aA<=az&&ay<=aw&&aG<=aE&&aD<=aC);
case"intersect":return(aA<az+(aH.helperProportions.width/2)&&ay-(aH.helperProportions.width/2)<aw&&aG<aE+(aH.helperProportions.height/2)&&aD-(aH.helperProportions.height/2)<aC);
case"pointer":return av(ax.pageY,aG,aB.proportions().height)&&av(ax.pageX,aA,aB.proportions().width);
case"touch":return((aE>=aG&&aE<=aC)||(aD>=aG&&aD<=aC)||(aE<aG&&aD>aC))&&((az>=aA&&az<=aw)||(ay>=aA&&ay<=aw)||(az<aA&&ay>aw));
default:return false
}}
})();
ak.ui.ddmanager={current:null,droppables:{"default":[]},prepareOffsets:function(ay,aA){var ax,aw,av=ak.ui.ddmanager.droppables[ay.options.scope]||[],az=aA?aA.type:null,aB=(ay.currentItem||ay.element).find(":data(ui-droppable)").addBack();
droppablesLoop:for(ax=0;
ax<av.length;
ax++){if(av[ax].options.disabled||(ay&&!av[ax].accept.call(av[ax].element[0],(ay.currentItem||ay.element)))){continue
}for(aw=0;
aw<aB.length;
aw++){if(aB[aw]===av[ax].element[0]){av[ax].proportions().height=0;
continue droppablesLoop
}}av[ax].visible=av[ax].element.css("display")!=="none";
if(!av[ax].visible){continue
}if(az==="mousedown"){av[ax]._activate.call(av[ax],aA)
}av[ax].offset=av[ax].element.offset();
av[ax].proportions({width:av[ax].element[0].offsetWidth,height:av[ax].element[0].offsetHeight})
}},drop:function(av,aw){var ax=false;
ak.each((ak.ui.ddmanager.droppables[av.options.scope]||[]).slice(),function(){if(!this.options){return
}if(!this.options.disabled&&this.visible&&s(av,this,this.options.tolerance,aw)){ax=this._drop.call(this,aw)||ax
}if(!this.options.disabled&&this.visible&&this.accept.call(this.element[0],(av.currentItem||av.element))){this.isout=true;
this.isover=false;
this._deactivate.call(this,aw)
}});
return ax
},dragStart:function(av,aw){av.element.parentsUntil("body").on("scroll.droppable",function(){if(!av.options.refreshPositions){ak.ui.ddmanager.prepareOffsets(av,aw)
}})
},drag:function(av,aw){if(av.options.refreshPositions){ak.ui.ddmanager.prepareOffsets(av,aw)
}ak.each(ak.ui.ddmanager.droppables[av.options.scope]||[],function(){if(this.options.disabled||this.greedyChild||!this.visible){return
}var aA,ay,ax,az=s(av,this,this.options.tolerance,aw),aB=!az&&this.isover?"isout":(az&&!this.isover?"isover":null);
if(!aB){return
}if(this.options.greedy){ay=this.options.scope;
ax=this.element.parents(":data(ui-droppable)").filter(function(){return ak(this).droppable("instance").options.scope===ay
});
if(ax.length){aA=ak(ax[0]).droppable("instance");
aA.greedyChild=(aB==="isover")
}}if(aA&&aB==="isover"){aA.isover=false;
aA.isout=true;
aA._out.call(aA,aw)
}this[aB]=true;
this[aB==="isout"?"isover":"isout"]=false;
this[aB==="isover"?"_over":"_out"].call(this,aw);
if(aA&&aB==="isout"){aA.isout=false;
aA.isover=true;
aA._over.call(aA,aw)
}})
},dragStop:function(av,aw){av.element.parentsUntil("body").off("scroll.droppable");
if(!av.options.refreshPositions){ak.ui.ddmanager.prepareOffsets(av,aw)
}}};
if(ak.uiBackCompat!==false){ak.widget("ui.droppable",ak.ui.droppable,{options:{hoverClass:false,activeClass:false},_addActiveClass:function(){this._super();
if(this.options.activeClass){this.element.addClass(this.options.activeClass)
}},_removeActiveClass:function(){this._super();
if(this.options.activeClass){this.element.removeClass(this.options.activeClass)
}},_addHoverClass:function(){this._super();
if(this.options.hoverClass){this.element.addClass(this.options.hoverClass)
}},_removeHoverClass:function(){this._super();
if(this.options.hoverClass){this.element.removeClass(this.options.hoverClass)
}}})
}var W=ak.ui.droppable;
/*!
 * jQuery UI Progressbar 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var Y=ak.widget("ui.progressbar",{version:"1.12.1",options:{classes:{"ui-progressbar":"ui-corner-all","ui-progressbar-value":"ui-corner-left","ui-progressbar-complete":"ui-corner-right"},max:100,value:0,change:null,complete:null},min:0,_create:function(){this.oldValue=this.options.value=this._constrainedValue();
this.element.attr({role:"progressbar","aria-valuemin":this.min});
this._addClass("ui-progressbar","ui-widget ui-widget-content");
this.valueDiv=ak("<div>").appendTo(this.element);
this._addClass(this.valueDiv,"ui-progressbar-value","ui-widget-header");
this._refreshValue()
},_destroy:function(){this.element.removeAttr("role aria-valuemin aria-valuemax aria-valuenow");
this.valueDiv.remove()
},value:function(av){if(av===undefined){return this.options.value
}this.options.value=this._constrainedValue(av);
this._refreshValue()
},_constrainedValue:function(av){if(av===undefined){av=this.options.value
}this.indeterminate=av===false;
if(typeof av!=="number"){av=0
}return this.indeterminate?false:Math.min(this.options.max,Math.max(this.min,av))
},_setOptions:function(av){var aw=av.value;
delete av.value;
this._super(av);
this.options.value=this._constrainedValue(aw);
this._refreshValue()
},_setOption:function(av,aw){if(av==="max"){aw=Math.max(this.min,aw)
}this._super(av,aw)
},_setOptionDisabled:function(av){this._super(av);
this.element.attr("aria-disabled",av);
this._toggleClass(null,"ui-state-disabled",!!av)
},_percentage:function(){return this.indeterminate?100:100*(this.options.value-this.min)/(this.options.max-this.min)
},_refreshValue:function(){var aw=this.options.value,av=this._percentage();
this.valueDiv.toggle(this.indeterminate||aw>this.min).width(av.toFixed(0)+"%");
this._toggleClass(this.valueDiv,"ui-progressbar-complete",null,aw===this.options.max)._toggleClass("ui-progressbar-indeterminate",null,this.indeterminate);
if(this.indeterminate){this.element.removeAttr("aria-valuenow");
if(!this.overlayDiv){this.overlayDiv=ak("<div>").appendTo(this.valueDiv);
this._addClass(this.overlayDiv,"ui-progressbar-overlay")
}}else{this.element.attr({"aria-valuemax":this.options.max,"aria-valuenow":aw});
if(this.overlayDiv){this.overlayDiv.remove();
this.overlayDiv=null
}}if(this.oldValue!==aw){this.oldValue=aw;
this._trigger("change")
}if(aw===this.options.max){this._trigger("complete")
}}});
/*!
 * jQuery UI Selectable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var r=ak.widget("ui.selectable",ak.ui.mouse,{version:"1.12.1",options:{appendTo:"body",autoRefresh:true,distance:0,filter:"*",tolerance:"touch",selected:null,selecting:null,start:null,stop:null,unselected:null,unselecting:null},_create:function(){var av=this;
this._addClass("ui-selectable");
this.dragged=false;
this.refresh=function(){av.elementPos=ak(av.element[0]).offset();
av.selectees=ak(av.options.filter,av.element[0]);
av._addClass(av.selectees,"ui-selectee");
av.selectees.each(function(){var ax=ak(this),aw=ax.offset(),ay={left:aw.left-av.elementPos.left,top:aw.top-av.elementPos.top};
ak.data(this,"selectable-item",{element:this,$element:ax,left:ay.left,top:ay.top,right:ay.left+ax.outerWidth(),bottom:ay.top+ax.outerHeight(),startselected:false,selected:ax.hasClass("ui-selected"),selecting:ax.hasClass("ui-selecting"),unselecting:ax.hasClass("ui-unselecting")})
})
};
this.refresh();
this._mouseInit();
this.helper=ak("<div>");
this._addClass(this.helper,"ui-selectable-helper")
},_destroy:function(){this.selectees.removeData("selectable-item");
this._mouseDestroy()
},_mouseStart:function(ax){var aw=this,av=this.options;
this.opos=[ax.pageX,ax.pageY];
this.elementPos=ak(this.element[0]).offset();
if(this.options.disabled){return
}this.selectees=ak(av.filter,this.element[0]);
this._trigger("start",ax);
ak(av.appendTo).append(this.helper);
this.helper.css({left:ax.pageX,top:ax.pageY,width:0,height:0});
if(av.autoRefresh){this.refresh()
}this.selectees.filter(".ui-selected").each(function(){var ay=ak.data(this,"selectable-item");
ay.startselected=true;
if(!ax.metaKey&&!ax.ctrlKey){aw._removeClass(ay.$element,"ui-selected");
ay.selected=false;
aw._addClass(ay.$element,"ui-unselecting");
ay.unselecting=true;
aw._trigger("unselecting",ax,{unselecting:ay.element})
}});
ak(ax.target).parents().addBack().each(function(){var ay,az=ak.data(this,"selectable-item");
if(az){ay=(!ax.metaKey&&!ax.ctrlKey)||!az.$element.hasClass("ui-selected");
aw._removeClass(az.$element,ay?"ui-unselecting":"ui-selected")._addClass(az.$element,ay?"ui-selecting":"ui-unselecting");
az.unselecting=!ay;
az.selecting=ay;
az.selected=ay;
if(ay){aw._trigger("selecting",ax,{selecting:az.element})
}else{aw._trigger("unselecting",ax,{unselecting:az.element})
}return false
}})
},_mouseDrag:function(aC){this.dragged=true;
if(this.options.disabled){return
}var az,aB=this,ax=this.options,aw=this.opos[0],aA=this.opos[1],av=aC.pageX,ay=aC.pageY;
if(aw>av){az=av;
av=aw;
aw=az
}if(aA>ay){az=ay;
ay=aA;
aA=az
}this.helper.css({left:aw,top:aA,width:av-aw,height:ay-aA});
this.selectees.each(function(){var aD=ak.data(this,"selectable-item"),aE=false,aF={};
if(!aD||aD.element===aB.element[0]){return
}aF.left=aD.left+aB.elementPos.left;
aF.right=aD.right+aB.elementPos.left;
aF.top=aD.top+aB.elementPos.top;
aF.bottom=aD.bottom+aB.elementPos.top;
if(ax.tolerance==="touch"){aE=(!(aF.left>av||aF.right<aw||aF.top>ay||aF.bottom<aA))
}else{if(ax.tolerance==="fit"){aE=(aF.left>aw&&aF.right<av&&aF.top>aA&&aF.bottom<ay)
}}if(aE){if(aD.selected){aB._removeClass(aD.$element,"ui-selected");
aD.selected=false
}if(aD.unselecting){aB._removeClass(aD.$element,"ui-unselecting");
aD.unselecting=false
}if(!aD.selecting){aB._addClass(aD.$element,"ui-selecting");
aD.selecting=true;
aB._trigger("selecting",aC,{selecting:aD.element})
}}else{if(aD.selecting){if((aC.metaKey||aC.ctrlKey)&&aD.startselected){aB._removeClass(aD.$element,"ui-selecting");
aD.selecting=false;
aB._addClass(aD.$element,"ui-selected");
aD.selected=true
}else{aB._removeClass(aD.$element,"ui-selecting");
aD.selecting=false;
if(aD.startselected){aB._addClass(aD.$element,"ui-unselecting");
aD.unselecting=true
}aB._trigger("unselecting",aC,{unselecting:aD.element})
}}if(aD.selected){if(!aC.metaKey&&!aC.ctrlKey&&!aD.startselected){aB._removeClass(aD.$element,"ui-selected");
aD.selected=false;
aB._addClass(aD.$element,"ui-unselecting");
aD.unselecting=true;
aB._trigger("unselecting",aC,{unselecting:aD.element})
}}}});
return false
},_mouseStop:function(aw){var av=this;
this.dragged=false;
ak(".ui-unselecting",this.element[0]).each(function(){var ax=ak.data(this,"selectable-item");
av._removeClass(ax.$element,"ui-unselecting");
ax.unselecting=false;
ax.startselected=false;
av._trigger("unselected",aw,{unselected:ax.element})
});
ak(".ui-selecting",this.element[0]).each(function(){var ax=ak.data(this,"selectable-item");
av._removeClass(ax.$element,"ui-selecting")._addClass(ax.$element,"ui-selected");
ax.selecting=false;
ax.selected=true;
ax.startselected=true;
av._trigger("selected",aw,{selected:ax.element})
});
this._trigger("stop",aw);
this.helper.remove();
return false
}});
/*!
 * jQuery UI Selectmenu 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var e=ak.widget("ui.selectmenu",[ak.ui.formResetMixin,{version:"1.12.1",defaultElement:"<select>",options:{appendTo:null,classes:{"ui-selectmenu-button-open":"ui-corner-top","ui-selectmenu-button-closed":"ui-corner-all"},disabled:null,icons:{button:"ui-icon-triangle-1-s"},position:{my:"left top",at:"left bottom",collision:"none"},width:false,change:null,close:null,focus:null,open:null,select:null},_create:function(){var av=this.element.uniqueId().attr("id");
this.ids={element:av,button:av+"-button",menu:av+"-menu"};
this._drawButton();
this._drawMenu();
this._bindFormResetHandler();
this._rendered=false;
this.menuItems=ak()
},_drawButton:function(){var av,ax=this,aw=this._parseOption(this.element.find("option:selected"),this.element[0].selectedIndex);
this.labels=this.element.labels().attr("for",this.ids.button);
this._on(this.labels,{click:function(ay){this.button.focus();
ay.preventDefault()
}});
this.element.hide();
this.button=ak("<span>",{tabindex:this.options.disabled?-1:0,id:this.ids.button,role:"combobox","aria-expanded":"false","aria-autocomplete":"list","aria-owns":this.ids.menu,"aria-haspopup":"true",title:this.element.attr("title")}).insertAfter(this.element);
this._addClass(this.button,"ui-selectmenu-button ui-selectmenu-button-closed","ui-button ui-widget");
av=ak("<span>").appendTo(this.button);
this._addClass(av,"ui-selectmenu-icon","ui-icon "+this.options.icons.button);
this.buttonItem=this._renderButtonItem(aw).appendTo(this.button);
if(this.options.width!==false){this._resizeButton()
}this._on(this.button,this._buttonEvents);
this.button.one("focusin",function(){if(!ax._rendered){ax._refreshMenu()
}})
},_drawMenu:function(){var av=this;
this.menu=ak("<ul>",{"aria-hidden":"true","aria-labelledby":this.ids.button,id:this.ids.menu});
this.menuWrap=ak("<div>").append(this.menu);
this._addClass(this.menuWrap,"ui-selectmenu-menu","ui-front");
this.menuWrap.appendTo(this._appendTo());
this.menuInstance=this.menu.menu({classes:{"ui-menu":"ui-corner-bottom"},role:"listbox",select:function(aw,ax){aw.preventDefault();
av._setSelection();
av._select(ax.item.data("ui-selectmenu-item"),aw)
},focus:function(ax,ay){var aw=ay.item.data("ui-selectmenu-item");
if(av.focusIndex!=null&&aw.index!==av.focusIndex){av._trigger("focus",ax,{item:aw});
if(!av.isOpen){av._select(aw,ax)
}}av.focusIndex=aw.index;
av.button.attr("aria-activedescendant",av.menuItems.eq(aw.index).attr("id"))
}}).menu("instance");
this.menuInstance._off(this.menu,"mouseleave");
this.menuInstance._closeOnDocumentClick=function(){return false
};
this.menuInstance._isDivider=function(){return false
}
},refresh:function(){this._refreshMenu();
this.buttonItem.replaceWith(this.buttonItem=this._renderButtonItem(this._getSelectedItem().data("ui-selectmenu-item")||{}));
if(this.options.width===null){this._resizeButton()
}},_refreshMenu:function(){var aw,av=this.element.find("option");
this.menu.empty();
this._parseOptions(av);
this._renderMenu(this.menu,this.items);
this.menuInstance.refresh();
this.menuItems=this.menu.find("li").not(".ui-selectmenu-optgroup").find(".ui-menu-item-wrapper");
this._rendered=true;
if(!av.length){return
}aw=this._getSelectedItem();
this.menuInstance.focus(null,aw);
this._setAria(aw.data("ui-selectmenu-item"));
this._setOption("disabled",this.element.prop("disabled"))
},open:function(av){if(this.options.disabled){return
}if(!this._rendered){this._refreshMenu()
}else{this._removeClass(this.menu.find(".ui-state-active"),null,"ui-state-active");
this.menuInstance.focus(null,this._getSelectedItem())
}if(!this.menuItems.length){return
}this.isOpen=true;
this._toggleAttr();
this._resizeMenu();
this._position();
this._on(this.document,this._documentClick);
this._trigger("open",av)
},_position:function(){this.menuWrap.position(ak.extend({of:this.button},this.options.position))
},close:function(av){if(!this.isOpen){return
}this.isOpen=false;
this._toggleAttr();
this.range=null;
this._off(this.document);
this._trigger("close",av)
},widget:function(){return this.button
},menuWidget:function(){return this.menu
},_renderButtonItem:function(aw){var av=ak("<span>");
this._setText(av,aw.label);
this._addClass(av,"ui-selectmenu-text");
return av
},_renderMenu:function(ax,aw){var ay=this,av="";
ak.each(aw,function(aA,aB){var az;
if(aB.optgroup!==av){az=ak("<li>",{text:aB.optgroup});
ay._addClass(az,"ui-selectmenu-optgroup","ui-menu-divider"+(aB.element.parent("optgroup").prop("disabled")?" ui-state-disabled":""));
az.appendTo(ax);
av=aB.optgroup
}ay._renderItemData(ax,aB)
})
},_renderItemData:function(av,aw){return this._renderItem(av,aw).data("ui-selectmenu-item",aw)
},_renderItem:function(aw,ax){var av=ak("<li>"),ay=ak("<div>",{title:ax.element.attr("title")});
if(ax.disabled){this._addClass(av,null,"ui-state-disabled")
}this._setText(ay,ax.label);
return av.append(ay).appendTo(aw)
},_setText:function(av,aw){if(aw){av.text(aw)
}else{av.html("&#160;")
}},_move:function(az,ay){var ax,aw,av=".ui-menu-item";
if(this.isOpen){ax=this.menuItems.eq(this.focusIndex).parent("li")
}else{ax=this.menuItems.eq(this.element[0].selectedIndex).parent("li");
av+=":not(.ui-state-disabled)"
}if(az==="first"||az==="last"){aw=ax[az==="first"?"prevAll":"nextAll"](av).eq(-1)
}else{aw=ax[az+"All"](av).eq(0)
}if(aw.length){this.menuInstance.focus(ay,aw)
}},_getSelectedItem:function(){return this.menuItems.eq(this.element[0].selectedIndex).parent("li")
},_toggle:function(av){this[this.isOpen?"close":"open"](av)
},_setSelection:function(){var av;
if(!this.range){return
}if(window.getSelection){av=window.getSelection();
av.removeAllRanges();
av.addRange(this.range)
}else{this.range.select()
}this.button.focus()
},_documentClick:{mousedown:function(av){if(!this.isOpen){return
}if(!ak(av.target).closest(".ui-selectmenu-menu, #"+ak.ui.escapeSelector(this.ids.button)).length){this.close(av)
}}},_buttonEvents:{mousedown:function(){var av;
if(window.getSelection){av=window.getSelection();
if(av.rangeCount){this.range=av.getRangeAt(0)
}}else{this.range=document.selection.createRange()
}},click:function(av){this._setSelection();
this._toggle(av)
},keydown:function(aw){var av=true;
switch(aw.keyCode){case ak.ui.keyCode.TAB:case ak.ui.keyCode.ESCAPE:this.close(aw);
av=false;
break;
case ak.ui.keyCode.ENTER:if(this.isOpen){this._selectFocusedItem(aw)
}break;
case ak.ui.keyCode.UP:if(aw.altKey){this._toggle(aw)
}else{this._move("prev",aw)
}break;
case ak.ui.keyCode.DOWN:if(aw.altKey){this._toggle(aw)
}else{this._move("next",aw)
}break;
case ak.ui.keyCode.SPACE:if(this.isOpen){this._selectFocusedItem(aw)
}else{this._toggle(aw)
}break;
case ak.ui.keyCode.LEFT:this._move("prev",aw);
break;
case ak.ui.keyCode.RIGHT:this._move("next",aw);
break;
case ak.ui.keyCode.HOME:case ak.ui.keyCode.PAGE_UP:this._move("first",aw);
break;
case ak.ui.keyCode.END:case ak.ui.keyCode.PAGE_DOWN:this._move("last",aw);
break;
default:this.menu.trigger(aw);
av=false
}if(av){aw.preventDefault()
}}},_selectFocusedItem:function(aw){var av=this.menuItems.eq(this.focusIndex).parent("li");
if(!av.hasClass("ui-state-disabled")){this._select(av.data("ui-selectmenu-item"),aw)
}},_select:function(aw,av){var ax=this.element[0].selectedIndex;
this.element[0].selectedIndex=aw.index;
this.buttonItem.replaceWith(this.buttonItem=this._renderButtonItem(aw));
this._setAria(aw);
this._trigger("select",av,{item:aw});
if(aw.index!==ax){this._trigger("change",av,{item:aw})
}this.close(av)
},_setAria:function(av){var aw=this.menuItems.eq(av.index).attr("id");
this.button.attr({"aria-labelledby":aw,"aria-activedescendant":aw});
this.menu.attr("aria-activedescendant",aw)
},_setOption:function(av,ax){if(av==="icons"){var aw=this.button.find("span.ui-icon");
this._removeClass(aw,null,this.options.icons.button)._addClass(aw,null,ax.button)
}this._super(av,ax);
if(av==="appendTo"){this.menuWrap.appendTo(this._appendTo())
}if(av==="width"){this._resizeButton()
}},_setOptionDisabled:function(av){this._super(av);
this.menuInstance.option("disabled",av);
this.button.attr("aria-disabled",av);
this._toggleClass(this.button,null,"ui-state-disabled",av);
this.element.prop("disabled",av);
if(av){this.button.attr("tabindex",-1);
this.close()
}else{this.button.attr("tabindex",0)
}},_appendTo:function(){var av=this.options.appendTo;
if(av){av=av.jquery||av.nodeType?ak(av):this.document.find(av).eq(0)
}if(!av||!av[0]){av=this.element.closest(".ui-front, dialog")
}if(!av.length){av=this.document[0].body
}return av
},_toggleAttr:function(){this.button.attr("aria-expanded",this.isOpen);
this._removeClass(this.button,"ui-selectmenu-button-"+(this.isOpen?"closed":"open"))._addClass(this.button,"ui-selectmenu-button-"+(this.isOpen?"open":"closed"))._toggleClass(this.menuWrap,"ui-selectmenu-open",null,this.isOpen);
this.menu.attr("aria-hidden",!this.isOpen)
},_resizeButton:function(){var av=this.options.width;
if(av===false){this.button.css("width","");
return
}if(av===null){av=this.element.show().outerWidth();
this.element.hide()
}this.button.outerWidth(av)
},_resizeMenu:function(){this.menu.outerWidth(Math.max(this.button.outerWidth(),this.menu.width("").outerWidth()+1))
},_getCreateOptions:function(){var av=this._super();
av.disabled=this.element.prop("disabled");
return av
},_parseOptions:function(av){var aw=this,ax=[];
av.each(function(ay,az){ax.push(aw._parseOption(ak(az),ay))
});
this.items=ax
},_parseOption:function(ax,aw){var av=ax.parent("optgroup");
return{element:ax,index:aw,value:ax.val(),label:ax.text(),optgroup:av.attr("label")||"",disabled:av.prop("disabled")||ax.prop("disabled")}
},_destroy:function(){this._unbindFormResetHandler();
this.menuWrap.remove();
this.button.remove();
this.element.show();
this.element.removeUniqueId();
this.labels.attr("for",this.ids.element)
}}]);
/*!
 * jQuery UI Slider 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var Q=ak.widget("ui.slider",ak.ui.mouse,{version:"1.12.1",widgetEventPrefix:"slide",options:{animate:false,classes:{"ui-slider":"ui-corner-all","ui-slider-handle":"ui-corner-all","ui-slider-range":"ui-corner-all ui-widget-header"},distance:0,max:100,min:0,orientation:"horizontal",range:false,step:1,value:0,values:null,change:null,slide:null,start:null,stop:null},numPages:5,_create:function(){this._keySliding=false;
this._mouseSliding=false;
this._animateOff=true;
this._handleIndex=null;
this._detectOrientation();
this._mouseInit();
this._calculateNewMax();
this._addClass("ui-slider ui-slider-"+this.orientation,"ui-widget ui-widget-content");
this._refresh();
this._animateOff=false
},_refresh:function(){this._createRange();
this._createHandles();
this._setupEvents();
this._refreshValue()
},_createHandles:function(){var ay,av,aw=this.options,aA=this.element.find(".ui-slider-handle"),az="<span tabindex='0'></span>",ax=[];
av=(aw.values&&aw.values.length)||1;
if(aA.length>av){aA.slice(av).remove();
aA=aA.slice(0,av)
}for(ay=aA.length;
ay<av;
ay++){ax.push(az)
}this.handles=aA.add(ak(ax.join("")).appendTo(this.element));
this._addClass(this.handles,"ui-slider-handle","ui-state-default");
this.handle=this.handles.eq(0);
this.handles.each(function(aB){ak(this).data("ui-slider-handle-index",aB).attr("tabIndex",0)
})
},_createRange:function(){var av=this.options;
if(av.range){if(av.range===true){if(!av.values){av.values=[this._valueMin(),this._valueMin()]
}else{if(av.values.length&&av.values.length!==2){av.values=[av.values[0],av.values[0]]
}else{if(ak.isArray(av.values)){av.values=av.values.slice(0)
}}}}if(!this.range||!this.range.length){this.range=ak("<div>").appendTo(this.element);
this._addClass(this.range,"ui-slider-range")
}else{this._removeClass(this.range,"ui-slider-range-min ui-slider-range-max");
this.range.css({left:"",bottom:""})
}if(av.range==="min"||av.range==="max"){this._addClass(this.range,"ui-slider-range-"+av.range)
}}else{if(this.range){this.range.remove()
}this.range=null
}},_setupEvents:function(){this._off(this.handles);
this._on(this.handles,this._handleEvents);
this._hoverable(this.handles);
this._focusable(this.handles)
},_destroy:function(){this.handles.remove();
if(this.range){this.range.remove()
}this._mouseDestroy()
},_mouseCapture:function(ax){var aB,aE,aw,az,aD,aF,aA,av,aC=this,ay=this.options;
if(ay.disabled){return false
}this.elementSize={width:this.element.outerWidth(),height:this.element.outerHeight()};
this.elementOffset=this.element.offset();
aB={x:ax.pageX,y:ax.pageY};
aE=this._normValueFromMouse(aB);
aw=this._valueMax()-this._valueMin()+1;
this.handles.each(function(aG){var aH=Math.abs(aE-aC.values(aG));
if((aw>aH)||(aw===aH&&(aG===aC._lastChangedValue||aC.values(aG)===ay.min))){aw=aH;
az=ak(this);
aD=aG
}});
aF=this._start(ax,aD);
if(aF===false){return false
}this._mouseSliding=true;
this._handleIndex=aD;
this._addClass(az,null,"ui-state-active");
az.trigger("focus");
aA=az.offset();
av=!ak(ax.target).parents().addBack().is(".ui-slider-handle");
this._clickOffset=av?{left:0,top:0}:{left:ax.pageX-aA.left-(az.width()/2),top:ax.pageY-aA.top-(az.height()/2)-(parseInt(az.css("borderTopWidth"),10)||0)-(parseInt(az.css("borderBottomWidth"),10)||0)+(parseInt(az.css("marginTop"),10)||0)};
if(!this.handles.hasClass("ui-state-hover")){this._slide(ax,aD,aE)
}this._animateOff=true;
return true
},_mouseStart:function(){return true
},_mouseDrag:function(ax){var av={x:ax.pageX,y:ax.pageY},aw=this._normValueFromMouse(av);
this._slide(ax,this._handleIndex,aw);
return false
},_mouseStop:function(av){this._removeClass(this.handles,null,"ui-state-active");
this._mouseSliding=false;
this._stop(av,this._handleIndex);
this._change(av,this._handleIndex);
this._handleIndex=null;
this._clickOffset=null;
this._animateOff=false;
return false
},_detectOrientation:function(){this.orientation=(this.options.orientation==="vertical")?"vertical":"horizontal"
},_normValueFromMouse:function(aw){var av,az,ay,ax,aA;
if(this.orientation==="horizontal"){av=this.elementSize.width;
az=aw.x-this.elementOffset.left-(this._clickOffset?this._clickOffset.left:0)
}else{av=this.elementSize.height;
az=aw.y-this.elementOffset.top-(this._clickOffset?this._clickOffset.top:0)
}ay=(az/av);
if(ay>1){ay=1
}if(ay<0){ay=0
}if(this.orientation==="vertical"){ay=1-ay
}ax=this._valueMax()-this._valueMin();
aA=this._valueMin()+ay*ax;
return this._trimAlignValue(aA)
},_uiHash:function(ax,ay,av){var aw={handle:this.handles[ax],handleIndex:ax,value:ay!==undefined?ay:this.value()};
if(this._hasMultipleValues()){aw.value=ay!==undefined?ay:this.values(ax);
aw.values=av||this.values()
}return aw
},_hasMultipleValues:function(){return this.options.values&&this.options.values.length
},_start:function(aw,av){return this._trigger("start",aw,this._uiHash(av))
},_slide:function(aA,ay,ax){var aB,av,az=this.value(),aw=this.values();
if(this._hasMultipleValues()){av=this.values(ay?0:1);
az=this.values(ay);
if(this.options.values.length===2&&this.options.range===true){ax=ay===0?Math.min(av,ax):Math.max(av,ax)
}aw[ay]=ax
}if(ax===az){return
}aB=this._trigger("slide",aA,this._uiHash(ay,ax,aw));
if(aB===false){return
}if(this._hasMultipleValues()){this.values(ay,ax)
}else{this.value(ax)
}},_stop:function(aw,av){this._trigger("stop",aw,this._uiHash(av))
},_change:function(aw,av){if(!this._keySliding&&!this._mouseSliding){this._lastChangedValue=av;
this._trigger("change",aw,this._uiHash(av))
}},value:function(av){if(arguments.length){this.options.value=this._trimAlignValue(av);
this._refreshValue();
this._change(null,0);
return
}return this._value()
},values:function(aw,az){var ay,av,ax;
if(arguments.length>1){this.options.values[aw]=this._trimAlignValue(az);
this._refreshValue();
this._change(null,aw);
return
}if(arguments.length){if(ak.isArray(arguments[0])){ay=this.options.values;
av=arguments[0];
for(ax=0;
ax<ay.length;
ax+=1){ay[ax]=this._trimAlignValue(av[ax]);
this._change(null,ax)
}this._refreshValue()
}else{if(this._hasMultipleValues()){return this._values(aw)
}else{return this.value()
}}}else{return this._values()
}},_setOption:function(aw,ax){var av,ay=0;
if(aw==="range"&&this.options.range===true){if(ax==="min"){this.options.value=this._values(0);
this.options.values=null
}else{if(ax==="max"){this.options.value=this._values(this.options.values.length-1);
this.options.values=null
}}}if(ak.isArray(this.options.values)){ay=this.options.values.length
}this._super(aw,ax);
switch(aw){case"orientation":this._detectOrientation();
this._removeClass("ui-slider-horizontal ui-slider-vertical")._addClass("ui-slider-"+this.orientation);
this._refreshValue();
if(this.options.range){this._refreshRange(ax)
}this.handles.css(ax==="horizontal"?"bottom":"left","");
break;
case"value":this._animateOff=true;
this._refreshValue();
this._change(null,0);
this._animateOff=false;
break;
case"values":this._animateOff=true;
this._refreshValue();
for(av=ay-1;
av>=0;
av--){this._change(null,av)
}this._animateOff=false;
break;
case"step":case"min":case"max":this._animateOff=true;
this._calculateNewMax();
this._refreshValue();
this._animateOff=false;
break;
case"range":this._animateOff=true;
this._refresh();
this._animateOff=false;
break
}},_setOptionDisabled:function(av){this._super(av);
this._toggleClass(null,"ui-state-disabled",!!av)
},_value:function(){var av=this.options.value;
av=this._trimAlignValue(av);
return av
},_values:function(av){var ay,ax,aw;
if(arguments.length){ay=this.options.values[av];
ay=this._trimAlignValue(ay);
return ay
}else{if(this._hasMultipleValues()){ax=this.options.values.slice();
for(aw=0;
aw<ax.length;
aw+=1){ax[aw]=this._trimAlignValue(ax[aw])
}return ax
}else{return[]
}}},_trimAlignValue:function(ay){if(ay<=this._valueMin()){return this._valueMin()
}if(ay>=this._valueMax()){return this._valueMax()
}var av=(this.options.step>0)?this.options.step:1,ax=(ay-this._valueMin())%av,aw=ay-ax;
if(Math.abs(ax)*2>=av){aw+=(ax>0)?av:(-av)
}return parseFloat(aw.toFixed(5))
},_calculateNewMax:function(){var av=this.options.max,aw=this._valueMin(),ax=this.options.step,ay=Math.round((av-aw)/ax)*ax;
av=ay+aw;
if(av>this.options.max){av-=ax
}this.max=parseFloat(av.toFixed(this._precision()))
},_precision:function(){var av=this._precisionOf(this.options.step);
if(this.options.min!==null){av=Math.max(av,this._precisionOf(this.options.min))
}return av
},_precisionOf:function(aw){var ax=aw.toString(),av=ax.indexOf(".");
return av===-1?0:ax.length-av-1
},_valueMin:function(){return this.options.min
},_valueMax:function(){return this.max
},_refreshRange:function(av){if(av==="vertical"){this.range.css({width:"",left:""})
}if(av==="horizontal"){this.range.css({height:"",bottom:""})
}},_refreshValue:function(){var aA,az,aD,aB,aE,ay=this.options.range,ax=this.options,aC=this,aw=(!this._animateOff)?ax.animate:false,av={};
if(this._hasMultipleValues()){this.handles.each(function(aF){az=(aC.values(aF)-aC._valueMin())/(aC._valueMax()-aC._valueMin())*100;
av[aC.orientation==="horizontal"?"left":"bottom"]=az+"%";
ak(this).stop(1,1)[aw?"animate":"css"](av,ax.animate);
if(aC.options.range===true){if(aC.orientation==="horizontal"){if(aF===0){aC.range.stop(1,1)[aw?"animate":"css"]({left:az+"%"},ax.animate)
}if(aF===1){aC.range[aw?"animate":"css"]({width:(az-aA)+"%"},{queue:false,duration:ax.animate})
}}else{if(aF===0){aC.range.stop(1,1)[aw?"animate":"css"]({bottom:(az)+"%"},ax.animate)
}if(aF===1){aC.range[aw?"animate":"css"]({height:(az-aA)+"%"},{queue:false,duration:ax.animate})
}}}aA=az
})
}else{aD=this.value();
aB=this._valueMin();
aE=this._valueMax();
az=(aE!==aB)?(aD-aB)/(aE-aB)*100:0;
av[this.orientation==="horizontal"?"left":"bottom"]=az+"%";
this.handle.stop(1,1)[aw?"animate":"css"](av,ax.animate);
if(ay==="min"&&this.orientation==="horizontal"){this.range.stop(1,1)[aw?"animate":"css"]({width:az+"%"},ax.animate)
}if(ay==="max"&&this.orientation==="horizontal"){this.range.stop(1,1)[aw?"animate":"css"]({width:(100-az)+"%"},ax.animate)
}if(ay==="min"&&this.orientation==="vertical"){this.range.stop(1,1)[aw?"animate":"css"]({height:az+"%"},ax.animate)
}if(ay==="max"&&this.orientation==="vertical"){this.range.stop(1,1)[aw?"animate":"css"]({height:(100-az)+"%"},ax.animate)
}}},_handleEvents:{keydown:function(az){var aA,ax,aw,ay,av=ak(az.target).data("ui-slider-handle-index");
switch(az.keyCode){case ak.ui.keyCode.HOME:case ak.ui.keyCode.END:case ak.ui.keyCode.PAGE_UP:case ak.ui.keyCode.PAGE_DOWN:case ak.ui.keyCode.UP:case ak.ui.keyCode.RIGHT:case ak.ui.keyCode.DOWN:case ak.ui.keyCode.LEFT:az.preventDefault();
if(!this._keySliding){this._keySliding=true;
this._addClass(ak(az.target),null,"ui-state-active");
aA=this._start(az,av);
if(aA===false){return
}}break
}ay=this.options.step;
if(this._hasMultipleValues()){ax=aw=this.values(av)
}else{ax=aw=this.value()
}switch(az.keyCode){case ak.ui.keyCode.HOME:aw=this._valueMin();
break;
case ak.ui.keyCode.END:aw=this._valueMax();
break;
case ak.ui.keyCode.PAGE_UP:aw=this._trimAlignValue(ax+((this._valueMax()-this._valueMin())/this.numPages));
break;
case ak.ui.keyCode.PAGE_DOWN:aw=this._trimAlignValue(ax-((this._valueMax()-this._valueMin())/this.numPages));
break;
case ak.ui.keyCode.UP:case ak.ui.keyCode.RIGHT:if(ax===this._valueMax()){return
}aw=this._trimAlignValue(ax+ay);
break;
case ak.ui.keyCode.DOWN:case ak.ui.keyCode.LEFT:if(ax===this._valueMin()){return
}aw=this._trimAlignValue(ax-ay);
break
}this._slide(az,av,aw)
},keyup:function(aw){var av=ak(aw.target).data("ui-slider-handle-index");
if(this._keySliding){this._keySliding=false;
this._stop(aw,av);
this._change(aw,av);
this._removeClass(ak(aw.target),null,"ui-state-active")
}}}});
/*!
 * jQuery UI Sortable 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
var T=ak.widget("ui.sortable",ak.ui.mouse,{version:"1.12.1",widgetEventPrefix:"sort",ready:false,options:{appendTo:"parent",axis:false,connectWith:false,containment:false,cursor:"auto",cursorAt:false,dropOnEmpty:true,forcePlaceholderSize:false,forceHelperSize:false,grid:false,handle:false,helper:"original",items:"> *",opacity:false,placeholder:false,revert:false,scroll:true,scrollSensitivity:20,scrollSpeed:20,scope:"default",tolerance:"intersect",zIndex:1000,activate:null,beforeStop:null,change:null,deactivate:null,out:null,over:null,receive:null,remove:null,sort:null,start:null,stop:null,update:null},_isOverAxis:function(aw,av,ax){return(aw>=av)&&(aw<(av+ax))
},_isFloating:function(av){return(/left|right/).test(av.css("float"))||(/inline|table-cell/).test(av.css("display"))
},_create:function(){this.containerCache={};
this._addClass("ui-sortable");
this.refresh();
this.offset=this.element.offset();
this._mouseInit();
this._setHandleClassName();
this.ready=true
},_setOption:function(av,aw){this._super(av,aw);
if(av==="handle"){this._setHandleClassName()
}},_setHandleClassName:function(){var av=this;
this._removeClass(this.element.find(".ui-sortable-handle"),"ui-sortable-handle");
ak.each(this.items,function(){av._addClass(this.instance.options.handle?this.item.find(this.instance.options.handle):this.item,"ui-sortable-handle")
})
},_destroy:function(){this._mouseDestroy();
for(var av=this.items.length-1;
av>=0;
av--){this.items[av].item.removeData(this.widgetName+"-item")
}return this
},_mouseCapture:function(ax,ay){var av=null,az=false,aw=this;
if(this.reverting){return false
}if(this.options.disabled||this.options.type==="static"){return false
}this._refreshItems(ax);
ak(ax.target).parents().each(function(){if(ak.data(this,aw.widgetName+"-item")===aw){av=ak(this);
return false
}});
if(ak.data(ax.target,aw.widgetName+"-item")===aw){av=ak(ax.target)
}if(!av){return false
}if(this.options.handle&&!ay){ak(this.options.handle,av).find("*").addBack().each(function(){if(this===ax.target){az=true
}});
if(!az){return false
}}this.currentItem=av;
this._removeCurrentsFromItems();
return true
},_mouseStart:function(ay,az,aw){var ax,av,aA=this.options;
this.currentContainer=this;
this.refreshPositions();
this.helper=this._createHelper(ay);
this._cacheHelperProportions();
this._cacheMargins();
this.scrollParent=this.helper.scrollParent();
this.offset=this.currentItem.offset();
this.offset={top:this.offset.top-this.margins.top,left:this.offset.left-this.margins.left};
ak.extend(this.offset,{click:{left:ay.pageX-this.offset.left,top:ay.pageY-this.offset.top},parent:this._getParentOffset(),relative:this._getRelativeOffset()});
this.helper.css("position","absolute");
this.cssPosition=this.helper.css("position");
this.originalPosition=this._generatePosition(ay);
this.originalPageX=ay.pageX;
this.originalPageY=ay.pageY;
(aA.cursorAt&&this._adjustOffsetFromHelper(aA.cursorAt));
this.domPosition={prev:this.currentItem.prev()[0],parent:this.currentItem.parent()[0]};
if(this.helper[0]!==this.currentItem[0]){this.currentItem.hide()
}this._createPlaceholder();
if(aA.containment){this._setContainment()
}if(aA.cursor&&aA.cursor!=="auto"){av=this.document.find("body");
this.storedCursor=av.css("cursor");
av.css("cursor",aA.cursor);
this.storedStylesheet=ak("<style>*{ cursor: "+aA.cursor+" !important; }</style>").appendTo(av)
}if(aA.opacity){if(this.helper.css("opacity")){this._storedOpacity=this.helper.css("opacity")
}this.helper.css("opacity",aA.opacity)
}if(aA.zIndex){if(this.helper.css("zIndex")){this._storedZIndex=this.helper.css("zIndex")
}this.helper.css("zIndex",aA.zIndex)
}if(this.scrollParent[0]!==this.document[0]&&this.scrollParent[0].tagName!=="HTML"){this.overflowOffset=this.scrollParent.offset()
}this._trigger("start",ay,this._uiHash());
if(!this._preserveHelperProportions){this._cacheHelperProportions()
}if(!aw){for(ax=this.containers.length-1;
ax>=0;
ax--){this.containers[ax]._trigger("activate",ay,this._uiHash(this))
}}if(ak.ui.ddmanager){ak.ui.ddmanager.current=this
}if(ak.ui.ddmanager&&!aA.dropBehaviour){ak.ui.ddmanager.prepareOffsets(this,ay)
}this.dragging=true;
this._addClass(this.helper,"ui-sortable-helper");
this._mouseDrag(ay);
return true
},_mouseDrag:function(az){var ax,ay,aw,aB,aA=this.options,av=false;
this.position=this._generatePosition(az);
this.positionAbs=this._convertPositionTo("absolute");
if(!this.lastPositionAbs){this.lastPositionAbs=this.positionAbs
}if(this.options.scroll){if(this.scrollParent[0]!==this.document[0]&&this.scrollParent[0].tagName!=="HTML"){if((this.overflowOffset.top+this.scrollParent[0].offsetHeight)-az.pageY<aA.scrollSensitivity){this.scrollParent[0].scrollTop=av=this.scrollParent[0].scrollTop+aA.scrollSpeed
}else{if(az.pageY-this.overflowOffset.top<aA.scrollSensitivity){this.scrollParent[0].scrollTop=av=this.scrollParent[0].scrollTop-aA.scrollSpeed
}}if((this.overflowOffset.left+this.scrollParent[0].offsetWidth)-az.pageX<aA.scrollSensitivity){this.scrollParent[0].scrollLeft=av=this.scrollParent[0].scrollLeft+aA.scrollSpeed
}else{if(az.pageX-this.overflowOffset.left<aA.scrollSensitivity){this.scrollParent[0].scrollLeft=av=this.scrollParent[0].scrollLeft-aA.scrollSpeed
}}}else{if(az.pageY-this.document.scrollTop()<aA.scrollSensitivity){av=this.document.scrollTop(this.document.scrollTop()-aA.scrollSpeed)
}else{if(this.window.height()-(az.pageY-this.document.scrollTop())<aA.scrollSensitivity){av=this.document.scrollTop(this.document.scrollTop()+aA.scrollSpeed)
}}if(az.pageX-this.document.scrollLeft()<aA.scrollSensitivity){av=this.document.scrollLeft(this.document.scrollLeft()-aA.scrollSpeed)
}else{if(this.window.width()-(az.pageX-this.document.scrollLeft())<aA.scrollSensitivity){av=this.document.scrollLeft(this.document.scrollLeft()+aA.scrollSpeed)
}}}if(av!==false&&ak.ui.ddmanager&&!aA.dropBehaviour){ak.ui.ddmanager.prepareOffsets(this,az)
}}this.positionAbs=this._convertPositionTo("absolute");
if(!this.options.axis||this.options.axis!=="y"){this.helper[0].style.left=this.position.left+"px"
}if(!this.options.axis||this.options.axis!=="x"){this.helper[0].style.top=this.position.top+"px"
}for(ax=this.items.length-1;
ax>=0;
ax--){ay=this.items[ax];
aw=ay.item[0];
aB=this._intersectsWithPointer(ay);
if(!aB){continue
}if(ay.instance!==this.currentContainer){continue
}if(aw!==this.currentItem[0]&&this.placeholder[aB===1?"next":"prev"]()[0]!==aw&&!ak.contains(this.placeholder[0],aw)&&(this.options.type==="semi-dynamic"?!ak.contains(this.element[0],aw):true)){this.direction=aB===1?"down":"up";
if(this.options.tolerance==="pointer"||this._intersectsWithSides(ay)){this._rearrange(az,ay)
}else{break
}this._trigger("change",az,this._uiHash());
break
}}this._contactContainers(az);
if(ak.ui.ddmanager){ak.ui.ddmanager.drag(this,az)
}this._trigger("sort",az,this._uiHash());
this.lastPositionAbs=this.positionAbs;
return false
},_mouseStop:function(ax,az){if(!ax){return
}if(ak.ui.ddmanager&&!this.options.dropBehaviour){ak.ui.ddmanager.drop(this,ax)
}if(this.options.revert){var aw=this,aA=this.placeholder.offset(),av=this.options.axis,ay={};
if(!av||av==="x"){ay.left=aA.left-this.offset.parent.left-this.margins.left+(this.offsetParent[0]===this.document[0].body?0:this.offsetParent[0].scrollLeft)
}if(!av||av==="y"){ay.top=aA.top-this.offset.parent.top-this.margins.top+(this.offsetParent[0]===this.document[0].body?0:this.offsetParent[0].scrollTop)
}this.reverting=true;
ak(this.helper).animate(ay,parseInt(this.options.revert,10)||500,function(){aw._clear(ax)
})
}else{this._clear(ax,az)
}return false
},cancel:function(){if(this.dragging){this._mouseUp(new ak.Event("mouseup",{target:null}));
if(this.options.helper==="original"){this.currentItem.css(this._storedCSS);
this._removeClass(this.currentItem,"ui-sortable-helper")
}else{this.currentItem.show()
}for(var av=this.containers.length-1;
av>=0;
av--){this.containers[av]._trigger("deactivate",null,this._uiHash(this));
if(this.containers[av].containerCache.over){this.containers[av]._trigger("out",null,this._uiHash(this));
this.containers[av].containerCache.over=0
}}}if(this.placeholder){if(this.placeholder[0].parentNode){this.placeholder[0].parentNode.removeChild(this.placeholder[0])
}if(this.options.helper!=="original"&&this.helper&&this.helper[0].parentNode){this.helper.remove()
}ak.extend(this,{helper:null,dragging:false,reverting:false,_noFinalSort:null});
if(this.domPosition.prev){ak(this.domPosition.prev).after(this.currentItem)
}else{ak(this.domPosition.parent).prepend(this.currentItem)
}}return this
},serialize:function(ax){var av=this._getItemsAsjQuery(ax&&ax.connected),aw=[];
ax=ax||{};
ak(av).each(function(){var ay=(ak(ax.item||this).attr(ax.attribute||"id")||"").match(ax.expression||(/(.+)[\-=_](.+)/));
if(ay){aw.push((ax.key||ay[1]+"[]")+"="+(ax.key&&ax.expression?ay[1]:ay[2]))
}});
if(!aw.length&&ax.key){aw.push(ax.key+"=")
}return aw.join("&")
},toArray:function(ax){var av=this._getItemsAsjQuery(ax&&ax.connected),aw=[];
ax=ax||{};
av.each(function(){aw.push(ak(ax.item||this).attr(ax.attribute||"id")||"")
});
return aw
},_intersectsWith:function(aG){var ax=this.positionAbs.left,aw=ax+this.helperProportions.width,aE=this.positionAbs.top,aD=aE+this.helperProportions.height,ay=aG.left,av=ay+aG.width,aH=aG.top,aC=aH+aG.height,aI=this.offset.click.top,aB=this.offset.click.left,aA=(this.options.axis==="x")||((aE+aI)>aH&&(aE+aI)<aC),aF=(this.options.axis==="y")||((ax+aB)>ay&&(ax+aB)<av),az=aA&&aF;
if(this.options.tolerance==="pointer"||this.options.forcePointerForContainers||(this.options.tolerance!=="pointer"&&this.helperProportions[this.floating?"width":"height"]>aG[this.floating?"width":"height"])){return az
}else{return(ay<ax+(this.helperProportions.width/2)&&aw-(this.helperProportions.width/2)<av&&aH<aE+(this.helperProportions.height/2)&&aD-(this.helperProportions.height/2)<aC)
}},_intersectsWithPointer:function(ax){var aw,aA,ay=(this.options.axis==="x")||this._isOverAxis(this.positionAbs.top+this.offset.click.top,ax.top,ax.height),av=(this.options.axis==="y")||this._isOverAxis(this.positionAbs.left+this.offset.click.left,ax.left,ax.width),az=ay&&av;
if(!az){return false
}aw=this._getDragVerticalDirection();
aA=this._getDragHorizontalDirection();
return this.floating?((aA==="right"||aw==="down")?2:1):(aw&&(aw==="down"?2:1))
},_intersectsWithSides:function(ay){var aw=this._isOverAxis(this.positionAbs.top+this.offset.click.top,ay.top+(ay.height/2),ay.height),ax=this._isOverAxis(this.positionAbs.left+this.offset.click.left,ay.left+(ay.width/2),ay.width),av=this._getDragVerticalDirection(),az=this._getDragHorizontalDirection();
if(this.floating&&az){return((az==="right"&&ax)||(az==="left"&&!ax))
}else{return av&&((av==="down"&&aw)||(av==="up"&&!aw))
}},_getDragVerticalDirection:function(){var av=this.positionAbs.top-this.lastPositionAbs.top;
return av!==0&&(av>0?"down":"up")
},_getDragHorizontalDirection:function(){var av=this.positionAbs.left-this.lastPositionAbs.left;
return av!==0&&(av>0?"right":"left")
},refresh:function(av){this._refreshItems(av);
this._setHandleClassName();
this.refreshPositions();
return this
},_connectWith:function(){var av=this.options;
return av.connectWith.constructor===String?[av.connectWith]:av.connectWith
},_getItemsAsjQuery:function(av){var ax,aw,aC,az,aA=[],ay=[],aB=this._connectWith();
if(aB&&av){for(ax=aB.length-1;
ax>=0;
ax--){aC=ak(aB[ax],this.document[0]);
for(aw=aC.length-1;
aw>=0;
aw--){az=ak.data(aC[aw],this.widgetFullName);
if(az&&az!==this&&!az.options.disabled){ay.push([ak.isFunction(az.options.items)?az.options.items.call(az.element):ak(az.options.items,az.element).not(".ui-sortable-helper").not(".ui-sortable-placeholder"),az])
}}}}ay.push([ak.isFunction(this.options.items)?this.options.items.call(this.element,null,{options:this.options,item:this.currentItem}):ak(this.options.items,this.element).not(".ui-sortable-helper").not(".ui-sortable-placeholder"),this]);
function aD(){aA.push(this)
}for(ax=ay.length-1;
ax>=0;
ax--){ay[ax][0].each(aD)
}return ak(aA)
},_removeCurrentsFromItems:function(){var av=this.currentItem.find(":data("+this.widgetName+"-item)");
this.items=ak.grep(this.items,function(ax){for(var aw=0;
aw<av.length;
aw++){if(av[aw]===ax.item[0]){return false
}}return true
})
},_refreshItems:function(av){this.items=[];
this.containers=[this];
var az,ax,aE,aA,aD,aw,aG,aF,aB=this.items,ay=[[ak.isFunction(this.options.items)?this.options.items.call(this.element[0],av,{item:this.currentItem}):ak(this.options.items,this.element),this]],aC=this._connectWith();
if(aC&&this.ready){for(az=aC.length-1;
az>=0;
az--){aE=ak(aC[az],this.document[0]);
for(ax=aE.length-1;
ax>=0;
ax--){aA=ak.data(aE[ax],this.widgetFullName);
if(aA&&aA!==this&&!aA.options.disabled){ay.push([ak.isFunction(aA.options.items)?aA.options.items.call(aA.element[0],av,{item:this.currentItem}):ak(aA.options.items,aA.element),aA]);
this.containers.push(aA)
}}}}for(az=ay.length-1;
az>=0;
az--){aD=ay[az][1];
aw=ay[az][0];
for(ax=0,aF=aw.length;
ax<aF;
ax++){aG=ak(aw[ax]);
aG.data(this.widgetName+"-item",aD);
aB.push({item:aG,instance:aD,width:0,height:0,left:0,top:0})
}}},refreshPositions:function(av){this.floating=this.items.length?this.options.axis==="x"||this._isFloating(this.items[0].item):false;
if(this.offsetParent&&this.helper){this.offset.parent=this._getParentOffset()
}var ax,ay,aw,az;
for(ax=this.items.length-1;
ax>=0;
ax--){ay=this.items[ax];
if(ay.instance!==this.currentContainer&&this.currentContainer&&ay.item[0]!==this.currentItem[0]){continue
}aw=this.options.toleranceElement?ak(this.options.toleranceElement,ay.item):ay.item;
if(!av){ay.width=aw.outerWidth();
ay.height=aw.outerHeight()
}az=aw.offset();
ay.left=az.left;
ay.top=az.top
}if(this.options.custom&&this.options.custom.refreshContainers){this.options.custom.refreshContainers.call(this)
}else{for(ax=this.containers.length-1;
ax>=0;
ax--){az=this.containers[ax].element.offset();
this.containers[ax].containerCache.left=az.left;
this.containers[ax].containerCache.top=az.top;
this.containers[ax].containerCache.width=this.containers[ax].element.outerWidth();
this.containers[ax].containerCache.height=this.containers[ax].element.outerHeight()
}}return this
},_createPlaceholder:function(aw){aw=aw||this;
var av,ax=aw.options;
if(!ax.placeholder||ax.placeholder.constructor===String){av=ax.placeholder;
ax.placeholder={element:function(){var az=aw.currentItem[0].nodeName.toLowerCase(),ay=ak("<"+az+">",aw.document[0]);
aw._addClass(ay,"ui-sortable-placeholder",av||aw.currentItem[0].className)._removeClass(ay,"ui-sortable-helper");
if(az==="tbody"){aw._createTrPlaceholder(aw.currentItem.find("tr").eq(0),ak("<tr>",aw.document[0]).appendTo(ay))
}else{if(az==="tr"){aw._createTrPlaceholder(aw.currentItem,ay)
}else{if(az==="img"){ay.attr("src",aw.currentItem.attr("src"))
}}}if(!av){ay.css("visibility","hidden")
}return ay
},update:function(ay,az){if(av&&!ax.forcePlaceholderSize){return
}if(!az.height()){az.height(aw.currentItem.innerHeight()-parseInt(aw.currentItem.css("paddingTop")||0,10)-parseInt(aw.currentItem.css("paddingBottom")||0,10))
}if(!az.width()){az.width(aw.currentItem.innerWidth()-parseInt(aw.currentItem.css("paddingLeft")||0,10)-parseInt(aw.currentItem.css("paddingRight")||0,10))
}}}
}aw.placeholder=ak(ax.placeholder.element.call(aw.element,aw.currentItem));
aw.currentItem.after(aw.placeholder);
ax.placeholder.update(aw,aw.placeholder)
},_createTrPlaceholder:function(aw,av){var ax=this;
aw.children().each(function(){ak("<td>&#160;</td>",ax.document[0]).attr("colspan",ak(this).attr("colspan")||1).appendTo(av)
})
},_contactContainers:function(av){var aA,ay,aE,aB,aC,aG,aH,az,aD,ax,aw=null,aF=null;
for(aA=this.containers.length-1;
aA>=0;
aA--){if(ak.contains(this.currentItem[0],this.containers[aA].element[0])){continue
}if(this._intersectsWith(this.containers[aA].containerCache)){if(aw&&ak.contains(this.containers[aA].element[0],aw.element[0])){continue
}aw=this.containers[aA];
aF=aA
}else{if(this.containers[aA].containerCache.over){this.containers[aA]._trigger("out",av,this._uiHash(this));
this.containers[aA].containerCache.over=0
}}}if(!aw){return
}if(this.containers.length===1){if(!this.containers[aF].containerCache.over){this.containers[aF]._trigger("over",av,this._uiHash(this));
this.containers[aF].containerCache.over=1
}}else{aE=10000;
aB=null;
aD=aw.floating||this._isFloating(this.currentItem);
aC=aD?"left":"top";
aG=aD?"width":"height";
ax=aD?"pageX":"pageY";
for(ay=this.items.length-1;
ay>=0;
ay--){if(!ak.contains(this.containers[aF].element[0],this.items[ay].item[0])){continue
}if(this.items[ay].item[0]===this.currentItem[0]){continue
}aH=this.items[ay].item.offset()[aC];
az=false;
if(av[ax]-aH>this.items[ay][aG]/2){az=true
}if(Math.abs(av[ax]-aH)<aE){aE=Math.abs(av[ax]-aH);
aB=this.items[ay];
this.direction=az?"up":"down"
}}if(!aB&&!this.options.dropOnEmpty){return
}if(this.currentContainer===this.containers[aF]){if(!this.currentContainer.containerCache.over){this.containers[aF]._trigger("over",av,this._uiHash());
this.currentContainer.containerCache.over=1
}return
}aB?this._rearrange(av,aB,null,true):this._rearrange(av,null,this.containers[aF].element,true);
this._trigger("change",av,this._uiHash());
this.containers[aF]._trigger("change",av,this._uiHash(this));
this.currentContainer=this.containers[aF];
this.options.placeholder.update(this.currentContainer,this.placeholder);
this.containers[aF]._trigger("over",av,this._uiHash(this));
this.containers[aF].containerCache.over=1
}},_createHelper:function(aw){var ax=this.options,av=ak.isFunction(ax.helper)?ak(ax.helper.apply(this.element[0],[aw,this.currentItem])):(ax.helper==="clone"?this.currentItem.clone():this.currentItem);
if(!av.parents("body").length){ak(ax.appendTo!=="parent"?ax.appendTo:this.currentItem[0].parentNode)[0].appendChild(av[0])
}if(av[0]===this.currentItem[0]){this._storedCSS={width:this.currentItem[0].style.width,height:this.currentItem[0].style.height,position:this.currentItem.css("position"),top:this.currentItem.css("top"),left:this.currentItem.css("left")}
}if(!av[0].style.width||ax.forceHelperSize){av.width(this.currentItem.width())
}if(!av[0].style.height||ax.forceHelperSize){av.height(this.currentItem.height())
}return av
},_adjustOffsetFromHelper:function(av){if(typeof av==="string"){av=av.split(" ")
}if(ak.isArray(av)){av={left:+av[0],top:+av[1]||0}
}if("left" in av){this.offset.click.left=av.left+this.margins.left
}if("right" in av){this.offset.click.left=this.helperProportions.width-av.right+this.margins.left
}if("top" in av){this.offset.click.top=av.top+this.margins.top
}if("bottom" in av){this.offset.click.top=this.helperProportions.height-av.bottom+this.margins.top
}},_getParentOffset:function(){this.offsetParent=this.helper.offsetParent();
var av=this.offsetParent.offset();
if(this.cssPosition==="absolute"&&this.scrollParent[0]!==this.document[0]&&ak.contains(this.scrollParent[0],this.offsetParent[0])){av.left+=this.scrollParent.scrollLeft();
av.top+=this.scrollParent.scrollTop()
}if(this.offsetParent[0]===this.document[0].body||(this.offsetParent[0].tagName&&this.offsetParent[0].tagName.toLowerCase()==="html"&&ak.ui.ie)){av={top:0,left:0}
}return{top:av.top+(parseInt(this.offsetParent.css("borderTopWidth"),10)||0),left:av.left+(parseInt(this.offsetParent.css("borderLeftWidth"),10)||0)}
},_getRelativeOffset:function(){if(this.cssPosition==="relative"){var av=this.currentItem.position();
return{top:av.top-(parseInt(this.helper.css("top"),10)||0)+this.scrollParent.scrollTop(),left:av.left-(parseInt(this.helper.css("left"),10)||0)+this.scrollParent.scrollLeft()}
}else{return{top:0,left:0}
}},_cacheMargins:function(){this.margins={left:(parseInt(this.currentItem.css("marginLeft"),10)||0),top:(parseInt(this.currentItem.css("marginTop"),10)||0)}
},_cacheHelperProportions:function(){this.helperProportions={width:this.helper.outerWidth(),height:this.helper.outerHeight()}
},_setContainment:function(){var aw,ay,av,ax=this.options;
if(ax.containment==="parent"){ax.containment=this.helper[0].parentNode
}if(ax.containment==="document"||ax.containment==="window"){this.containment=[0-this.offset.relative.left-this.offset.parent.left,0-this.offset.relative.top-this.offset.parent.top,ax.containment==="document"?this.document.width():this.window.width()-this.helperProportions.width-this.margins.left,(ax.containment==="document"?(this.document.height()||document.body.parentNode.scrollHeight):this.window.height()||this.document[0].body.parentNode.scrollHeight)-this.helperProportions.height-this.margins.top]
}if(!(/^(document|window|parent)$/).test(ax.containment)){aw=ak(ax.containment)[0];
ay=ak(ax.containment).offset();
av=(ak(aw).css("overflow")!=="hidden");
this.containment=[ay.left+(parseInt(ak(aw).css("borderLeftWidth"),10)||0)+(parseInt(ak(aw).css("paddingLeft"),10)||0)-this.margins.left,ay.top+(parseInt(ak(aw).css("borderTopWidth"),10)||0)+(parseInt(ak(aw).css("paddingTop"),10)||0)-this.margins.top,ay.left+(av?Math.max(aw.scrollWidth,aw.offsetWidth):aw.offsetWidth)-(parseInt(ak(aw).css("borderLeftWidth"),10)||0)-(parseInt(ak(aw).css("paddingRight"),10)||0)-this.helperProportions.width-this.margins.left,ay.top+(av?Math.max(aw.scrollHeight,aw.offsetHeight):aw.offsetHeight)-(parseInt(ak(aw).css("borderTopWidth"),10)||0)-(parseInt(ak(aw).css("paddingBottom"),10)||0)-this.helperProportions.height-this.margins.top]
}},_convertPositionTo:function(ax,az){if(!az){az=this.position
}var aw=ax==="absolute"?1:-1,av=this.cssPosition==="absolute"&&!(this.scrollParent[0]!==this.document[0]&&ak.contains(this.scrollParent[0],this.offsetParent[0]))?this.offsetParent:this.scrollParent,ay=(/(html|body)/i).test(av[0].tagName);
return{top:(az.top+this.offset.relative.top*aw+this.offset.parent.top*aw-((this.cssPosition==="fixed"?-this.scrollParent.scrollTop():(ay?0:av.scrollTop()))*aw)),left:(az.left+this.offset.relative.left*aw+this.offset.parent.left*aw-((this.cssPosition==="fixed"?-this.scrollParent.scrollLeft():ay?0:av.scrollLeft())*aw))}
},_generatePosition:function(ay){var aA,az,aB=this.options,ax=ay.pageX,aw=ay.pageY,av=this.cssPosition==="absolute"&&!(this.scrollParent[0]!==this.document[0]&&ak.contains(this.scrollParent[0],this.offsetParent[0]))?this.offsetParent:this.scrollParent,aC=(/(html|body)/i).test(av[0].tagName);
if(this.cssPosition==="relative"&&!(this.scrollParent[0]!==this.document[0]&&this.scrollParent[0]!==this.offsetParent[0])){this.offset.relative=this._getRelativeOffset()
}if(this.originalPosition){if(this.containment){if(ay.pageX-this.offset.click.left<this.containment[0]){ax=this.containment[0]+this.offset.click.left
}if(ay.pageY-this.offset.click.top<this.containment[1]){aw=this.containment[1]+this.offset.click.top
}if(ay.pageX-this.offset.click.left>this.containment[2]){ax=this.containment[2]+this.offset.click.left
}if(ay.pageY-this.offset.click.top>this.containment[3]){aw=this.containment[3]+this.offset.click.top
}}if(aB.grid){aA=this.originalPageY+Math.round((aw-this.originalPageY)/aB.grid[1])*aB.grid[1];
aw=this.containment?((aA-this.offset.click.top>=this.containment[1]&&aA-this.offset.click.top<=this.containment[3])?aA:((aA-this.offset.click.top>=this.containment[1])?aA-aB.grid[1]:aA+aB.grid[1])):aA;
az=this.originalPageX+Math.round((ax-this.originalPageX)/aB.grid[0])*aB.grid[0];
ax=this.containment?((az-this.offset.click.left>=this.containment[0]&&az-this.offset.click.left<=this.containment[2])?az:((az-this.offset.click.left>=this.containment[0])?az-aB.grid[0]:az+aB.grid[0])):az
}}return{top:(aw-this.offset.click.top-this.offset.relative.top-this.offset.parent.top+((this.cssPosition==="fixed"?-this.scrollParent.scrollTop():(aC?0:av.scrollTop())))),left:(ax-this.offset.click.left-this.offset.relative.left-this.offset.parent.left+((this.cssPosition==="fixed"?-this.scrollParent.scrollLeft():aC?0:av.scrollLeft())))}
},_rearrange:function(az,ay,aw,ax){aw?aw[0].appendChild(this.placeholder[0]):ay.item[0].parentNode.insertBefore(this.placeholder[0],(this.direction==="down"?ay.item[0]:ay.item[0].nextSibling));
this.counter=this.counter?++this.counter:1;
var av=this.counter;
this._delay(function(){if(av===this.counter){this.refreshPositions(!ax)
}})
},_clear:function(aw,ay){this.reverting=false;
var av,az=[];
if(!this._noFinalSort&&this.currentItem.parent().length){this.placeholder.before(this.currentItem)
}this._noFinalSort=null;
if(this.helper[0]===this.currentItem[0]){for(av in this._storedCSS){if(this._storedCSS[av]==="auto"||this._storedCSS[av]==="static"){this._storedCSS[av]=""
}}this.currentItem.css(this._storedCSS);
this._removeClass(this.currentItem,"ui-sortable-helper")
}else{this.currentItem.show()
}if(this.fromOutside&&!ay){az.push(function(aA){this._trigger("receive",aA,this._uiHash(this.fromOutside))
})
}if((this.fromOutside||this.domPosition.prev!==this.currentItem.prev().not(".ui-sortable-helper")[0]||this.domPosition.parent!==this.currentItem.parent()[0])&&!ay){az.push(function(aA){this._trigger("update",aA,this._uiHash())
})
}if(this!==this.currentContainer){if(!ay){az.push(function(aA){this._trigger("remove",aA,this._uiHash())
});
az.push((function(aA){return function(aB){aA._trigger("receive",aB,this._uiHash(this))
}
}).call(this,this.currentContainer));
az.push((function(aA){return function(aB){aA._trigger("update",aB,this._uiHash(this))
}
}).call(this,this.currentContainer))
}}function ax(aC,aA,aB){return function(aD){aB._trigger(aC,aD,aA._uiHash(aA))
}
}for(av=this.containers.length-1;
av>=0;
av--){if(!ay){az.push(ax("deactivate",this,this.containers[av]))
}if(this.containers[av].containerCache.over){az.push(ax("out",this,this.containers[av]));
this.containers[av].containerCache.over=0
}}if(this.storedCursor){this.document.find("body").css("cursor",this.storedCursor);
this.storedStylesheet.remove()
}if(this._storedOpacity){this.helper.css("opacity",this._storedOpacity)
}if(this._storedZIndex){this.helper.css("zIndex",this._storedZIndex==="auto"?"":this._storedZIndex)
}this.dragging=false;
if(!ay){this._trigger("beforeStop",aw,this._uiHash())
}this.placeholder[0].parentNode.removeChild(this.placeholder[0]);
if(!this.cancelHelperRemoval){if(this.helper[0]!==this.currentItem[0]){this.helper.remove()
}this.helper=null
}if(!ay){for(av=0;
av<az.length;
av++){az[av].call(this,aw)
}this._trigger("stop",aw,this._uiHash())
}this.fromOutside=false;
return !this.cancelHelperRemoval
},_trigger:function(){if(ak.Widget.prototype._trigger.apply(this,arguments)===false){this.cancel()
}},_uiHash:function(av){var aw=av||this;
return{helper:aw.helper,placeholder:aw.placeholder||ak([]),position:aw.position,originalPosition:aw.originalPosition,offset:aw.positionAbs,item:aw.currentItem,sender:av?av.element:null}
}});
/*!
 * jQuery UI Spinner 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
function U(av){return function(){var aw=this.element.val();
av.apply(this,arguments);
this._refresh();
if(aw!==this.element.val()){this._trigger("change")
}}
}ak.widget("ui.spinner",{version:"1.12.1",defaultElement:"<input>",widgetEventPrefix:"spin",options:{classes:{"ui-spinner":"ui-corner-all","ui-spinner-down":"ui-corner-br","ui-spinner-up":"ui-corner-tr"},culture:null,icons:{down:"ui-icon-triangle-1-s",up:"ui-icon-triangle-1-n"},incremental:true,max:null,min:null,numberFormat:null,page:10,step:1,change:null,spin:null,start:null,stop:null},_create:function(){this._setOption("max",this.options.max);
this._setOption("min",this.options.min);
this._setOption("step",this.options.step);
if(this.value()!==""){this._value(this.element.val(),true)
}this._draw();
this._on(this._events);
this._refresh();
this._on(this.window,{beforeunload:function(){this.element.removeAttr("autocomplete")
}})
},_getCreateOptions:function(){var av=this._super();
var aw=this.element;
ak.each(["min","max","step"],function(ax,ay){var az=aw.attr(ay);
if(az!=null&&az.length){av[ay]=az
}});
return av
},_events:{keydown:function(av){if(this._start(av)&&this._keydown(av)){av.preventDefault()
}},keyup:"_stop",focus:function(){this.previous=this.element.val()
},blur:function(av){if(this.cancelBlur){delete this.cancelBlur;
return
}this._stop();
this._refresh();
if(this.previous!==this.element.val()){this._trigger("change",av)
}},mousewheel:function(av,aw){if(!aw){return
}if(!this.spinning&&!this._start(av)){return false
}this._spin((aw>0?1:-1)*this.options.step,av);
clearTimeout(this.mousewheelTimer);
this.mousewheelTimer=this._delay(function(){if(this.spinning){this._stop(av)
}},100);
av.preventDefault()
},"mousedown .ui-spinner-button":function(aw){var av;
av=this.element[0]===ak.ui.safeActiveElement(this.document[0])?this.previous:this.element.val();
function ax(){var ay=this.element[0]===ak.ui.safeActiveElement(this.document[0]);
if(!ay){this.element.trigger("focus");
this.previous=av;
this._delay(function(){this.previous=av
})
}}aw.preventDefault();
ax.call(this);
this.cancelBlur=true;
this._delay(function(){delete this.cancelBlur;
ax.call(this)
});
if(this._start(aw)===false){return
}this._repeat(null,ak(aw.currentTarget).hasClass("ui-spinner-up")?1:-1,aw)
},"mouseup .ui-spinner-button":"_stop","mouseenter .ui-spinner-button":function(av){if(!ak(av.currentTarget).hasClass("ui-state-active")){return
}if(this._start(av)===false){return false
}this._repeat(null,ak(av.currentTarget).hasClass("ui-spinner-up")?1:-1,av)
},"mouseleave .ui-spinner-button":"_stop"},_enhance:function(){this.uiSpinner=this.element.attr("autocomplete","off").wrap("<span>").parent().append("<a></a><a></a>")
},_draw:function(){this._enhance();
this._addClass(this.uiSpinner,"ui-spinner","ui-widget ui-widget-content");
this._addClass("ui-spinner-input");
this.element.attr("role","spinbutton");
this.buttons=this.uiSpinner.children("a").attr("tabIndex",-1).attr("aria-hidden",true).button({classes:{"ui-button":""}});
this._removeClass(this.buttons,"ui-corner-all");
this._addClass(this.buttons.first(),"ui-spinner-button ui-spinner-up");
this._addClass(this.buttons.last(),"ui-spinner-button ui-spinner-down");
this.buttons.first().button({icon:this.options.icons.up,showLabel:false});
this.buttons.last().button({icon:this.options.icons.down,showLabel:false});
if(this.buttons.height()>Math.ceil(this.uiSpinner.height()*0.5)&&this.uiSpinner.height()>0){this.uiSpinner.height(this.uiSpinner.height())
}},_keydown:function(aw){var av=this.options,ax=ak.ui.keyCode;
switch(aw.keyCode){case ax.UP:this._repeat(null,1,aw);
return true;
case ax.DOWN:this._repeat(null,-1,aw);
return true;
case ax.PAGE_UP:this._repeat(null,av.page,aw);
return true;
case ax.PAGE_DOWN:this._repeat(null,-av.page,aw);
return true
}return false
},_start:function(av){if(!this.spinning&&this._trigger("start",av)===false){return false
}if(!this.counter){this.counter=1
}this.spinning=true;
return true
},_repeat:function(aw,av,ax){aw=aw||500;
clearTimeout(this.timer);
this.timer=this._delay(function(){this._repeat(40,av,ax)
},aw);
this._spin(av*this.options.step,ax)
},_spin:function(aw,av){var ax=this.value()||0;
if(!this.counter){this.counter=1
}ax=this._adjustValue(ax+aw*this._increment(this.counter));
if(!this.spinning||this._trigger("spin",av,{value:ax})!==false){this._value(ax);
this.counter++
}},_increment:function(av){var aw=this.options.incremental;
if(aw){return ak.isFunction(aw)?aw(av):Math.floor(av*av*av/50000-av*av/500+17*av/200+1)
}return 1
},_precision:function(){var av=this._precisionOf(this.options.step);
if(this.options.min!==null){av=Math.max(av,this._precisionOf(this.options.min))
}return av
},_precisionOf:function(aw){var ax=aw.toString(),av=ax.indexOf(".");
return av===-1?0:ax.length-av-1
},_adjustValue:function(ax){var aw,ay,av=this.options;
aw=av.min!==null?av.min:0;
ay=ax-aw;
ay=Math.round(ay/av.step)*av.step;
ax=aw+ay;
ax=parseFloat(ax.toFixed(this._precision()));
if(av.max!==null&&ax>av.max){return av.max
}if(av.min!==null&&ax<av.min){return av.min
}return ax
},_stop:function(av){if(!this.spinning){return
}clearTimeout(this.timer);
clearTimeout(this.mousewheelTimer);
this.counter=0;
this.spinning=false;
this._trigger("stop",av)
},_setOption:function(av,ax){var ay,az,aw;
if(av==="culture"||av==="numberFormat"){ay=this._parse(this.element.val());
this.options[av]=ax;
this.element.val(this._format(ay));
return
}if(av==="max"||av==="min"||av==="step"){if(typeof ax==="string"){ax=this._parse(ax)
}}if(av==="icons"){az=this.buttons.first().find(".ui-icon");
this._removeClass(az,null,this.options.icons.up);
this._addClass(az,null,ax.up);
aw=this.buttons.last().find(".ui-icon");
this._removeClass(aw,null,this.options.icons.down);
this._addClass(aw,null,ax.down)
}this._super(av,ax)
},_setOptionDisabled:function(av){this._super(av);
this._toggleClass(this.uiSpinner,null,"ui-state-disabled",!!av);
this.element.prop("disabled",!!av);
this.buttons.button(av?"disable":"enable")
},_setOptions:U(function(av){this._super(av)
}),_parse:function(av){if(typeof av==="string"&&av!==""){av=window.Globalize&&this.options.numberFormat?Globalize.parseFloat(av,10,this.options.culture):+av
}return av===""||isNaN(av)?null:av
},_format:function(av){if(av===""){return""
}return window.Globalize&&this.options.numberFormat?Globalize.format(av,this.options.numberFormat,this.options.culture):av
},_refresh:function(){this.element.attr({"aria-valuemin":this.options.min,"aria-valuemax":this.options.max,"aria-valuenow":this._parse(this.element.val())})
},isValid:function(){var av=this.value();
if(av===null){return false
}return av===this._adjustValue(av)
},_value:function(ax,av){var aw;
if(ax!==""){aw=this._parse(ax);
if(aw!==null){if(!av){aw=this._adjustValue(aw)
}ax=this._format(aw)
}}this.element.val(ax);
this._refresh()
},_destroy:function(){this.element.prop("disabled",false).removeAttr("autocomplete role aria-valuemin aria-valuemax aria-valuenow");
this.uiSpinner.replaceWith(this.element)
},stepUp:U(function(av){this._stepUp(av)
}),_stepUp:function(av){if(this._start()){this._spin((av||1)*this.options.step);
this._stop()
}},stepDown:U(function(av){this._stepDown(av)
}),_stepDown:function(av){if(this._start()){this._spin((av||1)*-this.options.step);
this._stop()
}},pageUp:U(function(av){this._stepUp((av||1)*this.options.page)
}),pageDown:U(function(av){this._stepDown((av||1)*this.options.page)
}),value:function(av){if(!arguments.length){return this._parse(this.element.val())
}U(this._value).call(this,av)
},widget:function(){return this.uiSpinner
}});
if(ak.uiBackCompat!==false){ak.widget("ui.spinner",ak.ui.spinner,{_enhance:function(){this.uiSpinner=this.element.attr("autocomplete","off").wrap(this._uiSpinnerHtml()).parent().append(this._buttonHtml())
},_uiSpinnerHtml:function(){return"<span>"
},_buttonHtml:function(){return"<a></a><a></a>"
}})
}var ag=ak.ui.spinner;
/*!
 * jQuery UI Tabs 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.tabs",{version:"1.12.1",delay:300,options:{active:null,classes:{"ui-tabs":"ui-corner-all","ui-tabs-nav":"ui-corner-all","ui-tabs-panel":"ui-corner-bottom","ui-tabs-tab":"ui-corner-top"},collapsible:false,event:"click",heightStyle:"content",hide:null,show:null,activate:null,beforeActivate:null,beforeLoad:null,load:null},_isLocal:(function(){var av=/#.*$/;
return function(ax){var az,ay;
az=ax.href.replace(av,"");
ay=location.href.replace(av,"");
try{az=decodeURIComponent(az)
}catch(aw){}try{ay=decodeURIComponent(ay)
}catch(aw){}return ax.hash.length>1&&az===ay
}
})(),_create:function(){var aw=this,av=this.options;
this.running=false;
this._addClass("ui-tabs","ui-widget ui-widget-content");
this._toggleClass("ui-tabs-collapsible",null,av.collapsible);
this._processTabs();
av.active=this._initialActive();
if(ak.isArray(av.disabled)){av.disabled=ak.unique(av.disabled.concat(ak.map(this.tabs.filter(".ui-state-disabled"),function(ax){return aw.tabs.index(ax)
}))).sort()
}if(this.options.active!==false&&this.anchors.length){this.active=this._findActive(av.active)
}else{this.active=ak()
}this._refresh();
if(this.active.length){this.load(av.active)
}},_initialActive:function(){var aw=this.options.active,av=this.options.collapsible,ax=location.hash.substring(1);
if(aw===null){if(ax){this.tabs.each(function(ay,az){if(ak(az).attr("aria-controls")===ax){aw=ay;
return false
}})
}if(aw===null){aw=this.tabs.index(this.tabs.filter(".ui-tabs-active"))
}if(aw===null||aw===-1){aw=this.tabs.length?0:false
}}if(aw!==false){aw=this.tabs.index(this.tabs.eq(aw));
if(aw===-1){aw=av?false:0
}}if(!av&&aw===false&&this.anchors.length){aw=0
}return aw
},_getCreateEventData:function(){return{tab:this.active,panel:!this.active.length?ak():this._getPanelForTab(this.active)}
},_tabKeydown:function(ax){var aw=ak(ak.ui.safeActiveElement(this.document[0])).closest("li"),av=this.tabs.index(aw),ay=true;
if(this._handlePageNav(ax)){return
}switch(ax.keyCode){case ak.ui.keyCode.RIGHT:case ak.ui.keyCode.DOWN:av++;
break;
case ak.ui.keyCode.UP:case ak.ui.keyCode.LEFT:ay=false;
av--;
break;
case ak.ui.keyCode.END:av=this.anchors.length-1;
break;
case ak.ui.keyCode.HOME:av=0;
break;
case ak.ui.keyCode.SPACE:ax.preventDefault();
clearTimeout(this.activating);
this._activate(av);
return;
case ak.ui.keyCode.ENTER:ax.preventDefault();
clearTimeout(this.activating);
this._activate(av===this.options.active?false:av);
return;
default:return
}ax.preventDefault();
clearTimeout(this.activating);
av=this._focusNextTab(av,ay);
if(!ax.ctrlKey&&!ax.metaKey){aw.attr("aria-selected","false");
this.tabs.eq(av).attr("aria-selected","true");
this.activating=this._delay(function(){this.option("active",av)
},this.delay)
}},_panelKeydown:function(av){if(this._handlePageNav(av)){return
}if(av.ctrlKey&&av.keyCode===ak.ui.keyCode.UP){av.preventDefault();
this.active.trigger("focus")
}},_handlePageNav:function(av){if(av.altKey&&av.keyCode===ak.ui.keyCode.PAGE_UP){this._activate(this._focusNextTab(this.options.active-1,false));
return true
}if(av.altKey&&av.keyCode===ak.ui.keyCode.PAGE_DOWN){this._activate(this._focusNextTab(this.options.active+1,true));
return true
}},_findNextTab:function(aw,ax){var av=this.tabs.length-1;
function ay(){if(aw>av){aw=0
}if(aw<0){aw=av
}return aw
}while(ak.inArray(ay(),this.options.disabled)!==-1){aw=ax?aw+1:aw-1
}return aw
},_focusNextTab:function(av,aw){av=this._findNextTab(av,aw);
this.tabs.eq(av).trigger("focus");
return av
},_setOption:function(av,aw){if(av==="active"){this._activate(aw);
return
}this._super(av,aw);
if(av==="collapsible"){this._toggleClass("ui-tabs-collapsible",null,aw);
if(!aw&&this.options.active===false){this._activate(0)
}}if(av==="event"){this._setupEvents(aw)
}if(av==="heightStyle"){this._setupHeightStyle(aw)
}},_sanitizeSelector:function(av){return av?av.replace(/[!"$%&'()*+,.\/:;<=>?@\[\]\^`{|}~]/g,"\\$&"):""
},refresh:function(){var aw=this.options,av=this.tablist.children(":has(a[href])");
aw.disabled=ak.map(av.filter(".ui-state-disabled"),function(ax){return av.index(ax)
});
this._processTabs();
if(aw.active===false||!this.anchors.length){aw.active=false;
this.active=ak()
}else{if(this.active.length&&!ak.contains(this.tablist[0],this.active[0])){if(this.tabs.length===aw.disabled.length){aw.active=false;
this.active=ak()
}else{this._activate(this._findNextTab(Math.max(0,aw.active-1),false))
}}else{aw.active=this.tabs.index(this.active)
}}this._refresh()
},_refresh:function(){this._setOptionDisabled(this.options.disabled);
this._setupEvents(this.options.event);
this._setupHeightStyle(this.options.heightStyle);
this.tabs.not(this.active).attr({"aria-selected":"false","aria-expanded":"false",tabIndex:-1});
this.panels.not(this._getPanelForTab(this.active)).hide().attr({"aria-hidden":"true"});
if(!this.active.length){this.tabs.eq(0).attr("tabIndex",0)
}else{this.active.attr({"aria-selected":"true","aria-expanded":"true",tabIndex:0});
this._addClass(this.active,"ui-tabs-active","ui-state-active");
this._getPanelForTab(this.active).show().attr({"aria-hidden":"false"})
}},_processTabs:function(){var ax=this,ay=this.tabs,aw=this.anchors,av=this.panels;
this.tablist=this._getList().attr("role","tablist");
this._addClass(this.tablist,"ui-tabs-nav","ui-helper-reset ui-helper-clearfix ui-widget-header");
this.tablist.on("mousedown"+this.eventNamespace,"> li",function(az){if(ak(this).is(".ui-state-disabled")){az.preventDefault()
}}).on("focus"+this.eventNamespace,".ui-tabs-anchor",function(){if(ak(this).closest("li").is(".ui-state-disabled")){this.blur()
}});
this.tabs=this.tablist.find("> li:has(a[href])").attr({role:"tab",tabIndex:-1});
this._addClass(this.tabs,"ui-tabs-tab","ui-state-default");
this.anchors=this.tabs.map(function(){return ak("a",this)[0]
}).attr({role:"presentation",tabIndex:-1});
this._addClass(this.anchors,"ui-tabs-anchor");
this.panels=ak();
this.anchors.each(function(aE,aC){var az,aA,aD,aB=ak(aC).uniqueId().attr("id"),aF=ak(aC).closest("li"),aG=aF.attr("aria-controls");
if(ax._isLocal(aC)){az=aC.hash;
aD=az.substring(1);
aA=ax.element.find(ax._sanitizeSelector(az))
}else{aD=aF.attr("aria-controls")||ak({}).uniqueId()[0].id;
az="#"+aD;
aA=ax.element.find(az);
if(!aA.length){aA=ax._createPanel(aD);
aA.insertAfter(ax.panels[aE-1]||ax.tablist)
}aA.attr("aria-live","polite")
}if(aA.length){ax.panels=ax.panels.add(aA)
}if(aG){aF.data("ui-tabs-aria-controls",aG)
}aF.attr({"aria-controls":aD,"aria-labelledby":aB});
aA.attr("aria-labelledby",aB)
});
this.panels.attr("role","tabpanel");
this._addClass(this.panels,"ui-tabs-panel","ui-widget-content");
if(ay){this._off(ay.not(this.tabs));
this._off(aw.not(this.anchors));
this._off(av.not(this.panels))
}},_getList:function(){return this.tablist||this.element.find("ol, ul").eq(0)
},_createPanel:function(av){return ak("<div>").attr("id",av).data("ui-tabs-destroy",true)
},_setOptionDisabled:function(ay){var ax,av,aw;
if(ak.isArray(ay)){if(!ay.length){ay=false
}else{if(ay.length===this.anchors.length){ay=true
}}}for(aw=0;
(av=this.tabs[aw]);
aw++){ax=ak(av);
if(ay===true||ak.inArray(aw,ay)!==-1){ax.attr("aria-disabled","true");
this._addClass(ax,null,"ui-state-disabled")
}else{ax.removeAttr("aria-disabled");
this._removeClass(ax,null,"ui-state-disabled")
}}this.options.disabled=ay;
this._toggleClass(this.widget(),this.widgetFullName+"-disabled",null,ay===true)
},_setupEvents:function(aw){var av={};
if(aw){ak.each(aw.split(" "),function(ay,ax){av[ax]="_eventHandler"
})
}this._off(this.anchors.add(this.tabs).add(this.panels));
this._on(true,this.anchors,{click:function(ax){ax.preventDefault()
}});
this._on(this.anchors,av);
this._on(this.tabs,{keydown:"_tabKeydown"});
this._on(this.panels,{keydown:"_panelKeydown"});
this._focusable(this.tabs);
this._hoverable(this.tabs)
},_setupHeightStyle:function(av){var ax,aw=this.element.parent();
if(av==="fill"){ax=aw.height();
ax-=this.element.outerHeight()-this.element.height();
this.element.siblings(":visible").each(function(){var az=ak(this),ay=az.css("position");
if(ay==="absolute"||ay==="fixed"){return
}ax-=az.outerHeight(true)
});
this.element.children().not(this.panels).each(function(){ax-=ak(this).outerHeight(true)
});
this.panels.each(function(){ak(this).height(Math.max(0,ax-ak(this).innerHeight()+ak(this).height()))
}).css("overflow","auto")
}else{if(av==="auto"){ax=0;
this.panels.each(function(){ax=Math.max(ax,ak(this).height("").height())
}).height(ax)
}}},_eventHandler:function(av){var aE=this.options,az=this.active,aA=ak(av.currentTarget),ay=aA.closest("li"),aC=ay[0]===az[0],aw=aC&&aE.collapsible,ax=aw?ak():this._getPanelForTab(ay),aB=!az.length?ak():this._getPanelForTab(az),aD={oldTab:az,oldPanel:aB,newTab:aw?ak():ay,newPanel:ax};
av.preventDefault();
if(ay.hasClass("ui-state-disabled")||ay.hasClass("ui-tabs-loading")||this.running||(aC&&!aE.collapsible)||(this._trigger("beforeActivate",av,aD)===false)){return
}aE.active=aw?false:this.tabs.index(ay);
this.active=aC?ak():ay;
if(this.xhr){this.xhr.abort()
}if(!aB.length&&!ax.length){ak.error("jQuery UI Tabs: Mismatching fragment identifier.")
}if(ax.length){this.load(this.tabs.index(ay),av)
}this._toggle(av,aD)
},_toggle:function(aB,aA){var az=this,av=aA.newPanel,ay=aA.oldPanel;
this.running=true;
function ax(){az.running=false;
az._trigger("activate",aB,aA)
}function aw(){az._addClass(aA.newTab.closest("li"),"ui-tabs-active","ui-state-active");
if(av.length&&az.options.show){az._show(av,az.options.show,ax)
}else{av.show();
ax()
}}if(ay.length&&this.options.hide){this._hide(ay,this.options.hide,function(){az._removeClass(aA.oldTab.closest("li"),"ui-tabs-active","ui-state-active");
aw()
})
}else{this._removeClass(aA.oldTab.closest("li"),"ui-tabs-active","ui-state-active");
ay.hide();
aw()
}ay.attr("aria-hidden","true");
aA.oldTab.attr({"aria-selected":"false","aria-expanded":"false"});
if(av.length&&ay.length){aA.oldTab.attr("tabIndex",-1)
}else{if(av.length){this.tabs.filter(function(){return ak(this).attr("tabIndex")===0
}).attr("tabIndex",-1)
}}av.attr("aria-hidden","false");
aA.newTab.attr({"aria-selected":"true","aria-expanded":"true",tabIndex:0})
},_activate:function(aw){var av,ax=this._findActive(aw);
if(ax[0]===this.active[0]){return
}if(!ax.length){ax=this.active
}av=ax.find(".ui-tabs-anchor")[0];
this._eventHandler({target:av,currentTarget:av,preventDefault:ak.noop})
},_findActive:function(av){return av===false?ak():this.tabs.eq(av)
},_getIndex:function(av){if(typeof av==="string"){av=this.anchors.index(this.anchors.filter("[href$='"+ak.ui.escapeSelector(av)+"']"))
}return av
},_destroy:function(){if(this.xhr){this.xhr.abort()
}this.tablist.removeAttr("role").off(this.eventNamespace);
this.anchors.removeAttr("role tabIndex").removeUniqueId();
this.tabs.add(this.panels).each(function(){if(ak.data(this,"ui-tabs-destroy")){ak(this).remove()
}else{ak(this).removeAttr("role tabIndex aria-live aria-busy aria-selected aria-labelledby aria-hidden aria-expanded")
}});
this.tabs.each(function(){var av=ak(this),aw=av.data("ui-tabs-aria-controls");
if(aw){av.attr("aria-controls",aw).removeData("ui-tabs-aria-controls")
}else{av.removeAttr("aria-controls")
}});
this.panels.show();
if(this.options.heightStyle!=="content"){this.panels.css("height","")
}},enable:function(av){var aw=this.options.disabled;
if(aw===false){return
}if(av===undefined){aw=false
}else{av=this._getIndex(av);
if(ak.isArray(aw)){aw=ak.map(aw,function(ax){return ax!==av?ax:null
})
}else{aw=ak.map(this.tabs,function(ax,ay){return ay!==av?ay:null
})
}}this._setOptionDisabled(aw)
},disable:function(av){var aw=this.options.disabled;
if(aw===true){return
}if(av===undefined){aw=true
}else{av=this._getIndex(av);
if(ak.inArray(av,aw)!==-1){return
}if(ak.isArray(aw)){aw=ak.merge([av],aw).sort()
}else{aw=[av]
}}this._setOptionDisabled(aw)
},load:function(ay,aC){ay=this._getIndex(ay);
var aB=this,az=this.tabs.eq(ay),ax=az.find(".ui-tabs-anchor"),aw=this._getPanelForTab(az),aA={tab:az,panel:aw},av=function(aE,aD){if(aD==="abort"){aB.panels.stop(false,true)
}aB._removeClass(az,"ui-tabs-loading");
aw.removeAttr("aria-busy");
if(aE===aB.xhr){delete aB.xhr
}};
if(this._isLocal(ax[0])){return
}this.xhr=ak.ajax(this._ajaxSettings(ax,aC,aA));
if(this.xhr&&this.xhr.statusText!=="canceled"){this._addClass(az,"ui-tabs-loading");
aw.attr("aria-busy","true");
this.xhr.done(function(aE,aD,aF){setTimeout(function(){aw.html(aE);
aB._trigger("load",aC,aA);
av(aF,aD)
},1)
}).fail(function(aE,aD){setTimeout(function(){av(aE,aD)
},1)
})
}},_ajaxSettings:function(av,ay,ax){var aw=this;
return{url:av.attr("href").replace(/#.*$/,""),beforeSend:function(aA,az){return aw._trigger("beforeLoad",ay,ak.extend({jqXHR:aA,ajaxSettings:az},ax))
}}
},_getPanelForTab:function(av){var aw=ak(av).attr("aria-controls");
return this.element.find(this._sanitizeSelector("#"+aw))
}});
if(ak.uiBackCompat!==false){ak.widget("ui.tabs",ak.ui.tabs,{_processTabs:function(){this._superApply(arguments);
this._addClass(this.tabs,"ui-tab")
}})
}var R=ak.ui.tabs;
/*!
 * jQuery UI Tooltip 1.12.1
 * http://jqueryui.com
 *
 * Copyright jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 */
ak.widget("ui.tooltip",{version:"1.12.1",options:{classes:{"ui-tooltip":"ui-corner-all ui-widget-shadow"},content:function(){var av=ak(this).attr("title")||"";
return ak("<a>").text(av).html()
},hide:true,items:"[title]:not([disabled])",position:{my:"left top+15",at:"left bottom",collision:"flipfit flip"},show:true,track:false,close:null,open:null},_addDescribedBy:function(aw,ax){var av=(aw.attr("aria-describedby")||"").split(/\s+/);
av.push(ax);
aw.data("ui-tooltip-id",ax).attr("aria-describedby",ak.trim(av.join(" ")))
},_removeDescribedBy:function(ax){var ay=ax.data("ui-tooltip-id"),aw=(ax.attr("aria-describedby")||"").split(/\s+/),av=ak.inArray(ay,aw);
if(av!==-1){aw.splice(av,1)
}ax.removeData("ui-tooltip-id");
aw=ak.trim(aw.join(" "));
if(aw){ax.attr("aria-describedby",aw)
}else{ax.removeAttr("aria-describedby")
}},_create:function(){this._on({mouseover:"open",focusin:"open"});
this.tooltips={};
this.parents={};
this.liveRegion=ak("<div>").attr({role:"log","aria-live":"assertive","aria-relevant":"additions"}).appendTo(this.document[0].body);
this._addClass(this.liveRegion,null,"ui-helper-hidden-accessible");
this.disabledTitles=ak([])
},_setOption:function(av,ax){var aw=this;
this._super(av,ax);
if(av==="content"){ak.each(this.tooltips,function(az,ay){aw._updateContent(ay.element)
})
}},_setOptionDisabled:function(av){this[av?"_disable":"_enable"]()
},_disable:function(){var av=this;
ak.each(this.tooltips,function(ay,ax){var aw=ak.Event("blur");
aw.target=aw.currentTarget=ax.element[0];
av.close(aw,true)
});
this.disabledTitles=this.disabledTitles.add(this.element.find(this.options.items).addBack().filter(function(){var aw=ak(this);
if(aw.is("[title]")){return aw.data("ui-tooltip-title",aw.attr("title")).removeAttr("title")
}}))
},_enable:function(){this.disabledTitles.each(function(){var av=ak(this);
if(av.data("ui-tooltip-title")){av.attr("title",av.data("ui-tooltip-title"))
}});
this.disabledTitles=ak([])
},open:function(aw){var av=this,ax=ak(aw?aw.target:this.element).closest(this.options.items);
if(!ax.length||ax.data("ui-tooltip-id")){return
}if(ax.attr("title")){ax.data("ui-tooltip-title",ax.attr("title"))
}ax.data("ui-tooltip-open",true);
if(aw&&aw.type==="mouseover"){ax.parents().each(function(){var az=ak(this),ay;
if(az.data("ui-tooltip-open")){ay=ak.Event("blur");
ay.target=ay.currentTarget=this;
av.close(ay,true)
}if(az.attr("title")){az.uniqueId();
av.parents[this.id]={element:this,title:az.attr("title")};
az.attr("title","")
}})
}this._registerCloseHandlers(aw,ax);
this._updateContent(ax,aw)
},_updateContent:function(aA,az){var ay,av=this.options.content,ax=this,aw=az?az.type:null;
if(typeof av==="string"||av.nodeType||av.jquery){return this._open(az,aA,av)
}ay=av.call(aA[0],function(aB){ax._delay(function(){if(!aA.data("ui-tooltip-open")){return
}if(az){az.type=aw
}this._open(az,aA,aB)
})
});
if(ay){this._open(az,aA,ay)
}},_open:function(aw,az,aA){var av,aD,aC,ax,aB=ak.extend({},this.options.position);
if(!aA){return
}av=this._find(az);
if(av){av.tooltip.find(".ui-tooltip-content").html(aA);
return
}if(az.is("[title]")){if(aw&&aw.type==="mouseover"){az.attr("title","")
}else{az.removeAttr("title")
}}av=this._tooltip(az);
aD=av.tooltip;
this._addDescribedBy(az,aD.attr("id"));
aD.find(".ui-tooltip-content").html(aA);
this.liveRegion.children().hide();
ax=ak("<div>").html(aD.find(".ui-tooltip-content").html());
ax.removeAttr("name").find("[name]").removeAttr("name");
ax.removeAttr("id").find("[id]").removeAttr("id");
ax.appendTo(this.liveRegion);
function ay(aE){aB.of=aE;
if(aD.is(":hidden")){return
}aD.position(aB)
}if(this.options.track&&aw&&/^mouse/.test(aw.type)){this._on(this.document,{mousemove:ay});
ay(aw)
}else{aD.position(ak.extend({of:az},this.options.position))
}aD.hide();
this._show(aD,this.options.show);
if(this.options.track&&this.options.show&&this.options.show.delay){aC=this.delayedShow=setInterval(function(){if(aD.is(":visible")){ay(aB.of);
clearInterval(aC)
}},ak.fx.interval)
}this._trigger("open",aw,{tooltip:aD})
},_registerCloseHandlers:function(aw,ax){var av={keyup:function(ay){if(ay.keyCode===ak.ui.keyCode.ESCAPE){var az=ak.Event(ay);
az.currentTarget=ax[0];
this.close(az,true)
}}};
if(ax[0]!==this.element[0]){av.remove=function(){this._removeTooltip(this._find(ax).tooltip)
}
}if(!aw||aw.type==="mouseover"){av.mouseleave="close"
}if(!aw||aw.type==="focusin"){av.focusout="close"
}this._on(true,ax,av)
},close:function(aw){var ay,av=this,az=ak(aw?aw.currentTarget:this.element),ax=this._find(az);
if(!ax){az.removeData("ui-tooltip-open");
return
}ay=ax.tooltip;
if(ax.closing){return
}clearInterval(this.delayedShow);
if(az.data("ui-tooltip-title")&&!az.attr("title")){az.attr("title",az.data("ui-tooltip-title"))
}this._removeDescribedBy(az);
ax.hiding=true;
ay.stop(true);
this._hide(ay,this.options.hide,function(){av._removeTooltip(ak(this))
});
az.removeData("ui-tooltip-open");
this._off(az,"mouseleave focusout keyup");
if(az[0]!==this.element[0]){this._off(az,"remove")
}this._off(this.document,"mousemove");
if(aw&&aw.type==="mouseleave"){ak.each(this.parents,function(aB,aA){ak(aA.element).attr("title",aA.title);
delete av.parents[aB]
})
}ax.closing=true;
this._trigger("close",aw,{tooltip:ay});
if(!ax.hiding){ax.closing=false
}},_tooltip:function(av){var ax=ak("<div>").attr("role","tooltip"),aw=ak("<div>").appendTo(ax),ay=ax.uniqueId().attr("id");
this._addClass(aw,"ui-tooltip-content");
this._addClass(ax,"ui-tooltip","ui-widget ui-widget-content");
ax.appendTo(this._appendTo(av));
return this.tooltips[ay]={element:av,tooltip:ax}
},_find:function(av){var aw=av.data("ui-tooltip-id");
return aw?this.tooltips[aw]:null
},_removeTooltip:function(av){av.remove();
delete this.tooltips[av.attr("id")]
},_appendTo:function(aw){var av=aw.closest(".ui-front, dialog");
if(!av.length){av=this.document[0].body
}return av
},_destroy:function(){var av=this;
ak.each(this.tooltips,function(az,ay){var ax=ak.Event("blur"),aw=ay.element;
ax.target=ax.currentTarget=aw[0];
av.close(ax,true);
ak("#"+az).remove();
if(aw.data("ui-tooltip-title")){if(!aw.attr("title")){aw.attr("title",aw.data("ui-tooltip-title"))
}aw.removeData("ui-tooltip-title")
}});
this.liveRegion.remove()
}});
if(ak.uiBackCompat!==false){ak.widget("ui.tooltip",ak.ui.tooltip,{options:{tooltipClass:null},_tooltip:function(){var av=this._superApply(arguments);
if(this.options.tooltipClass){av.tooltip.addClass(this.options.tooltipClass)
}return av
}})
}var D=ak.ui.tooltip
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.ar={closeText:"إغلاق",prevText:"<السابق",nextText:"التالي>",currentText:"اليوم",monthNames:["يناير/كانون الثاني","فبراير/شباط","مارس/آذار","أبريل/نيسان","مايو/آيار","يونيو/حزيران","يوليو/تموز","أغسطس/آب","سبتمبر/أيلول","أكتوبر/تشرين الأول","نوفمبر/تشرين الثاني","ديسمبر/كانون الأول"],monthNamesShort:["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"],dayNames:["الأحد","الاثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت"],dayNamesShort:["الأحد","الاثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت"],dayNamesMin:["ح","ن","ث","ر","خ","ج","س"],weekHeader:"أسبوع",dateFormat:"dd/mm/yy",firstDay:6,isRTL:true,showMonthAfterYear:false,yearSuffix:""};
return a.regional.ar
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.fr={closeText:"Fermer",prevText:"Précédent",nextText:"Suivant",currentText:"Aujourd'hui",monthNames:["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],monthNamesShort:["Janv","Févr","Mars","Avril","Mai","Juin","Juil","Août","Sept","Oct","Nov","Déc"],dayNames:["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"],dayNamesShort:["Dim","Lun","Mar","Mer","Jeu","Ven","Sam"],dayNamesMin:["D","L","M","M","J","V","S"],weekHeader:"Sem.",dateFormat:"dd/mm/yy",firstDay:1,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
return a.regional.fr
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.it={closeText:"Chiudi",prevText:"&#x3c;Prec",nextText:"Succ&#x3e;",currentText:"Oggi",monthNames:["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"],monthNamesShort:["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"],dayNames:["Domenica","Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato"],dayNamesShort:["Dom","Lun","Mar","Mer","Gio","Ven","Sab"],dayNamesMin:["Do","Lu","Ma","Me","Gi","Ve","Sa"],weekHeader:"Sm.",dateFormat:"dd/mm/yy",firstDay:1,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
return a.regional.it
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.de={closeText:"Schließen",prevText:"&#x3c;Vorher",nextText:"Nachher&#x3e;",currentText:"Heute",monthNames:["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"],monthNamesShort:["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"],dayNames:["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"],dayNamesShort:["So","Mo","Di","Mi","Do","Fr","Sa"],dayNamesMin:["So","Mo","Di","Mi","Do","Fr","Sa"],weekHeader:"Wo",dateFormat:"dd/mm/yy",firstDay:1,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
return a.regional.de
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.es={closeText:"Cerrar",prevText:"&#x3c;Ant",nextText:"Sig&#x3e;",currentText:"Hoy",monthNames:["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],monthNamesShort:["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],dayNames:["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],dayNamesShort:["Dom","Lun","Mar","Mié","Juv","Vie","Sáb"],dayNamesMin:["Do","Lu","Ma","Mi","Ju","Vi","S&#225;"],weekHeader:"Sm",dateFormat:"dd/mm/yy",firstDay:1,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
return a.regional.es
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.pt={closeText:"Fechar",prevText:"&#x3c;Ant",nextText:"Seg&#x3e;",currentText:"Hoje",monthNames:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],monthNamesShort:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],dayNames:["Domingo","Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado"],dayNamesShort:["Dom","Seg","Ter","Qua","Qui","Sex","Sáb"],dayNamesMin:["D","S","T","Q","Q","S","S"],weekHeader:"Sem",dateFormat:"dd/mm/yy",firstDay:0,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
return a.regional.pt
}));
(function(a){if(typeof define==="function"&&define.amd){define(["../jquery.ui.datepicker"],a)
}else{a(jQuery.datepicker)
}}(function(a){a.regional.pl={closeText:"Zamknij",prevText:"&#x3c;Poprzedni",nextText:"Następny&#x3e;",currentText:"Dziś",monthNames:["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"],monthNamesShort:["Sty","Lu","Mar","Kw","Maj","Cze","Lip","Sie","Wrz","Pa","Lis","Gru"],dayNames:["Niedziela","Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota"],dayNamesShort:["Nie","Pn","Wt","Śr","Czw","Pt","So"],dayNamesMin:["N","Pn","Wt","Śr","Cz","Pt","So"],weekHeader:"Tydz",dateFormat:"dd/mm/yy",firstDay:1,isRTL:false,showMonthAfterYear:false,yearSuffix:""};
return a.regional.pl
}));
/*!
 * mustache.js - Logic-less {{mustache}} templates with JavaScript
 * http://github.com/janl/mustache.js
 */
(function(b,a){if(typeof exports==="object"&&exports){a(exports)
}else{if(typeof define==="function"&&define.amd){define(["exports"],a)
}else{a(b.Mustache={})
}}}(this,function(a){var u=Object.prototype.toString;
var k=Array.isArray||function(x){return u.call(x)==="[object Array]"
};
function b(x){return typeof x==="function"
}function e(x){return x.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g,"\\$&")
}var g=RegExp.prototype.test;
function q(y,x){return g.call(y,x)
}var j=/\S/;
function h(x){return !q(j,x)
}var d={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;","/":"&#x2F;"};
function m(x){return String(x).replace(/[&<>"'\/]/g,function(y){return d[y]
})
}var f=/\s*/;
var l=/\s+/;
var t=/\s*=/;
var n=/\s*\}/;
var r=/#|\^|\/|>|\{|&|=|!/;
function w(Q,F){if(!Q){return[]
}var H=[];
var G=[];
var C=[];
var R=false;
var O=false;
function N(){if(R&&!O){while(C.length){delete G[C.pop()]
}}else{C=[]
}R=false;
O=false
}var J,E,P;
function D(S){if(typeof S==="string"){S=S.split(l,2)
}if(!k(S)||S.length!==2){throw new Error("Invalid tags: "+S)
}J=new RegExp(e(S[0])+"\\s*");
E=new RegExp("\\s*"+e(S[1]));
P=new RegExp("\\s*"+e("}"+S[1]))
}D(F||a.tags);
var z=new s(Q);
var A,y,I,L,B,x;
while(!z.eos()){A=z.pos;
I=z.scanUntil(J);
if(I){for(var M=0,K=I.length;
M<K;
++M){L=I.charAt(M);
if(h(L)){C.push(G.length)
}else{O=true
}G.push(["text",L,A,A+1]);
A+=1;
if(L==="\n"){N()
}}}if(!z.scan(J)){break
}R=true;
y=z.scan(r)||"name";
z.scan(f);
if(y==="="){I=z.scanUntil(t);
z.scan(t);
z.scanUntil(E)
}else{if(y==="{"){I=z.scanUntil(P);
z.scan(n);
z.scanUntil(E);
y="&"
}else{I=z.scanUntil(E)
}}if(!z.scan(E)){throw new Error("Unclosed tag at "+z.pos)
}B=[y,I,A,z.pos];
G.push(B);
if(y==="#"||y==="^"){H.push(B)
}else{if(y==="/"){x=H.pop();
if(!x){throw new Error('Unopened section "'+I+'" at '+A)
}if(x[1]!==I){throw new Error('Unclosed section "'+x[1]+'" at '+A)
}}else{if(y==="name"||y==="{"||y==="&"){O=true
}else{if(y==="="){D(I)
}}}}}x=H.pop();
if(x){throw new Error('Unclosed section "'+x[1]+'" at '+z.pos)
}return v(c(G))
}function c(C){var y=[];
var A,x;
for(var z=0,B=C.length;
z<B;
++z){A=C[z];
if(A){if(A[0]==="text"&&x&&x[0]==="text"){x[1]+=A[1];
x[3]=A[3]
}else{y.push(A);
x=A
}}}return y
}function v(C){var E=[];
var B=E;
var D=[];
var y,A;
for(var x=0,z=C.length;
x<z;
++x){y=C[x];
switch(y[0]){case"#":case"^":B.push(y);
D.push(y);
B=y[4]=[];
break;
case"/":A=D.pop();
A[5]=y[2];
B=D.length>0?D[D.length-1][4]:E;
break;
default:B.push(y)
}}return E
}function s(x){this.string=x;
this.tail=x;
this.pos=0
}s.prototype.eos=function(){return this.tail===""
};
s.prototype.scan=function(z){var y=this.tail.match(z);
if(!y||y.index!==0){return""
}var x=y[0];
this.tail=this.tail.substring(x.length);
this.pos+=x.length;
return x
};
s.prototype.scanUntil=function(z){var y=this.tail.search(z),x;
switch(y){case -1:x=this.tail;
this.tail="";
break;
case 0:x="";
break;
default:x=this.tail.substring(0,y);
this.tail=this.tail.substring(y)
}this.pos+=x.length;
return x
};
function p(y,x){this.view=y==null?{}:y;
this.cache={".":this.view};
this.parent=x
}p.prototype.push=function(x){return new p(x,this)
};
p.prototype.lookup=function(z){var x=this.cache;
var B;
if(z in x){B=x[z]
}else{var A=this,C,y;
while(A){if(z.indexOf(".")>0){B=A.view;
C=z.split(".");
y=0;
while(B!=null&&y<C.length){B=B[C[y++]]
}}else{B=A.view[z]
}if(B!=null){break
}A=A.parent
}x[z]=B
}if(b(B)){B=B.call(this.view)
}return B
};
function o(){this.cache={}
}o.prototype.clearCache=function(){this.cache={}
};
o.prototype.parse=function(z,y){var x=this.cache;
var A=x[z];
if(A==null){A=x[z]=w(z,y)
}return A
};
o.prototype.render=function(A,x,z){var B=this.parse(A);
var y=(x instanceof p)?x:new p(x);
return this.renderTokens(B,y,z,A)
};
o.prototype.renderTokens=function(F,x,D,I){var B="";
var J=this;
function y(K){return J.render(K,x,D)
}var z,G;
for(var C=0,E=F.length;
C<E;
++C){z=F[C];
switch(z[0]){case"#":G=x.lookup(z[1]);
if(!G){continue
}if(k(G)){for(var A=0,H=G.length;
A<H;
++A){B+=this.renderTokens(z[4],x.push(G[A]),D,I)
}}else{if(typeof G==="object"||typeof G==="string"){B+=this.renderTokens(z[4],x.push(G),D,I)
}else{if(b(G)){if(typeof I!=="string"){throw new Error("Cannot use higher-order sections without the original template")
}G=G.call(x.view,I.slice(z[3],z[5]),y);
if(G!=null){B+=G
}}else{B+=this.renderTokens(z[4],x,D,I)
}}}break;
case"^":G=x.lookup(z[1]);
if(!G||(k(G)&&G.length===0)){B+=this.renderTokens(z[4],x,D,I)
}break;
case">":if(!D){continue
}G=b(D)?D(z[1]):D[z[1]];
if(G!=null){B+=this.renderTokens(this.parse(G),x,D,G)
}break;
case"&":G=x.lookup(z[1]);
if(G!=null){B+=G
}break;
case"name":G=x.lookup(z[1]);
if(G!=null){B+=a.escape(G)
}break;
case"text":B+=z[1];
break
}}return B
};
a.name="mustache.js";
a.version="0.8.1";
a.tags=["{{","}}"];
var i=new o();
a.clearCache=function(){return i.clearCache()
};
a.parse=function(y,x){return i.parse(y,x)
};
a.render=function(z,x,y){return i.render(z,x,y)
};
a.to_html=function(A,y,z,B){var x=a.render(A,y,z);
if(b(B)){B(x)
}else{return x
}};
a.escape=m;
a.Scanner=s;
a.Context=p;
a.Writer=o
}));
/*!
	Colorbox v1.5.10 - 2014-06-26
	jQuery lightbox and modal window plugin
	(c) 2014 Jack Moore - http://www.jacklmoore.com/colorbox
	license: http://www.opensource.org/licenses/mit-license.php
*/
(function(aT,a8,a4){function aZ(a,d,c){var b=a8.createElement(a);
return d&&(b.id=ab+d),c&&(b.style.cssText=c),aT(b)
}function aY(){return a4.innerHeight?a4.innerHeight:aT(a4).height()
}function aV(b,a){a!==Object(a)&&(a={}),this.cache={},this.el=b,this.value=function(c){var d;
return void 0===this.cache[c]&&(d=aT(this.el).attr("data-cbox-"+c),void 0!==d?this.cache[c]=d:void 0!==a[c]?this.cache[c]=a[c]:void 0!==ad[c]&&(this.cache[c]=ad[c])),this.cache[c]
},this.get=function(d){var c=this.value(d);
return aT.isFunction(c)?c.call(this.el,this):c
}
}function a5(b){var c=ag.length,a=(aM+b)%c;
return 0>a?c+a:a
}function bd(a,b){return Math.round((/%/.test(a)?("x"===b?az.width():aY())/100:1)*parseInt(a,10))
}function aU(a,b){return a.get("photo")||a.get("photoRegex").test(b)
}function a1(a,b){return a.get("retinaUrl")&&a4.devicePixelRatio>1?b.replace(a.get("photoRegex"),a.get("retinaSuffix")):b
}function a9(a){"contains" in aN[0]&&!aN[0].contains(a.target)&&a.target!==aR[0]&&(a.stopPropagation(),aN.focus())
}function ba(a){ba.str!==a&&(aN.add(aR).removeClass(ba.str).addClass(a),ba.str=a)
}function a6(a){aM=0,a&&a!==!1&&"nofollow"!==a?(ag=aT("."+af).filter(function(){var b=aT.data(this,ac),c=new aV(this,b);
return c.get("rel")===a
}),aM=ag.index(bf.el),-1===aM&&(ag=ag.add(bf.el),aM=ag.length-1)):ag=aT(bf.el)
}function aS(a){aT(a8).trigger(a),aA.triggerHandler(a)
}function a7(b){var g;
if(!ax){if(g=aT(b).data(ac),bf=new aV(b,g),a6(bf.get("rel")),!aH){aH=aW=!0,ba(bf.get("className")),aN.css({visibility:"hidden",display:"block",opacity:""}),ar=aZ(aG,"LoadedContent","width:0; height:0; overflow:hidden; visibility:hidden"),bb.css({width:"",height:""}).append(ar),aB=aj.height()+a2.height()+bb.outerHeight(!0)-bb.height(),a3=aC.width()+aw.width()+bb.outerWidth(!0)-bb.width(),aF=ar.outerHeight(!0),ap=ar.outerWidth(!0);
var d=bd(bf.get("initialWidth"),"x"),c=bd(bf.get("initialHeight"),"y"),a=bf.get("maxWidth"),e=bf.get("maxHeight");
bf.w=(a!==!1?Math.min(d,bd(a,"x")):d)-ap-a3,bf.h=(e!==!1?Math.min(c,bd(e,"y")):c)-aF-aB,ar.css({width:"",height:bf.h}),au.position(),aS(bc),bf.get("onOpen"),ao.add(av).hide(),aN.focus(),bf.get("trapFocus")&&a8.addEventListener&&(a8.addEventListener("focus",a9,!0),aA.one(aO,function(){a8.removeEventListener("focus",a9,!0)
})),bf.get("returnFocus")&&aA.one(aO,function(){aT(bf.el).focus()
})
}aR.css({opacity:parseFloat(bf.get("opacity"))||"",cursor:bf.get("overlayClose")?"pointer":"",visibility:"visible"}).show(),bf.get("closeButton")?aE.html(bf.get("close")).appendTo(bb):aE.appendTo("<div/>"),aQ()
}}function aX(){!aN&&a8.body&&(ah=!1,az=aT(a4),aN=aZ(aG).attr({id:ac,"class":aT.support.opacity===!1?ab+"IE":"",role:"dialog",tabindex:"-1"}).hide(),aR=aZ(aG,"Overlay").hide(),ak=aT([aZ(aG,"LoadingOverlay")[0],aZ(aG,"LoadingGraphic")[0]]),aP=aZ(aG,"Wrapper"),bb=aZ(aG,"Content").append(av=aZ(aG,"Title"),al=aZ(aG,"Current"),an=aT('<button type="button"/>').attr({id:ab+"Previous"}),at=aT('<button type="button"/>').attr({id:ab+"Next"}),ay=aZ("button","Slideshow"),ak),aE=aT('<button type="button"/>').attr({id:ab+"Close"}),aP.append(aZ(aG).append(aZ(aG,"TopLeft"),aj=aZ(aG,"TopCenter"),aZ(aG,"TopRight")),aZ(aG,!1,"clear:left").append(aC=aZ(aG,"MiddleLeft"),bb,aw=aZ(aG,"MiddleRight")),aZ(aG,!1,"clear:left").append(aZ(aG,"BottomLeft"),a2=aZ(aG,"BottomCenter"),aZ(aG,"BottomRight"))).find("div div").css({"float":"left"}),aq=aZ(aG,!1,"position:absolute; width:9999px; visibility:hidden; display:none; max-width:none;"),ao=at.add(an).add(al).add(ay),aT(a8.body).append(aR,aN.append(aP,aq)))
}function a0(){function a(b){b.which>1||b.shiftKey||b.altKey||b.metaKey||b.ctrlKey||(b.preventDefault(),a7(this))
}return aN?(ah||(ah=!0,at.click(function(){au.next()
}),an.click(function(){au.prev()
}),aE.click(function(){au.close()
}),aR.click(function(){bf.get("overlayClose")&&au.close()
}),aT(a8).bind("keydown."+ab,function(b){var c=b.keyCode;
aH&&bf.get("escKey")&&27===c&&(b.preventDefault(),au.close()),aH&&bf.get("arrowKey")&&ag[1]&&!b.altKey&&(37===c?(b.preventDefault(),an.click()):39===c&&(b.preventDefault(),at.click()))
}),aT.isFunction(aT.fn.on)?aT(a8).on("click."+ab,"."+af,a):aT("."+af).live("click."+ab,a)),!0):!1
}function aQ(){var f,i,b,a=au.prep,g=++aK;
if(aW=!0,ai=!1,aS(be),aS(aJ),bf.get("onLoad"),bf.h=bf.get("height")?bd(bf.get("height"),"y")-aF-aB:bf.get("innerHeight")&&bd(bf.get("innerHeight"),"y"),bf.w=bf.get("width")?bd(bf.get("width"),"x")-ap-a3:bf.get("innerWidth")&&bd(bf.get("innerWidth"),"x"),bf.mw=bf.w,bf.mh=bf.h,bf.get("maxWidth")&&(bf.mw=bd(bf.get("maxWidth"),"x")-ap-a3,bf.mw=bf.w&&bf.w<bf.mw?bf.w:bf.mw),bf.get("maxHeight")&&(bf.mh=bd(bf.get("maxHeight"),"y")-aF-aB,bf.mh=bf.h&&bf.h<bf.mh?bf.h:bf.mh),f=bf.get("href"),am=setTimeout(function(){ak.show()
},100),bf.get("inline")){var j=aT(f);
b=aT("<div>").hide().insertBefore(j),aA.one(be,function(){b.replaceWith(j)
}),a(j)
}else{bf.get("iframe")?a(" "):bf.get("html")?a(bf.get("html")):aU(bf,f)?(f=a1(bf,f),ai=new Image,aT(ai).addClass(ab+"Photo").bind("error",function(){a(aZ(aG,"Error").html(bf.get("imgError")))
}).one("load",function(){g===aK&&setTimeout(function(){var c;
aT.each(["alt","longdesc","aria-describedby"],function(h,d){var k=aT(bf.el).attr(d)||aT(bf.el).attr("data-"+d);
k&&ai.setAttribute(d,k)
}),bf.get("retinaImage")&&a4.devicePixelRatio>1&&(ai.height=ai.height/a4.devicePixelRatio,ai.width=ai.width/a4.devicePixelRatio),bf.get("scalePhotos")&&(i=function(){ai.height-=ai.height*c,ai.width-=ai.width*c
},bf.mw&&ai.width>bf.mw&&(c=(ai.width-bf.mw)/ai.width,i()),bf.mh&&ai.height>bf.mh&&(c=(ai.height-bf.mh)/ai.height,i())),bf.h&&(ai.style.marginTop=Math.max(bf.mh-ai.height,0)/2+"px"),ag[1]&&(bf.get("loop")||ag[aM+1])&&(ai.style.cursor="pointer",ai.onclick=function(){au.next()
}),ai.style.width=ai.width+"px",ai.style.height=ai.height+"px",a(ai)
},1)
}),ai.src=f):f&&aq.load(f,bf.get("data"),function(d,c){g===aK&&a("error"===c?aZ(aG,"Error").html(bf.get("xhrError")):aT(this).contents())
})
}}var aR,aN,aP,bb,aj,aC,aw,a2,ag,az,ar,aq,ak,av,al,ay,at,an,aE,ao,bf,aB,a3,aF,ap,aM,ai,aH,aW,ax,am,au,ah,ad={html:!1,photo:!1,iframe:!1,inline:!1,transition:"elastic",speed:300,fadeOut:300,width:!1,initialWidth:"600",innerWidth:!1,maxWidth:!1,height:!1,initialHeight:"450",innerHeight:!1,maxHeight:!1,scalePhotos:!0,scrolling:!0,opacity:0.9,preloading:!0,className:!1,overlayClose:!0,escKey:!0,arrowKey:!0,top:!1,bottom:!1,left:!1,right:!1,fixed:!1,data:void 0,closeButton:!0,fastIframe:!0,open:!1,reposition:!0,loop:!0,slideshow:!1,slideshowAuto:!0,slideshowSpeed:2500,slideshowStart:"start slideshow",slideshowStop:"stop slideshow",photoRegex:/\.(gif|png|jp(e|g|eg)|bmp|ico|webp|jxr|svg)((#|\?).*)?$/i,retinaImage:!1,retinaUrl:!1,retinaSuffix:"@2x.$1",current:"image {current} of {total}",previous:"previous",next:"next",close:"close",xhrError:"This content failed to load.",imgError:"This image failed to load.",returnFocus:!0,trapFocus:!0,onOpen:!1,onLoad:!1,onComplete:!1,onCleanup:!1,onClosed:!1,rel:function(){return this.rel
},href:function(){return aT(this).attr("href")
},title:function(){return this.title
}},ac="colorbox",ab="cbox",af=ab+"Element",bc=ab+"_open",aJ=ab+"_load",aa=ab+"_complete",aL=ab+"_cleanup",aO=ab+"_closed",be=ab+"_purge",aA=aT("<a/>"),aG="div",aK=0,aD={},aI=function(){function l(){clearTimeout(g)
}function j(){(bf.get("loop")||ag[aM+1])&&(l(),g=setTimeout(au.next,bf.get("slideshowSpeed")))
}function f(){ay.html(bf.get("slideshowStop")).unbind(m).one(m,d),aA.bind(aa,j).bind(aJ,l),aN.removeClass(k+"off").addClass(k+"on")
}function d(){l(),aA.unbind(aa,j).unbind(aJ,l),ay.html(bf.get("slideshowStart")).unbind(m).one(m,function(){au.next(),f()
}),aN.removeClass(k+"on").addClass(k+"off")
}function c(){b=!1,ay.hide(),l(),aA.unbind(aa,j).unbind(aJ,l),aN.removeClass(k+"off "+k+"on")
}var b,g,k=ab+"Slideshow_",m="click."+ab;
return function(){b?bf.get("slideshow")||(aA.unbind(aL,c),c()):bf.get("slideshow")&&ag[1]&&(b=!0,aA.one(aL,c),bf.get("slideshowAuto")?f():d(),ay.show())
}
}();
aT[ac]||(aT(aX),au=aT.fn[ac]=aT[ac]=function(b,a){var d,c=this;
if(b=b||{},aT.isFunction(c)){c=aT("<a/>"),b.open=!0
}else{if(!c[0]){return c
}}return c[0]?(aX(),a0()&&(a&&(b.onComplete=a),c.each(function(){var e=aT.data(this,ac)||{};
aT.data(this,ac,aT.extend(e,b))
}).addClass(af),d=new aV(c[0],b),d.get("open")&&a7(c[0])),c):c
},au.position=function(o,j){function b(){aj[0].style.width=a2[0].style.width=bb[0].style.width=parseInt(aN[0].style.width,10)-a3+"px",bb[0].style.height=aC[0].style.height=aw[0].style.height=parseInt(aN[0].style.height,10)-aB+"px"
}var a,k,t,f=0,p=0,q=aN.offset();
if(az.unbind("resize."+ab),aN.css({top:-90000,left:-90000}),k=az.scrollTop(),t=az.scrollLeft(),bf.get("fixed")?(q.top-=k,q.left-=t,aN.css({position:"fixed"})):(f=k,p=t,aN.css({position:"absolute"})),p+=bf.get("right")!==!1?Math.max(az.width()-bf.w-ap-a3-bd(bf.get("right"),"x"),0):bf.get("left")!==!1?bd(bf.get("left"),"x"):Math.round(Math.max(az.width()-bf.w-ap-a3,0)/2),f+=bf.get("bottom")!==!1?Math.max(aY()-bf.h-aF-aB-bd(bf.get("bottom"),"y"),0):bf.get("top")!==!1?bd(bf.get("top"),"y"):Math.round(Math.max(aY()-bf.h-aF-aB,0)/2),aN.css({top:q.top,left:q.left,visibility:"visible"}),aP[0].style.width=aP[0].style.height="9999px",a={width:bf.w+ap+a3,height:bf.h+aF+aB,top:f,left:p},o){var m=0;
aT.each(a,function(c){return a[c]!==aD[c]?(m=o,void 0):void 0
}),o=m
}aD=a,o||aN.css(a),aN.dequeue().animate(a,{duration:o||0,complete:function(){b(),aW=!1,aP[0].style.width=bf.w+ap+a3+"px",aP[0].style.height=bf.h+aF+aB+"px",bf.get("reposition")&&setTimeout(function(){az.bind("resize."+ab,au.position)
},1),j&&j()
},step:b})
},au.resize=function(a){var b;
aH&&(a=a||{},a.width&&(bf.w=bd(a.width,"x")-ap-a3),a.innerWidth&&(bf.w=bd(a.innerWidth,"x")),ar.css({width:bf.w}),a.height&&(bf.h=bd(a.height,"y")-aF-aB),a.innerHeight&&(bf.h=bd(a.innerHeight,"y")),a.innerHeight||a.height||(b=ar.scrollTop(),ar.css({height:"auto"}),bf.h=ar.height()),ar.css({height:bf.h}),b&&ar.scrollTop(b),au.position("none"===bf.get("transition")?0:bf.get("speed")))
},au.prep=function(c){function h(){return bf.w=bf.w||ar.width(),bf.w=bf.mw&&bf.mw<bf.w?bf.mw:bf.w,bf.w
}function b(){return bf.h=bf.h||ar.height(),bf.h=bf.mh&&bf.mh<bf.h?bf.mh:bf.h,bf.h
}if(aH){var f,e="none"===bf.get("transition")?0:bf.get("speed");
ar.remove(),ar=aZ(aG,"LoadedContent").append(c),ar.hide().appendTo(aq.show()).css({width:h(),overflow:bf.get("scrolling")?"auto":"hidden"}).css({height:b()}).prependTo(bb),aq.hide(),aT(ai).css({"float":"none"}),ba(bf.get("className")),f=function(){function g(){aT.support.opacity===!1&&aN[0].style.removeAttribute("filter")
}var k,j,d=ag.length;
aH&&(j=function(){clearTimeout(am),ak.hide(),aS(aa),bf.get("onComplete")
},av.html(bf.get("title")).show(),ar.show(),d>1?("string"==typeof bf.get("current")&&al.html(bf.get("current").replace("{current}",aM+1).replace("{total}",d)).show(),at[bf.get("loop")||d-1>aM?"show":"hide"]().html(bf.get("next")),an[bf.get("loop")||aM?"show":"hide"]().html(bf.get("previous")),aI(),bf.get("preloading")&&aT.each([a5(-1),a5(1)],function(){var a,p=ag[this],m=new aV(p,aT.data(p,ac)),l=m.get("href");
l&&aU(m,l)&&(l=a1(m,l),a=a8.createElement("img"),a.src=l)
})):ao.hide(),bf.get("iframe")?(k=a8.createElement("iframe"),"frameBorder" in k&&(k.frameBorder=0),"allowTransparency" in k&&(k.allowTransparency="true"),bf.get("scrolling")||(k.scrolling="no"),aT(k).attr({src:bf.get("href"),name:(new Date).getTime(),"class":ab+"Iframe",allowFullScreen:!0}).one("load",j).appendTo(ar),aA.one(be,function(){k.src="//about:blank"
}),bf.get("fastIframe")&&aT(k).trigger("load")):j(),"fade"===bf.get("transition")?aN.fadeTo(e,1,g):g())
},"fade"===bf.get("transition")?aN.fadeTo(e,0,function(){au.position(0,f)
}):au.position(e,f)
}},au.next=function(){!aW&&ag[1]&&(bf.get("loop")||ag[aM+1])&&(aM=a5(1),a7(ag[aM]))
},au.prev=function(){!aW&&ag[1]&&(bf.get("loop")||aM)&&(aM=a5(-1),a7(ag[aM]))
},au.close=function(){aH&&!ax&&(ax=!0,aH=!1,aS(aL),bf.get("onCleanup"),az.unbind("."+ab),aR.fadeTo(bf.get("fadeOut")||0,0),aN.stop().fadeTo(bf.get("fadeOut")||0,0,function(){aN.hide(),aR.hide(),aS(be),ar.remove(),setTimeout(function(){ax=!1,aS(aO),bf.get("onClosed")
},1)
}))
},au.remove=function(){aN&&(aN.stop(),aT[ac].close(),aN.stop(!1,!0).remove(),aR.remove(),ax=!1,aN=null,aT("."+af).removeData(ac).removeClass(af),aT(a8).unbind("click."+ab).unbind("keydown."+ab))
},au.element=function(){return aT(bf.el)
},au.settings=ad)
})(jQuery,document,window);
(function(e,j,n,f){var b="jquery-lazyload-any";
var g="appear";
var d=b+"-"+g;
var i=":"+d;
var h=b+"-scroller";
var x=b+"-container";
var o=":"+x;
var u,p,r=false;
var t=50,k,l=e();
e.expr[":"][d]=function(y){return !!e(y).data(d)
};
e.expr[":"][x]=function(y){return !!e(y).data(x)
};
function s(){var y=e(this);
if(y.is(":visible")&&c(y)){y.trigger(g)
}}function c(B){var C=B[0].getBoundingClientRect();
var z=y1=-B.data(b).threshold;
var A=u-y1;
var y=p-z;
return(C.top>=y1&&C.top<=A||C.bottom>=y1&&C.bottom<=A)&&(C.left>=z&&C.left<=y||C.right>=z&&C.right<=y)
}function w(){u=j.innerHeight||n.documentElement.clientHeight;
p=j.innerWidth||n.documentElement.clientWidth;
a()
}function a(){e(i).each(s)
}function v(){var z=e(this);
var y=z.data(b);
var B=z.contents().filter(function(){return this.nodeType===8
}).get(0);
var A=e(B&&B.data.trim());
z.replaceWith(A);
if(typeof y!="undefined"&&e.isFunction(y.load)){y.load.call(A,A)
}}function m(){var y=e(this);
if(y.find(i).length==0){y.removeData(h);
y.removeData(x);
y.unbind("scroll",a).unbind(g,m)
}}function q(){l.find(i).each(s);
l=l.filter(o);
if(l.length==0){k=clearInterval(k)
}}e.fn.lazyload=function(z){var A={threshold:0,trigger:g};
e.extend(A,z);
var y=A.trigger.split(" ");
this.data(d,e.inArray(g,y)!=-1).data(b,A);
this.bind(A.trigger,v);
this.each(s);
this.parents().each(function(){var B=e(this);
if(!B.data(h)){var D=B.css("overflow");
if(D=="scroll"||D=="auto"){B.data(h,1);
B.bind("scroll",a);
if(!B.data(x)){B.bind(g,m)
}}}if(!B.data(x)){var C=B.css("display");
if(C=="none"){B.data(x,1);
if(!B.data(h)){B.bind(g,m)
}l=l.add(B);
if(t&&!k){k=setInterval(q,t)
}}}});
if(!r){r=true;
e(n).ready(function(){e(j).bind("resize",w).bind("scroll",a);
w()
})
}return this
};
e.lazyload={check:a,setInterval:function(y){if(y==t||!e.isNumeric(y)||y<0){return
}t=y;
k=clearInterval(k);
if(t>0){k=setInterval(q,t)
}}}
})(jQuery,window,document);
(function(c){var l={},b,m,e=document,j=window,i=e.documentElement,k=c.expando,a;
c.event.special.inview={add:function(d){l[d.guid+"-"+this[k]]={data:d,$element:c(this)};
if(!a&&!c.isEmptyObject(l)){a=setInterval(g,250)
}},remove:function(d){try{delete l[d.guid+"-"+this[k]]
}catch(n){}if(c.isEmptyObject(l)){clearInterval(a);
a=null
}}};
function h(){var o,d,n={height:j.innerHeight,width:j.innerWidth};
if(!n.height){o=e.compatMode;
if(o||!c.support.boxModel){d=o==="CSS1Compat"?i:e.body;
n={height:d.clientHeight,width:d.clientWidth}
}}return n
}function f(){return{top:j.pageYOffset||i.scrollTop||e.body.scrollTop,left:j.pageXOffset||i.scrollLeft||e.body.scrollLeft}
}function g(){var p=c(),o,n=0;
c.each(l,function(z,y){var w=y.data.selector,x=y.$element;
p=p.add(w?x.find(w):x)
});
o=p.length;
if(o){b=b||h();
m=m||f();
for(;
n<o;
n++){if(!c.contains(i,p[n])){continue
}var u=c(p[n]),v={height:u.height(),width:u.width()},d=u.offset(),q=u.data("inview"),s,r,t;
if(!m||!b){return
}if(d.top+v.height>m.top&&d.top<m.top+b.height&&d.left+v.width>m.left&&d.left<m.left+b.width){s=(m.left>d.left?"right":(m.left+b.width)<(d.left+v.width)?"left":"both");
r=(m.top>d.top?"bottom":(m.top+b.height)<(d.top+v.height)?"top":"both");
t=s+"-"+r;
if(!q||q!==t){u.data("inview",t).trigger("inview",[true,s,r])
}}else{if(q){u.data("inview",false).trigger("inview",[false])
}}}}}c(j).bind("scroll resize scrollstop",function(){b=m=null
});
if(!i.addEventListener&&i.attachEvent){i.attachEvent("onfocusin",function(){m=null
})
}})(jQuery);
var testEvent;
var testBullettin;
var EventList=(function(){var c="";
var f="";
var a=false;
var h;
var b;
var e=false;
var g=true;
function d(k,m,l,i,o,n,j,q,p){this.url=k;
this.selector=m;
this.lang=l;
this.langOverwrite=(i)?i:l;
this.view=o;
this.refresh=n;
this.pagination=true;
this.docsPerPage=j;
this.setTotalDocs();
this.currDocs=0;
this.page=0;
this.showDate=q;
this.bullettinlUrl=p;
if(!this.docsPerPage){this.pagination=false
}this.loading=false;
if(!this.selector){return
}this.setLocale();
this.getEvents("replace");
console.log("bullettinUrl: "+p)
}return d
})();
EventList.prototype.getEvents=function(d){var c=this;
var a="";
var b=c.url;
if(this.pagination){a="/page."+c.page+"."+c.docsPerPage;
if(c.hasSuffix(b)){render=c.getRender(b);
suffix=c.getSuffix(b);
b=c.getNavigationJsPath(render,suffix+a)
}else{b=c.getNavigationJsPath(b,a)
}}console.log("url"+b);
jQuery.ajax(b,{statusCode:{403:function(){},404:function(){}},dataType:"json"}).done(function(g){if(g.error!==undefined||g.events.length===0){c.buildNoEvent()
}else{if(c.refresh&&c.page===0){var f=JSON.stringify(g);
var e=CryptoJS.MD5(f);
c.notificaPush(e)
}c.buildList(g,d)
}}).fail(function(e){c.buildNoEvent()
});
if(c.pagination){c.initPagination()
}};
EventList.prototype.setTotalDocs=function(){var c=this;
var b="/count";
var a=c.url;
if(c.hasSuffix(a)){render=c.getRender(a);
suffix=c.getSuffix(a);
a=c.getNavigationJsPath(render,suffix+b)
}else{a=c.getNavigationJsPath(a,b)
}jQuery.ajax(a,{statusCode:{403:function(){},404:function(){}},dataType:"json",async:false}).done(function(d){if(d!==undefined){c.totDocs=d.total
}})
};
EventList.prototype.initPagination=function(){var a=this;
jQuery("#"+this.selector).delegate(".pagination-next","inview",function(c,b){if(b&&!a.loading){a.loading=true;
jQuery(this).removeClass("pagination-next");
setTimeout(function(){a.page=a.page+1;
a.getEvents("append");
jQuery(this).remove();
a.loading=false
},800)
}})
};
EventList.prototype.notificaPush=function(d){var c=this;
var a="";
var b=c.url;
if(c.pagination){a="/page.0."+c.docsPerPage;
if(c.hasSuffix(b)){render=c.getRender(b);
suffix=c.getSuffix(b);
b=c.getNavigationJsPath(render,suffix+a)
}else{b=c.getNavigationJsPath(b,a)
}}jQuery.ajax(b,{statusCode:{403:function(){},404:function(){}},dataType:"json"}).done(function(g){var f=JSON.stringify(g);
var e=CryptoJS.MD5(f);
if(JSON.stringify(d)===JSON.stringify(e)){setTimeout(function(){c.notificaPush(d)
},90000)
}else{this.setTotalDocs();
$("#refresh-button").css("display","block");
$("#refresh-button").click(function(){$("html,body").scrollTop(0);
$(this).css("display","none");
c.page=0;
c.getEvents("replace")
})
}})
};
EventList.prototype.createYear=function(j){var d="";
var i="";
var c=null;
var b=null;
var f={id:this.selector+"-content",pagination:this.pagination,monthsList:[]};
var e=this;
var h=new Intl.DateTimeFormat(e.lang,{month:"long"});
var a=new Intl.DateTimeFormat(e.lang,{month:"short"});
var g=new Intl.DateTimeFormat(e.lang,{weekday:"long"});
jQuery.each(j.events,function(o,w){var l=dateFromISO8601(w.start_date);
var q=h.format(l);
var k=a.format(l);
var m=g.format(l);
var t=l.getDate();
var s=l.getFullYear();
var p=l.getMonth()+1;
var v=window.location.pathname;
var n=e.getRender(v);
var u=e.getNavigationPagePath(n.replace("/year","/month"),"/"+s+"/"+p);
if(q!==d){c={monthName:q,monthPath:u,year:s,days:[]};
f.monthsList.push(c);
d=q;
i=""
}if(t!==i){var r=e.getNavigationPagePath(n.replace("year","day"),"/"+s+"/"+p+"/"+t);
b={dayNum:l.getDate("dd"),monthShort:k,dayOfWeek:m,year:l.getFullYear(),destDay:r,events:[]};
c.days.push(b);
i=t
}b.events.push(e.getEvent(w,e.lang))
});
f.monthsList.reverse();
jQuery.each(f.monthsList,function(k,l){l.days.reverse();
jQuery.each(l.days,function(n,m){m.events.reverse()
})
});
return f
};
EventList.prototype.createMonth=function(c){var a="";
var g={id:this.selector+"-content",pagination:this.pagination,daysList:[]};
var b={};
var f=this;
var e=new Intl.DateTimeFormat(f.lang,{month:"long"});
var d=new Intl.DateTimeFormat(f.lang,{month:"short"});
var h=new Intl.DateTimeFormat(f.lang,{weekday:"long"});
jQuery.each(c.events,function(n,u){var l=dateFromISO8601(u.start_date);
var s=l.getDate("dd");
var r=l.getFullYear();
var o=l.getMonth()+1;
var p=e.format(l);
var j=d.format(l);
var k=h.format(l);
if(s!==a){var t=window.location.pathname;
var m=f.getRender(t);
var q=f.getNavigationPagePath(m.replace("/month","/day"),"/"+r+"/"+o+"/"+s);
b={dayNum:l.getDate("dd"),monthShort:j,dayOfWeek:k,year:l.getFullYear(),destDay:q,events:[]};
g.daysList.push(b);
a=s
}b.events.push(f.getEvent(u,f.lang))
});
g.daysList.reverse();
jQuery.each(g.daysList,function(k,j){j.events.reverse()
});
return g
};
EventList.prototype.createDay=function(b){var a={id:this.selector+"-content",pagination:this.pagination,events:[]};
var c=this;
jQuery.each(b.events,function(d,f){var e=c.getEvent(f,c.lang);
e.index=c.totDocs-c.currDocs;
e.showDate=c.showDate;
c.currDocs++;
a.events.push(e)
});
a.events.reverse();
return a
};
EventList.prototype.createTopic=function(a){return this.createDay(a)
};
EventList.prototype.createLast=function(c){var d=this;
var a="";
var b=null;
var e={id:this.selector+"-content",pagination:this.pagination,daysList:[]};
var d=this;
jQuery.each(c.events,function(g,h){var f=dateFromISO8601(h.start_date);
var j=jQuery.datepicker.formatDate("dd - m - yy",f);
if(j!==a){b={day:j,events:[]};
e.daysList.push(b);
a=j
}b.events.push(d.getEvent(h,d.lang))
});
return e
};
EventList.prototype.createLast_and_ClientBullettins=function(c){var d=this;
var a="";
var b=null;
var e={id:this.selector+"-content",pagination:this.pagination,daysList:[]};
var d=this;
jQuery.each(c.events,function(h,j){var g=dateFromISO8601(j.start_date);
var f=jQuery.datepicker.formatDate("yy-mm-dd",g);
var k=jQuery.datepicker.formatDate("dd - m - yy",g);
if(k!==a){b={day:k,events:[]};
e.daysList.push(b);
a=k
}if(j.type=="pressBullettins"){b.events.push(d.getEventToBullettin(j,d.lang))
}else{b.events.push(d.getEvent(j,d.lang))
}});
return e
};
EventList.prototype.createLatest=function(c){var a="";
var e={id:this.selector+"-content",pagination:this.pagination,daysList:[]};
var b={};
var d=this;
jQuery.each(c.events,function(k,r){var h=dateFromISO8601(r.start_date);
var p=h.getDate("dd");
var o=h.getFullYear();
var l=h.getMonth()+1;
var m=jQuery.datepicker.formatDate("MM",h);
var f=jQuery.datepicker.formatDate("M",h);
var g=jQuery.datepicker.formatDate("DD",h);
if(p!==a){var q=window.location.pathname;
var j=d.getRender(q);
var n=d.getNavigationPagePath(j.replace("/latest","/day"),"/"+o+"/"+l+"/"+p);
b={dayNum:h.getDate("dd"),monthShort:f,dayOfWeek:g,year:h.getFullYear(),destDay:n,events:[]};
e.daysList.push(b);
a=p
}b.events.push(d.getEvent(r,d.lang))
});
return e
};
EventList.prototype.createCurrentMonth=function(c){var a="";
var e={id:this.selector+"-content",pagination:this.pagination,daysList:[]};
var b={};
var d=this;
jQuery.each(c.events,function(k,r){var h=dateFromISO8601(r.start_date);
var p=h.getDate("dd");
var o=h.getFullYear();
var l=h.getMonth()+1;
var m=jQuery.datepicker.formatDate("MM",h);
var f=jQuery.datepicker.formatDate("M",h);
var g=jQuery.datepicker.formatDate("DD",h);
if(p!==a){var q=window.location.pathname;
var j=d.getRender(q);
var n=d.getNavigationPagePath(j.replace("/thismonth","/day"),"/"+o+"/"+l+"/"+p);
b={dayNum:h.getDate("dd"),monthShort:f,dayOfWeek:g,year:h.getFullYear(),destDay:n,events:[]};
e.daysList.push(b);
a=p
}b.events.push(d.getEvent(r,d.lang))
});
return e
};
EventList.prototype.setLocale=function(){var a=jQuery.datepicker.regional[this.langOverwrite];
if(typeof a=="undefined"){a=jQuery.datepicker.regional.en
}jQuery.datepicker.setDefaults(a)
};
EventList.prototype.createListDays=function(a){var b=this;
var c={id:this.selector+"-content",pagination:this.pagination,days:[]};
jQuery.each(a.events,function(f,g){var e=dateFromISO8601(g.startDateTime);
g.dayName=jQuery.datepicker.formatDate("DD",e);
g.startDate=jQuery.datepicker.formatDate("d MM yy",e);
var d={startDate:g.startDate,dayName:g.dayName,dayUrl:g.dayUrl,daySelected:(location.pathname==g.dayUrl)};
c.days.push(d)
});
return c
};
EventList.prototype.createListTags=function(a){var b=this;
var c={id:this.selector+"-content",pagination:this.pagination,tags:[]};
jQuery.each(a.events,function(e,f){var d={tagName:f.tagName,tagTitle:f.tagTitle,tagUrl:f.tagUrl,tagSelected:(location.pathname==f.tagUrl)};
c.tags.push(d)
});
return c
};
EventList.prototype.addZero=function(a){if(a<10){a="0"+a
}return a
};
EventList.prototype.getUrl=function(d){if((d.type!=null&&d.type=="link")&&d.externallink.length>0){var b=d.externallink[0].indexOf("|");
var c=d.externallink[0];
var a=c.substring(b+1,c.length)
}else{var a=d.contentUrl
}return a
};
EventList.prototype.getEvent=function(n,d){var j=this;
var f=dateFromISO8601(n.start_date);
var e={weekday:"long",year:"numeric",month:"long",day:"numeric"};
var c=n.owner;
var m=j.getUrl(n);
var k=j.addZero(f.getHours())+":"+j.addZero(f.getMinutes());
var g=jQuery.datepicker.formatDate("dd MM yy",f)+" - "+k;
var a={eventPath:n.contentUrl,eventTitle:n.title,eventGeolocal:n.geolocal,eventDate:k,isoDate:n.start_date,startDate:jQuery.datepicker.formatDate("dd MM yy",f)+" - "+k,ownerPath:m,type:n.type,socialUrl:"http://"+window.location.hostname+n.contentUrl,detailUrl:n.contentUrl};
if(n.subtitle!=null&&n.subtitle.length>0){a.existSubtitle={subtitle:n.subtitle}
}if(n.langs!=null&&n.langs.length>0){a.existLangs={langs:n.langs};
n.langs[n.langs.length-1]["last"]=true;
$.each(n.langs,function(q,p){var o=j.getUrl(p);
n.langs[q]["ownerPath"]=o
})
}if(n.embedcode!=null&&n.embedcode.length>0){a.embedcode=n.embedcode;
a.hasEmbed=true
}if(n.description!=null&&n.description.length>0){a.description=n.description;
a.hasDescription=true
}var h=false;
if(n.attachments!=null&&n.attachments.length>0){a.attachments=true;
h=true
}if(n.externallink!=null&&n.externallink.length>0){a.externallink=true;
var i=n.externallink[0].split("|");
a.link=i[1];
h=true
}else{if(n.urlsite!=null){a.externallink=true;
a.link=n.urlsite;
h=true
}}if(n.photos!=null&&n.photos.length>0){a.photos=true;
var l=n.photos[0].split(".").pop();
if(l==="jpg"){l="jpeg"
}a.foto=n.photos[0].indexOf("/content/dam/")!=-1?this.getLazyPhoto(n.photos[0]+"/_jcr_content/renditions/cq5dam.web.1280.1280."+l):this.getLazyPhoto(n.photos[0]);
h=true
}if(n.videos!=null&&n.videos.length>0){a.videos=true;
var b=n.videos[0].split("|");
if(typeof b!="undefined"&&b.length>0){a.firstVideo=this.getEmbedVideo(b[1]);
h=true
}}if(n.galleries!=null&&n.galleries.length>0){a.galleries=true;
h=true
}a.existRelated=h;
if(n.type=="foto"||(n.photos!=null&&n.photos.length>0)){a.hasFoto=true
}if(n.type=="link"){if(typeof a.link!="undefined"&&$.trim(a.link)!=""){a.socialUrl=a.link;
a.detailUrl=a.link
}a.isNotEmpty=true
}else{if((n.pages!=null&&n.pages.length>0)||(h)||(n.description!=null&&n.description.length>0)){a.isNotEmpty=true
}}a.socialUrlEnc=encodeURIComponent(a.socialUrl);
a.eventTitleEnc=encodeURIComponent(a.eventTitle);
if(n.tags!=null&&n.tags.length>0){a.hasTags=true;
a.tags=n.tags
}console.log("hiddenTime");
if(n.hiddenTime!=null&&n.hiddenTime==="true"){a.eventDate="";
a.hiddenTimeClass="hidden_time"
}return a
};
EventList.prototype.getEventToBullettin=function(f){var e=this;
var b=dateFromISO8601(f.start_date);
var a=e.addZero(b.getHours())+":"+e.addZero(b.getMinutes());
var c=jQuery.datepicker.formatDate("dd MM yy",b)+" - "+a;
var d={eventPath:f.path,eventTitle:f.label,eventGeolocal:f.geolocal,eventDate:a,isoDate:f.start_date,ownerPath:f.link,startDate:jQuery.datepicker.formatDate("dd MM yy",b)+" - "+a,};
if(f.link!=null&&f.link.length>0){d.externallink=true;
d.link=f.link
}d.isNotEmpty=true;
d.eventTitleEnc=encodeURIComponent(d.eventLabel);
return d
};
EventList.prototype.getLazyPhoto=function(a){return'    <figure><img src="'+a+'" /></figure>'
};
EventList.prototype.getEmbedVideo=function(c){var b=new RegExp("http.*youtube.*\\?v=([a-zA-Z0-9_\\-]+)(&?)(.*)");
var a=b.exec(c);
if(a!=null&&a.length>0){return'<div class="lazyload"><!--    <iframe src="//www.youtube.com/embed/'+a[1]+'?rel=0" frameborder="0" allowfullscreen></iframe>--></div>'
}else{return""
}};
EventList.prototype.buildList=function(a,c){if(this.view==="year"){this.render(Mustache.render(EventList.Template.YEAR(),this.createYear(a)),c)
}else{if(this.view==="month"){this.render(Mustache.render(EventList.Template.MONTH(),this.createMonth(a)),c)
}else{if(this.view==="day"){this.render(Mustache.render(EventList.Template.DAY(),this.createDay(a)),c)
}else{if(this.view==="last"){this.render(Mustache.render(EventList.Template.LAST(),this.createLast(a)),c)
}else{if(this.view==="latest"){this.render(Mustache.render(EventList.Template.LATEST(),this.createLatest(a)),c)
}else{if(this.view==="mesecorrente"){this.render(Mustache.render(EventList.Template.LATEST(),this.createCurrentMonth(a)),c)
}else{if(this.view==="topic-list-days"){this.render(Mustache.render(EventList.Template.LIST_DAYS(),this.createListDays(a)),c)
}else{if(this.view==="topic-list-tags"){this.render(Mustache.render(EventList.Template.LIST_TAGS(),this.createListTags(a)),c)
}else{if(this.view.indexOf("topic")!=-1){this.render(Mustache.render(EventList.Template.TOPIC(),this.createTopic(a)),c)
}else{if(this.view==="last_and_client_bulletin"){var b=this;
jQuery.ajax({type:"GET",dataType:"jsonp",async:false,timeout:5000,jsonpCallback:"pressVatican",url:b.bullettinlUrl,error:function(d,f,e){b.render(Mustache.render(EventList.Template.LAST(),b.createLast(a)),c)
},success:function(d){jQuery.each(d.bullettin[0],function(e,f){a.events.push(f)
});
a.events.sort(function(f,e){return(new Date(f.start_date).getTime()<new Date(e.start_date).getTime())?+1:-1
});
testEvent=a;
b.render(Mustache.render(EventList.Template.LAST(),b.createLast_and_ClientBullettins(a)),c)
}})
}}}}}}}}}}$(".lazyload").lazyload({threshold:200});
if($(".siv-maincontainer.vaticanevents").length>0){setTimeout(function(){scrollToCurrentDate()
},400)
}};
EventList.prototype.render=function(a,c){jQuery("#"+this.selector+" .spinner").hide();
var b=jQuery("#"+this.selector+" .eventlist");
if(c==="append"){b.append(a)
}else{b.html(a)
}};
EventList.prototype.buildNoEvent=function(){jQuery("#"+this.selector+" .spinner").hide();
var b=jQuery(this.selector+" .eventlist");
var a=Mustache.render(EventList.NO_EVENT);
b.append(a);
jQuery("#"+this.selector).append(b)
};
EventList.prototype.load=function(a){a.fadeOut(0,function(){a.fadeIn(1000)
})
};
function dateFromISO8601(f){var d=f.match(/\d+/g);
var c=Date.UTC(d[0],d[1]-1,d[2],d[3],d[4],d[5]);
var a=new Date(c);
var e=a.getTimezoneOffset()*60000;
utc=c+e;
offset=0;
var b=utc+(3600000*offset);
return new Date(b)
}EventList.prototype.getNavigationPagePath=function(b,a){path="";
if(b&&b!=""&&a&&a!=""){path=this.clearPagePath(b)+".dir.html"+this.clearPagePath(a)+".html"
}else{if(b!=null){path=this.clearPagePath(b)+".html"
}}return path
};
EventList.prototype.getNavigationJsPath=function(b,a){if(b&&b!=""&&a&&a!=""){path=this.clearJsPath(b)+".dir.js"+this.clearJsPath(a)+".json"
}else{if(b!=null){path=this.clearJsPath(b)+".js"
}}return path
};
EventList.prototype.clearPagePath=function(a){if(a){a=a.replace(".dir.html","").replace(".dir","").replace(".html","")
}return a
};
EventList.prototype.clearJsPath=function(a){if(a){a=a.replace(".dir.js","").replace(".dir","").replace(".json","").replace(".js","")
}return a
};
EventList.prototype.clearPath=function(a){a=this.clearPagePath(a);
a=this.clearJsPath(a);
return a
};
EventList.prototype.hasSuffix=function(a){if(a&&(a.indexOf(".html/")>0||a.indexOf(".js/")>0||a.indexOf(".json/")>0)){return true
}else{return false
}};
EventList.prototype.getRender=function(a){if(a){if(a.indexOf(".html/")>0){render=a.substring(0,a.indexOf(".html/"))
}else{if(a.indexOf(".js/")>0){render=a.substring(0,a.indexOf(".js/"))
}else{if(a.indexOf(".json/")>0){render=a.substring(0,a.indexOf(".json/"))
}}}}return this.clearPath(render)
};
EventList.prototype.getSuffix=function(a){if(a){if(a.indexOf(".html/")>0){suffix=a.substring(a.indexOf(".html/")+5)
}else{if(a.indexOf(".js/")>0){suffix=a.substring(a.indexOf(".js/")+3)
}else{if(a.indexOf(".json/")>0){suffix=a.substring(a.indexOf(".json/")+5)
}}}}return this.clearPath(suffix)
};
function scrollToCurrentDate(){var d=new Date();
var c=d.getFullYear();
var b=d.getMonth()+1;
var f=d.getDate();
var e="/"+c+"/"+b+"/"+f+".html";
var i=jQuery('a[href*="'+e+'"]').first();
if(i.length===0){var h="/"+c+"/"+b+".html";
i=jQuery('a[href*="'+h+'"]').first()
}if(i.length>0){var j=i.closest(".day").length?i.closest(".day"):i.closest(".month");
if(j.length>0){jQuery("html, body").animate({scrollTop:j.offset().top-100},400)
}}}window.EventList.Template={BASE:"/content/%OWNER%/%LANG%/events/event.html%PATH%",BLANK:"/content/%OWNER%/%LANG%/events/eventblank.html%PATH%",YEAR:function(){return'{{#monthsList}}<div class="month"><h2><a href="{{monthPath}}">{{monthName}} {{year}}</a></h2>  <ul>    {{#days}}      <li>         <a name="{{dayNum}}"></a>         <div class="day">           <a href="{{destDay}}">                <div class="baloon">                    <div class="bday">{{dayNum}}</div>                    <div class="bweek">{{{dayOfWeek}}}</div>                </div>           </a>           <ul>             {{#events}}               <li>                 <div class="event">                   <div class="info">                     <div class="title">                        {{#isNotEmpty}}<a href="{{ownerPath}}">{{{eventTitle}}}</a>{{/isNotEmpty}}                        {{^isNotEmpty}}<span>{{{eventTitle}}}</span>{{/isNotEmpty}}                     </div>                     <div class="subtitle date"><p>{{eventDate}}</p></div><div class="subtitle location"><p>{{eventGeolocal}}</p></div>                   </div>                   <div class="resources">                   </div>                   <div class="clear"></div>                 </div>               </li>             {{/events}}           </ul>         </div>      </li>    {{/days}}  </ul></div>{{/monthsList}}{{#pagination}}<div class="pagination-next spinner"></div>{{/pagination}}'
},MONTH:function(){return'{{#daysList}}  <div class="day">    <a href="{{destDay}}">        <div class="baloon">            <div class="bday">{{dayNum}}</div>            <div class="bweek">{{{dayOfWeek}}}</div>        </div>    </a>    <ul>      {{#events}}        <li>          <div class="event">            <div class="info">              <div class="title">                {{#isNotEmpty}}<a href="{{ownerPath}}">{{{eventTitle}}}</a>{{/isNotEmpty}}                {{^isNotEmpty}}<span>{{{eventTitle}}}</span>{{/isNotEmpty}}              </div>              <div class="subtitle date {{hiddenTimeClass}}"><p> {{eventDate}}   </p></div><div class="subtitle location"><p>{{eventGeolocal}}</p></div>            </div>            <div class="resources"></div>            <div class="clear"></div>          </div>        </li>      {{/events}}    </ul>  </div>{{/daysList}}{{#pagination}}<div class="pagination-next spinner"></div>{{/pagination}}'
},DAY:function(){return'<ul>  {{#events}}    <li>      <div class="event">        <div class="info">          <div class="title">                {{#isNotEmpty}}<a href="{{ownerPath}}">{{{eventTitle}}}</a>{{/isNotEmpty}}                {{^isNotEmpty}}<span>{{{eventTitle}}}</span>{{/isNotEmpty}}          </div>          <div class="subtitle date"><p> {{eventDate}}   </p></div><div class="subtitle location"><p>{{eventGeolocal}}</p></div>        </div>        <div class="resources">        </div>        <div class="clear"></div>      </div>    </li>  {{/events}}</ul>{{#pagination}}<div class="pagination-next spinner"></div>{{/pagination}}'
},LAST:function(){return'  {{#daysList}}    <section class="event">      <h2 class="assistive-text">{{day}}</h2>      <time>{{day}}</time>         {{#events}}          <article>            <h2>              {{#isNotEmpty}}<a href="{{ownerPath}}">{{/isNotEmpty}}{{{eventTitle}}}{{#isNotEmpty}}</a>{{/isNotEmpty}}            </h2>            {{#existSubtitle}}               <h2>                   <a href="{{ownerPath}}">{{{subtitle}}}</a>               </h2>            {{/existSubtitle}}          </article>        {{/events}}    </section>  {{/daysList}}  {{#pagination}}<div class="pagination-next spinner"></div>{{/pagination}}'
},LATEST:function(){return'{{#daysList}}  <div class="day">    <a href="{{destDay}}">        <div class="baloon">            <div class="bday">{{dayNum}}</div>            <div class="bweek">{{{dayOfWeek}}}</div>        </div>    </a>    <ul>      {{#events}}        <li>          <div class="event">            <div class="info">              <div class="title">                {{#isNotEmpty}}<a href="{{ownerPath}}">{{{eventTitle}}}</a>{{/isNotEmpty}}                {{^isNotEmpty}}<span>{{{eventTitle}}}</span>{{/isNotEmpty}}              </div>              <div class="subtitle date"><p> {{eventDate}}   </p></div><div class="subtitle location"><p>{{eventGeolocal}}</p></div>            </div>            <div class="resources"></div>            <div class="clear"></div>          </div>        </li>      {{/events}}    </ul>  </div>{{/daysList}}{{#pagination}}<div class="pagination-next spinner"></div>{{/pagination}}'
},TOPIC:function(){return'<section>       {{#events}}           <article class="type-{{type}}">               <header>                   {{#hideDate}}<time datetime="{{isoDate}}">{{startDate}}</time>{{/hideDate}}                   <div class="item-number">{{index}}</div>               </header>               <h2><a href="{{{detailUrl}}}">{{{eventTitle}}}</a></h2>               {{#hasDescription}}<div class="text">{{{description}}}</div>{{/hasDescription}}               {{#hasFoto}}{{{foto}}}{{/hasFoto}}               {{#hasEmbed}}                   <div class="embed-container">{{{embedcode}}}</div>               {{/hasEmbed}}               {{#videos}}                   <div class="embed-container">{{{firstVideo}}}</div>               {{/videos}}               {{#hasTags}}               <ul class="tags">               {{#tags}}                   <li><a href="{{url}}">#{{title}}</a></li>               {{/tags}}               </ul>               {{/hasTags}}               <footer>                   <div class="author">{{{startDate}}}</div>                   <div class="event-share"><a href="#">share</a></div>               </footer>	            <aside class="share-layer">                   <ul>                       <li class="share-fb"><a href="javascript:window.open(\'https://www.facebook.com/sharer/sharer.php?u={{{socialUrlEnc}}}\', \'width=670, height=340\');" title="Share on Facebook"></a></li>                       <li class="share-tw"><a href="javascript:window.open(\'https://x.com/intent/tweet?text={{{eventTitleEnc}}}&amp;url={{{socialUrlEnc}}}\', \'width=670, height=340\');" title="Share on Twitter"></a></li>                       <li class="share-mail"><a href="mailto:?subject={{{eventTitleEnc}}}&amp;body={{{socialUrlEnc}}}" title="Share via email"></a></li>                       <li class="share-link"><a href="{{{socialUrl}}}"></a></li>                   </ul>                   <div class="share-txt-link"><input type="text" value="{{{socialUrl}}}" readonly></div>                  <div class="share-close"><a href="#">close</a></div>               </aside>           </article>      {{/events}}      {{#pagination}}<div class="pagination-next spinner"></div>{{/pagination}}   </section>'
},LIST_DAYS:function(){return'<div class="swiper-container" id="listday-swiper-container">   <div class="swiper-wrapper">       {{#days}}          <div class="swiper-slide{{#daySelected}} day-selected{{/daySelected}}">              <a href="{{{dayUrl}}}"><div>{{dayName}},</div> {{startDate}}</a>          </div>       {{/days}}   </div></div><div class="daylist-pagination"></div><script>TopicListDays.main()<\/script>'
},LIST_TAGS:function(){return'<ul class="tags">       {{#tags}}          <li class="{{#tagSelected}} tag-selected{{/tagSelected}}">              <a href="{{{tagUrl}}}">#{{tagTitle}}</a>          </li>       {{/tags}}   </ul>'
},NO_EVENT:function(){return"<p>NO EVENT</p>"
}};
var showDate=new Date();
var dates=[];
var datePickerSelector="#datepicker";
jQuery(document).ready(function(){if(typeof window.eventCalendarConfig!="undefined"){if(window.eventCalendarConfig.day!=-1){showDate.setDate(window.eventCalendarConfig.day)
}if(window.eventCalendarConfig.month!=-1){showDate.setMonth(window.eventCalendarConfig.month-1)
}if(window.eventCalendarConfig.year!=-1){showDate.setYear(window.eventCalendarConfig.year)
}getAvailableDays(showDate.getFullYear(),(showDate.getMonth()+1));
jQuery.datepicker.setDefaults(jQuery.datepicker.regional[window.eventCalendarConfig.lang]);
jQuery(window.datePickerSelector).datepicker({defaultDate:showDate,dateFormat:"yy/mm/dd",firstDay:0,onSelect:linkToEvents,beforeShowDay:disableNotAvailableDays,onChangeMonthYear:getAvailableDays})
}});
function linkToEvents(f,e){var b=new Date(f);
var g=b.getDate();
var a=b.getMonth()+1;
var h=b.getFullYear();
var c=h+"/"+a+"/"+g;
window.location.href=window.eventCalendarConfig.contentRootUrl+"/day.dir.html/"+c+".html"
}function disableNotAvailableDays(b){var a=dateToString(b);
return[jQuery.inArray(a,dates)!=-1]
}function navigateFromCalendar(a,b){jQuery(window.datePickerSelector+" .ui-datepicker-month").live("click",function(){window.location.href=window.eventCalendarConfig.contentRootUrl+"/month.dir.html/"+a+"/"+b+".html"
});
jQuery(window.datePickerSelector+" .ui-datepicker-year").live("click",function(){window.location.href=window.eventCalendarConfig.contentRootUrl+"/year.dir.html/"+a+".html"
})
}function getAvailableDays(d,f){var e=window.eventCalendarConfig.baseUrl;
var b=window.eventCalendarConfig.owner;
var a=".events";
if(eventCalendarConfig.filter!=null&&jQuery.trim(window.eventCalendarConfig.filter).length>0){a=a+"."+window.eventCalendarConfig.filter
}var c=e+"/"+window.eventCalendarConfig.lang+"/"+d+"/"+f+".events."+b+".js";
navigateFromCalendar(d,f);
jQuery.ajax({statusCode:{403:function(){},404:function(){}},url:c,type:"GET",dataType:"json",success:function(l){var k=l.events;
for(var j=0;
j<k.length;
j++){var h=k[j];
var g=new Date(h.start_date);
var m=dateToString(g);
if(jQuery.inArray(m,dates)){dates.push(m)
}}}}).done(function(g){jQuery("#navigationToday a").attr("href",window.eventCalendarConfig.contentRootUrl+"/day.dir.html/"+currentDateToString(new Date)+".html");
jQuery(window.datePickerSelector).datepicker("refresh")
})
}function dateToString(b){var c=b.getDate();
var a=b.getMonth()+1;
var e=b.getFullYear();
return e+"-"+a+"-"+c
}function currentDateToString(){var b=new Date();
var c=b.getDate();
var a=b.getMonth()+1;
var e=b.getFullYear();
return e+"/"+a+"/"+c
}window.Translation={url:"",selector:"",viewCallback:"Translation.Template.defaultTemplate",emptyCallback:"Translation.Template.defaultEmpty",init:function(c,a,b,d){this.url=c;
this.selector=a;
if(b!=null&&typeof b!="undefined"){this.viewCallback=b
}if(!this.selector){return
}this.getLanguages()
},getLanguages:function(){var a=this;
var b=this.getSiteName(this.url);
if(typeof b!="undefined"){jQuery.ajax("/content/"+b+"/crosslang.service.js"+this.url,{dataType:"json"}).done(function(c){if(c&&typeof c.translations!=="undefined"&&c.translations.length>0){a.build(c.translations)
}else{a.buildEmpty()
}}).fail(function(){a.buildEmpty()
})
}else{this.buildEmpty()
}},buildEmpty:function(){var fn=eval(this.emptyCallback);
fn(this.selector)
},build:function(translations){var fn=eval(this.viewCallback);
fn(translations,this.selector)
},getSiteName:function(b){if(typeof b!="undefined"){var a=b.split("/");
if(a.length>2){return a[2]
}}return null
}};
window.Translation.Template={defaultEmpty:function(a){var b=jQuery(a);
b.empty().hide().addClass("translation-empty");
var e=b.closest(".info_pages");
var c=e.find(".translation").length;
var d=e.find(".translation.translation-empty").length;
if(c>0&&c===d){var f=e.prevAll(".info_subtitle").first();
f.prevAll("hr.event-hr").first().hide();
f.hide()
}},defaultTemplate:function(c,b){var a={IT:"Italiano",EN:"English",FR:"Français",DE:"Deutsch",ES:"Español",PT:"Português",PL:"Polski",BE:"Беларуская",AR:"العربيَّة",RU:"Русский",UK:"Українська",LA:"Latina",CS:"Čeština",EL:"Ελληνικά",SQ:"Shqip",SL:"Slovenščina",SK:"Slovenčina",VI:"Tiếng Việt",TA:"தமிழ்",TR:"Türkçe",ZH_CN:"简体中文",ZH_TW:"繁體中文"};
var d='<p class="lang">';
if(c.length>0){jQuery.each(c,function(h,l){var i=l.locale.toUpperCase();
var g="";
if(a[i]){g=a[i]
}else{try{var f=i.replace("_","-");
var k=new Intl.DisplayNames([f],{type:"language"});
g=k.of(f);
g=g.charAt(0).toUpperCase()+g.slice(1)
}catch(j){g=i.toUpperCase()
}}d+='<a href="'+l.path+'.html">'+g+"</a>";
if(h!=c.length-1){d+=" - "
}});
d+="</p>";
var e=b+" .lang";
jQuery(b).html(d).show();
jQuery(e).show()
}}};
function getPageJson(c){var b=c+".3.json";
var a;
jQuery.ajax({statusCode:{403:function(){},404:function(){}},type:"GET",dataType:"json",url:b,async:false,success:function(d){a=d
}});
return a
}function getTitle(b){try{var c=b["jcr:content"];
var a=c["jcr:title"];
if(typeof c!="undefined"&&a!="undefined"){return a
}}catch(d){}}function getPageTitle(a){var c=a["jcr:content"];
var b=c.pageTitle;
if(typeof b!="undefined"&&b!=null&&b.trim().length>0){return b
}else{return getTitle(a)
}}function getEventDate(){var d=json["jcr:content"];
var a=d.eventDate;
if(typeof a!="undefined"&&a!=null&&a.trim().length>0){var c=new Date(a);
var e="<%= lang %>";
var b={weekday:"long",year:"numeric",month:"short",day:"numeric",hour:"2-digit",minute:"2-digit"};
return c.toLocaleTimeString(e,b)
}else{return getTitle(json)
}}function getSection(){var b=json["jcr:content"];
var a=b.sectionName;
if(typeof a!="undefined"&&a!=null&&a.length>0){return a[0]
}else{return getTitle(json)
}}function getSubSection(){var a=json["jcr:content"];
var b=a.subSectionName;
if(typeof b!="undefined"&&b!=null&&b.length>0){return b
}else{return getTitle(json)
}}function deduceTitle(b){var a="<%= outputValue %>";
var c;
if(a=="title"){c=getTitle(b)
}else{if(a=="pagetitle"){c=getPageTitle(b)
}else{if(a=="date"){c=getEventDate(b)
}else{if(a=="section"){c=getSection(b)
}else{if(a=="subsection"){c=getSubSection(b)
}else{c=getTitle(b)
}}}}}return c
}function loadGallery(){jQuery("#info_galleries ul li a").each(function(){var a=jQuery(this).attr("data-json");
if(typeof a!="undefined"&&a!=null){if(a.indexOf("http://www.photogallery.va")>=0){a=a.replace("http://www.photogallery.va","https://www.vatican.va")
}jQuery.ajax({statusCode:{403:function(){},404:function(){}},type:"GET",crossDomain:true,dataType:"jsonp",url:a,success:jsonGallery})
}})
}function jsonGallery(f){if(typeof f!="undefined"&&f!=null){var c=f.page["link"];
var g=f.page["title"];
var a=f.page["images"];
if(a.length>0){var b=a[0]["thumb"];
var e=jQuery("#info_galleries ul li a[href='"+c+"']");
var d=e.html();
if(jQuery.trim(d)===""){e.html(g)
}e.after('<a href="'+c+'"><img src="'+b+'"></a>')
}}}function getText(b){try{var c=b["jcr:content"];
var a=c.container;
if(a){var f=a.vaticanrichtext;
if(f){return f.text
}else{return a.text
}}else{return null
}}catch(d){}}function compactText(b,a){b=b.substr(0,a);
b=b.substr(0,b.lastIndexOf(" "));
return b
}function removeHeader(c){var a=jQuery.parseHTML(c);
var b="";
if(a!=null){jQuery.each(a,function(f,g){var e=jQuery(g).get(0).tagName;
if(typeof e!="undefined"){if("P"==e){var d=jQuery(g).get(0).getAttribute("align");
if(d!=null&&(d.toLowerCase()=="center"||d.toLowerCase()=="left")){jQuery(g).empty()
}else{return false
}}else{jQuery(g).empty()
}}});
jQuery.each(a,function(d,e){if(typeof e.outerHTML!="undefined"){b+=e.outerHTML
}})
}return b
}function loadDocuments(){var a=jQuery(".document").length;
if(a>0){jQuery(".document").each(function(){var b=jQuery(this).attr("id");
var j=jQuery(this).attr("data-path");
var h=getPageJson(j);
var g=deduceTitle(h);
var c=getText(h);
text=removeHeader(c);
text=compactText(text,1000);
var e="";
var f=jQuery(this).attr("data-translate-more");
if(f=="undefined"){f="More..."
}if(typeof c!="undefined"&&jQuery.trim(c).length>=5){e='<div class="more"> <a href="'+j+'.html">'+f+"</a> </div>"
}var d="#"+b;
var i=jQuery(d);
i.find("p").html(text).append(e);
if(a>1){i.find("h2").html(g).click(function(){i.find("p").toggle("fast","linear",function(){})
})
}else{i.find("p").show()
}window.Translation.init(j+".html",d+" .translation")
})
}}function loadMaps(){if(jQuery(".map-canvas").length>0){jQuery(".map-canvas").each(function(){var b=jQuery(this).attr("data-lat");
var a=jQuery(this).attr("data-lng");
var c=jQuery(this).attr("data-title");
var d=jQuery(this).attr("id");
drawMap(d,b,a,c)
})
}}function drawMap(h,g,c,e){var d=new google.maps.LatLng(parseFloat(g),parseFloat(c));
var b={center:d,zoom:15,zoomControl:true,scaleControl:false,streetViewControl:false,mapTypeControl:false,scrollwheel:false};
var a=new google.maps.Marker({position:d});
var f=new google.maps.Map(document.getElementById(h),b);
a.setMap(f)
}function patchPlayerRva(){$(".cboxElement").click(function(){$(".iframe_container").css("display","none");
setTimeout("jQuery('#cboxClose').click(function(){jQuery('.iframe_container').css('display', 'block') })",1000)
});
$("#cboxOverlay").click(function(){$(".iframe_container").css("display","block")
})
}function cropPhoto(){if(jQuery("#info_photos .gallery").length>0){$("#info_photos .gallery img").resizecrop({width:80,height:45,zoom:false,vertical:"top"})
}}function vmLiveEmbed(){if(jQuery(".element .iframe_live_container").length>0){jQuery.ajax({type:"GET",dataType:"jsonp",jsonpCallback:"jsonLiveTv",url:"https://www.comunicazione.va/it/servizi/live.properties.js",success:function(c,a,b){console.log(""+c+"-"+a+"-"+b);
if(c){var d=c.prop.video;
jQuery(".element .iframe_live_container").html('<iframe width="595" height="360" frameborder="0" scrolling="no" allowfullscreen src="'+d+'"></iframe>')
}}})
}}$(document).ready(function(){if(jQuery(".eventview").length>0){loadGallery();
loadDocuments();
jQuery("#info_photos a.gallery").colorbox({rel:"group_photo"});
jQuery("#info_video a.gallery").colorbox({rel:"group_video",width:"600px",height:"400px",iframe:true});
loadMaps();
cropPhoto();
patchPlayerRva();
vmLiveEmbed()
}});
/*! jquery.selectBoxIt - v3.8.1 - 2013-10-17
* http://www.selectboxit.com
* Copyright (c) 2013 Greg Franko; Licensed MIT*/
(function(a){a(window.jQuery,window,document)
}(function(d,c,b,e){d.widget("selectBox.selectBoxIt",{VERSION:"3.8.1",options:{showEffect:"none",showEffectOptions:{},showEffectSpeed:"medium",hideEffect:"none",hideEffectOptions:{},hideEffectSpeed:"medium",showFirstOption:true,defaultText:"",defaultIcon:"",downArrowIcon:"",theme:"default",keydownOpen:true,isMobile:function(){var f=navigator.userAgent||navigator.vendor||c.opera;
return(/iPhone|iPod|iPad|Silk|Android|BlackBerry|Opera Mini|IEMobile/).test(f)
},"native":false,aggressiveChange:false,selectWhenHidden:true,viewport:d(c),similarSearch:false,copyAttributes:["title","rel"],copyClasses:"button",nativeMousedown:false,customShowHideEvent:false,autoWidth:true,html:true,populate:"",dynamicPositioning:true,hideCurrent:false},getThemes:function(){var f=this,g=d(f.element).attr("data-theme")||"c";
return{bootstrap:{focus:"active",hover:"",enabled:"enabled",disabled:"disabled",arrow:"caret",button:"btn",list:"dropdown-menu",container:"bootstrap",open:"open"},jqueryui:{focus:"ui-state-focus",hover:"ui-state-hover",enabled:"ui-state-enabled",disabled:"ui-state-disabled",arrow:"ui-icon ui-icon-triangle-1-s",button:"ui-widget ui-state-default",list:"ui-widget ui-widget-content",container:"jqueryui",open:"selectboxit-open"},jquerymobile:{focus:"ui-btn-down-"+g,hover:"ui-btn-hover-"+g,enabled:"ui-enabled",disabled:"ui-disabled",arrow:"ui-icon ui-icon-arrow-d ui-icon-shadow",button:"ui-btn ui-btn-icon-right ui-btn-corner-all ui-shadow ui-btn-up-"+g,list:"ui-btn ui-btn-icon-right ui-btn-corner-all ui-shadow ui-btn-up-"+g,container:"jquerymobile",open:"selectboxit-open"},"default":{focus:"selectboxit-focus",hover:"selectboxit-hover",enabled:"selectboxit-enabled",disabled:"selectboxit-disabled",arrow:"selectboxit-default-arrow",button:"selectboxit-btn",list:"selectboxit-list",container:"selectboxit-container",open:"selectboxit-open"}}
},isDeferred:function(f){return d.isPlainObject(f)&&f.promise&&f.done
},_create:function(f){var g=this,h=g.options.populate,i=g.options.theme;
if(!g.element.is("select")){return
}g.widgetProto=d.Widget.prototype;
g.originalElem=g.element[0];
g.selectBox=g.element;
if(g.options.populate&&g.add&&!f){g.add(h)
}g.selectItems=g.element.find("option");
g.firstSelectItem=g.selectItems.slice(0,1);
g.documentHeight=d(b).height();
g.theme=d.isPlainObject(i)?d.extend({},g.getThemes()["default"],i):g.getThemes()[i]?g.getThemes()[i]:g.getThemes()["default"];
g.currentFocus=0;
g.blur=true;
g.textArray=[];
g.currentIndex=0;
g.currentText="";
g.flipped=false;
if(!f){g.selectBoxStyles=g.selectBox.attr("style")
}g._createDropdownButton()._createUnorderedList()._copyAttributes()._replaceSelectBox()._addClasses(g.theme)._eventHandlers();
if(g.originalElem.disabled&&g.disable){g.disable()
}if(g._ariaAccessibility){g._ariaAccessibility()
}g.isMobile=g.options.isMobile();
if(g._mobile){g._mobile()
}if(g.options["native"]){this._applyNativeSelect()
}g.triggerEvent("create");
return g
},_createDropdownButton:function(){var f=this,j=f.originalElemId=f.originalElem.id||"",k=f.originalElemValue=f.originalElem.value||"",i=f.originalElemName=f.originalElem.name||"",h=f.options.copyClasses,g=f.selectBox.attr("class")||"";
f.dropdownText=d("<span/>",{id:j&&j+"SelectBoxItText","class":"selectboxit-text",unselectable:"on",text:f.firstSelectItem.text()}).attr("data-val",k);
f.dropdownImageContainer=d("<span/>",{"class":"selectboxit-option-icon-container"});
f.dropdownImage=d("<i/>",{id:j&&j+"SelectBoxItDefaultIcon","class":"selectboxit-default-icon",unselectable:"on"});
f.dropdown=d("<span/>",{id:j&&j+"SelectBoxIt","class":"selectboxit "+(h==="button"?g:"")+" "+(f.selectBox.prop("disabled")?f.theme.disabled:f.theme.enabled),name:i,tabindex:f.selectBox.attr("tabindex")||"0",unselectable:"on"}).append(f.dropdownImageContainer.append(f.dropdownImage)).append(f.dropdownText);
f.dropdownContainer=d("<span/>",{id:j&&j+"SelectBoxItContainer","class":"selectboxit-container "+f.theme.container+" "+(h==="container"?g:"")}).append(f.dropdown);
return f
},_createUnorderedList:function(){var p=this,u,m,r,g,j,o,t,k="",i=p.originalElemId||"",w=d("<ul/>",{id:i&&i+"SelectBoxItOptions","class":"selectboxit-options",tabindex:-1}),v,q,s,f,h,l;
if(!p.options.showFirstOption){p.selectItems.first().attr("disabled","disabled");
p.selectItems=p.selectBox.find("option").slice(1)
}p.selectItems.each(function(x){h=d(this);
m="";
r="";
u=h.prop("disabled");
g=h.attr("data-icon")||"";
j=h.attr("data-iconurl")||"";
o=j?"selectboxit-option-icon-url":"";
t=j?"style=\"background-image:url('"+j+"');\"":"";
v=h.attr("data-selectedtext");
q=h.attr("data-text");
f=q?q:h.text();
l=h.parent();
if(l.is("optgroup")){m="selectboxit-optgroup-option";
if(h.index()===0){r='<span class="selectboxit-optgroup-header '+l.first().attr("class")+'"data-disabled="true">'+l.first().attr("label")+"</span>"
}}h.attr("value",this.value);
k+=r+'<li data-id="'+x+'" data-val="'+this.value+'" data-disabled="'+u+'" class="'+m+" selectboxit-option "+(d(this).attr("class")||"")+'"><a class="selectboxit-option-anchor"><span class="selectboxit-option-icon-container"><i class="selectboxit-option-icon '+g+" "+(o||p.theme.container)+'"'+t+"></i></span>"+(p.options.html?f:p.htmlEscape(f))+"</a></li>";
s=h.attr("data-search");
p.textArray[x]=u?"":s?s:f;
if(this.selected){p._setText(p.dropdownText,v||f);
p.currentFocus=x
}});
if((p.options.defaultText||p.selectBox.attr("data-text"))){var n=p.options.defaultText||p.selectBox.attr("data-text");
p._setText(p.dropdownText,n);
p.options.defaultText=n
}w.append(k);
p.list=w;
p.dropdownContainer.append(p.list);
p.listItems=p.list.children("li");
p.listAnchors=p.list.find("a");
p.listItems.first().addClass("selectboxit-option-first");
p.listItems.last().addClass("selectboxit-option-last");
p.list.find("li[data-disabled='true']").not(".optgroupHeader").addClass(p.theme.disabled);
p.dropdownImage.addClass(p.selectBox.attr("data-icon")||p.options.defaultIcon||p.listItems.eq(p.currentFocus).find("i").attr("class"));
p.dropdownImage.attr("style",p.listItems.eq(p.currentFocus).find("i").attr("style"));
return p
},_replaceSelectBox:function(){var h=this,g,l=h.originalElem.id||"",j=h.selectBox.attr("data-size"),i=h.listSize=j===e?"auto":j==="0"||"size"==="auto"?"auto":+j,f,k;
h.selectBox.css("display","none").after(h.dropdownContainer);
h.dropdownContainer.appendTo("body").addClass("selectboxit-rendering");
g=h.dropdown.height();
h.downArrow=d("<i/>",{id:l&&l+"SelectBoxItArrow","class":"selectboxit-arrow",unselectable:"on"});
h.downArrowContainer=d("<span/>",{id:l&&l+"SelectBoxItArrowContainer","class":"selectboxit-arrow-container",unselectable:"on"}).append(h.downArrow);
h.dropdown.append(h.downArrowContainer);
h.listItems.removeClass("selectboxit-selected").eq(h.currentFocus).addClass("selectboxit-selected");
f=h.downArrowContainer.outerWidth(true);
k=h.dropdownImage.outerWidth(true);
if(h.options.autoWidth){h.dropdown.css({width:"auto"}).css({width:h.list.outerWidth(true)+f+k});
h.list.css({"min-width":h.dropdown.width()})
}h.dropdownText.css({"max-width":h.dropdownContainer.outerWidth(true)-(f+k)});
h.selectBox.after(h.dropdownContainer);
h.dropdownContainer.removeClass("selectboxit-rendering");
if(d.type(i)==="number"){h.maxHeight=h.listAnchors.outerHeight(true)*i
}return h
},_scrollToView:function(j){var n=this,l=n.listItems.eq(n.currentFocus),i=n.list.scrollTop(),m=l.height(),f=l.position().top,h=Math.abs(f),g=n.list.height(),k;
if(j==="search"){if(g-f<m){n.list.scrollTop(i+(f-(g-m)))
}else{if(f<-1){n.list.scrollTop(f-m)
}}}else{if(j==="up"){if(f<-1){n.list.scrollTop(i-h)
}}else{if(j==="down"){if(g-f<m){n.list.scrollTop((i+(h-g+m)))
}}}}return n
},_callbackSupport:function(g){var f=this;
if(d.isFunction(g)){g.call(f,f.dropdown)
}return f
},_setText:function(g,h){var f=this;
if(f.options.html){g.html(h)
}else{g.text(h)
}return f
},open:function(l){var j=this,i=j.options.showEffect,k=j.options.showEffectSpeed,g=j.options.showEffectOptions,h=j.options["native"],f=j.isMobile;
if(!j.listItems.length||j.dropdown.hasClass(j.theme.disabled)){return j
}if((!h&&!f)&&!this.list.is(":visible")){j.triggerEvent("open");
if(j._dynamicPositioning&&j.options.dynamicPositioning){j._dynamicPositioning()
}if(i==="none"){j.list.show()
}else{if(i==="show"||i==="slideDown"||i==="fadeIn"){j.list[i](k)
}else{j.list.show(i,g,k)
}}j.list.promise().done(function(){j._scrollToView("search");
j.triggerEvent("opened")
})
}j._callbackSupport(l);
return j
},close:function(l){var i=this,k=i.options.hideEffect,j=i.options.hideEffectSpeed,h=i.options.hideEffectOptions,g=i.options["native"],f=i.isMobile;
if((!g&&!f)&&i.list.is(":visible")){i.triggerEvent("close");
if(k==="none"){i.list.hide()
}else{if(k==="hide"||k==="slideUp"||k==="fadeOut"){i.list[k](j)
}else{i.list.hide(k,h,j)
}}i.list.promise().done(function(){i.triggerEvent("closed")
})
}i._callbackSupport(l);
return i
},toggle:function(){var f=this,g=f.list.is(":visible");
if(g){f.close()
}else{if(!g){f.open()
}}},_keyMappings:{"38":"up","40":"down","13":"enter","8":"backspace","9":"tab","32":"space","27":"esc"},_keydownMethods:function(){var f=this,g=f.list.is(":visible")||!f.options.keydownOpen;
return{down:function(){if(f.moveDown&&g){f.moveDown()
}},up:function(){if(f.moveUp&&g){f.moveUp()
}},enter:function(){var h=f.listItems.eq(f.currentFocus);
f._update(h);
if(h.attr("data-preventclose")!=="true"){f.close()
}f.triggerEvent("enter")
},tab:function(){f.triggerEvent("tab-blur");
f.close()
},backspace:function(){f.triggerEvent("backspace")
},esc:function(){f.close()
}}
},_eventHandlers:function(){var g=this,l=g.options.nativeMousedown,i=g.options.customShowHideEvent,f,k,h=g.focusClass,m=g.hoverClass,j=g.openClass;
this.dropdown.on({"click.selectBoxIt":function(){g.dropdown.trigger("focus",true);
if(!g.originalElem.disabled){g.triggerEvent("click");
if(!l&&!i){g.toggle()
}}},"mousedown.selectBoxIt":function(){d(this).data("mdown",true);
g.triggerEvent("mousedown");
if(l&&!i){g.toggle()
}},"mouseup.selectBoxIt":function(){g.triggerEvent("mouseup")
},"blur.selectBoxIt":function(){if(g.blur){g.triggerEvent("blur");
g.close();
d(this).removeClass(h)
}},"focus.selectBoxIt":function(p,n){var o=d(this).data("mdown");
d(this).removeData("mdown");
if(!o&&!n){setTimeout(function(){g.triggerEvent("tab-focus")
},0)
}if(!n){if(!d(this).hasClass(g.theme.disabled)){d(this).addClass(h)
}g.triggerEvent("focus")
}},"keydown.selectBoxIt":function(o){var p=g._keyMappings[o.keyCode],n=g._keydownMethods()[p];
if(n){n();
if(g.options.keydownOpen&&(p==="up"||p==="down")){g.open()
}}if(n&&p!=="tab"){o.preventDefault()
}},"keypress.selectBoxIt":function(p){var q=p.charCode||p.keyCode,o=g._keyMappings[p.charCode||p.keyCode],n=String.fromCharCode(q);
if(g.search&&(!o||(o&&o==="space"))){g.search(n,true,true)
}if(o==="space"){p.preventDefault()
}},"mouseenter.selectBoxIt":function(){g.triggerEvent("mouseenter")
},"mouseleave.selectBoxIt":function(){g.triggerEvent("mouseleave")
}});
g.list.on({"mouseover.selectBoxIt":function(){g.blur=false
},"mouseout.selectBoxIt":function(){g.blur=true
},"focusin.selectBoxIt":function(){g.dropdown.trigger("focus",true)
}});
g.list.on({"mousedown.selectBoxIt":function(){g._update(d(this));
g.triggerEvent("option-click");
if(d(this).attr("data-disabled")==="false"&&d(this).attr("data-preventclose")!=="true"){g.close()
}setTimeout(function(){g.dropdown.trigger("focus",true)
},0)
},"focusin.selectBoxIt":function(){g.listItems.not(d(this)).removeAttr("data-active");
d(this).attr("data-active","");
var n=g.list.is(":hidden");
if((g.options.searchWhenHidden&&n)||g.options.aggressiveChange||(n&&g.options.selectWhenHidden)){g._update(d(this))
}d(this).addClass(h)
},"mouseup.selectBoxIt":function(){if(l&&!i){g._update(d(this));
g.triggerEvent("option-mouseup");
if(d(this).attr("data-disabled")==="false"&&d(this).attr("data-preventclose")!=="true"){g.close()
}}},"mouseenter.selectBoxIt":function(){if(d(this).attr("data-disabled")==="false"){g.listItems.removeAttr("data-active");
d(this).addClass(h).attr("data-active","");
g.listItems.not(d(this)).removeClass(h);
d(this).addClass(h);
g.currentFocus=+d(this).attr("data-id")
}},"mouseleave.selectBoxIt":function(){if(d(this).attr("data-disabled")==="false"){g.listItems.not(d(this)).removeClass(h).removeAttr("data-active");
d(this).addClass(h);
g.currentFocus=+d(this).attr("data-id")
}},"blur.selectBoxIt":function(){d(this).removeClass(h)
}},".selectboxit-option");
g.list.on({"click.selectBoxIt":function(n){n.preventDefault()
}},"a");
g.selectBox.on({"change.selectBoxIt, internal-change.selectBoxIt":function(q,n){var p,o;
if(!n){p=g.list.find('li[data-val="'+g.originalElem.value+'"]');
if(p.length){g.listItems.eq(g.currentFocus).removeClass(g.focusClass);
g.currentFocus=+p.attr("data-id")
}}p=g.listItems.eq(g.currentFocus);
o=p.attr("data-selectedtext");
f=p.attr("data-text");
k=f?f:p.find("a").text();
g._setText(g.dropdownText,o||k);
g.dropdownText.attr("data-val",g.originalElem.value);
if(p.find("i").attr("class")){g.dropdownImage.attr("class",p.find("i").attr("class")).addClass("selectboxit-default-icon");
g.dropdownImage.attr("style",p.find("i").attr("style"))
}g.triggerEvent("changed")
},"disable.selectBoxIt":function(){g.dropdown.addClass(g.theme.disabled)
},"enable.selectBoxIt":function(){g.dropdown.removeClass(g.theme.disabled)
},"open.selectBoxIt":function(){var n=g.list.find("li[data-val='"+g.dropdownText.attr("data-val")+"']"),o;
if(!n.length){n=g.listItems.not("[data-disabled=true]").first()
}g.currentFocus=+n.attr("data-id");
o=g.listItems.eq(g.currentFocus);
g.dropdown.addClass(j).removeClass(m).addClass(h);
g.listItems.removeClass(g.selectedClass).removeAttr("data-active").not(o).removeClass(h);
o.addClass(g.selectedClass).addClass(h);
if(g.options.hideCurrent){g.listItems.show();
o.hide()
}},"close.selectBoxIt":function(){g.dropdown.removeClass(j)
},"blur.selectBoxIt":function(){g.dropdown.removeClass(h)
},"mouseenter.selectBoxIt":function(){if(!d(this).hasClass(g.theme.disabled)){g.dropdown.addClass(m)
}},"mouseleave.selectBoxIt":function(){g.dropdown.removeClass(m)
},destroy:function(n){n.preventDefault();
n.stopPropagation()
}});
return g
},_update:function(k){var g=this,i,f,l,h=g.options.defaultText||g.selectBox.attr("data-text"),j=g.listItems.eq(g.currentFocus);
if(k.attr("data-disabled")==="false"){i=g.listItems.eq(g.currentFocus).attr("data-selectedtext");
f=j.attr("data-text");
l=f?f:j.text();
if((h&&g.options.html?g.dropdownText.html()===h:g.dropdownText.text()===h)&&g.selectBox.val()===k.attr("data-val")){g.triggerEvent("change")
}else{g.selectBox.val(k.attr("data-val"));
g.currentFocus=+k.attr("data-id");
if(g.originalElem.value!==g.dropdownText.attr("data-val")){g.triggerEvent("change")
}}}},_addClasses:function(f){var l=this,n=l.focusClass=f.focus,h=l.hoverClass=f.hover,j=f.button,m=f.list,i=f.arrow,k=f.container,g=l.openClass=f.open;
l.selectedClass="selectboxit-selected";
l.downArrow.addClass(l.selectBox.attr("data-downarrow")||l.options.downArrowIcon||i);
l.dropdownContainer.addClass(k);
l.dropdown.addClass(j);
l.list.addClass(m);
return l
},refresh:function(h,f){var g=this;
g._destroySelectBoxIt()._create(true);
if(!f){g.triggerEvent("refresh")
}g._callbackSupport(h);
return g
},htmlEscape:function(f){return String(f).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/'/g,"&#39;").replace(/</g,"&lt;").replace(/>/g,"&gt;")
},triggerEvent:function(h){var g=this,f=g.options.showFirstOption?g.currentFocus:((g.currentFocus-1)>=0?g.currentFocus:0);
g.selectBox.trigger(h,{selectbox:g.selectBox,selectboxOption:g.selectItems.eq(f),dropdown:g.dropdown,dropdownOption:g.listItems.eq(g.currentFocus)});
return g
},_copyAttributes:function(){var f=this;
if(f._addSelectBoxAttributes){f._addSelectBoxAttributes()
}return f
},_realOuterWidth:function(g){if(g.is(":visible")){return g.outerWidth(true)
}var f=this,i=g.clone(),h;
i.css({visibility:"hidden",display:"block",position:"absolute"}).appendTo("body");
h=i.outerWidth(true);
i.remove();
return h
}});
var a=d.selectBox.selectBoxIt.prototype;
a._ariaAccessibility=function(){var f=this,g=d("label[for='"+f.originalElem.id+"']");
f.dropdownContainer.attr({role:"combobox","aria-autocomplete":"list","aria-haspopup":"true","aria-expanded":"false","aria-owns":f.list[0].id});
f.dropdownText.attr({"aria-live":"polite"});
f.dropdown.on({"disable.selectBoxIt":function(){f.dropdownContainer.attr("aria-disabled","true")
},"enable.selectBoxIt":function(){f.dropdownContainer.attr("aria-disabled","false")
}});
if(g.length){f.dropdownContainer.attr("aria-labelledby",g[0].id)
}f.list.attr({role:"listbox","aria-hidden":"true"});
f.listItems.attr({role:"option"});
f.selectBox.on({"open.selectBoxIt":function(){f.list.attr("aria-hidden","false");
f.dropdownContainer.attr("aria-expanded","true")
},"close.selectBoxIt":function(){f.list.attr("aria-hidden","true");
f.dropdownContainer.attr("aria-expanded","false")
}});
return f
};
a._addSelectBoxAttributes=function(){var f=this;
f._addAttributes(f.selectBox.prop("attributes"),f.dropdown);
f.selectItems.each(function(g){f._addAttributes(d(this).prop("attributes"),f.listItems.eq(g))
});
return f
};
a._addAttributes=function(f,i){var g=this,h=g.options.copyAttributes;
if(f.length){d.each(f,function(j,l){var k=(l.name).toLowerCase(),m=l.value;
if(m!=="null"&&(d.inArray(k,h)!==-1||k.indexOf("data")!==-1)){i.attr(k,m)
}})
}return g
};
a.destroy=function(g){var f=this;
f._destroySelectBoxIt();
f.widgetProto.destroy.call(f);
f._callbackSupport(g);
return f
};
a._destroySelectBoxIt=function(){var f=this;
f.dropdown.off(".selectBoxIt");
if(d.contains(f.dropdownContainer[0],f.originalElem)){f.dropdownContainer.before(f.selectBox)
}f.dropdownContainer.remove();
f.selectBox.removeAttr("style").attr("style",f.selectBoxStyles);
f.triggerEvent("destroy");
return f
};
a.disable=function(g){var f=this;
if(!f.options.disabled){f.close();
f.selectBox.attr("disabled","disabled");
f.dropdown.removeAttr("tabindex").removeClass(f.theme.enabled).addClass(f.theme.disabled);
f.setOption("disabled",true);
f.triggerEvent("disable")
}f._callbackSupport(g);
return f
};
a.disableOption=function(h,l){var g=this,i,k,f,j=d.type(h);
if(j==="number"){g.close();
i=g.selectBox.find("option").eq(h);
g.triggerEvent("disable-option");
i.attr("disabled","disabled");
g.listItems.eq(h).attr("data-disabled","true").addClass(g.theme.disabled);
if(g.currentFocus===h){k=g.listItems.eq(g.currentFocus).nextAll("li").not("[data-disabled='true']").first().length;
f=g.listItems.eq(g.currentFocus).prevAll("li").not("[data-disabled='true']").first().length;
if(k){g.moveDown()
}else{if(f){g.moveUp()
}else{g.disable()
}}}}g._callbackSupport(l);
return g
};
a._isDisabled=function(g){var f=this;
if(f.originalElem.disabled){f.disable()
}return f
};
a._dynamicPositioning=function(){var o=this;
if(d.type(o.listSize)==="number"){o.list.css("max-height",o.maxHeight||"none")
}else{var j=o.dropdown.offset().top,g=o.list.data("max-height")||o.list.outerHeight(),k=o.dropdown.outerHeight(),m=o.options.viewport,i=m.height(),f=d.isWindow(m.get(0))?m.scrollTop():m.offset().top,p=(j+k+g<=i+f),l=!p;
if(!o.list.data("max-height")){o.list.data("max-height",o.list.outerHeight())
}if(!l){o.list.css("max-height",g);
o.list.css("top","auto")
}else{if((o.dropdown.offset().top-f)>=g){o.list.css("max-height",g);
o.list.css("top",(o.dropdown.position().top-o.list.outerHeight()))
}else{var h=Math.abs((j+k+g)-(i+f)),n=Math.abs((o.dropdown.offset().top-f)-g);
if(h<n){o.list.css("max-height",g-h-(k/2));
o.list.css("top","auto")
}else{o.list.css("max-height",g-n-(k/2));
o.list.css("top",(o.dropdown.position().top-o.list.outerHeight()))
}}}}return o
};
a.enable=function(g){var f=this;
if(f.options.disabled){f.triggerEvent("enable");
f.selectBox.removeAttr("disabled");
f.dropdown.attr("tabindex",0).removeClass(f.theme.disabled).addClass(f.theme.enabled);
f.setOption("disabled",false);
f._callbackSupport(g)
}return f
};
a.enableOption=function(i,m){var h=this,j,g=0,l,f,k=d.type(i);
if(k==="number"){j=h.selectBox.find("option").eq(i);
h.triggerEvent("enable-option");
j.removeAttr("disabled");
h.listItems.eq(i).attr("data-disabled","false").removeClass(h.theme.disabled)
}h._callbackSupport(m);
return h
};
a.moveDown=function(i){var f=this;
f.currentFocus+=1;
var g=f.listItems.eq(f.currentFocus).attr("data-disabled")==="true"?true:false,h=f.listItems.eq(f.currentFocus).nextAll("li").not("[data-disabled='true']").first().length;
if(f.currentFocus===f.listItems.length){f.currentFocus-=1
}else{if(g&&h){f.listItems.eq(f.currentFocus-1).blur();
f.moveDown();
return
}else{if(g&&!h){f.currentFocus-=1
}else{f.listItems.eq(f.currentFocus-1).blur().end().eq(f.currentFocus).focusin();
f._scrollToView("down");
f.triggerEvent("moveDown")
}}}f._callbackSupport(i);
return f
};
a.moveUp=function(i){var g=this;
g.currentFocus-=1;
var h=g.listItems.eq(g.currentFocus).attr("data-disabled")==="true"?true:false,f=g.listItems.eq(g.currentFocus).prevAll("li").not("[data-disabled='true']").first().length;
if(g.currentFocus===-1){g.currentFocus+=1
}else{if(h&&f){g.listItems.eq(g.currentFocus+1).blur();
g.moveUp();
return
}else{if(h&&!f){g.currentFocus+=1
}else{g.listItems.eq(this.currentFocus+1).blur().end().eq(g.currentFocus).focusin();
g._scrollToView("up");
g.triggerEvent("moveUp")
}}}g._callbackSupport(i);
return g
};
a._setCurrentSearchOption=function(g){var f=this;
if((f.options.aggressiveChange||f.options.selectWhenHidden||f.listItems.eq(g).is(":visible"))&&f.listItems.eq(g).data("disabled")!==true){f.listItems.eq(f.currentFocus).blur();
f.currentIndex=g;
f.currentFocus=g;
f.listItems.eq(f.currentFocus).focusin();
f._scrollToView("search");
f.triggerEvent("search")
}return f
};
a._searchAlgorithm=function(k,j){var o=this,f=false,n,l,h,i,g=o.textArray,m=o.currentText;
for(n=k,h=g.length;
n<h;
n+=1){i=g[n];
for(l=0;
l<h;
l+=1){if(g[l].search(j)!==-1){f=true;
l=h
}}if(!f){o.currentText=o.currentText.charAt(o.currentText.length-1).replace(/[|()\[{.+*?$\\]/g,"\\$0");
m=o.currentText
}j=new RegExp(m,"gi");
if(m.length<3){j=new RegExp(m.charAt(0),"gi");
if((i.charAt(0).search(j)!==-1)){o._setCurrentSearchOption(n);
if((i.substring(0,m.length).toLowerCase()!==m.toLowerCase())||o.options.similarSearch){o.currentIndex+=1
}return false
}}else{if((i.search(j)!==-1)){o._setCurrentSearchOption(n);
return false
}}if(i.toLowerCase()===o.currentText.toLowerCase()){o._setCurrentSearchOption(n);
o.currentText="";
return false
}}return true
};
a.search=function(g,j,i){var f=this;
if(i){f.currentText+=g.replace(/[|()\[{.+*?$\\]/g,"\\$0")
}else{f.currentText=g.replace(/[|()\[{.+*?$\\]/g,"\\$0")
}var h=f._searchAlgorithm(f.currentIndex,new RegExp(f.currentText,"gi"));
if(h){f._searchAlgorithm(0,f.currentText)
}f._callbackSupport(j);
return f
};
a._updateMobileText=function(){var g=this,h,f,i;
h=g.selectBox.find("option").filter(":selected");
f=h.attr("data-text");
i=f?f:h.text();
g._setText(g.dropdownText,i);
if(g.list.find('li[data-val="'+h.val()+'"]').find("i").attr("class")){g.dropdownImage.attr("class",g.list.find('li[data-val="'+h.val()+'"]').find("i").attr("class")).addClass("selectboxit-default-icon")
}};
a._applyNativeSelect=function(){var f=this;
f.dropdownContainer.append(f.selectBox);
f.dropdown.attr("tabindex","-1");
f.selectBox.css({display:"block",visibility:"visible",width:f._realOuterWidth(f.dropdown),height:f.dropdown.outerHeight(),opacity:"0",position:"absolute",top:"0",left:"0",cursor:"pointer","z-index":"999999",margin:f.dropdown.css("margin"),padding:"0","-webkit-appearance":"menulist-button"});
if(f.originalElem.disabled){f.triggerEvent("disable")
}return this
};
a._mobileEvents=function(){var f=this;
f.selectBox.on({"changed.selectBoxIt":function(){f.hasChanged=true;
f._updateMobileText();
f.triggerEvent("option-click")
},"mousedown.selectBoxIt":function(){if(!f.hasChanged&&f.options.defaultText&&!f.originalElem.disabled){f._updateMobileText();
f.triggerEvent("option-click")
}},"enable.selectBoxIt":function(){f.selectBox.removeClass("selectboxit-rendering")
},"disable.selectBoxIt":function(){f.selectBox.addClass("selectboxit-rendering")
}})
};
a._mobile=function(g){var f=this;
if(f.isMobile){f._applyNativeSelect();
f._mobileEvents()
}return this
};
a.selectOption=function(h,i){var f=this,g=d.type(h);
if(g==="number"){f.selectBox.val(f.selectItems.eq(h).val()).change()
}else{if(g==="string"){f.selectBox.val(h).change()
}}f._callbackSupport(i);
return f
};
a.setOption=function(g,h,i){var f=this;
if(d.type(g)==="string"){f.options[g]=h
}f.refresh(function(){f._callbackSupport(i)
},true);
return f
};
a.setOptions=function(g,h){var f=this;
if(d.isPlainObject(g)){f.options=d.extend({},f.options,g)
}f.refresh(function(){f._callbackSupport(h)
},true);
return f
};
a.wait=function(g,h){var f=this;
f.widgetProto._delay.call(f,h,g);
return f
};
a.add=function(f,g){this._populate(f,function(l){var p=this,m=d.type(l),o,n=0,k,i=[],j=p._isJSON(l),h=j&&p._parseJSON(l);
if(l&&(m==="array"||(j&&h.data&&d.type(h.data)==="array"))||(m==="object"&&l.data&&d.type(l.data)==="array")){if(p._isJSON(l)){l=h
}if(l.data){l=l.data
}for(k=l.length;
n<=k-1;
n+=1){o=l[n];
if(d.isPlainObject(o)){i.push(d("<option/>",o))
}else{if(d.type(o)==="string"){i.push(d("<option/>",{text:o,value:o}))
}}}p.selectBox.append(i)
}else{if(l&&m==="string"&&!p._isJSON(l)){p.selectBox.append(l)
}else{if(l&&m==="object"){p.selectBox.append(d("<option/>",l))
}else{if(l&&p._isJSON(l)&&d.isPlainObject(p._parseJSON(l))){p.selectBox.append(d("<option/>",p._parseJSON(l)))
}}}}if(p.dropdown){p.refresh(function(){p._callbackSupport(g)
},true)
}else{p._callbackSupport(g)
}return p
})
};
a._parseJSON=function(f){return(JSON&&JSON.parse&&JSON.parse(f))||d.parseJSON(f)
};
a._isJSON=function(h){var f=this,g;
try{g=f._parseJSON(h);
return true
}catch(i){return false
}};
a._populate=function(g,h){var f=this;
g=d.isFunction(g)?g.call():g;
if(f.isDeferred(g)){g.done(function(i){h.call(f,i)
})
}else{h.call(f,g)
}return f
};
a.remove=function(j,m){var i=this,h=d.type(j),k,f=0,l,g="";
if(h==="array"){for(l=j.length;
f<=l-1;
f+=1){k=j[f];
if(d.type(k)==="number"){if(g.length){g+=", option:eq("+k+")"
}else{g+="option:eq("+k+")"
}}}i.selectBox.find(g).remove()
}else{if(h==="number"){i.selectBox.find("option").eq(j).remove()
}else{i.selectBox.find("option").remove()
}}if(i.dropdown){i.refresh(function(){i._callbackSupport(m)
},true)
}else{i._callbackSupport(m)
}return i
}
}));
EventArchive={options:{container:".archive",baseUrl:null,owner:null,lang:"it",yearLabel:"Anno",monthLabel:"Mese",dayLabel:"Giorno",contentRootUrl:""},$selectYear:null,$selectMonth:null,$selectDay:null,$submit:null,init:function(a){var b=this;
b.options=jQuery.extend(b.options,a);
jQuery.datepicker.setDefaults(jQuery.datepicker.regional[b.options.lang]);
b.$selectYear=jQuery("select[name='year']",b.container);
b.$selectMonth=jQuery("select[name='month']",b.container);
b.$selectDay=jQuery("select[name='day']",b.container);
b.$submit=jQuery("input[name='go']",b.container);
if(b.$selectYear.length>0&&b.$selectMonth.length>0&&b.$selectDay.length>0){b.$selectMonth.selectBoxIt();
b.$selectDay.selectBoxIt();
b.$selectYear.selectBoxIt();
b.resetYear();
b.resetMonth();
b.resetDay();
b.preapareYear();
b.configureEventChange();
b.configureEventSubmit()
}},getListYearUrl:function(){return this.options.baseUrl+"/"+this.options.lang+".1.json"
},getListMonthUrl:function(a){return this.options.baseUrl+"/"+this.options.lang+"/"+a+".1.json"
},getListDayUrl:function(a,b){return this.options.baseUrl+"/"+this.options.lang+"/"+a+"/"+b+".1.json"
},resetYear:function(){var a=this;
a.$selectYear.data("selectBoxSelectBoxIt").remove();
a.$selectYear.data("selectBoxSelectBoxIt").add({value:"",text:a.options.yearLabel})
},resetMonth:function(){var a=this;
a.$selectMonth.data("selectBoxSelectBoxIt").remove();
a.$selectMonth.data("selectBoxSelectBoxIt").add({value:"",text:a.options.monthLabel})
},resetDay:function(){var a=this;
a.$selectDay.data("selectBoxSelectBoxIt").remove();
a.$selectDay.data("selectBoxSelectBoxIt").add({value:"",text:a.options.dayLabel})
},preapareYear:function(){var a=this;
jQuery.ajax({statusCode:{403:function(){},404:function(){}},url:a.getListYearUrl(),type:"GET",dataType:"json",success:function(b){jQuery.each(b,function(c,d){if(c.indexOf("jcr:")==-1&&c.indexOf("rep:")==-1){a.$selectYear.data("selectBoxSelectBoxIt").add({value:c,text:c})
}});
a.$selectYear.data("selectBoxSelectBoxIt").enable()
}})
},configureEventChange:function(){this.configureYearChange();
this.configureMonthChange()
},configureYearChange:function(){var a=this;
a.$selectYear.change(function(){var b=jQuery(this);
var c=b.val();
a.resetMonth();
a.resetDay();
jQuery.ajax({statusCode:{403:function(){},404:function(){}},url:a.getListMonthUrl(c),type:"GET",dataType:"json",success:function(d){jQuery.each(d,function(f,g){if(f.indexOf("jcr:")==-1){var e=new Date();
e.setMonth(f-1,1);
var h=$.datepicker.formatDate("MM",e);
a.$selectMonth.data("selectBoxSelectBoxIt").add({value:f,text:h})
}});
a.$selectMonth.data("selectBoxSelectBoxIt").enable()
}})
})
},configureMonthChange:function(){var a=this;
a.$selectMonth.change(function(){var b=jQuery(this);
var d=a.$selectYear.val();
var c=b.val();
a.resetDay();
jQuery.ajax({statusCode:{403:function(){},404:function(){}},url:a.getListDayUrl(d,c),type:"GET",dataType:"json",success:function(e){jQuery.each(e,function(f,g){if(f.indexOf("jcr:")==-1){a.$selectDay.data("selectBoxSelectBoxIt").add({value:f,text:f})
}});
a.$selectDay.data("selectBoxSelectBoxIt").enable()
}})
})
},getRedirectUrl:function(){var a=this;
if(a.notEmptyString(a.$selectDay.val())&&a.notEmptyString(a.$selectMonth.val())&&a.notEmptyString(a.$selectYear.val())){return a.options.contentRootUrl+"/day.dir.html/"+a.$selectYear.val()+"/"+a.$selectMonth.val()+"/"+a.$selectDay.val()+".html"
}else{if(a.notEmptyString(a.$selectMonth.val())&&a.notEmptyString(a.$selectYear.val())){return a.options.contentRootUrl+"/month.dir.html/"+a.$selectYear.val()+"/"+a.$selectMonth.val()+".html"
}else{if(a.notEmptyString(a.$selectYear.val())){return a.options.contentRootUrl+"/year.dir.html/"+a.$selectYear.val()+".html"
}}}},notEmptyString:function(a){return((typeof a!="undefined")&&a!=null&&jQuery.trim(a)!="")
},configureEventSubmit:function(){var a=this;
a.$submit.click(function(){var b=a.getRedirectUrl();
if(a.notEmptyString(b)){location.href=b
}})
},initYearCalendarV2:function(a){var b=this;
b.options=jQuery.extend(b.options,a);
jQuery.datepicker.setDefaults(jQuery.datepicker.regional[b.options.lang]);
b.$selectYear=jQuery("select[name='year']",b.container);
if(b.$selectYear.length>0){b.$selectYear.selectBoxIt();
b.resetYear();
b.preapareYear()
}}};
var Swiper=function(l,a){if(!document.body.outerHTML&&document.body.__defineGetter__){if(HTMLElement){var t=HTMLElement.prototype;
if(t.__defineGetter__){t.__defineGetter__("outerHTML",function(){return new XMLSerializer().serializeToString(this)
})
}}}if(!window.getComputedStyle){window.getComputedStyle=function(i,j){this.el=i;
this.getPropertyValue=function(ag){var p=/(\-([a-z]){1})/g;
if(ag==="float"){ag="styleFloat"
}if(p.test(ag)){ag=ag.replace(p,function(){return arguments[2].toUpperCase()
})
}return i.currentStyle[ag]?i.currentStyle[ag]:null
};
return this
}
}if(!Array.prototype.indexOf){Array.prototype.indexOf=function(ah,ai){for(var ag=(ai||0),p=this.length;
ag<p;
ag++){if(this[ag]===ah){return ag
}}return -1
}
}if(!document.querySelectorAll){if(!window.jQuery){return
}}function R(i,j){if(document.querySelectorAll){return(j||document).querySelectorAll(i)
}else{return jQuery(i,j)
}}if(typeof l==="undefined"){return
}if(!(l.nodeType)){if(R(l).length===0){return
}}var f=this;
f.touches={start:0,startX:0,startY:0,current:0,currentX:0,currentY:0,diff:0,abs:0};
f.positions={start:0,abs:0,diff:0,current:0};
f.times={start:0,end:0};
f.id=(new Date()).getTime();
f.container=(l.nodeType)?l:R(l)[0];
f.isTouched=false;
f.isMoved=false;
f.activeIndex=0;
f.centerIndex=0;
f.activeLoaderIndex=0;
f.activeLoopIndex=0;
f.previousIndex=null;
f.velocity=0;
f.snapGrid=[];
f.slidesGrid=[];
f.imagesToLoad=[];
f.imagesLoaded=0;
f.wrapperLeft=0;
f.wrapperRight=0;
f.wrapperTop=0;
f.wrapperBottom=0;
f.isAndroid=navigator.userAgent.toLowerCase().indexOf("android")>=0;
var z,J,ae,r,b,d;
var G={eventTarget:"wrapper",mode:"horizontal",touchRatio:1,speed:300,freeMode:false,freeModeFluid:false,momentumRatio:1,momentumBounce:true,momentumBounceRatio:1,slidesPerView:1,slidesPerGroup:1,slidesPerViewFit:true,simulateTouch:true,followFinger:true,shortSwipes:true,longSwipesRatio:0.5,moveStartThreshold:false,onlyExternal:false,createPagination:true,pagination:false,paginationElement:"span",paginationClickable:false,paginationAsRange:true,resistance:true,scrollContainer:false,preventLinks:true,preventLinksPropagation:false,noSwiping:false,noSwipingClass:"swiper-no-swiping",initialSlide:0,keyboardControl:false,mousewheelControl:false,mousewheelControlForceToAxis:false,useCSS3Transforms:true,autoplay:false,autoplayDisableOnInteraction:true,autoplayStopOnLast:false,loop:false,loopAdditionalSlides:0,roundLengths:false,calculateHeight:false,cssWidthAndHeight:false,updateOnImagesReady:true,releaseFormElements:true,watchActiveIndex:false,visibilityFullFit:false,offsetPxBefore:0,offsetPxAfter:0,offsetSlidesBefore:0,offsetSlidesAfter:0,centeredSlides:false,queueStartCallbacks:false,queueEndCallbacks:false,autoResize:true,resizeReInit:false,DOMAnimation:true,loader:{slides:[],slidesHTMLType:"inner",surroundGroups:1,logic:"reload",loadAllSlides:false},swipeToPrev:true,swipeToNext:true,slideElement:"div",slideClass:"swiper-slide",slideActiveClass:"swiper-slide-active",slideVisibleClass:"swiper-slide-visible",slideDuplicateClass:"swiper-slide-duplicate",wrapperClass:"swiper-wrapper",paginationElementClass:"swiper-pagination-switch",paginationActiveClass:"swiper-active-switch",paginationVisibleClass:"swiper-visible-switch"};
a=a||{};
for(var x in G){if(x in a&&typeof a[x]==="object"){for(var e in G[x]){if(!(e in a[x])){a[x][e]=G[x][e]
}}}else{if(!(x in a)){a[x]=G[x]
}}}f.params=a;
if(a.scrollContainer){a.freeMode=true;
a.freeModeFluid=true
}if(a.loop){a.resistance="100%"
}var D=a.mode==="horizontal";
var v=["mousedown","mousemove","mouseup"];
if(f.browser.ie10){v=["MSPointerDown","MSPointerMove","MSPointerUp"]
}if(f.browser.ie11){v=["pointerdown","pointermove","pointerup"]
}f.touchEvents={touchStart:f.support.touch||!a.simulateTouch?"touchstart":v[0],touchMove:f.support.touch||!a.simulateTouch?"touchmove":v[1],touchEnd:f.support.touch||!a.simulateTouch?"touchend":v[2]};
for(var V=f.container.childNodes.length-1;
V>=0;
V--){if(f.container.childNodes[V].className){var s=f.container.childNodes[V].className.split(/\s+/);
for(var S=0;
S<s.length;
S++){if(s[S]===a.wrapperClass){z=f.container.childNodes[V]
}}}}f.wrapper=z;
f._extendSwiperSlide=function(i){i.append=function(){if(a.loop){i.insertAfter(f.slides.length-f.loopedSlides)
}else{f.wrapper.appendChild(i);
f.reInit()
}return i
};
i.prepend=function(){if(a.loop){f.wrapper.insertBefore(i,f.slides[f.loopedSlides]);
f.removeLoopedSlides();
f.calcSlides();
f.createLoop()
}else{f.wrapper.insertBefore(i,f.wrapper.firstChild)
}f.reInit();
return i
};
i.insertAfter=function(j){if(typeof j==="undefined"){return false
}var p;
if(a.loop){p=f.slides[j+1+f.loopedSlides];
if(p){f.wrapper.insertBefore(i,p)
}else{f.wrapper.appendChild(i)
}f.removeLoopedSlides();
f.calcSlides();
f.createLoop()
}else{p=f.slides[j+1];
f.wrapper.insertBefore(i,p)
}f.reInit();
return i
};
i.clone=function(){return f._extendSwiperSlide(i.cloneNode(true))
};
i.remove=function(){f.wrapper.removeChild(i);
f.reInit()
};
i.html=function(j){if(typeof j==="undefined"){return i.innerHTML
}else{i.innerHTML=j;
return i
}};
i.index=function(){var j;
for(var p=f.slides.length-1;
p>=0;
p--){if(i===f.slides[p]){j=p
}}return j
};
i.isActive=function(){if(i.index()===f.activeIndex){return true
}else{return false
}};
if(!i.swiperSlideDataStorage){i.swiperSlideDataStorage={}
}i.getData=function(j){return i.swiperSlideDataStorage[j]
};
i.setData=function(j,p){i.swiperSlideDataStorage[j]=p;
return i
};
i.data=function(j,p){if(typeof p==="undefined"){return i.getAttribute("data-"+j)
}else{i.setAttribute("data-"+j,p);
return i
}};
i.getWidth=function(p,j){return f.h.getWidth(i,p,j)
};
i.getHeight=function(p,j){return f.h.getHeight(i,p,j)
};
i.getOffset=function(){return f.h.getOffset(i)
};
return i
};
f.calcSlides=function(ah){var aj=f.slides?f.slides.length:false;
f.slides=[];
f.displaySlides=[];
for(var ai=0;
ai<f.wrapper.childNodes.length;
ai++){if(f.wrapper.childNodes[ai].className){var ak=f.wrapper.childNodes[ai].className;
var p=ak.split(/\s+/);
for(var ag=0;
ag<p.length;
ag++){if(p[ag]===a.slideClass){f.slides.push(f.wrapper.childNodes[ai])
}}}}for(ai=f.slides.length-1;
ai>=0;
ai--){f._extendSwiperSlide(f.slides[ai])
}if(aj===false){return
}if(aj!==f.slides.length||ah){o();
q();
f.updateActiveSlide();
if(f.params.pagination){f.createPagination()
}f.callPlugins("numberOfSlidesChanged")
}};
f.createSlide=function(p,j,ag){j=j||f.params.slideClass;
ag=ag||a.slideElement;
var i=document.createElement(ag);
i.innerHTML=p||"";
i.className=j;
return f._extendSwiperSlide(i)
};
f.appendSlide=function(j,i,p){if(!j){return
}if(j.nodeType){return f._extendSwiperSlide(j).append()
}else{return f.createSlide(j,i,p).append()
}};
f.prependSlide=function(j,i,p){if(!j){return
}if(j.nodeType){return f._extendSwiperSlide(j).prepend()
}else{return f.createSlide(j,i,p).prepend()
}};
f.insertSlideAfter=function(j,p,i,ag){if(typeof j==="undefined"){return false
}if(p.nodeType){return f._extendSwiperSlide(p).insertAfter(j)
}else{return f.createSlide(p,i,ag).insertAfter(j)
}};
f.removeSlide=function(i){if(f.slides[i]){if(a.loop){if(!f.slides[i+f.loopedSlides]){return false
}f.slides[i+f.loopedSlides].remove();
f.removeLoopedSlides();
f.calcSlides();
f.createLoop()
}else{f.slides[i].remove()
}return true
}else{return false
}};
f.removeLastSlide=function(){if(f.slides.length>0){if(a.loop){f.slides[f.slides.length-1-f.loopedSlides].remove();
f.removeLoopedSlides();
f.calcSlides();
f.createLoop()
}else{f.slides[f.slides.length-1].remove()
}return true
}else{return false
}};
f.removeAllSlides=function(){var j=f.slides.length;
for(var p=f.slides.length-1;
p>=0;
p--){f.slides[p].remove();
if(p===j-1){f.setWrapperTranslate(0)
}}};
f.getSlide=function(i){return f.slides[i]
};
f.getLastSlide=function(){return f.slides[f.slides.length-1]
};
f.getFirstSlide=function(){return f.slides[0]
};
f.activeSlide=function(){return f.slides[f.activeIndex]
};
f.fireCallback=function(){var p=arguments[0];
if(Object.prototype.toString.call(p)==="[object Array]"){for(var j=0;
j<p.length;
j++){if(typeof p[j]==="function"){p[j](arguments[1],arguments[2],arguments[3],arguments[4],arguments[5])
}}}else{if(Object.prototype.toString.call(p)==="[object String]"){if(a["on"+p]){f.fireCallback(a["on"+p],arguments[1],arguments[2],arguments[3],arguments[4],arguments[5])
}}else{p(arguments[1],arguments[2],arguments[3],arguments[4],arguments[5])
}}};
function B(i){if(Object.prototype.toString.apply(i)==="[object Array]"){return true
}return false
}f.addCallback=function(ag,i){var p=this,j;
if(p.params["on"+ag]){if(B(this.params["on"+ag])){return this.params["on"+ag].push(i)
}else{if(typeof this.params["on"+ag]==="function"){j=this.params["on"+ag];
this.params["on"+ag]=[];
this.params["on"+ag].push(j);
return this.params["on"+ag].push(i)
}}}else{this.params["on"+ag]=[];
return this.params["on"+ag].push(i)
}};
f.removeCallbacks=function(i){if(f.params["on"+i]){f.params["on"+i]=null
}};
var A=[];
for(var ac in f.plugins){if(a[ac]){var P=f.plugins[ac](f,a[ac]);
if(P){A.push(P)
}}}f.callPlugins=function(ag,j){if(!j){j={}
}for(var p=0;
p<A.length;
p++){if(ag in A[p]){A[p][ag](j)
}}};
if((f.browser.ie10||f.browser.ie11)&&!a.onlyExternal){f.wrapper.classList.add("swiper-wp8-"+(D?"horizontal":"vertical"))
}if(a.freeMode){f.container.className+=" swiper-free-mode"
}f.initialized=false;
f.init=function(aj,ai){var an=f.h.getWidth(f.container,false,a.roundLengths);
var aA=f.h.getHeight(f.container,false,a.roundLengths);
if(an===f.width&&aA===f.height&&!aj){return
}f.width=an;
f.height=aA;
var ao,aq,ax,ak,au,az;
var aw;
d=D?an:aA;
var ap=f.wrapper;
if(aj){f.calcSlides(ai)
}if(a.slidesPerView==="auto"){var al=0;
var ag=0;
if(a.slidesOffset>0){ap.style.paddingLeft="";
ap.style.paddingRight="";
ap.style.paddingTop="";
ap.style.paddingBottom=""
}ap.style.width="";
ap.style.height="";
if(a.offsetPxBefore>0){if(D){f.wrapperLeft=a.offsetPxBefore
}else{f.wrapperTop=a.offsetPxBefore
}}if(a.offsetPxAfter>0){if(D){f.wrapperRight=a.offsetPxAfter
}else{f.wrapperBottom=a.offsetPxAfter
}}if(a.centeredSlides){if(D){f.wrapperLeft=(d-this.slides[0].getWidth(true,a.roundLengths))/2;
f.wrapperRight=(d-f.slides[f.slides.length-1].getWidth(true,a.roundLengths))/2
}else{f.wrapperTop=(d-f.slides[0].getHeight(true,a.roundLengths))/2;
f.wrapperBottom=(d-f.slides[f.slides.length-1].getHeight(true,a.roundLengths))/2
}}if(D){if(f.wrapperLeft>=0){ap.style.paddingLeft=f.wrapperLeft+"px"
}if(f.wrapperRight>=0){ap.style.paddingRight=f.wrapperRight+"px"
}}else{if(f.wrapperTop>=0){ap.style.paddingTop=f.wrapperTop+"px"
}if(f.wrapperBottom>=0){ap.style.paddingBottom=f.wrapperBottom+"px"
}}az=0;
var ay=0;
f.snapGrid=[];
f.slidesGrid=[];
ax=0;
for(aw=0;
aw<f.slides.length;
aw++){ao=f.slides[aw].getWidth(true,a.roundLengths);
aq=f.slides[aw].getHeight(true,a.roundLengths);
if(a.calculateHeight){ax=Math.max(ax,aq)
}var at=D?ao:aq;
if(a.centeredSlides){var p=aw===f.slides.length-1?0:f.slides[aw+1].getWidth(true,a.roundLengths);
var ah=aw===f.slides.length-1?0:f.slides[aw+1].getHeight(true,a.roundLengths);
var am=D?p:ah;
if(at>d){if(a.slidesPerViewFit){f.snapGrid.push(az+f.wrapperLeft);
f.snapGrid.push(az+at-d+f.wrapperLeft)
}else{for(var av=0;
av<=Math.floor(at/(d+f.wrapperLeft));
av++){if(av===0){f.snapGrid.push(az+f.wrapperLeft)
}else{f.snapGrid.push(az+f.wrapperLeft+d*av)
}}}f.slidesGrid.push(az+f.wrapperLeft)
}else{f.snapGrid.push(ay);
f.slidesGrid.push(ay)
}ay+=at/2+am/2
}else{if(at>d){if(a.slidesPerViewFit){f.snapGrid.push(az);
f.snapGrid.push(az+at-d)
}else{if(d!==0){for(var ar=0;
ar<=Math.floor(at/d);
ar++){f.snapGrid.push(az+d*ar)
}}else{f.snapGrid.push(az)
}}}else{f.snapGrid.push(az)
}f.slidesGrid.push(az)
}az+=at;
al+=ao;
ag+=aq
}if(a.calculateHeight){f.height=ax
}if(D){ae=al+f.wrapperRight+f.wrapperLeft;
if(!a.cssWidthAndHeight||a.cssWidthAndHeight==="height"){ap.style.width=(al)+"px"
}if(!a.cssWidthAndHeight||a.cssWidthAndHeight==="width"){ap.style.height=(f.height)+"px"
}}else{if(!a.cssWidthAndHeight||a.cssWidthAndHeight==="height"){ap.style.width=(f.width)+"px"
}if(!a.cssWidthAndHeight||a.cssWidthAndHeight==="width"){ap.style.height=(ag)+"px"
}ae=ag+f.wrapperTop+f.wrapperBottom
}}else{if(a.scrollContainer){ap.style.width="";
ap.style.height="";
ak=f.slides[0].getWidth(true,a.roundLengths);
au=f.slides[0].getHeight(true,a.roundLengths);
ae=D?ak:au;
ap.style.width=ak+"px";
ap.style.height=au+"px";
J=D?ak:au
}else{if(a.calculateHeight){ax=0;
au=0;
if(!D){f.container.style.height=""
}ap.style.height="";
for(aw=0;
aw<f.slides.length;
aw++){f.slides[aw].style.height="";
ax=Math.max(f.slides[aw].getHeight(true),ax);
if(!D){au+=f.slides[aw].getHeight(true)
}}aq=ax;
f.height=aq;
if(D){au=aq
}else{d=aq;
f.container.style.height=d+"px"
}}else{aq=D?f.height:f.height/a.slidesPerView;
if(a.roundLengths){aq=Math.ceil(aq)
}au=D?f.height:f.slides.length*aq
}ao=D?f.width/a.slidesPerView:f.width;
if(a.roundLengths){ao=Math.ceil(ao)
}ak=D?f.slides.length*ao:f.width;
J=D?ao:aq;
if(a.offsetSlidesBefore>0){if(D){f.wrapperLeft=J*a.offsetSlidesBefore
}else{f.wrapperTop=J*a.offsetSlidesBefore
}}if(a.offsetSlidesAfter>0){if(D){f.wrapperRight=J*a.offsetSlidesAfter
}else{f.wrapperBottom=J*a.offsetSlidesAfter
}}if(a.offsetPxBefore>0){if(D){f.wrapperLeft=a.offsetPxBefore
}else{f.wrapperTop=a.offsetPxBefore
}}if(a.offsetPxAfter>0){if(D){f.wrapperRight=a.offsetPxAfter
}else{f.wrapperBottom=a.offsetPxAfter
}}if(a.centeredSlides){if(D){f.wrapperLeft=(d-J)/2;
f.wrapperRight=(d-J)/2
}else{f.wrapperTop=(d-J)/2;
f.wrapperBottom=(d-J)/2
}}if(D){if(f.wrapperLeft>0){ap.style.paddingLeft=f.wrapperLeft+"px"
}if(f.wrapperRight>0){ap.style.paddingRight=f.wrapperRight+"px"
}}else{if(f.wrapperTop>0){ap.style.paddingTop=f.wrapperTop+"px"
}if(f.wrapperBottom>0){ap.style.paddingBottom=f.wrapperBottom+"px"
}}ae=D?ak+f.wrapperRight+f.wrapperLeft:au+f.wrapperTop+f.wrapperBottom;
if(parseFloat(ak)>0&&(!a.cssWidthAndHeight||a.cssWidthAndHeight==="height")){ap.style.width=ak+"px"
}if(parseFloat(au)>0&&(!a.cssWidthAndHeight||a.cssWidthAndHeight==="width")){ap.style.height=au+"px"
}az=0;
f.snapGrid=[];
f.slidesGrid=[];
for(aw=0;
aw<f.slides.length;
aw++){f.snapGrid.push(az);
f.slidesGrid.push(az);
az+=J;
if(parseFloat(ao)>0&&(!a.cssWidthAndHeight||a.cssWidthAndHeight==="height")){f.slides[aw].style.width=ao+"px"
}if(parseFloat(aq)>0&&(!a.cssWidthAndHeight||a.cssWidthAndHeight==="width")){f.slides[aw].style.height=aq+"px"
}}}}if(!f.initialized){f.callPlugins("onFirstInit");
if(a.onFirstInit){f.fireCallback(a.onFirstInit,f)
}}else{f.callPlugins("onInit");
if(a.onInit){f.fireCallback(a.onInit,f)
}}f.initialized=true
};
f.reInit=function(i){f.init(true,i)
};
f.resizeFix=function(i){f.callPlugins("beforeResizeFix");
f.init(a.resizeReInit||i);
if(!a.freeMode){f.swipeTo((a.loop?f.activeLoopIndex:f.activeIndex),0,false);
if(a.autoplay){if(f.support.transitions&&typeof K!=="undefined"){if(typeof K!=="undefined"){clearTimeout(K);
K=undefined;
f.startAutoplay()
}}else{if(typeof X!=="undefined"){clearInterval(X);
X=undefined;
f.startAutoplay()
}}}}else{if(f.getWrapperTranslate()<-ab()){f.setWrapperTransition(0);
f.setWrapperTranslate(-ab())
}}f.callPlugins("afterResizeFix")
};
function ab(){var i=(ae-d);
if(a.freeMode){i=ae-d
}if(a.slidesPerView>f.slides.length&&!a.centeredSlides){i=0
}if(i<0){i=0
}return i
}function m(){var ai=f.h.addEventListener;
var ah=a.eventTarget==="wrapper"?f.wrapper:f.container;
if(!(f.browser.ie10||f.browser.ie11)){if(f.support.touch){ai(ah,"touchstart",U);
ai(ah,"touchmove",aa);
ai(ah,"touchend",N)
}if(a.simulateTouch){ai(ah,"mousedown",U);
ai(document,"mousemove",aa);
ai(document,"mouseup",N)
}}else{ai(ah,f.touchEvents.touchStart,U);
ai(document,f.touchEvents.touchMove,aa);
ai(document,f.touchEvents.touchEnd,N)
}if(a.autoResize){ai(window,"resize",f.resizeFix)
}q();
f._wheelEvent=false;
if(a.mousewheelControl){if(document.onmousewheel!==undefined){f._wheelEvent="mousewheel"
}if(!f._wheelEvent){try{new WheelEvent("wheel");
f._wheelEvent="wheel"
}catch(ag){}}if(!f._wheelEvent){f._wheelEvent="DOMMouseScroll"
}if(f._wheelEvent){ai(f.container,f._wheelEvent,c)
}}function p(aj){var i=new Image();
i.onload=function(){if(typeof f==="undefined"||f===null){return
}if(f.imagesLoaded!==undefined){f.imagesLoaded++
}if(f.imagesLoaded===f.imagesToLoad.length){f.reInit();
if(a.onImagesReady){f.fireCallback(a.onImagesReady,f)
}}};
i.src=aj
}if(a.keyboardControl){ai(document,"keydown",F)
}if(a.updateOnImagesReady){f.imagesToLoad=R("img",f.container);
for(var j=0;
j<f.imagesToLoad.length;
j++){p(f.imagesToLoad[j].getAttribute("src"))
}}}f.destroy=function(ah){var p=f.h.removeEventListener;
var ag=a.eventTarget==="wrapper"?f.wrapper:f.container;
if(!(f.browser.ie10||f.browser.ie11)){if(f.support.touch){p(ag,"touchstart",U);
p(ag,"touchmove",aa);
p(ag,"touchend",N)
}if(a.simulateTouch){p(ag,"mousedown",U);
p(document,"mousemove",aa);
p(document,"mouseup",N)
}}else{p(ag,f.touchEvents.touchStart,U);
p(document,f.touchEvents.touchMove,aa);
p(document,f.touchEvents.touchEnd,N)
}if(a.autoResize){p(window,"resize",f.resizeFix)
}o();
if(a.paginationClickable){C()
}if(a.mousewheelControl&&f._wheelEvent){p(f.container,f._wheelEvent,c)
}if(a.keyboardControl){p(document,"keydown",F)
}if(a.autoplay){f.stopAutoplay()
}if(ah){f.wrapper.removeAttribute("style");
for(var j=0;
j<f.slides.length;
j++){f.slides[j].removeAttribute("style")
}}f.callPlugins("onDestroy");
if(window.jQuery&&window.jQuery(f.container).data("swiper")){window.jQuery(f.container).removeData("swiper")
}if(window.Zepto&&window.Zepto(f.container).data("swiper")){window.Zepto(f.container).removeData("swiper")
}f=null
};
function q(){var ah=f.h.addEventListener,ag;
if(a.preventLinks){var j=R("a",f.container);
for(ag=0;
ag<j.length;
ag++){ah(j[ag],"click",O)
}}if(a.releaseFormElements){var p=R("input, textarea, select",f.container);
for(ag=0;
ag<p.length;
ag++){ah(p[ag],f.touchEvents.touchStart,y,true);
if(f.support.touch&&a.simulateTouch){ah(p[ag],"mousedown",y,true)
}}}if(a.onSlideClick){for(ag=0;
ag<f.slides.length;
ag++){ah(f.slides[ag],"click",W)
}}if(a.onSlideTouch){for(ag=0;
ag<f.slides.length;
ag++){ah(f.slides[ag],f.touchEvents.touchStart,k)
}}}function o(){var ah=f.h.removeEventListener,ag;
if(a.onSlideClick){for(ag=0;
ag<f.slides.length;
ag++){ah(f.slides[ag],"click",W)
}}if(a.onSlideTouch){for(ag=0;
ag<f.slides.length;
ag++){ah(f.slides[ag],f.touchEvents.touchStart,k)
}}if(a.releaseFormElements){var p=R("input, textarea, select",f.container);
for(ag=0;
ag<p.length;
ag++){ah(p[ag],f.touchEvents.touchStart,y,true);
if(f.support.touch&&a.simulateTouch){ah(p[ag],"mousedown",y,true)
}}}if(a.preventLinks){var j=R("a",f.container);
for(ag=0;
ag<j.length;
ag++){ah(j[ag],"click",O)
}}}function F(am){var ak=am.keyCode||am.charCode;
if(am.shiftKey||am.altKey||am.ctrlKey||am.metaKey){return
}if(ak===37||ak===39||ak===38||ak===40){var an=false;
var al=f.h.getOffset(f.container);
var ai=f.h.windowScroll().left;
var ag=f.h.windowScroll().top;
var ah=f.h.windowWidth();
var j=f.h.windowHeight();
var p=[[al.left,al.top],[al.left+f.width,al.top],[al.left,al.top+f.height],[al.left+f.width,al.top+f.height]];
for(var aj=0;
aj<p.length;
aj++){var ao=p[aj];
if(ao[0]>=ai&&ao[0]<=ai+ah&&ao[1]>=ag&&ao[1]<=ag+j){an=true
}}if(!an){return
}}if(D){if(ak===37||ak===39){if(am.preventDefault){am.preventDefault()
}else{am.returnValue=false
}}if(ak===39){f.swipeNext()
}if(ak===37){f.swipePrev()
}}else{if(ak===38||ak===40){if(am.preventDefault){am.preventDefault()
}else{am.returnValue=false
}}if(ak===40){f.swipeNext()
}if(ak===38){f.swipePrev()
}}}f.disableKeyboardControl=function(){a.keyboardControl=false;
f.h.removeEventListener(document,"keydown",F)
};
f.enableKeyboardControl=function(){a.keyboardControl=true;
f.h.addEventListener(document,"keydown",F)
};
var T=(new Date()).getTime();
function c(p){var j=f._wheelEvent;
var ag=0;
if(p.detail){ag=-p.detail
}else{if(j==="mousewheel"){if(a.mousewheelControlForceToAxis){if(D){if(Math.abs(p.wheelDeltaX)>Math.abs(p.wheelDeltaY)){ag=p.wheelDeltaX
}else{return
}}else{if(Math.abs(p.wheelDeltaY)>Math.abs(p.wheelDeltaX)){ag=p.wheelDeltaY
}else{return
}}}else{ag=p.wheelDelta
}}else{if(j==="DOMMouseScroll"){ag=-p.detail
}else{if(j==="wheel"){if(a.mousewheelControlForceToAxis){if(D){if(Math.abs(p.deltaX)>Math.abs(p.deltaY)){ag=-p.deltaX
}else{return
}}else{if(Math.abs(p.deltaY)>Math.abs(p.deltaX)){ag=-p.deltaY
}else{return
}}}else{ag=Math.abs(p.deltaX)>Math.abs(p.deltaY)?-p.deltaX:-p.deltaY
}}}}}if(!a.freeMode){if((new Date()).getTime()-T>60){if(ag<0){f.swipeNext()
}else{f.swipePrev()
}}T=(new Date()).getTime()
}else{var i=f.getWrapperTranslate()+ag;
if(i>0){i=0
}if(i<-ab()){i=-ab()
}f.setWrapperTransition(0);
f.setWrapperTranslate(i);
f.updateActiveSlide(i);
if(i===0||i===-ab()){return
}}if(a.autoplay){f.stopAutoplay(true)
}if(p.preventDefault){p.preventDefault()
}else{p.returnValue=false
}return false
}f.disableMousewheelControl=function(){if(!f._wheelEvent){return false
}a.mousewheelControl=false;
f.h.removeEventListener(f.container,f._wheelEvent,c);
return true
};
f.enableMousewheelControl=function(){if(!f._wheelEvent){return false
}a.mousewheelControl=true;
f.h.addEventListener(f.container,f._wheelEvent,c);
return true
};
if(a.grabCursor){var g=f.container.style;
g.cursor="move";
g.cursor="grab";
g.cursor="-moz-grab";
g.cursor="-webkit-grab"
}f.allowSlideClick=true;
function W(i){if(f.allowSlideClick){E(i);
f.fireCallback(a.onSlideClick,f,i)
}}function k(i){E(i);
f.fireCallback(a.onSlideTouch,f,i)
}function E(j){if(!j.currentTarget){var i=j.srcElement;
do{if(i.className.indexOf(a.slideClass)>-1){break
}i=i.parentNode
}while(i);
f.clickedSlide=i
}else{f.clickedSlide=j.currentTarget
}f.clickedSlideIndex=f.slides.indexOf(f.clickedSlide);
f.clickedSlideLoopIndex=f.clickedSlideIndex-(f.loopedSlides||0)
}f.allowLinks=true;
function O(i){if(!f.allowLinks){if(i.preventDefault){i.preventDefault()
}else{i.returnValue=false
}if(a.preventLinksPropagation&&"stopPropagation" in i){i.stopPropagation()
}return false
}}function y(i){if(i.stopPropagation){i.stopPropagation()
}else{i.returnValue=false
}return false
}var w=false;
var L;
var ad=true;
function U(ag){if(a.preventLinks){f.allowLinks=true
}if(f.isTouched||a.onlyExternal){return false
}var ah=ag.target||ag.srcElement;
if(document.activeElement){if(document.activeElement!==ah){document.activeElement.blur()
}}var p=("input select textarea").split(" ");
if(a.noSwiping&&(ah)&&I(ah)){return false
}ad=false;
f.isTouched=true;
w=ag.type==="touchstart";
if(!w&&"which" in ag&&ag.which===3){f.isTouched=false;
return false
}if(!w||ag.targetTouches.length===1){f.callPlugins("onTouchStartBegin");
if(!w&&!f.isAndroid&&p.indexOf(ah.tagName.toLowerCase())<0){if(ag.preventDefault){ag.preventDefault()
}else{ag.returnValue=false
}}var j=w?ag.targetTouches[0].pageX:(ag.pageX||ag.clientX);
var i=w?ag.targetTouches[0].pageY:(ag.pageY||ag.clientY);
f.touches.startX=f.touches.currentX=j;
f.touches.startY=f.touches.currentY=i;
f.touches.start=f.touches.current=D?j:i;
f.setWrapperTransition(0);
f.positions.start=f.positions.current=f.getWrapperTranslate();
f.setWrapperTranslate(f.positions.start);
f.times.start=(new Date()).getTime();
b=undefined;
if(a.moveStartThreshold>0){L=false
}if(a.onTouchStart){f.fireCallback(a.onTouchStart,f,ag)
}f.callPlugins("onTouchStartEnd")
}}var h,H;
function aa(ah){if(!f.isTouched||a.onlyExternal){return
}if(w&&ah.type==="mousemove"){return
}var ag=w?ah.targetTouches[0].pageX:(ah.pageX||ah.clientX);
var j=w?ah.targetTouches[0].pageY:(ah.pageY||ah.clientY);
if(typeof b==="undefined"&&D){b=!!(b||Math.abs(j-f.touches.startY)>Math.abs(ag-f.touches.startX))
}if(typeof b==="undefined"&&!D){b=!!(b||Math.abs(j-f.touches.startY)<Math.abs(ag-f.touches.startX))
}if(b){f.isTouched=false;
return
}if(D){if((!a.swipeToNext&&ag<f.touches.startX)||((!a.swipeToPrev&&ag>f.touches.startX))){return
}}else{if((!a.swipeToNext&&j<f.touches.startY)||((!a.swipeToPrev&&j>f.touches.startY))){return
}}if(ah.assignedToSwiper){f.isTouched=false;
return
}ah.assignedToSwiper=true;
if(a.preventLinks){f.allowLinks=false
}if(a.onSlideClick){f.allowSlideClick=false
}if(a.autoplay){f.stopAutoplay(true)
}if(!w||ah.touches.length===1){if(!f.isMoved){f.callPlugins("onTouchMoveStart");
if(a.loop){f.fixLoop();
f.positions.start=f.getWrapperTranslate()
}if(a.onTouchMoveStart){f.fireCallback(a.onTouchMoveStart,f)
}}f.isMoved=true;
if(ah.preventDefault){ah.preventDefault()
}else{ah.returnValue=false
}f.touches.current=D?ag:j;
f.positions.current=(f.touches.current-f.touches.start)*a.touchRatio+f.positions.start;
if(f.positions.current>0&&a.onResistanceBefore){f.fireCallback(a.onResistanceBefore,f,f.positions.current)
}if(f.positions.current<-ab()&&a.onResistanceAfter){f.fireCallback(a.onResistanceAfter,f,Math.abs(f.positions.current+ab()))
}if(a.resistance&&a.resistance!=="100%"){var p;
if(f.positions.current>0){p=1-f.positions.current/d/2;
if(p<0.5){f.positions.current=(d/2)
}else{f.positions.current=f.positions.current*p
}}if(f.positions.current<-ab()){var ai=(f.touches.current-f.touches.start)*a.touchRatio+(ab()+f.positions.start);
p=(d+ai)/(d);
var i=f.positions.current-ai*(1-p)/2;
var aj=-ab()-d/2;
if(i<aj||p<=0){f.positions.current=aj
}else{f.positions.current=i
}}}if(a.resistance&&a.resistance==="100%"){if(f.positions.current>0&&!(a.freeMode&&!a.freeModeFluid)){f.positions.current=0
}if(f.positions.current<-ab()&&!(a.freeMode&&!a.freeModeFluid)){f.positions.current=-ab()
}}if(!a.followFinger){return
}if(!a.moveStartThreshold){f.setWrapperTranslate(f.positions.current)
}else{if(Math.abs(f.touches.current-f.touches.start)>a.moveStartThreshold||L){if(!L){L=true;
f.touches.start=f.touches.current;
return
}f.setWrapperTranslate(f.positions.current)
}else{f.positions.current=f.positions.start
}}if(a.freeMode||a.watchActiveIndex){f.updateActiveSlide(f.positions.current)
}if(a.grabCursor){f.container.style.cursor="move";
f.container.style.cursor="grabbing";
f.container.style.cursor="-moz-grabbin";
f.container.style.cursor="-webkit-grabbing"
}if(!h){h=f.touches.current
}if(!H){H=(new Date()).getTime()
}f.velocity=(f.touches.current-h)/((new Date()).getTime()-H)/2;
if(Math.abs(f.touches.current-h)<2){f.velocity=0
}h=f.touches.current;
H=(new Date()).getTime();
f.callPlugins("onTouchMoveEnd");
if(a.onTouchMove){f.fireCallback(a.onTouchMove,f,ah)
}return false
}}function N(p){if(b){f.swipeReset()
}if(a.onlyExternal||!f.isTouched){return
}f.isTouched=false;
if(a.grabCursor){f.container.style.cursor="move";
f.container.style.cursor="grab";
f.container.style.cursor="-moz-grab";
f.container.style.cursor="-webkit-grab"
}if(!f.positions.current&&f.positions.current!==0){f.positions.current=f.positions.start
}if(a.followFinger){f.setWrapperTranslate(f.positions.current)
}f.times.end=(new Date()).getTime();
f.touches.diff=f.touches.current-f.touches.start;
f.touches.abs=Math.abs(f.touches.diff);
f.positions.diff=f.positions.current-f.positions.start;
f.positions.abs=Math.abs(f.positions.diff);
var aq=f.positions.diff;
var au=f.positions.abs;
var j=f.times.end-f.times.start;
if(au<5&&(j)<300&&f.allowLinks===false){if(!a.freeMode&&au!==0){f.swipeReset()
}if(a.preventLinks){f.allowLinks=true
}if(a.onSlideClick){f.allowSlideClick=true
}}setTimeout(function(){if(typeof f==="undefined"||f===null){return
}if(a.preventLinks){f.allowLinks=true
}if(a.onSlideClick){f.allowSlideClick=true
}},100);
var am=ab();
if(!f.isMoved&&a.freeMode){f.isMoved=false;
if(a.onTouchEnd){f.fireCallback(a.onTouchEnd,f,p)
}f.callPlugins("onTouchEnd");
return
}if(!f.isMoved||f.positions.current>0||f.positions.current<-am){f.swipeReset();
if(a.onTouchEnd){f.fireCallback(a.onTouchEnd,f,p)
}f.callPlugins("onTouchEnd");
return
}f.isMoved=false;
if(a.freeMode){if(a.freeModeFluid){var an=1000*a.momentumRatio;
var aj=f.velocity*an;
var ai=f.positions.current+aj;
var ah=false;
var ao;
var at=Math.abs(f.velocity)*20*a.momentumBounceRatio;
if(ai<-am){if(a.momentumBounce&&f.support.transitions){if(ai+am<-at){ai=-am-at
}ao=-am;
ah=true;
ad=true
}else{ai=-am
}}if(ai>0){if(a.momentumBounce&&f.support.transitions){if(ai>at){ai=at
}ao=0;
ah=true;
ad=true
}else{ai=0
}}if(f.velocity!==0){an=Math.abs((ai-f.positions.current)/f.velocity)
}f.setWrapperTranslate(ai);
f.setWrapperTransition(an);
if(a.momentumBounce&&ah){f.wrapperTransitionEnd(function(){if(!ad){return
}if(a.onMomentumBounce){f.fireCallback(a.onMomentumBounce,f)
}f.callPlugins("onMomentumBounce");
f.setWrapperTranslate(ao);
f.setWrapperTransition(300)
})
}f.updateActiveSlide(ai)
}if(!a.freeModeFluid||j>=300){f.updateActiveSlide(f.positions.current)
}if(a.onTouchEnd){f.fireCallback(a.onTouchEnd,f,p)
}f.callPlugins("onTouchEnd");
return
}r=aq<0?"toNext":"toPrev";
if(r==="toNext"&&(j<=300)){if(au<30||!a.shortSwipes){f.swipeReset()
}else{f.swipeNext(true,true)
}}if(r==="toPrev"&&(j<=300)){if(au<30||!a.shortSwipes){f.swipeReset()
}else{f.swipePrev(true,true)
}}var ar=0;
if(a.slidesPerView==="auto"){var ag=Math.abs(f.getWrapperTranslate());
var ap=0;
var al;
for(var ak=0;
ak<f.slides.length;
ak++){al=D?f.slides[ak].getWidth(true,a.roundLengths):f.slides[ak].getHeight(true,a.roundLengths);
ap+=al;
if(ap>ag){ar=al;
break
}}if(ar>d){ar=d
}}else{ar=J*a.slidesPerView
}if(r==="toNext"&&(j>300)){if(au>=ar*a.longSwipesRatio){f.swipeNext(true,true)
}else{f.swipeReset()
}}if(r==="toPrev"&&(j>300)){if(au>=ar*a.longSwipesRatio){f.swipePrev(true,true)
}else{f.swipeReset()
}}if(a.onTouchEnd){f.fireCallback(a.onTouchEnd,f,p)
}f.callPlugins("onTouchEnd")
}function I(j){var i=false;
do{if(j.className.indexOf(a.noSwipingClass)>-1){i=true
}j=j.parentElement
}while(!i&&j.parentElement&&j.className.indexOf(a.wrapperClass)===-1);
if(!i&&j.className.indexOf(a.wrapperClass)>-1&&j.className.indexOf(a.noSwipingClass)>-1){i=true
}return i
}function M(i,j){var p=document.createElement("div");
var ag;
p.innerHTML=j;
ag=p.firstChild;
ag.className+=" "+i;
return ag.outerHTML
}f.swipeNext=function(aj,p){if(typeof aj==="undefined"){aj=true
}if(!p&&a.loop){f.fixLoop()
}if(!p&&a.autoplay){f.stopAutoplay(true)
}f.callPlugins("onSwipeNext");
var ai=f.getWrapperTranslate().toFixed(2);
var ah=ai;
if(a.slidesPerView==="auto"){for(var ag=0;
ag<f.snapGrid.length;
ag++){if(-ai>=f.snapGrid[ag].toFixed(2)&&-ai<f.snapGrid[ag+1].toFixed(2)){ah=-f.snapGrid[ag+1];
break
}}}else{var j=J*a.slidesPerGroup;
ah=-(Math.floor(Math.abs(ai)/Math.floor(j))*j+j)
}if(ah<-ab()){ah=-ab()
}if(ah===ai){return false
}n(ah,"next",{runCallbacks:aj});
return true
};
f.swipePrev=function(aj,p){if(typeof aj==="undefined"){aj=true
}if(!p&&a.loop){f.fixLoop()
}if(!p&&a.autoplay){f.stopAutoplay(true)
}f.callPlugins("onSwipePrev");
var ai=Math.ceil(f.getWrapperTranslate());
var ah;
if(a.slidesPerView==="auto"){ah=0;
for(var ag=1;
ag<f.snapGrid.length;
ag++){if(-ai===f.snapGrid[ag]){ah=-f.snapGrid[ag-1];
break
}if(-ai>f.snapGrid[ag]&&-ai<f.snapGrid[ag+1]){ah=-f.snapGrid[ag];
break
}}}else{var j=J*a.slidesPerGroup;
ah=-(Math.ceil(-ai/j)-1)*j
}if(ah>0){ah=0
}if(ah===ai){return false
}n(ah,"prev",{runCallbacks:aj});
return true
};
f.swipeReset=function(aj){if(typeof aj==="undefined"){aj=true
}f.callPlugins("onSwipeReset");
var ah=f.getWrapperTranslate();
var j=J*a.slidesPerGroup;
var ag;
var ai=-ab();
if(a.slidesPerView==="auto"){ag=0;
for(var p=0;
p<f.snapGrid.length;
p++){if(-ah===f.snapGrid[p]){return
}if(-ah>=f.snapGrid[p]&&-ah<f.snapGrid[p+1]){if(f.positions.diff>0){ag=-f.snapGrid[p+1]
}else{ag=-f.snapGrid[p]
}break
}}if(-ah>=f.snapGrid[f.snapGrid.length-1]){ag=-f.snapGrid[f.snapGrid.length-1]
}if(ah<=-ab()){ag=-ab()
}}else{ag=ah<0?Math.round(ah/j)*j:0;
if(ah<=-ab()){ag=-ab()
}}if(a.scrollContainer){ag=ah<0?ah:0
}if(ag<-ab()){ag=-ab()
}if(a.scrollContainer&&(d>J)){ag=0
}if(ag===ah){return false
}n(ag,"reset",{runCallbacks:aj});
return true
};
f.swipeTo=function(i,ag,ah){i=parseInt(i,10);
f.callPlugins("onSwipeTo",{index:i,speed:ag});
if(a.loop){i=i+f.loopedSlides
}var p=f.getWrapperTranslate();
if(i>(f.slides.length-1)||i<0){return
}var j;
if(a.slidesPerView==="auto"){j=-f.slidesGrid[i]
}else{j=-i*J
}if(j<-ab()){j=-ab()
}if(j===p){return false
}if(typeof ah==="undefined"){ah=true
}n(j,"to",{index:i,speed:ag,runCallbacks:ah});
return true
};
function n(ag,ah,am){var j=(ah==="to"&&am.speed>=0)?am.speed:a.speed;
var aj=+new Date();
function ai(){var an=+new Date();
var ao=an-aj;
p+=ak*ao/(1000/60);
i=al==="toNext"?p>ag:p<ag;
if(i){f.setWrapperTranslate(Math.ceil(p));
f._DOMAnimating=true;
window.setTimeout(function(){ai()
},1000/60)
}else{if(a.onSlideChangeEnd){if(ah==="to"){if(am.runCallbacks===true){f.fireCallback(a.onSlideChangeEnd,f,al)
}}else{f.fireCallback(a.onSlideChangeEnd,f,al)
}}f.setWrapperTranslate(ag);
f._DOMAnimating=false
}}if(f.support.transitions||!a.DOMAnimation){f.setWrapperTranslate(ag);
f.setWrapperTransition(j)
}else{var p=f.getWrapperTranslate();
var ak=Math.ceil((ag-p)/j*(1000/60));
var al=p>ag?"toNext":"toPrev";
var i=al==="toNext"?p>ag:p<ag;
if(f._DOMAnimating){return
}ai()
}f.updateActiveSlide(ag);
if(a.onSlideNext&&ah==="next"&&am.runCallbacks===true){f.fireCallback(a.onSlideNext,f,ag)
}if(a.onSlidePrev&&ah==="prev"&&am.runCallbacks===true){f.fireCallback(a.onSlidePrev,f,ag)
}if(a.onSlideReset&&ah==="reset"&&am.runCallbacks===true){f.fireCallback(a.onSlideReset,f,ag)
}if((ah==="next"||ah==="prev"||ah==="to")&&am.runCallbacks===true){af(ah)
}}f._queueStartCallbacks=false;
f._queueEndCallbacks=false;
function af(i){f.callPlugins("onSlideChangeStart");
if(a.onSlideChangeStart){if(a.queueStartCallbacks&&f.support.transitions){if(f._queueStartCallbacks){return
}f._queueStartCallbacks=true;
f.fireCallback(a.onSlideChangeStart,f,i);
f.wrapperTransitionEnd(function(){f._queueStartCallbacks=false
})
}else{f.fireCallback(a.onSlideChangeStart,f,i)
}}if(a.onSlideChangeEnd){if(f.support.transitions){if(a.queueEndCallbacks){if(f._queueEndCallbacks){return
}f._queueEndCallbacks=true;
f.wrapperTransitionEnd(function(j){f.fireCallback(a.onSlideChangeEnd,j,i)
})
}else{f.wrapperTransitionEnd(function(j){f.fireCallback(a.onSlideChangeEnd,j,i)
})
}}else{if(!a.DOMAnimation){setTimeout(function(){f.fireCallback(a.onSlideChangeEnd,f,i)
},10)
}}}}f.updateActiveSlide=function(aj){if(!f.initialized){return
}if(f.slides.length===0){return
}f.previousIndex=f.activeIndex;
if(typeof aj==="undefined"){aj=f.getWrapperTranslate()
}if(aj>0){aj=0
}var ai;
if(a.slidesPerView==="auto"){var am=0;
f.activeIndex=f.slidesGrid.indexOf(-aj);
if(f.activeIndex<0){for(ai=0;
ai<f.slidesGrid.length-1;
ai++){if(-aj>f.slidesGrid[ai]&&-aj<f.slidesGrid[ai+1]){break
}}var ag=Math.abs(f.slidesGrid[ai]+aj);
var p=Math.abs(f.slidesGrid[ai+1]+aj);
if(ag<=p){f.activeIndex=ai
}else{f.activeIndex=ai+1
}}}else{f.activeIndex=Math[a.visibilityFullFit?"ceil":"round"](-aj/J)
}if(f.activeIndex===f.slides.length){f.activeIndex=f.slides.length-1
}if(f.activeIndex<0){f.activeIndex=0
}if(!f.slides[f.activeIndex]){return
}f.calcVisibleSlides(aj);
if(f.support.classList){var ak;
for(ai=0;
ai<f.slides.length;
ai++){ak=f.slides[ai];
ak.classList.remove(a.slideActiveClass);
if(f.visibleSlides.indexOf(ak)>=0){ak.classList.add(a.slideVisibleClass)
}else{ak.classList.remove(a.slideVisibleClass)
}}f.slides[f.activeIndex].classList.add(a.slideActiveClass)
}else{var al=new RegExp("\\s*"+a.slideActiveClass);
var j=new RegExp("\\s*"+a.slideVisibleClass);
for(ai=0;
ai<f.slides.length;
ai++){f.slides[ai].className=f.slides[ai].className.replace(al,"").replace(j,"");
if(f.visibleSlides.indexOf(f.slides[ai])>=0){f.slides[ai].className+=" "+a.slideVisibleClass
}}f.slides[f.activeIndex].className+=" "+a.slideActiveClass
}if(a.loop){var ah=f.loopedSlides;
f.activeLoopIndex=f.activeIndex-ah;
if(f.activeLoopIndex>=f.slides.length-ah*2){f.activeLoopIndex=f.slides.length-ah*2-f.activeLoopIndex
}if(f.activeLoopIndex<0){f.activeLoopIndex=f.slides.length-ah*2+f.activeLoopIndex
}if(f.activeLoopIndex<0){f.activeLoopIndex=0
}}else{f.activeLoopIndex=f.activeIndex
}if(a.pagination){f.updatePagination(aj)
}};
f.createPagination=function(p){if(a.paginationClickable&&f.paginationButtons){C()
}f.paginationContainer=a.pagination.nodeType?a.pagination:R(a.pagination)[0];
if(a.createPagination){var j="";
var ai=f.slides.length;
var ah=ai;
if(a.loop){ah-=f.loopedSlides*2
}for(var ag=0;
ag<ah;
ag++){j+="<"+a.paginationElement+' class="'+a.paginationElementClass+'"></'+a.paginationElement+">"
}f.paginationContainer.innerHTML=j
}f.paginationButtons=R("."+a.paginationElementClass,f.paginationContainer);
if(!p){f.updatePagination()
}f.callPlugins("onCreatePagination");
if(a.paginationClickable){Y()
}};
function C(){var j=f.paginationButtons;
if(j){for(var p=0;
p<j.length;
p++){f.h.removeEventListener(j[p],"click",u)
}}}function Y(){var j=f.paginationButtons;
if(j){for(var p=0;
p<j.length;
p++){f.h.addEventListener(j[p],"click",u)
}}}function u(ai){var p;
var ah=ai.target||ai.srcElement;
var j=f.paginationButtons;
for(var ag=0;
ag<j.length;
ag++){if(ah===j[ag]){p=ag
}}if(a.autoplay){f.stopAutoplay(true)
}f.swipeTo(p)
}f.updatePagination=function(p){if(!a.pagination){return
}if(f.slides.length<1){return
}var ak=R("."+a.paginationActiveClass,f.paginationContainer);
if(!ak){return
}var ai=f.paginationButtons;
if(ai.length===0){return
}for(var aj=0;
aj<ai.length;
aj++){ai[aj].className=a.paginationElementClass
}var am=a.loop?f.loopedSlides:0;
if(a.paginationAsRange){if(!f.visibleSlides){f.calcVisibleSlides(p)
}var ag=[];
var ah;
for(ah=0;
ah<f.visibleSlides.length;
ah++){var al=f.slides.indexOf(f.visibleSlides[ah])-am;
if(a.loop&&al<0){al=f.slides.length-f.loopedSlides*2+al
}if(a.loop&&al>=f.slides.length-f.loopedSlides*2){al=f.slides.length-f.loopedSlides*2-al;
al=Math.abs(al)
}ag.push(al)
}for(ah=0;
ah<ag.length;
ah++){if(ai[ag[ah]]){ai[ag[ah]].className+=" "+a.paginationVisibleClass
}}if(a.loop){if(ai[f.activeLoopIndex]!==undefined){ai[f.activeLoopIndex].className+=" "+a.paginationActiveClass
}}else{if(ai[f.activeIndex]){ai[f.activeIndex].className+=" "+a.paginationActiveClass
}}}else{if(a.loop){if(ai[f.activeLoopIndex]){ai[f.activeLoopIndex].className+=" "+a.paginationActiveClass+" "+a.paginationVisibleClass
}}else{if(ai[f.activeIndex]){ai[f.activeIndex].className+=" "+a.paginationActiveClass+" "+a.paginationVisibleClass
}}}};
f.calcVisibleSlides=function(j){var ai=[];
var ak=0,ah=0,aj=0;
if(D&&f.wrapperLeft>0){j=j+f.wrapperLeft
}if(!D&&f.wrapperTop>0){j=j+f.wrapperTop
}for(var ag=0;
ag<f.slides.length;
ag++){ak+=ah;
if(a.slidesPerView==="auto"){ah=D?f.h.getWidth(f.slides[ag],true,a.roundLengths):f.h.getHeight(f.slides[ag],true,a.roundLengths)
}else{ah=J
}aj=ak+ah;
var p=false;
if(a.visibilityFullFit){if(ak>=-j&&aj<=-j+d){p=true
}if(ak<=-j&&aj>=-j+d){p=true
}}else{if(aj>-j&&aj<=((-j+d))){p=true
}if(ak>=-j&&ak<((-j+d))){p=true
}if(ak<-j&&aj>((-j+d))){p=true
}}if(p){ai.push(f.slides[ag])
}}if(ai.length===0){ai=[f.slides[f.activeIndex]]
}f.visibleSlides=ai
};
var K,X;
f.startAutoplay=function(){if(f.support.transitions){if(typeof K!=="undefined"){return false
}if(!a.autoplay){return
}f.callPlugins("onAutoplayStart");
if(a.onAutoplayStart){f.fireCallback(a.onAutoplayStart,f)
}Z()
}else{if(typeof X!=="undefined"){return false
}if(!a.autoplay){return
}f.callPlugins("onAutoplayStart");
if(a.onAutoplayStart){f.fireCallback(a.onAutoplayStart,f)
}X=setInterval(function(){if(a.loop){f.fixLoop();
f.swipeNext(true,true)
}else{if(!f.swipeNext(true,true)){if(!a.autoplayStopOnLast){f.swipeTo(0)
}else{clearInterval(X);
X=undefined
}}}},a.autoplay)
}};
f.stopAutoplay=function(i){if(f.support.transitions){if(!K){return
}if(K){clearTimeout(K)
}K=undefined;
if(i&&!a.autoplayDisableOnInteraction){f.wrapperTransitionEnd(function(){Z()
})
}f.callPlugins("onAutoplayStop");
if(a.onAutoplayStop){f.fireCallback(a.onAutoplayStop,f)
}}else{if(X){clearInterval(X)
}X=undefined;
f.callPlugins("onAutoplayStop");
if(a.onAutoplayStop){f.fireCallback(a.onAutoplayStop,f)
}}};
function Z(){K=setTimeout(function(){if(a.loop){f.fixLoop();
f.swipeNext(true,true)
}else{if(!f.swipeNext(true,true)){if(!a.autoplayStopOnLast){f.swipeTo(0)
}else{clearTimeout(K);
K=undefined
}}}f.wrapperTransitionEnd(function(){if(typeof K!=="undefined"){Z()
}})
},a.autoplay)
}f.loopCreated=false;
f.removeLoopedSlides=function(){if(f.loopCreated){for(var j=0;
j<f.slides.length;
j++){if(f.slides[j].getData("looped")===true){f.wrapper.removeChild(f.slides[j])
}}}};
f.createLoop=function(){if(f.slides.length===0){return
}if(a.slidesPerView==="auto"){f.loopedSlides=a.loopedSlides||1
}else{f.loopedSlides=a.slidesPerView+a.loopAdditionalSlides
}if(f.loopedSlides>f.slides.length){f.loopedSlides=f.slides.length
}var an="",ak="",aj;
var ai="";
var ao=f.slides.length;
var ag=Math.floor(f.loopedSlides/ao);
var am=f.loopedSlides%ao;
for(aj=0;
aj<(ag*ao);
aj++){var ah=aj;
if(aj>=ao){var al=Math.floor(aj/ao);
ah=aj-(ao*al)
}ai+=f.slides[ah].outerHTML
}for(aj=0;
aj<am;
aj++){ak+=M(a.slideDuplicateClass,f.slides[aj].outerHTML)
}for(aj=ao-am;
aj<ao;
aj++){an+=M(a.slideDuplicateClass,f.slides[aj].outerHTML)
}var p=an+ai+z.innerHTML+ai+ak;
z.innerHTML=p;
f.loopCreated=true;
f.calcSlides();
for(aj=0;
aj<f.slides.length;
aj++){if(aj<f.loopedSlides||aj>=f.slides.length-f.loopedSlides){f.slides[aj].setData("looped",true)
}}f.callPlugins("onCreateLoop")
};
f.fixLoop=function(){var i;
if(f.activeIndex<f.loopedSlides){i=f.slides.length-f.loopedSlides*3+f.activeIndex;
f.swipeTo(i,0,false)
}else{if((a.slidesPerView==="auto"&&f.activeIndex>=f.loopedSlides*2)||(f.activeIndex>f.slides.length-a.slidesPerView*2)){i=-f.slides.length+f.activeIndex+f.loopedSlides;
f.swipeTo(i,0,false)
}}};
f.loadSlides=function(){var ag="";
f.activeLoaderIndex=0;
var p=a.loader.slides;
var ah=a.loader.loadAllSlides?p.length:a.slidesPerView*(1+a.loader.surroundGroups);
for(var j=0;
j<ah;
j++){if(a.loader.slidesHTMLType==="outer"){ag+=p[j]
}else{ag+="<"+a.slideElement+' class="'+a.slideClass+'" data-swiperindex="'+j+'">'+p[j]+"</"+a.slideElement+">"
}}f.wrapper.innerHTML=ag;
f.calcSlides(true);
if(!a.loader.loadAllSlides){f.wrapperTransitionEnd(f.reloadSlides,true)
}};
f.reloadSlides=function(){var j=a.loader.slides;
var am=parseInt(f.activeSlide().data("swiperindex"),10);
if(am<0||am>j.length-1){return
}f.activeLoaderIndex=am;
var p=Math.max(0,am-a.slidesPerView*a.loader.surroundGroups);
var ak=Math.min(am+a.slidesPerView*(1+a.loader.surroundGroups)-1,j.length-1);
if(am>0){var ag=-J*(am-p);
f.setWrapperTranslate(ag);
f.setWrapperTransition(0)
}var aj;
if(a.loader.logic==="reload"){f.wrapper.innerHTML="";
var an="";
for(aj=p;
aj<=ak;
aj++){an+=a.loader.slidesHTMLType==="outer"?j[aj]:"<"+a.slideElement+' class="'+a.slideClass+'" data-swiperindex="'+aj+'">'+j[aj]+"</"+a.slideElement+">"
}f.wrapper.innerHTML=an
}else{var ah=1000;
var ai=0;
for(aj=0;
aj<f.slides.length;
aj++){var al=f.slides[aj].data("swiperindex");
if(al<p||al>ak){f.wrapper.removeChild(f.slides[aj])
}else{ah=Math.min(al,ah);
ai=Math.max(al,ai)
}}for(aj=p;
aj<=ak;
aj++){var ao;
if(aj<ah){ao=document.createElement(a.slideElement);
ao.className=a.slideClass;
ao.setAttribute("data-swiperindex",aj);
ao.innerHTML=j[aj];
f.wrapper.insertBefore(ao,f.wrapper.firstChild)
}if(aj>ai){ao=document.createElement(a.slideElement);
ao.className=a.slideClass;
ao.setAttribute("data-swiperindex",aj);
ao.innerHTML=j[aj];
f.wrapper.appendChild(ao)
}}}f.reInit(true)
};
function Q(){f.calcSlides();
if(a.loader.slides.length>0&&f.slides.length===0){f.loadSlides()
}if(a.loop){f.createLoop()
}f.init();
m();
if(a.pagination){f.createPagination(true)
}if(a.loop||a.initialSlide>0){f.swipeTo(a.initialSlide,0,false)
}else{f.updateActiveSlide(0)
}if(a.autoplay){f.startAutoplay()
}f.centerIndex=f.activeIndex;
if(a.onSwiperCreated){f.fireCallback(a.onSwiperCreated,f)
}f.callPlugins("onSwiperCreated")
}Q()
};
Swiper.prototype={plugins:{},wrapperTransitionEnd:function(h,f){var b=this,e=b.wrapper,d=["webkitTransitionEnd","transitionend","oTransitionEnd","MSTransitionEnd","msTransitionEnd"],c;
function g(a){if(a.target!==e){return
}h(b);
if(b.params.queueEndCallbacks){b._queueEndCallbacks=false
}if(!f){for(c=0;
c<d.length;
c++){b.h.removeEventListener(e,d[c],g)
}}}if(h){for(c=0;
c<d.length;
c++){b.h.addEventListener(e,d[c],g)
}}},getWrapperTranslate:function(e){var d=this.wrapper,a,c,f,b;
if(typeof e==="undefined"){e=this.params.mode==="horizontal"?"x":"y"
}if(this.support.transforms&&this.params.useCSS3Transforms){f=window.getComputedStyle(d,null);
if(window.WebKitCSSMatrix){b=new WebKitCSSMatrix(f.webkitTransform==="none"?"":f.webkitTransform)
}else{b=f.MozTransform||f.OTransform||f.MsTransform||f.msTransform||f.transform||f.getPropertyValue("transform").replace("translate(","matrix(1, 0, 0, 1,");
a=b.toString().split(",")
}if(e==="x"){if(window.WebKitCSSMatrix){c=b.m41
}else{if(a.length===16){c=parseFloat(a[12])
}else{c=parseFloat(a[4])
}}}if(e==="y"){if(window.WebKitCSSMatrix){c=b.m42
}else{if(a.length===16){c=parseFloat(a[13])
}else{c=parseFloat(a[5])
}}}}else{if(e==="x"){c=parseFloat(d.style.left,10)||0
}if(e==="y"){c=parseFloat(d.style.top,10)||0
}}return c||0
},setWrapperTranslate:function(a,f,e){var d=this.wrapper.style,b={x:0,y:0,z:0},c;
if(arguments.length===3){b.x=a;
b.y=f;
b.z=e
}else{if(typeof f==="undefined"){f=this.params.mode==="horizontal"?"x":"y"
}b[f]=a
}if(this.support.transforms&&this.params.useCSS3Transforms){c=this.support.transforms3d?"translate3d("+b.x+"px, "+b.y+"px, "+b.z+"px)":"translate("+b.x+"px, "+b.y+"px)";
d.webkitTransform=d.MsTransform=d.msTransform=d.MozTransform=d.OTransform=d.transform=c
}else{d.left=b.x+"px";
d.top=b.y+"px"
}this.callPlugins("onSetWrapperTransform",b);
if(this.params.onSetWrapperTransform){this.fireCallback(this.params.onSetWrapperTransform,this,b)
}},setWrapperTransition:function(a){var b=this.wrapper.style;
b.webkitTransitionDuration=b.MsTransitionDuration=b.msTransitionDuration=b.MozTransitionDuration=b.OTransitionDuration=b.transitionDuration=(a/1000)+"s";
this.callPlugins("onSetWrapperTransition",{duration:a});
if(this.params.onSetWrapperTransition){this.fireCallback(this.params.onSetWrapperTransition,this,a)
}},h:{getWidth:function(e,c,a){var d=window.getComputedStyle(e,null).getPropertyValue("width");
var b=parseFloat(d);
if(isNaN(b)||d.indexOf("%")>0||b<0){b=e.offsetWidth-parseFloat(window.getComputedStyle(e,null).getPropertyValue("padding-left"))-parseFloat(window.getComputedStyle(e,null).getPropertyValue("padding-right"))
}if(c){b+=parseFloat(window.getComputedStyle(e,null).getPropertyValue("padding-left"))+parseFloat(window.getComputedStyle(e,null).getPropertyValue("padding-right"))
}if(a){return Math.ceil(b)
}else{return b
}},getHeight:function(d,c,b){if(c){return d.offsetHeight
}var a=window.getComputedStyle(d,null).getPropertyValue("height");
var e=parseFloat(a);
if(isNaN(e)||a.indexOf("%")>0||e<0){e=d.offsetHeight-parseFloat(window.getComputedStyle(d,null).getPropertyValue("padding-top"))-parseFloat(window.getComputedStyle(d,null).getPropertyValue("padding-bottom"))
}if(c){e+=parseFloat(window.getComputedStyle(d,null).getPropertyValue("padding-top"))+parseFloat(window.getComputedStyle(d,null).getPropertyValue("padding-bottom"))
}if(b){return Math.ceil(e)
}else{return e
}},getOffset:function(b){var c=b.getBoundingClientRect();
var a=document.body;
var g=b.clientTop||a.clientTop||0;
var f=b.clientLeft||a.clientLeft||0;
var d=window.pageYOffset||b.scrollTop;
var e=window.pageXOffset||b.scrollLeft;
if(document.documentElement&&!window.pageYOffset){d=document.documentElement.scrollTop;
e=document.documentElement.scrollLeft
}return{top:c.top+d-g,left:c.left+e-f}
},windowWidth:function(){if(window.innerWidth){return window.innerWidth
}else{if(document.documentElement&&document.documentElement.clientWidth){return document.documentElement.clientWidth
}}},windowHeight:function(){if(window.innerHeight){return window.innerHeight
}else{if(document.documentElement&&document.documentElement.clientHeight){return document.documentElement.clientHeight
}}},windowScroll:function(){if(typeof pageYOffset!=="undefined"){return{left:window.pageXOffset,top:window.pageYOffset}
}else{if(document.documentElement){return{left:document.documentElement.scrollLeft,top:document.documentElement.scrollTop}
}}},addEventListener:function(b,c,d,a){if(typeof a==="undefined"){a=false
}if(b.addEventListener){b.addEventListener(c,d,a)
}else{if(b.attachEvent){b.attachEvent("on"+c,d)
}}},removeEventListener:function(b,c,d,a){if(typeof a==="undefined"){a=false
}if(b.removeEventListener){b.removeEventListener(c,d,a)
}else{if(b.detachEvent){b.detachEvent("on"+c,d)
}}}},setTransform:function(b,a){var c=b.style;
c.webkitTransform=c.MsTransform=c.msTransform=c.MozTransform=c.OTransform=c.transform=a
},setTranslate:function(b,d){var c=b.style;
var e={x:d.x||0,y:d.y||0,z:d.z||0};
var a=this.support.transforms3d?"translate3d("+(e.x)+"px,"+(e.y)+"px,"+(e.z)+"px)":"translate("+(e.x)+"px,"+(e.y)+"px)";
c.webkitTransform=c.MsTransform=c.msTransform=c.MozTransform=c.OTransform=c.transform=a;
if(!this.support.transforms){c.left=e.x+"px";
c.top=e.y+"px"
}},setTransition:function(a,b){var c=a.style;
c.webkitTransitionDuration=c.MsTransitionDuration=c.msTransitionDuration=c.MozTransitionDuration=c.OTransitionDuration=c.transitionDuration=b+"ms"
},support:{touch:(window.Modernizr&&Modernizr.touch===true)||(function(){return !!(("ontouchstart" in window)||window.DocumentTouch&&document instanceof DocumentTouch)
})(),transforms3d:(window.Modernizr&&Modernizr.csstransforms3d===true)||(function(){var a=document.createElement("div").style;
return("webkitPerspective" in a||"MozPerspective" in a||"OPerspective" in a||"MsPerspective" in a||"perspective" in a)
})(),transforms:(window.Modernizr&&Modernizr.csstransforms===true)||(function(){var a=document.createElement("div").style;
return("transform" in a||"WebkitTransform" in a||"MozTransform" in a||"msTransform" in a||"MsTransform" in a||"OTransform" in a)
})(),transitions:(window.Modernizr&&Modernizr.csstransitions===true)||(function(){var a=document.createElement("div").style;
return("transition" in a||"WebkitTransition" in a||"MozTransition" in a||"msTransition" in a||"MsTransition" in a||"OTransition" in a)
})(),classList:(function(){var a=document.createElement("div");
return"classList" in a
})()},browser:{ie8:(function(){var c=-1;
if(navigator.appName==="Microsoft Internet Explorer"){var a=navigator.userAgent;
var b=new RegExp(/MSIE ([0-9]{1,}[\.0-9]{0,})/);
if(b.exec(a)!==null){c=parseFloat(RegExp.$1)
}}return c!==-1&&c<9
})(),ie10:window.navigator.msPointerEnabled,ie11:window.navigator.pointerEnabled}};
if(window.jQuery||window.Zepto){(function(a){a.fn.swiper=function(c){var b;
this.each(function(d){var f=a(this);
var e=new Swiper(f[0],c);
if(!d){b=e
}f.data("swiper",e)
});
return b
}
})(window.jQuery||window.Zepto)
}if(typeof(module)!=="undefined"){module.exports=Swiper
}if(typeof define==="function"&&define.amd){define([],function(){return Swiper
})
}var CryptoJS=CryptoJS||function(z,d){var f={},h=f.lib={},e=function(){},b=h.Base={extend:function(a){e.prototype=this;
var g=new e;
a&&g.mixIn(a);
g.hasOwnProperty("init")||(g.init=function(){g.$super.init.apply(this,arguments)
});
g.init.prototype=g;
g.$super=this;
return g
},create:function(){var a=this.extend();
a.init.apply(a,arguments);
return a
},init:function(){},mixIn:function(a){for(var g in a){a.hasOwnProperty(g)&&(this[g]=a[g])
}a.hasOwnProperty("toString")&&(this.toString=a.toString)
},clone:function(){return this.init.prototype.extend(this)
}},c=h.WordArray=b.extend({init:function(a,g){a=this.words=a||[];
this.sigBytes=g!=d?g:4*a.length
},toString:function(a){return(a||y).stringify(this)
},concat:function(k){var n=this.words,l=k.words,m=this.sigBytes;
k=k.sigBytes;
this.clamp();
if(m%4){for(var p=0;
p<k;
p++){n[m+p>>>2]|=(l[p>>>2]>>>24-8*(p%4)&255)<<24-8*((m+p)%4)
}}else{if(65535<l.length){for(p=0;
p<k;
p+=4){n[m+p>>>2]=l[p>>>2]
}}else{n.push.apply(n,l)
}}this.sigBytes+=k;
return this
},clamp:function(){var a=this.words,g=this.sigBytes;
a[g>>>2]&=4294967295<<32-8*(g%4);
a.length=z.ceil(g/4)
},clone:function(){var a=b.clone.call(this);
a.words=this.words.slice(0);
return a
},random:function(g){for(var l=[],k=0;
k<g;
k+=4){l.push(4294967296*z.random()|0)
}return new c.init(l,g)
}}),w=f.enc={},y=w.Hex={stringify:function(l){var m=l.words;
l=l.sigBytes;
for(var q=[],p=0;
p<l;
p++){var n=m[p>>>2]>>>24-8*(p%4)&255;
q.push((n>>>4).toString(16));
q.push((n&15).toString(16))
}return q.join("")
},parse:function(k){for(var l=k.length,n=[],m=0;
m<l;
m+=2){n[m>>>3]|=parseInt(k.substr(m,2),16)<<24-4*(m%8)
}return new c.init(n,l/2)
}},o=w.Latin1={stringify:function(k){var l=k.words;
k=k.sigBytes;
for(var n=[],m=0;
m<k;
m++){n.push(String.fromCharCode(l[m>>>2]>>>24-8*(m%4)&255))
}return n.join("")
},parse:function(k){for(var l=k.length,n=[],m=0;
m<l;
m++){n[m>>>2]|=(k.charCodeAt(m)&255)<<24-8*(m%4)
}return new c.init(n,l)
}},x=w.Utf8={stringify:function(a){try{return decodeURIComponent(escape(o.stringify(a)))
}catch(k){throw Error("Malformed UTF-8 data")
}},parse:function(a){return o.parse(unescape(encodeURIComponent(a)))
}},j=h.BufferedBlockAlgorithm=b.extend({reset:function(){this._data=new c.init;
this._nDataBytes=0
},_append:function(a){"string"==typeof a&&(a=x.parse(a));
this._data.concat(a);
this._nDataBytes+=a.sigBytes
},_process:function(p){var r=this._data,u=r.words,t=r.sigBytes,s=this.blockSize,n=t/(4*s),n=p?z.ceil(n):z.max((n|0)-this._minBufferSize,0);
p=n*s;
t=z.min(4*p,t);
if(p){for(var q=0;
q<p;
q+=s){this._doProcessBlock(u,q)
}q=u.splice(0,p);
r.sigBytes-=t
}return new c.init(q,t)
},clone:function(){var a=b.clone.call(this);
a._data=this._data.clone();
return a
},_minBufferSize:0});
h.Hasher=j.extend({cfg:b.extend(),init:function(a){this.cfg=this.cfg.extend(a);
this.reset()
},reset:function(){j.reset.call(this);
this._doReset()
},update:function(a){this._append(a);
this._process();
return this
},finalize:function(a){a&&this._append(a);
return this._doFinalize()
},blockSize:16,_createHelper:function(a){return function(k,l){return(new a.init(l)).finalize(k)
}
},_createHmacHelper:function(a){return function(k,l){return(new i.HMAC.init(a,l)).finalize(k)
}
}});
var i=f.algo={};
return f
}(Math);
(function(o){function d(r,s,p,u,q,t,n){r=r+(s&p|~s&u)+q+n;
return(r<<t|r>>>32-t)+s
}function f(r,s,p,u,q,t,n){r=r+(s&u|p&~u)+q+n;
return(r<<t|r>>>32-t)+s
}function g(r,s,p,u,q,t,n){r=r+(s^p^u)+q+n;
return(r<<t|r>>>32-t)+s
}function e(r,s,p,u,q,t,n){r=r+(p^(s|~u))+q+n;
return(r<<t|r>>>32-t)+s
}for(var b=CryptoJS,c=b.lib,i=c.WordArray,k=c.Hasher,c=b.algo,h=[],j=0;
64>j;
j++){h[j]=4294967296*o.abs(o.sin(j+1))|0
}c=c.MD5=k.extend({_doReset:function(){this._hash=new i.init([1732584193,4023233417,2562383102,271733878])
},_doProcessBlock:function(Q,N){for(var V=0;
16>V;
V++){var P=N+V,n=Q[P];
Q[P]=(n<<8|n>>>24)&16711935|(n<<24|n>>>8)&4278255360
}var V=this._hash.words,P=Q[N+0],n=Q[N+1],O=Q[N+2],L=Q[N+3],J=Q[N+4],H=Q[N+5],F=Q[N+6],E=Q[N+7],p=Q[N+8],m=Q[N+9],l=Q[N+10],a=Q[N+11],M=Q[N+12],K=Q[N+13],I=Q[N+14],G=Q[N+15],U=V[0],T=V[1],S=V[2],R=V[3],U=d(U,T,S,R,P,7,h[0]),R=d(R,U,T,S,n,12,h[1]),S=d(S,R,U,T,O,17,h[2]),T=d(T,S,R,U,L,22,h[3]),U=d(U,T,S,R,J,7,h[4]),R=d(R,U,T,S,H,12,h[5]),S=d(S,R,U,T,F,17,h[6]),T=d(T,S,R,U,E,22,h[7]),U=d(U,T,S,R,p,7,h[8]),R=d(R,U,T,S,m,12,h[9]),S=d(S,R,U,T,l,17,h[10]),T=d(T,S,R,U,a,22,h[11]),U=d(U,T,S,R,M,7,h[12]),R=d(R,U,T,S,K,12,h[13]),S=d(S,R,U,T,I,17,h[14]),T=d(T,S,R,U,G,22,h[15]),U=f(U,T,S,R,n,5,h[16]),R=f(R,U,T,S,F,9,h[17]),S=f(S,R,U,T,a,14,h[18]),T=f(T,S,R,U,P,20,h[19]),U=f(U,T,S,R,H,5,h[20]),R=f(R,U,T,S,l,9,h[21]),S=f(S,R,U,T,G,14,h[22]),T=f(T,S,R,U,J,20,h[23]),U=f(U,T,S,R,m,5,h[24]),R=f(R,U,T,S,I,9,h[25]),S=f(S,R,U,T,L,14,h[26]),T=f(T,S,R,U,p,20,h[27]),U=f(U,T,S,R,K,5,h[28]),R=f(R,U,T,S,O,9,h[29]),S=f(S,R,U,T,E,14,h[30]),T=f(T,S,R,U,M,20,h[31]),U=g(U,T,S,R,H,4,h[32]),R=g(R,U,T,S,p,11,h[33]),S=g(S,R,U,T,a,16,h[34]),T=g(T,S,R,U,I,23,h[35]),U=g(U,T,S,R,n,4,h[36]),R=g(R,U,T,S,J,11,h[37]),S=g(S,R,U,T,E,16,h[38]),T=g(T,S,R,U,l,23,h[39]),U=g(U,T,S,R,K,4,h[40]),R=g(R,U,T,S,P,11,h[41]),S=g(S,R,U,T,L,16,h[42]),T=g(T,S,R,U,F,23,h[43]),U=g(U,T,S,R,m,4,h[44]),R=g(R,U,T,S,M,11,h[45]),S=g(S,R,U,T,G,16,h[46]),T=g(T,S,R,U,O,23,h[47]),U=e(U,T,S,R,P,6,h[48]),R=e(R,U,T,S,E,10,h[49]),S=e(S,R,U,T,I,15,h[50]),T=e(T,S,R,U,H,21,h[51]),U=e(U,T,S,R,M,6,h[52]),R=e(R,U,T,S,L,10,h[53]),S=e(S,R,U,T,l,15,h[54]),T=e(T,S,R,U,n,21,h[55]),U=e(U,T,S,R,p,6,h[56]),R=e(R,U,T,S,G,10,h[57]),S=e(S,R,U,T,F,15,h[58]),T=e(T,S,R,U,K,21,h[59]),U=e(U,T,S,R,J,6,h[60]),R=e(R,U,T,S,a,10,h[61]),S=e(S,R,U,T,O,15,h[62]),T=e(T,S,R,U,m,21,h[63]);
V[0]=V[0]+U|0;
V[1]=V[1]+T|0;
V[2]=V[2]+S|0;
V[3]=V[3]+R|0
},_doFinalize:function(){var p=this._data,q=p.words,m=8*this._nDataBytes,r=8*p.sigBytes;
q[r>>>5]|=128<<24-r%32;
var n=o.floor(m/4294967296);
q[(r+64>>>9<<4)+15]=(n<<8|n>>>24)&16711935|(n<<24|n>>>8)&4278255360;
q[(r+64>>>9<<4)+14]=(m<<8|m>>>24)&16711935|(m<<24|m>>>8)&4278255360;
p.sigBytes=4*(q.length+1);
this._process();
p=this._hash;
q=p.words;
for(m=0;
4>m;
m++){r=q[m],q[m]=(r<<8|r>>>24)&16711935|(r<<24|r>>>8)&4278255360
}return p
},clone:function(){var l=k.clone.call(this);
l._hash=this._hash.clone();
return l
}});
b.MD5=k._createHelper(c);
b.HmacMD5=k._createHmacHelper(c)
})(Math);
(function(a){a.fn.resizecrop=function(b){var c={width:50,height:50,vertical:"center",horizontal:"center",wrapper:"span",moveClass:true,moveId:true,className:"resizecrop",zoom:true,wrapperCSS:{}};
var b=a.extend(c,b);
return this.each(function(){var i=a(this);
i.css("display","none");
i.removeAttr("width").removeAttr("height");
var h=a(document.createElement(b.wrapper)).css({width:b.width,height:b.height,overflow:"hidden",display:"inline-block","vertical-align":"middle",position:"relative"}).css(b.wrapperCSS);
if(b.moveClass){var e=i.attr("class");
if(typeof e!=="undefined"&&e!==false&&e!==""){var g=e.split(/\s+/);
a.each(g,function(j,k){h.addClass(k)
});
i.removeAttr("class");
i.addClass(b.className)
}}if(b.moveId){var d=i.attr("id");
if(typeof d!=="undefined"&&d!==false&&d!==""){i.removeAttr("id");
h.attr("id",d)
}}i.wrap(h);
function f(j){width_ratio=b.width/j.width();
height_ratio=b.height/j.height();
if(width_ratio>height_ratio){if(b.zoom||width_ratio<1){j.width(b.width)
}switch(b.vertical){case"top":j.css("top",0);
break;
case"bottom":j.css("bottom",0);
break;
case"center":default:j.css("top",((j.height()-b.height)/-2)+"px")
}if(b.zoom||width_ratio<1){j.css("left",0)
}else{j.css("left",((j.width()-b.width)/-2)+"px")
}}else{if(b.zoom||height_ratio<1){j.height(b.height)
}switch(b.horizontal){case"left":j.css("left",0);
break;
case"right":j.css("right",0);
break;
case"center":default:j.css("left",((j.width()-b.width)/-2)+"px")
}if(b.zoom||height_ratio<1){j.css("top",0)
}else{j.css("top",((j.height()-b.height)/-2)+"px")
}}j.css({position:"relative",display:"block"})
}if(this.complete){f(i)
}else{i.load(function(){f(a(this))
})
}})
};
a.fn.cropresize=a.fn.resizecrop
})(jQuery);
jQuery(document).ready(function(){Topic.main();
BlockScroll.main();
ScrollUp.main()
});
Topic={main:function(){this.initShare()
},initShare:function(){if(jQuery.fn.live){jQuery(".event-share a").live("click",function(d){d.preventDefault();
var c=jQuery(this).parent().parent().parent();
var b=c.find(".share-layer");
var a=c.outerHeight()-40;
b.css("height",a).fadeIn("fast");
c.find(".share-layer .share-link").off("click").on("click",function(f){f.preventDefault();
b.find(".share-txt-link").show().find("input").focus().select()
});
c.find(".share-layer .share-close a").off("click").on("click",function(f){f.preventDefault();
b.fadeOut()
})
})
}}};
TopicListDays={options:{selector:"#listday-swiper-container"},main:function(b){if(typeof b!="undefined"){this.options=jQuery.extend(this.options,b)
}var c=$(this.options.selector).find(".swiper-wrapper").children();
var a=(c.length>0)?Math.floor(c.length/5):1;
new Swiper(this.options.selector,{mode:"vertical",pagination:".daylist-pagination",paginationClickable:true,paginationAsRange:false});
jQuery(".swiper-pagination-switch:gt("+a+")").hide()
}};
ScrollUp={selector:"#right-top-button",main:function(){this.up()
},goTop:function(){$("html,body").scrollTop(0)
},up:function(){var b=this;
var a=jQuery(b.selector);
if(a.length>0){a.click(function(c){c.preventDefault();
b.goTop()
})
}}};
BlockScroll={options:{selector:".vaticanevents-page",},main:function(a){var c=this;
if(typeof a!="undefined"){this.options=jQuery.extend(c.options,a)
}var d=jQuery(c.options.selector);
if(d.length>0){var b=d.attr("id");
this.factory(b)
}},factory:function(a){if(typeof a!="undefined"&&a=="topic"){this.topic()
}else{this.common()
}},common:function(){var a=$(".parsys.rightbar_parsys");
if(typeof rigth!="undefined"){var b=a.offset().top;
$(window).scroll(function(){if($(window).scrollTop()>=b){a.addClass("fixed")
}else{a.removeClass("fixed")
}})
}},topic:function(){var a=jQuery("#right-fix-container");
if(a.length>0){var b=jQuery("#gotop-button");
var d=jQuery("body");
var c=a.offset().top;
jQuery(window).scroll(function(){var e=jQuery(window).scrollTop();
if(e>=c){if(e>((d.outerHeight()-a.outerHeight())-75)){a.removeClass().addClass("scroll-bottom")
}else{a.removeClass().addClass("scroll-fixed")
}b.fadeIn("slow")
}else{a.removeClass().addClass("scroll-top");
b.fadeOut("fast")
}})
}}};