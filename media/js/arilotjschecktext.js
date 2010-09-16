function checkTheText()
{

	var strlen = 7000; //Менять допустимое кол-во символов
	var nImgCount = 20; //Менять допустимое кол-во изображений

	var strStringToCheck = CKEDITOR.instances["newstext"].getData();

	var strReplacedString;
	var strRegExp = new RegExp("(<[^>]*>|<\\?|\\?>)", "g");
	strReplacedString = strStringToCheck.replace(strRegExp, "My");
	var strRegExp1 = new RegExp("(<[ \t]{0,}img[ \t]{1,})", "g");
	var strMatchImg = strStringToCheck.match(strRegExp1);
	if(strMatchImg==null) {strMatchImg="";}
	var nNumbOfImg = strMatchImg.length;
	if(nNumbOfImg==null) {nNumbOfImg = 0;}
	var nNumbOfSymbols = strReplacedString.length;
	if(nNumbOfImg > nImgCount) {
		alert('В вашем тексте более '+nImgCount+' изображений. Пожалуйста, разделите его на страницы!');return false;
	}
	if( nNumbOfSymbols > strlen )
	{
		alert('Ваш текст превышает '+strlen+' символов. Пожалуйста, разделите его, на страницы!');return false;
	}
	else if(nNumbOfSymbols==0) {
		alert('Вы не ввели текст');return false;
	}

}

function checkChk(f) {
  
  var checkedbox = "";
  for (i=0; i<f.elements.length; i++) {
      if (f.elements[i].type=='checkbox' && f.elements[i].checked==true) {
	checkedbox = "FindOne";
      }
  }
  if(checkedbox.length<=0)
  {
    alert("Вы не выбрали рубрику!");
	remakeThePage(2);
    return false;
  }

}

function remakeThePage(page)
{
	if(page == 0)
	{
		document.getElementById('nwstxt').style.display='block';
		document.getElementById('link1').className='linksofmenu-active';
		document.getElementById('newsimg').style.display='none';
		document.getElementById('link3').className='linksofmenu';
		document.getElementById('rubrics').style.display='none';
		document.getElementById('link2').className='linksofmenu';
		document.getElementById('td1').className='open';
		document.getElementById('td2').className='close';
		document.getElementById('td3').className='close';
	}
	else if(page == 1)
	{
		document.getElementById('nwstxt').style.display='none';
		document.getElementById('link1').className='linksofmenu';
		document.getElementById('newsimg').style.display='block';
		document.getElementById('link3').className='linksofmenu-active';
		document.getElementById('rubrics').style.display='none';
		document.getElementById('link2').className='linksofmenu';
		document.getElementById('td1').className='close';
		document.getElementById('td2').className='close';
		document.getElementById('td3').className='open';
	}
	else if(page == 2)
	{
		document.getElementById('nwstxt').style.display='none';
		document.getElementById('link1').className='linksofmenu';
		document.getElementById('newsimg').style.display='none';
		document.getElementById('link3').className='linksofmenu';
		document.getElementById('rubrics').style.display='block';
		document.getElementById('link2').className='linksofmenu-active';
		document.getElementById('td1').className='close';
		document.getElementById('td2').className='open';
		document.getElementById('td3').className='close';
	}
}

function changeTab()
{
	var strParent = window.parent.document
	strParent.getElementById('nwstxt').style.display='block';
	strParent.getElementById('link1').className='linksofmenu-active';
	strParent.getElementById('newsimg').style.display='none';
	strParent.getElementById('link3').className='linksofmenu';
	strParent.getElementById('rubrics').style.display='none';
	strParent.getElementById('link2').className='linksofmenu';
	strParent.getElementById('td1').className='open';
	strParent.getElementById('td2').className='close';
	strParent.getElementById('td3').className='close';
}

function insertImages(imagem, image)
{
	var CKEDITOR   = window.parent.CKEDITOR;
	var oEditor   = CKEDITOR.instances.editorName;
	var strIncludeImg = '<div style="text-align:center;"><a href="' + image + '" target="_blank"><img src="' + imagem + '" border="1" align="center" alt="" /></a></div>&nbsp;<br />&nbsp;<br />&nbsp;';
	CKEDITOR.instances['newstext'].setData(CKEDITOR.instances['newstext'].getData()+strIncludeImg);
	changeTab();
}

function insertAllImages()
{
	var nCnt = 1;
    var strStringToCheck = document.getElementById("piclist1").innerHTML;
	var strRegExp1 = new RegExp('id=[\"]{0,}ms_class_', 'g');
    var strMatchImg = strStringToCheck.match(strRegExp1);
    if(strMatchImg==null) {strMatchImg="";}
    var nNumbOfImg = strMatchImg.length;
    var nEndPos = 0;
    var nBeginPos;
    var nStartPos;
    var nStrLength;
    var strFileM;
    var strFileL;
	var strIncludeImg = "";
    while(nNumbOfImg >= nCnt)
    {
      nCnt++;
      nStartPos = nEndPos;
      nBeginPos = strStringToCheck.indexOf("<a href=\"javascript:insertImages('", nEndPos);
      if(nBeginPos=="-1") {nBeginPos = strStringToCheck.indexOf("<A href=\"javascript:insertImages('", nEndPos);}
      nBeginPos = nBeginPos + 34;
      nBeginPos1 = strStringToCheck.indexOf("','", nBeginPos);
      nStrLength = nBeginPos1 - nBeginPos;
      nBeginPos1 = nBeginPos1 + 3;
      strFileM = strStringToCheck.substr(nBeginPos, nStrLength);
      nEndPos = strStringToCheck.indexOf(");\">", nBeginPos1);
      nEndPos = nEndPos - 1;
      nStrLength = nEndPos - nBeginPos1;
      strFileL = strStringToCheck.substr(nBeginPos1, nStrLength);
	  strIncludeImg = strIncludeImg+'<div style="text-align:center;"><a href="' + strFileL + '" target="_blank"><img src="' + strFileM + '" border="1" align="center" alt="" /></a></div>&nbsp;<br />&nbsp;<br />&nbsp;';
    }
	var CKEDITOR   = window.parent.CKEDITOR;
	CKEDITOR.instances['newstext'].setData(CKEDITOR.instances['newstext'].getData()+strIncludeImg);
	changeTab();
}