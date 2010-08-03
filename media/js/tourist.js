/** global */
var rtn4p_item          = 17449;
var rtn4p_show_src      = 0;
var rtn4p_show_desc     = 0;
var rtn4p_show_photo    = 1;
var rtn4p_show_align    = 'left';
/** styles */
var rtn4p_class_title   = 'rtitle23';
var rtn4p_class_src     = '';
var rtn4p_class_desc    = 'desc';
var rtn4p_class_photo   = '';
var rtn4p_style_photo   = 'margin-bottom:10px;margin-right:5px; width: 79px; height: 59px; border:1px solid #ccc;';
/** header/footer */
var rtn4p_header        = '<table border="0" cellpadding="0" cellspacing="0" width="100%">';
var rtn4p_footer        = '<'+'/table><img src="http://nc.ru.redtram.com/px/936.gif" alt="" width="1" height="1" border="0" />';
/** news line */
var rtn4p_line_before   = '<tr><td valign="top" align="left" style="">';
var rtn4p_line_after    = '<'+'/td><'+'/tr>';

var rtn4p_title_before  = '<div style="">';
var rtn4p_title_after   = '<'+'/div>';

var rtn4p_src_before    = '';
var rtn4p_src_after     = '';

var rtn4p_desc_before   = '';
var rtn4p_desc_after    = '';

var rtn4p_domain        = 'http://ru.redtram.com/';
var rtn4p_host          = 'http://n4p.ru.redtram.com/';
var rtn4p_photo         = 'http://img232.ru.redtram.com/news/';
var rtn4p_page          = 1;

var rtn4p_data          = '';
var rtn4p_css_styles    = 'a.rtitle23:link{font-family:tahoma; font-size:11px; font-weight:normal; color:#a91e0a; text-decoration:none;}a.rtitle23:hover{color:#a91e0a; text-decoration:underline;}a.rtitle23:active{color:#a91e0a; text-decoration:underline;}a.rtitle23:visited{font-family:tahoma; font-size:11px; font-weight:bold; color:#a91e0a; text-decoration:none;}';

var rtn4p_initid        = 'rtn4p_neb_jdty';

var ak = Array();	
var count_ak = 0;	
	
/** do not edit */
function getCookie(name){var dc=document.cookie;var prefix=name+"=";var begin=dc.indexOf("; "+prefix);if(begin==-1){begin=dc.indexOf(prefix);if(begin!=0){return null;}}else{begin += 2;}var end=dc.indexOf(";", begin);if (end==-1){end=dc.length;}return unescape(dc.substring(begin+prefix.length,end));}
function setCookie(name,value,expires,path,domain,secure){document.cookie=name+"="+escape(value)+((expires)?"; expires="+expires.toGMTString():"")+((path)?"; path="+path:"")+((domain)?";domain="+domain:"")+((secure)?"; secure":"");}
function RedTramCookies(value){var rtcn="rtn4p";if(value){rtn4p_page=value;}else{var rtc=getCookie(rtcn);if(rtc!=null&&parseInt(rtc)<=10&&(parseInt(rtc)+1)<=10){rtn4p_page=parseInt(rtc)+1;}setCookie(rtcn,rtn4p_page,"","/");}}RedTramCookies();

var rtn4p_init          = document.getElementById(rtn4p_initid);

function RedTramI(){if(rtn4p_init){rtn4p_init.innerHTML = rtn4p_data;}}
function RedTramH(){rtn4p_data+=rtn4p_header;}
function RedTramF(){rtn4p_data+=rtn4p_footer;RedTramI();}
function RedTramAdd(title,url,src,desc,photo,special){

    str=rtn4p_line_before;

    if(rtn4p_show_src){str+=rtn4p_src_before+'<a target="_blank" href="'+rtn4p_domain+'sources/'+src+'/"'+(rtn4p_class_src?' class="'+rtn4p_class_src+'"':'')+'>'+src+'<'+'/a>'+rtn4p_src_after;}
    if(rtn4p_show_photo&&photo!=''){str+='<a target="_blank" href="'+rtn4p_domain+'go/'+url+'/n4p/'+rtn4p_item+'/'+ak[count_ak]+'"><img'+(rtn4p_class_photo?' class="'+rtn4p_class_photo+'"':'')+' src="'+rtn4p_photo+''+photo+'" border=0 align="'+rtn4p_show_align+'"'+(rtn4p_style_photo?' style="'+rtn4p_style_photo+'"':'')+' /><'+'/a>';}
    str+=rtn4p_title_before+'<a target="_blank" href="'+rtn4p_domain+'go/'+url+'/n4p/'+rtn4p_item+'/'+ak[count_ak]+'"'+(rtn4p_class_title?' class="'+rtn4p_class_title+'"':'')+'>'+title+'<'+'/a>'+rtn4p_title_after;
    if(rtn4p_show_desc&&desc!=''){str+=rtn4p_desc_before+'<a target="_blank" href="'+rtn4p_domain+'go/'+url+'/n4p/'+rtn4p_item+'/'+ak[count_ak]+'"'+(rtn4p_class_desc?' class="'+rtn4p_class_desc+'"':'')+'>'+desc+'<'+'/a>'+rtn4p_desc_after;}
    rtn4p_data+=str+rtn4p_line_after;

    count_ak = count_ak + 1;
}


if (rtn4p_init) {
    document.write('<style type="text/css">'+rtn4p_css_styles+'<'+'/style>');
	document.write('<scr'+'ipt language="javascript" type="text/javascript" src="'+rtn4p_host+'?i='+rtn4p_item+'&p='+rtn4p_page+'"><'+'/scr'+'ipt>');
} 
