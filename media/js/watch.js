window.Ya=window.Ya||{};if(!window.ya_hit_param){var ya_hit_param=[]}Ya.Metrika=function(a,c,b){if(!window.__yaCounter){window.__yaCounter=this}this.id=a||0;this.type=b||0;this.initCounter(c);this.lastReferer=null};Ya.Metrika.prototype=new function(){var f=window,a=document,m=f.location,r=f.navigator,v="$Rev: 911 $".match(/(\d+)/)[1],q="application/x-shockwave-flash",c="Shockwave Flash",E="ShockwaveFlash.ShockwaveFlash",u="undefined",D=null,p=null;this.initCounter=function(G){var F=this.id+":"+this.type;if(ya_hit_param[F]){return false}if(this.id){ya_hit_param[F]=1;d(this,G)}};this.reachGoal=function(F,G){this.target=F||"";d(this,G)};function n(G){var F=z();if(F){F.insertBefore(s(G+"&wmode=3"),F.firstChild)}else{(new Image(1,1)).src=G}}this.hit=function(G,J,I,H){if(!G){return}var F=o()+"//mc.yandex.ru/watch/"+this.id+"?"+g.call(this,G,J,I);if(H){F+="&site-info="+A(y(H),512)}F+="&ar=1";n(F)};function b(G){var I=m.host,F=m.href;if(!G){return F}if(G.search(/^\w+:\/\//)!=-1){return G}if(G.charAt(0)=="?"){var H=F.search(/\?/);if(H==-1){return F+G}return F.substr(0,H)+G}if(G.charAt(0)=="#"){var H=F.search(/#/);if(H==-1){return F+G}return F.substr(0,H)+G}if(G.charAt(0)=="/"){var H=F.search(I);if(H!=-1){return F.substr(0,H+I.length)+G}}else{var J=F.split("/");J[J.length-1]=G;return J.join("/")}return G}function d(F,H){var G=o()+"//mc.yandex.ru/watch/"+F.id+"?"+i(F.type,F.target);if(H){G+="&site-info="+A(y(H),512)}n(G);if(F.target){j(100)}}function i(H,F){var G="";G+="rn="+Math.floor(Math.random()*1000000);G+="&cnt-class="+H;G+="&page-ref="+A(F?m.href:a.referrer,512);G+="&page-url="+A(F?"goal://"+a.domain+"/"+F:m.href,512);G+="&browser-info="+w();return G}function g(F,I,H){var J="",G=(typeof H!=u)?H:(this.lastReferer===null?m.href:this.lastReferer);J+="rn="+Math.floor(Math.random()*1000000);J+="&cnt-class="+this.type;G=b(G);J+="&page-ref="+A(G,512);F=b(F);J+="&page-url="+A(F,512);J+="&browser-info="+w(I);this.lastReferer=G;return J}function o(){return m.protocol=="https:"?"https:":"http:"}function w(J){var H=[],F="";H[0]=r.javaEnabled()?"j:1":"";H[1]="s:"+screen.width+"x"+screen.height+"x"+(screen.colorDepth?screen.colorDepth:screen.pixelDepth);if(D===null){D=B()}H[2]=D;H[3]=(top&&(self!==top))?"fr:1":"";H[4]="w:"+x()+"x"+h();H[5]="z:"+t();H[6]="i:"+e();if(p===null){p=C()}H[7]=p?"l:"+p:"";var K=k();H[8]=K?"en:"+K:"";H[9]="v:"+v;H[10]=r.cookieEnabled?"c:1":"";var I=l();H[11]=(typeof J!=u)?"t:"+A(J,100):(I?"t:"+A(I,100):"");for(var G=0;G<H.length;G++){if(H[G]){F+=(F?":":"")+H[G]}}return F}function k(){var J="",I=a.getElementsByTagName("meta");if(I&&I.length>0){for(var G=0,F=I.length;G<F;G++){if(I[G].content){var H=I[G].content.match(/charset=(.*)/);if(H){J=H[1];break}}}}else{J=a.characterSet||a.charset}return J}function B(){var G=null,I=null,F;if(typeof r.plugins!=u&&typeof r.plugins[c]=="object"){G=r.plugins[c].description;if(G&&!(typeof r.mimeTypes!=u&&r.mimeTypes[q]&&!r.mimeTypes[q].enabledPlugin)){I=G.replace(/([a-zA-Z]|\s)+/,"").replace(/(\s+r|\s+b[0-9]+)/,".")}}else{if(typeof f.ActiveXObject!=u){try{F=new ActiveXObject(E);if(F){G=F.GetVariable("$version");if(G){I=G.split(" ")[1].replace(/,/g,".").replace(/[^.\d]/g,"")}}}catch(H){}}}return I&&("f:"+I)}function t(){return(new Date()).getTimezoneOffset()*(-1)}function e(){function H(K){return K<10?"0"+K:K}var G=new Date(),F=[G.getFullYear(),G.getMonth()+1,G.getDate(),G.getHours(),G.getMinutes(),G.getSeconds()],J="";for(var I=0;I<F.length;I++){J+=H(F[I])}return J}function x(){var F=-1;if(f.innerWidth){F=parseInt(f.innerWidth)}else{if(a.documentElement&&a.compatMode=="CSS1Compat"){F=a.documentElement.clientWidth}else{if(a.body){F=a.body.clientWidth}}}return F}function h(){var F=-1;if(f.innerHeight){F=parseInt(f.innerHeight)}else{if(a.documentElement&&a.compatMode=="CSS1Compat"){F=a.documentElement.clientHeight}else{if(a.body){F=a.body.clientHeight}}}return F}function C(){var F=null;if(f.ActiveXObject){try{var K=new ActiveXObject("AgControl.AgControl");function L(P,N,M,O){while(H(P,N)){N[M]+=O}N[M]-=O}function H(N,M){return N.isVersionSupported(M[0]+"."+M[1]+"."+M[2]+"."+M[3])}var G=[1,0,0,0];L(K,G,0,1);L(K,G,1,1);L(K,G,2,10000);L(K,G,2,1000);L(K,G,2,100);L(K,G,2,10);L(K,G,2,1);L(K,G,3,1);F=G.join(".")}catch(J){}}else{var I=r.plugins["Silverlight Plug-In"];if(I){F=I.description}}return F}function z(){return a.getElementsByTagName("body")[0]}function l(){var G=a.title;if(typeof G!="string"){var F=a.getElementsByTagName("title");if(F&&F.length){G=F[0].innerHTML}else{G=""}}return G}function s(G){var F=a.createElement("script");F.type="text/javascript";F.async=true;F.defer=true;F.src=G;return F}function A(G,F){F=F||256;if(!G){return""}if(G.length>F){G=G.substr(0,F)}return(window.encodeURIComponent||escape)(G).replace(/\+/g,"%2B")}function y(H){function K(L){return L?L.replace(/\\/,"\\\\").replace(/"/,'\\"'):""}switch(H.constructor){case Boolean:return H.toString();case Number:return isFinite(H)?H.toString():"null";case String:return'"'+K(H)+'"';case Array:var F=[];for(var J=0,I=H.length;J<I;J++){F[F.length]=y(H[J])}return"["+F.join(",")+"]";case Object:var F="{",J=0;for(var G in H){if(!H.hasOwnProperty(G)){continue}F+=(J==0?"":",")+'"'+K(G)+'":'+y(H[G]);J++}F+="}";return F;default:return"null"}}this.convertToString=y;function j(I){var G=new Date().getTime();for(var H=1;H>0;H++){if(H%1000==0){var F=new Date().getTime();if(F-G>I){break}}}}};if(window.ya_cid){new Ya.Metrika(ya_cid,window.ya_params,window.ya_class)}if(!window.ya_hit){var ya_hit=function(a,b){__yaCounter.reachGoal(a,b)}}(function(){var g=window,f=document,h=g.location;if(typeof g.yandex_metrika_callback=="function"){g.yandex_metrika_callback()}if(h.href.search(/ym_playback=linkmap/)!=-1){var a=f.createElement("script");a.type="text/javascript";a.async=a.defer=true;a.src=h.protocol+"//metrika.yandex.ru/js/linkmap/_loader.js";try{var c=f.getElementsByTagName("html")[0];if(!f.getElementsByTagName("head")[0]){c.appendChild(f.createElement("head"))}var b=f.getElementsByTagName("head")[0];b.insertBefore(a,b.firstChild)}catch(d){}}})();