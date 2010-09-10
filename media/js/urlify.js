var LATIN_MAP = {
    'A': 'A', 'A': 'A', 'A': 'A', 'A': 'A', 'A': 'A', 'A': 'A', '?': 'AE', 'C':
    'C', 'E': 'E', 'E': 'E', 'E': 'E', 'E': 'E', 'I': 'I', 'I': 'I', 'I': 'I',
    'I': 'I', '?': 'D', 'N': 'N', 'O': 'O', 'O': 'O', 'O': 'O', 'O': 'O', 'O':
    'O', 'O': 'O', 'O': 'O', 'U': 'U', 'U': 'U', 'U': 'U', 'U': 'U', 'U': 'U',
    'Y': 'Y', '?': 'TH', '?': 'ss', 'a':'a', 'a':'a', 'a': 'a', 'a': 'a', 'a':
    'a', 'a': 'a', '?': 'ae', 'c': 'c', 'e': 'e', 'e': 'e', 'e': 'e', 'e': 'e',
    'i': 'i', 'i': 'i', 'i': 'i', 'i': 'i', '?': 'd', 'n': 'n', 'o': 'o', 'o':
    'o', 'o': 'o', 'o': 'o', 'o': 'o', 'o': 'o', 'o': 'o', 'u': 'u', 'u': 'u',
    'u': 'u', 'u': 'u', 'u': 'u', 'y': 'y', '?': 'th', 'y': 'y'
}
var LATIN_SYMBOLS_MAP = {
    '©':'(c)'
}

var TURKISH_MAP = {
    's':'s', 'S':'S', '?':'i', 'I':'I', 'c':'c', 'C':'C', 'u':'u', 'U':'U',
    'o':'o', 'O':'O', 'g':'g', 'G':'G'
}
var RUSSIAN_MAP = {
    'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo', 'ж':'zh',
    'з':'z', 'и':'i', 'й':'j', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o',
    'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'h', 'ц':'c',
    'ч':'ch', 'ш':'sh', 'щ':'sh', 'ъ':'', 'ы':'y', 'ь':'', 'э':'e', 'ю':'yu',
    'я':'ya',
    'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'Yo', 'Ж':'Zh',
    'З':'Z', 'И':'I', 'Й':'J', 'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 'О':'O',
    'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 'Х':'H', 'Ц':'C',
    'Ч':'Ch', 'Ш':'Sh', 'Щ':'Sh', 'Ъ':'', 'Ы':'Y', 'Ь':'', 'Э':'E', 'Ю':'Yu',
    'Я':'Ya'
}
var UKRAINIAN_MAP = {
    'Є':'Ye', 'І':'I', 'Ї':'Yi', 'Ґ':'G', 'є':'ye', 'і':'i', 'ї':'yi', 'ґ':'g'
}
var CZECH_MAP = {
    'c':'c', 'd':'d', 'e':'e', 'n': 'n', 'r':'r', 's':'s', 't':'t', 'u':'u',
    'z':'z', 'C':'C', 'D':'D', 'E':'E', 'N': 'N', 'R':'R', 'S':'S', 'T':'T',
    'U':'U', 'Z':'Z'
}

var POLISH_MAP = {
    'a':'a', 'c':'c', 'e':'e', 'l':'l', 'n':'n', 'o':'o', 's':'s', 'z':'z',
    'z':'z', 'A':'A', 'C':'C', 'E':'e', 'L':'L', 'N':'N', 'O':'o', 'S':'S',
    'Z':'Z', 'Z':'Z'
}

var LATVIAN_MAP = {
    'a':'a', 'c':'c', 'e':'e', 'g':'g', 'i':'i', 'k':'k', 'l':'l', 'n':'n',
    's':'s', 'u':'u', 'z':'z', 'A':'A', 'C':'C', 'E':'E', 'G':'G', 'I':'i',
    'K':'k', 'L':'L', 'N':'N', 'S':'S', 'U':'u', 'Z':'Z'
}

var ALL_DOWNCODE_MAPS=new Array()
ALL_DOWNCODE_MAPS[0]=LATIN_MAP
ALL_DOWNCODE_MAPS[1]=LATIN_SYMBOLS_MAP
ALL_DOWNCODE_MAPS[3]=TURKISH_MAP
ALL_DOWNCODE_MAPS[4]=RUSSIAN_MAP
ALL_DOWNCODE_MAPS[5]=UKRAINIAN_MAP
ALL_DOWNCODE_MAPS[6]=CZECH_MAP
ALL_DOWNCODE_MAPS[7]=POLISH_MAP
ALL_DOWNCODE_MAPS[8]=LATVIAN_MAP

var Downcoder = new Object();
Downcoder.Initialize = function()
{
    if (Downcoder.map) // already made
        return ;
    Downcoder.map ={}
    Downcoder.chars = '' ;
    for(var i in ALL_DOWNCODE_MAPS)
    {
        var lookup = ALL_DOWNCODE_MAPS[i]
        for (var c in lookup)
        {
            Downcoder.map[c] = lookup[c] ;
            Downcoder.chars += c ;
        }
     }
    Downcoder.regex = new RegExp('[' + Downcoder.chars + ']|[^' + Downcoder.chars + ']+','g') ;
}

downcode= function( slug )
{
    Downcoder.Initialize() ;
    var downcoded =""
    var pieces = slug.match(Downcoder.regex);
    if(pieces)
    {
        for (var i = 0 ; i < pieces.length ; i++)
        {
            if (pieces[i].length == 1)
            {
                var mapped = Downcoder.map[pieces[i]] ;
                if (mapped != null)
                {
                    downcoded+=mapped;
                    continue ;
                }
            }
            downcoded+=pieces[i];
        }
    }
    else
    {
        downcoded = slug;
    }
    return downcoded;
}


function URLify(s, num_chars) {
    // changes, e.g., "Petty theft" to "petty_theft"
    // remove all these words from the string before urlifying
    s = downcode(s);
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for", "from",
                  "is", "in", "into", "like", "of", "off", "on", "onto", "per",
                  "since", "than", "the", "this", "that", "to", "up", "via",
                  "with"];
    r = new RegExp('\\b(' + removelist.join('|') + ')\\b', 'gi');
    s = s.replace(r, '');
    // if downcode doesn't hit, the char will be stripped here
    s = s.replace(/[^-\w\s]/g, '');  // remove unneeded chars
    s = s.replace(/^\s+|\s+$/g, ''); // trim leading/trailing spaces
    s = s.replace(/[-\s]+/g, '-');   // convert spaces to hyphens
    s = s.toLowerCase();             // convert to lowercase
    return s.substring(0, num_chars);// trim to first num_chars chars
}

